.. -*- coding: utf-8 -*-

Changelog
=========

2.2.2 (unreleased)
------------------

- Add support for Python 3.13 and drop Python 3.8.
  [gforcada]

- Drop python 3.9 support and add Python 3.14 support.
  [gforcada]

- Bump pypy minimum version to 3.10.

2.2.1 (2023-11-02)
------------------

- Something went wrong with the previous release.
  [gforcada]

2.2.0 (2023-11-02)
------------------

- Use `pyproject.toml` rather than `setup.py`.
  [gforcada]

- Switch from `setuptools` to `hatchling`.
  [gforcada]

- Switch to `main` branch.
  [gforcada]

- Use `tox` and `pre-commit` to ease project maintenance.
  [gforcada]

2.1.0 (2023-09-16)
------------------

- Drop python 3.7 support.
  [gforcada]

- Fix error message.
  [dhood]

2.0.1 (2022-10-11)
------------------

- Handle subscripts in method calls, thanks to @The-Compiler for the report. [gforcada]

2.0.0 (2022-10-09)
------------------

- Test the code in all python versions supported on GitHub actions. [gforcada]

- Pin dependencies, to ensure reproducible builds. [gforcada]

- Drop python 2.7 and only support 3.7+. [gforcada]

- Ensure all deprecation aliases work. [gforcada]

- Check decorators as well. [gforcada]

1.3 (2017-10-31)
----------------

- Fix flake8 errors on this package and enforce them on CI.
  [alexmuller]

1.2.2.dev0 (2017-10-22)
-----------------------

- Use the ast module to parse the code and ensure no false positives are found.
  [alexmuller]

1.2.1 (2017-07-24)
------------------
- Fix UnicodeDecodeError if system locale is not UTF-8.
  [sshishov]

1.2 (2017-05-12)
----------------
- added support for sublimetext (stdin/filename handling).
  [iham]

- Release as universal wheels.
  [gforcada]

- Only test against Python 2.7, 3.5 and 3.6.
  It most probably works on earlier versions of 2.x and 3.x but it's pointless to test on them as well.
  [gforcada]

1.1 (2016-10-26)
----------------
- Fix compatibility with flake8 3.
  [gforcada]

- Require flake8 > 3.0.
  [gforcada]

1.0 (2016-02-27)
----------------
- Warn if using xmlconfig.file, self.loadZCML is the preferred option.
  [gforcada]

- Avoid false reports by suffixing an opening parenthesis on all methods.
  [gforcada]

- Add decorators from zope.interface and zope.component.
  [gforcada]

0.2 (2016-01-20)
----------------
- Suggest to use AccessControl and zope.interface decorators.
  [gforcada]

0.1 (2015-09-17)
----------------
- Initial release.
  [gforcada]

- Create the flake8 plugin per se.
  [gforcada]

