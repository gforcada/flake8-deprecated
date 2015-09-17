# -*- coding: utf-8 -*-


class Flake8Deprecated(object):
    name = 'flake8_deprecated'
    version = '0.1'
    message = 'D001 found {0:s} replace it with {1:s}'
    checks = {
        'assertEqual': ('failUnlessEqual', 'assertEquals', ),
        'assertNotEqual': ('failIfEqual', ),
        'assertTrue': ('failUnless(', 'assert_', ),
        'assertFalse': ('failIf(', ),
        'assertRaises': ('failUnlessRaises', ),
        'assertAlmostEqual': ('failUnlessAlmostEqual', ),
        'assertNotAlmostEqual': ('failIfAlmostEqual', ),
    }

    def __init__(self, tree, filename):
        self.filename = filename
        self.flat_checks = self._flatten_checks()

    def run(self):
        with open(self.filename) as f:
            for lineno, line in enumerate(f, start=1):
                for newer_version, old_alias in self.flat_checks:
                    if line.find(old_alias) != -1:
                        msg = self.message.format(old_alias, newer_version)
                        yield lineno, line.find(old_alias), msg, type(self)

    def _flatten_checks(self):
        flattened_checks = []
        for new_version, old_alias in self.checks.items():
            for alias in old_alias:
                flattened_checks.append((new_version, alias, ))

        return flattened_checks
