#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains general tests for tpRigToolkit
"""

import pytest

from tpRigToolkit.tools.musclespline import __version__


def test_version():
    assert __version__.get_version()
