#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Version module for tpRigToolkit-tools-musclespline
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

__version__ = None


def get_version():
    global __version__
    if __version__:
        return __version__

    from ._version import get_versions
    __version__ = get_versions()['version']
    del get_versions

    return __version__
