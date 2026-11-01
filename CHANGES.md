# Changelog

## 2.3.1 (unreleased)

- update supported python versions (3.11 to 3.15) @gforcada

- improve CI speed by using `uvx` and `prek` @gforcada

- tighten GHA with `zizmor` @gforcada

## 2.3.0 (2025-10-25)

- add support for Python 3.13 and drop Python 3.8 @gforcada

- drop Python 3.9 support and add Python 3.14 support @gforcada

- bump pypy minimum version to 3.10 @gforcada

## 2.2.1 (2023-11-02)

- something went wrong with the previous release @gforcada

## 2.2.0 (2023-11-02)

- use `pyproject.toml` rather than `setup.py` @gforcada

- switch from `setuptools` to `hatchling` @gforcada

- switch to `main` branch @gforcada

- use `tox` and `pre-commit` to ease project maintenance @gforcada

## 2.1.0 (2023-09-16)

- drop python 3.7 support @gforcada

- fix error message @dhood

## 2.0.1 (2022-10-11)

- handle subscripts in method calls, thanks to @The-Compiler for the report @gforcada

## 2.0.0 (2022-10-09)

- test the code in all python versions supported on GitHub actions @gforcada

- pin dependencies, to ensure reproducible builds @gforcada

- drop python 2.7 and only support 3.7+ @gforcada

- ensure all deprecation aliases work @gforcada

- check decorators as well @gforcada

## 1.3 (2017-10-31)

- fix `flake8` errors on this package and enforce them on CI @alexmuller

## 1.2.2.dev0 (2017-10-22)

- use the `ast` module to parse the code and ensure no false positives are found @alexmuller

## 1.2.1 (2017-07-24)

- fix `UnicodeDecodeError` if system locale is not UTF-8 @sshishov

## 1.2 (2017-05-12)

- added support for sublimetext (stdin/filename handling) @iham

- release as universal wheels @gforcada

- only test against Python 2.7, 3.5 and 3.6.
  It most probably works on earlier versions of 2.x and 3.x but it's pointless to test on them as well @gforcada

## 1.1 (2016-10-26)

- fix compatibility with `flake8` version 3 @gforcada

- require `flake8 > 3.0` @gforcada

## 1.0 (2016-02-27)

- warn if using `xmlconfig.file`, `self.loadZCML` is the preferred option @gforcada

- avoid false reports by suffixing an opening parenthesis on all methods @gforcada

- add decorators from `zope.interface` and `zope.component` @gforcada

## 0.2 (2016-01-20)

- suggest to use `AccessControl` and `zope.interface` decorators @gforcada

## 0.1 (2015-09-17)

- initial release @gforcada

- create the `flake8` plugin per se @gforcada
