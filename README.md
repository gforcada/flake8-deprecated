# Flake8 deprecations plugin

No language, library or framework ever get everything right from the very beginning.
Projects evolve, new features are added/changed/removed.

This means that projects relying on them must keep an eye
on what's currently best practices.

This `flake8` plugin helps you keeping up with method deprecations
and giving hints about what they should be replaced with.

This plugin is based on a python checker
that was in [plone.recipe.codeanalysis](https://pypi.python.org/pypi/plone.recipe.codeanalysis).

## Install

Install with pip::

```shell
pip install flake8-deprecated
```

## Requirements

- Python 3.11 to 3.15 and pypy3
- flake8

## TODO

- add a way to provide more deprecations on a per user basis(?), other plugins(?)
- add a way to ignore specific deprecations

## License

GPL 2.0
