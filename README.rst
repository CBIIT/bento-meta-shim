=================
Bento MetaDB Shim
=================


.. image:: https://img.shields.io/pypi/v/bento_meta_shim.svg
        :target: https://pypi.python.org/pypi/bento_meta_shim

.. image:: https://img.shields.io/travis/bensonml/bento_meta_shim.svg
        :target: https://travis-ci.com/bensonml/bento_meta_shim

.. image:: https://readthedocs.org/projects/bento-meta-shim/badge/?version=latest
        :target: https://bento-meta-shim.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


.. image:: https://pyup.io/repos/github/bensonml/bento_meta_shim/shield.svg
     :target: https://pyup.io/repos/github/bensonml/bento_meta_shim/
     :alt: Updates



Shim layer for accessing Bento MetaDB

It requires using the feat/nanoidvsid, branch of bento_meta because it relies on having nanoids. 

It also requires the uri, username, and password for the mdb database to be in the environmental variables `NEO4J_MDB_URI`, `NEO4J_MDB_USER`, and `NEO4J_MDB_PASS`.

Run with `>$ python -m bento_meta_shim`


Profiling data in `profiling/`.

* Free software: MIT license
* Documentation: https://bento-meta-shim.readthedocs.io.


Features
--------

* TODO

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
