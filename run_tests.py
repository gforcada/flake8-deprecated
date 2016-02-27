# -*- coding: utf-8 -*-
from flake8_deprecated import Flake8Deprecated
from tempfile import mkdtemp

import os
import unittest


class TestFlake8Deprecated(unittest.TestCase):

    def _given_a_file_in_test_dir(self, contents):
        test_dir = os.path.realpath(mkdtemp())
        file_path = os.path.join(test_dir, 'test.py')
        with open(file_path, 'w') as a_file:
            a_file.write(contents)

        return file_path

    def test_no_deprecations_all_good(self):
        file_path = self._given_a_file_in_test_dir('\n'.join([
            'b = 3',
            'b.lower()',
        ]))
        checker = Flake8Deprecated(None, file_path)
        ret = list(checker.run())
        self.assertEqual(len(ret), 0)

    def test_s_formatter(self):
        file_path = self._given_a_file_in_test_dir('\n'.join([
            'import unittest',
            'unittest.failUnlessAlmostEqual()',
        ]))
        checker = Flake8Deprecated(None, file_path)
        ret = list(checker.run())
        self.assertEqual(len(ret), 1)
        self.assertEqual(ret[0][0], 2)
        self.assertEqual(ret[0][1], 9)
        self.assertEqual(
            ret[0][2],
            'D001 found failUnlessAlmostEqual( replace it with '
            'assertAlmostEqual'
        )


if __name__ == '__main__':
    unittest.main()
