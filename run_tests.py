import ast
import textwrap

import pytest

from flake8_deprecated import Flake8Deprecated


def check_code(source, expected_codes=None):
    """Check if the given source code generates the given flake8 errors

    If `expected_codes` is a string is converted to a list,
    if it is not given, then it is expected to **not** generate any error.
    """
    if isinstance(expected_codes, str):
        expected_codes = [expected_codes]
    elif expected_codes is None:
        expected_codes = []

    tree = ast.parse(textwrap.dedent(source))
    checker = Flake8Deprecated(tree)
    return_statements = list(checker.run())

    assert len(return_statements) == len(expected_codes)
    for item, code in zip(return_statements, expected_codes):
        assert item[2].startswith(f'{code} ')


def test_all_good():
    source = 'a = 3'
    check_code(source)


def test_ignore_comments():
    source = """
    a = 3
    # fortunately we remove all failIfEqual !
    """
    check_code(source)


def test_error():
    source = 'self.assertEquals()'
    check_code(source, 'D001')


def test_error_line():
    source = """
        import unittest
        unittest.assertEquals()
    """
    tree = ast.parse(textwrap.dedent(source))
    checker = Flake8Deprecated(tree)
    return_statements = list(checker.run())

    assert len(return_statements) == 1
    assert return_statements[0][0] == 3


def test_error_column():
    source = """
        class Foo:
            def test_all_good(self):
                self.assertEquals()
    """
    tree = ast.parse(textwrap.dedent(source))
    checker = Flake8Deprecated(tree)
    return_statements = list(checker.run())

    assert len(return_statements) == 1
    assert return_statements[0][1] == 8


def test_nested_method_call():
    source = 'self.context.deep.chained.element.with_deprecated.assertEquals()'
    check_code(source, 'D001')


test_aliases = [
    {
        'name': old_alias.lower(),
        'code': old_alias,
    }
    for old_alias, _ in Flake8Deprecated(None).old_aliases.items()
]


@pytest.mark.parametrize(
    'example',
    test_aliases,
    ids=[t['name'] for t in test_aliases],
)
def test_code_suggestions(example):
    source = f'self.{example["code"]}()'
    check_code(source, 'D001')


decorator_test_cases = [
    {
        'name': 'decorator-basic',
        'code': '@assertEquals()',
    },
    {
        'name': 'decorator-basic-no-parenthesis',
        'code': '@assertEquals',
    },
    {
        'name': 'decorator-method-chain-basic',
        'code': '@obj.assertEquals()',
    },
    {
        'name': 'decorator-method-chain-deep',
        'code': '@obj.another.yet_anoher.last_one.assertEquals()',
    },
    {
        'name': 'decorator-method-chain-basic-no-parenthesis',
        'code': '@obj.assertEquals',
    },
    {
        'name': 'decorator-method-chain-deep-no-parenthesis',
        'code': '@obj.another.yet_anoher.last_one.assertEquals',
    },
    {
        'name': 'decorator-nested-first',
        'code': """
            @obj.assertEquals()
            @another_decorator()
        """,
    },
    {
        'name': 'decorator-nested-last',
        'code': """
            @another_decorator()
            @obj.assertEquals()
        """,
    },
    {
        'name': 'decorator-nested-in-between',
        'code': """
            @another_decorator()
            @obj.assertEquals
            @yet_another_decorator()
        """,
    },
    {
        'name': 'full-example-decorator-chained-in-method',
        'code': """
            class Foo:
                @another_decorator()
                @obj.another_one.yet_one_more.assertEquals
                def my_method(self): ...
        """,
    },
    {
        'name': 'full-example-decorator-basic-in-method',
        'code': """
            class Foo:
                @another_decorator()
                @assertEquals
                def my_method(self): ...
        """,
    },
]


@pytest.mark.parametrize(
    'testcase', decorator_test_cases, ids=[t['name'] for t in decorator_test_cases]
)
def test_decorators(testcase):
    if 'nested' in testcase['name']:
        indentation = ' ' * 4 * 3
        source = f'{testcase["code"]}\n{indentation}def my_function(): ...'
    elif 'full-example' in testcase['name']:
        source = testcase['code']
    else:
        source = f"""
        {testcase['code']}
        def my_function(): ...
        """
    check_code(source, 'D001')
