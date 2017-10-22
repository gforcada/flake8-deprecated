# -*- coding: utf-8 -*-
from flake8_deprecated import Flake8Deprecated

import ast
import unittest


class TestFlake8Deprecated(unittest.TestCase):

    def _given_test_data(self, contents):
        return ast.parse(contents)

    def test_no_deprecations_all_good(self):
        tree = self._given_test_data('\n'.join([
            'b = 3',
            'b.lower()',
        ]))
        checker = Flake8Deprecated(tree)
        ret = list(checker.run())
        self.assertEqual(len(ret), 0)

    def test_s_formatter(self):
        tree = self._given_test_data('\n'.join([
            'import unittest',
            'unittest.failUnlessAlmostEqual()',
        ]))
        checker = Flake8Deprecated(tree)
        ret = list(checker.run())
        self.assertEqual(len(ret), 1)
        self.assertEqual(ret[0][0], 2)
        self.assertEqual(ret[0][1], 0)
        self.assertEqual(
            ret[0][2],
            'D001 found failUnlessAlmostEqual replace it with '
            'assertAlmostEqual'
        )

    def test_ignores_comments(self):
        tree = self._given_test_data('\n'.join([
            'import unittest',
            '# Maybe we could use assertEquals() here?',
            'unittest.assertEquals()',
        ]))
        checker = Flake8Deprecated(tree)
        ret = list(checker.run())
        self.assertEqual(len(ret), 1)
        lint_line_number = ret[0][0]
        self.assertEqual(lint_line_number, 3)


if __name__ == '__main__':
    unittest.main()
