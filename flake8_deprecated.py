# -*- coding: utf-8 -*-
import ast


class Flake8Deprecated(object):
    name = 'flake8_deprecated'
    version = '1.2'
    message = 'D001 found {0:s} replace it with {1:s}'
    checks = {
        'assertEqual': ('failUnlessEqual', 'assertEquals', ),
        'assertNotEqual': ('failIfEqual', ),
        'assertTrue': ('failUnless', 'assert_', ),
        'assertFalse': ('failIf', ),
        'assertRaises': ('failUnlessRaises', ),
        'assertAlmostEqual': ('failUnlessAlmostEqual', ),
        'assertNotAlmostEqual': ('failIfAlmostEqual', ),
        'AccessControl.ClassSecurityInfo.protected': ('declareProtected', ),
        'AccessControl.ClassSecurityInfo.private': ('declarePrivate', ),
        'AccessControl.ClassSecurityInfo.public': ('declarePublic', ),
        'zope.interface.provider': ('directlyProvides', ),
        'zope.interface.implementer': ('classImplements', 'implements', ),
        'self.loadZCML(': ('xmlconfig.file', ),
        'zope.component.adapter': ('adapts', ),
    }

    def __init__(self, tree):
        self.flat_checks = self._flatten_checks()
        self.tree = tree

    def run(self):
        for node in ast.walk(self.tree):
            if isinstance(node, ast.Call) and \
               isinstance(node.func, ast.Attribute):
                for newer_version, old_alias in self.flat_checks:
                    if node.func.attr == old_alias:
                        msg = self.message.format(old_alias, newer_version)
                        yield node.lineno, node.col_offset, msg, type(self)

    def _flatten_checks(self):
        flattened_checks = []
        for new_version, old_alias in self.checks.items():
            for alias in old_alias:
                flattened_checks.append((new_version, alias, ))

        return flattened_checks
