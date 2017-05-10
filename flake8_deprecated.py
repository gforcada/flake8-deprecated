# -*- coding: utf-8 -*-
try:
    from flake8.engine import pep8 as stdin_utils
except ImportError:
    from flake8 import utils as stdin_utils


class Flake8Deprecated(object):
    name = 'flake8_deprecated'
    version = '1.2'
    message = 'D001 found {0:s} replace it with {1:s}'
    checks = {
        'assertEqual': ('failUnlessEqual(', 'assertEquals(', ),
        'assertNotEqual': ('failIfEqual(', ),
        'assertTrue': ('failUnless(', 'assert_(', ),
        'assertFalse': ('failIf(', ),
        'assertRaises': ('failUnlessRaises(', ),
        'assertAlmostEqual': ('failUnlessAlmostEqual(', ),
        'assertNotAlmostEqual': ('failIfAlmostEqual(', ),
        'AccessControl.ClassSecurityInfo.protected': ('declareProtected(', ),
        'AccessControl.ClassSecurityInfo.private': ('declarePrivate(', ),
        'AccessControl.ClassSecurityInfo.public': ('declarePublic(', ),
        'zope.interface.provider': ('directlyProvides(', ),
        'zope.interface.implementer': ('classImplements(', ),
        'self.loadZCML(': ('xmlconfig.file(', ),
        'zope.interface.implementer': ('implements(', ),
        'zope.component.adapter': ('adapts(', ),
    }

    def __init__(self, tree, filename):
        self.filename = filename
        self.flat_checks = self._flatten_checks()

    def run(self):
        if self.filename == 'stdin':
            lines = stdin_utils.stdin_get_value().splitlines(True)
        else:
            with open(self.filename) as f:
                lines = f.readlines()

        for lineno, line in enumerate(lines, start=1):
            for newer_version, old_alias in self.flat_checks:
                position = line.find(old_alias)
                if position != -1:
                    msg = self.message.format(old_alias, newer_version)
                    yield lineno, position, msg, type(self)

    def _flatten_checks(self):
        flattened_checks = []
        for new_version, old_alias in self.checks.items():
            for alias in old_alias:
                flattened_checks.append((new_version, alias, ))

        return flattened_checks
