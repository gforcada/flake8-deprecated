.. -*- coding: utf-8 -*-

.. image:: https://travis-ci.org/gforcada/flake8-deprecated.svg?branch=master
   :target: https://travis-ci.org/gforcada/flake8-deprecated

.. image:: https://coveralls.io/repos/gforcada/flake8-deprecated/badge.svg?branch=master&service=github
   :target: https://coveralls.io/github/gforcada/flake8-deprecated?branch=master

Flake8 deprecations plugin
==========================
No language, library or framework ever get everything right from the very beginning.
The project evolves, new features are added/changed/removed.

This means that projects relying on them must keep an eye on what's currently best practices.

This flake8 plugin helps you keeping up with method deprecations ans giving hints about what
they should be replaced with.

This plugin is based on a python checker that was in `plone.recipe.codeanalysis`_.

Install
-------
Install with pip::

    $ pip install flake8-deprecated

Requirements
------------
- Python 2.7, 3.3, 3.4
- flake8

TODO
----
- add a way to provide more deprecations on a per user basis(?), other plugins(?)
- add a way to ignore specific deprecations

License
-------
GPL 2.0

.. _`plone.recipe.codeanalysis`: https://pypi.python.org/pypi/plone.recipe.codeanalysis
