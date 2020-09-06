#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Muscle Spline  widget controller class implementation
"""

from __future__ import print_function, division, absolute_import

import os

import tpDcc as tp
from tpDcc.libs.python import jsonio

from tpRigToolkit.tools.interpolateit.widgets import interpolator

LOGGER = tp.LogsMgr().get_logger('tpRigToolkit-tools-musclespline')


class MuscleSplineController(object):
    def __init__(self, client, model):
        super(MuscleSplineController, self).__init__()

        self._client = client
        self._model = model

    @property
    def client(self):
        return self._client

    @property
    def model(self):
        return self._model
