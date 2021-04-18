braces.py
=========

.. image:: https://img.shields.io/pypi/l/braces.py.svg
    :target: https://opensource.org/licenses/MIT
    :alt: Project License

.. image:: https://img.shields.io/pypi/v/braces.py.svg
    :target: https://pypi.python.org/pypi/braces.py
    :alt: Library Version

.. image:: https://img.shields.io/pypi/pyversions/braces.py.svg
    :target: https://pypi.python.org/pypi/braces.py
    :alt: Required Python Versions

.. image:: https://img.shields.io/pypi/status/braces.py.svg
    :target: https://github.com/nekitdev/braces.py
    :alt: Development Status

.. image:: https://img.shields.io/pypi/dw/braces.py.svg
    :target: https://pypi.python.org/pypi/braces.py
    :alt: Library Downloads / Week

.. image:: https://app.codacy.com/project/badge/Grade/6c8b6893a1204953bf4fec15c0c080fd
    :target: https://www.codacy.com/gh/nekitdev/iters.py/dashboard
    :alt: Code Quality

braces.py is a library that allows using ``{}`` braces and ``;`` for indentation.

Warning
-------

There is a known limitation in braces.py. That is, indentation like this does **NOT** work:

.. code:: python

    def identity(value: T) -> T
    {
        return value;
    }

The said limitation was partially intentional,
as it brings more problems than solutions in analysis.

Installing
----------

**Python 3.5 or higher is required**

To install the library, you can just run the following command:

.. code:: sh

    # Linux / OS X
    python3 -m pip install --upgrade braces.py

    # Windows
    py -3 -m pip install --upgrade braces.py

In order to install the library from source, you can do the following:

.. code:: sh

    $ git clone https://github.com/nekitdev/braces.py
    $ cd braces.py
    $ python -m pip install --upgrade .

Quick example
-------------

Below is an example of identity function using braces style.

.. code:: python

    # coding: braces

    from typing import TypeVar;

    T = TypeVar("T");


    def identity(some: T) -> T {
        return some;
    }

This snippet gets translated to syntactically valid python code:

.. code:: python

    from typing import TypeVar

    T = TypeVar("T")


    def identity(some: T) -> T:
        return some

You can find more examples in examples directory.

Authors
-------

This project is mainly developed by `nekitdev <https://github.com/nekitdev>`_,
with help of `isidentical <https://github.com/isidentical>`_.
