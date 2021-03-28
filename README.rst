braces.py
=========

.. image:: https://img.shields.io/pypi/l/braces.py.svg
    :target: https://opensource.org/licenses/MIT
    :alt: Project License

.. image:: https://img.shields.io/pypi/v/braces.py.svg
    :target: https://pypi.python.org/pypi/braces.py
    :alt: PyPI Library Version

.. image:: https://img.shields.io/pypi/pyversions/braces.py.svg
    :target: https://pypi.python.org/pypi/braces.py
    :alt: Required Python Versions

.. image:: https://img.shields.io/pypi/status/braces.py.svg
    :target: https://github.com/nekitdev/braces.py
    :alt: Project Development Status

.. image:: https://img.shields.io/pypi/dm/braces.py.svg
    :target: https://pypi.python.org/pypi/braces.py
    :alt: Library Downloads/Month

.. image:: https://img.shields.io/endpoint.svg?url=https%3A%2F%2Fshieldsio-patreon.herokuapp.com%2Fnekit%2Fpledges
    :target: https://patreon.com/nekit
    :alt: Patreon Page [Support]

braces.py is a library that allows using ``{}`` braces and ``;`` for indentation.

Warning
-------

There is a known limitation in braces.py. That is, indentation like this does **NOT** work:

.. code:: python

    def identity(value)
    {
        return value;
    }

Installing
----------

**Python 3.5 or higher is required**

To install the library, you can just run the following command:

.. code:: sh

    # Linux/OS X
    python3 -m pip install -U braces.py

    # Windows
    py -3 -m pip install -U braces.py

In order to install the library from source, you can do the following:

.. code:: sh

    $ git clone https://github.com/nekitdev/braces.py
    $ cd braces.py
    $ python -m pip install -U .

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
