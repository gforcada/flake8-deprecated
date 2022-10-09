import ast


class Flake8Deprecated:
    name = 'flake8_deprecated'
    version = '1.2'
    message = 'D001 found {0:s} replace it with {1:s}'
    deprecations = {
        'assertEqual': (
            'failUnlessEqual',
            'assertEquals',
        ),
        'assertNotEqual': ('failIfEqual',),
        'assertTrue': (
            'failUnless',
            'assert_',
        ),
        'assertFalse': ('failIf',),
        'assertRaises': ('failUnlessRaises',),
        'assertAlmostEqual': ('failUnlessAlmostEqual',),
        'assertNotAlmostEqual': ('failIfAlmostEqual',),
        'AccessControl.ClassSecurityInfo.protected': ('declareProtected',),
        'AccessControl.ClassSecurityInfo.private': ('declarePrivate',),
        'AccessControl.ClassSecurityInfo.public': ('declarePublic',),
        'zope.interface.provider': ('directlyProvides',),
        'zope.interface.implementer': (
            'classImplements',
            'implements',
        ),
        'self.loadZCML(': ('xmlconfig.file',),
        'zope.component.adapter': ('adapts',),
    }

    def __init__(self, tree):
        self.old_aliases = self._reverse_data()
        self.tree = tree

    def run(self):
        for node in ast.walk(self.tree):
            value = None
            if isinstance(node, ast.Call):
                value = self.check_calls(node)
            elif isinstance(node, ast.FunctionDef):
                value = self.check_decorators(node)

            if value:
                yield from value

    def check_calls(self, node):
        function_name = getattr(node.func, 'id', '')
        if function_name:
            value = self.check_function_call(node)
        else:
            value = self.check_method_call(node)

        if value:
            yield from value

    def check_function_call(self, node):
        function_name = node.func.id
        for old_alias in self.old_aliases:
            if function_name == old_alias:
                yield self.error(node, old_alias)

    def check_method_call(self, node):
        """Check method calls, i.e. self.SOME_CALL()

        Note that this can be endlessly nested, i.e. self.obj.another.more.SOME_CALL()
        """
        method_name = node.func.attr
        is_obj = getattr(node.func, 'value', False)
        for old_alias in self.old_aliases:
            if method_name == old_alias:
                yield self.error(node, old_alias)

            elif '.' in old_alias and is_obj:
                obj_name = getattr(node.func.value, 'attr', False)
                obj_id = getattr(node.func.value, 'id', False)
                for name in (obj_name, obj_id):
                    if f'{name}.{method_name}' == old_alias:
                        yield self.error(node, old_alias)

    def check_decorators(self, node):
        """Check decorators names for deprecated aliases

        Check for function-style decorators, i.e @my_deprecated_decorator()
        as well as for alias-like decorators, i.e @my_deprecated_decorator
        """
        for decorator in node.decorator_list:
            name = None
            if isinstance(decorator, ast.Attribute):
                name = decorator.attr
            elif isinstance(decorator, ast.Name):
                name = decorator.id
            if not name:
                continue

            for old_alias in self.old_aliases:
                if name == old_alias:
                    yield self.error(node, old_alias)

    def _reverse_data(self):
        """Reverse the deprecation dictionary

        This way, we can more easily loop through the deprecated snippets.

        We only care about the new version at error reporting time.
        """
        return {
            old_alias: new_version
            for new_version, alias_list in self.deprecations.items()
            for old_alias in alias_list
        }

    def error(self, statement, old_alias):
        return (
            statement.lineno,
            statement.col_offset,
            self.message.format(self.old_aliases[old_alias], old_alias),
            type(self),
        )
