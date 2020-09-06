#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Muscle Spline widget model class implementation
"""

from __future__ import print_function, division, absolute_import

from Qt.QtCore import *


class MuscleSplineModel(QObject, object):

    def __init__(self):
        super(MuscleSplineModel, self).__init__()

        self._interpolator_widgets = list()
