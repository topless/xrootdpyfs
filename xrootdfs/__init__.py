# -*- coding: utf-8 -*-
#
# This file is part of xrootdfs
# Copyright (C) 2015 CERN.
#
# xrootdfs is free software; you can redistribute it and/or modify it under the
# terms of the Revised BSD License; see LICENSE file for more details.

r"""XRootDFS is a PyFilesystem interface for XRootD.

XRootD protocol aims at giving high performance, scalable fault tolerant access
to data repositories of many kinds. The XRootDFS adds a high-level interface
on top of the existing Python interface (pyxrootd) and makes it easy to e.g.
copy a directory in parallel or recursively remove a directory.

.. testsetup::

   from os.path import dirname, join, exists
   import os
   import shutil
   import tempfile

   if exists("/tmp/xrootdfs"):
       shutil.rmtree("/tmp/xrootdfs")
   os.makedirs("/tmp/xrootdfs")
   f = open("/tmp/xrootdfs/test.txt", "w")
   f.write("Welcome to xrootdfs!")
   f.close()

.. testcleanup::

   shutil.rmtree("/tmp/xrootdfs")

Installation
============

The XRootDFS package is on PyPI so all you need is:

.. code-block:: console

    $ pip install xrootdfs

XRootDFS depends on `PyFilesystem <http://docs.pyfilesystem.org>`_ and
`XRootD Python bindings <http://xrootd.org/doc/python/xrootd-python-0.1.0/>`_.

Getting started
===============

The easiest way to run the examples is using the provided docker container.
This way you don't need to have access to an XRootD server plus all the
dependencies installed:

.. code-block:: console

   $ docker build -t xrootd .
   $ docker run -h xrootdfs -it xrootd bash

Next, start a XRootD server in the container and fire up an ipython shell:

.. code-block:: console

   [xrootdfs@xrootdfs code]$ xrootd -b -l /dev/null
   [xrootdfs@xrootdfs code]$ ipython

Quick examples
--------------

Here is a quick example of a file listing with the xrootd PyFilesystem
integration:

    >>> from xrootdfs import XRootDFS
    >>> fs = XRootDFS("root://localhost//tmp/")
    >>> fs.listdir("xrootdfs")
    ['test.txt']

Or, alternatively using the PyFilesystem opener:

    >>> import xrootdfs
    >>> from fs.opener import opener
    >>> fs, path = opener.parse("root://localhost//tmp/")
    >>> fs.listdir("xrootdfs")
    [u'test.txt']

Reading files:

    >>> f = fs.open("xrootdfs/test.txt")
    >>> f.read()
    'Welcome to xrootdfs!'
    >>> f.close()

Reading files using the ``getcontents()`` method:

    >>> fs.getcontents("xrootdfs/test.txt")
    'Welcome to xrootdfs!'

Writing files:

    >>> f = fs.open("xrootdfs/hello.txt", "w+")
    >>> f.write("World")
    >>> f.close()

Writing files using the ``setcontents()`` method:

    >>> fs.setcontents("xrootdfs/test.txt", "World")
"""

from __future__ import absolute_import, print_function, unicode_literals

from .fs import XRootDFS
from .opener import XRootDOpener
from .xrdfile import XRootDFile
from .version import __version__

__all__ = ('__version__', 'XRootDFS', 'XRootDOpener', 'XRootDFile')
