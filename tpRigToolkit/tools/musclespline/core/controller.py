#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Muscle Spline  widget controller class implementation
"""

from __future__ import print_function, division, absolute_import

import tpDcc as tp

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

    def change_name(self, value):
        self._model.name = value

    def change_size(self, value):
        self._model.size = value

    def change_insertion_controls(self, value):
        self._model.insertion_controls = value

    def change_control_type(self, value):
        self._model.control_type = value

    def change_number_driven_joints(self, value):
        self._model.driven_joints = value

    def change_driven_type(self, value):
        self._model.driven_type = value

    def change_constraint_mid_controls(self, flag):
        self._model.constraint_mid_controls = flag

    def change_lock_controls_scale(self, flag):
        self._model.lock_controls_scale = flag

    def change_lock_jiggle_attributes(self, flag):
        self._model.lock_jiggle_attributes = flag

    def change_enable_advanced(self, flag):
        self._model.enable_advanced = flag

    def change_control_suffix(self, value):
        self._model.control_suffix = value

    def change_joint_suffix(self, value):
        self._model.joint_suffix = value

    def change_group_suffix(self, value):
        self._model.group_suffix = value

    def change_driven_suffix(self, value):
        self._model.driven_suffix = value

    def change_create_sets(self, flag):
        self._model.create_sets = flag

    def change_main_muscle_set_name(self, value):
        self._model.main_muscle_set_name = value

    def change_muscle_set_suffix(self, value):
        self._model.muscle_set_suffix = value

    def change_muscle_spline_name(self, value):
        self._model.muscle_spline_name = value

    def change_controls_group_suffix(self, value):
        self._model.controls_group_suffix = value

    def change_joints_group_suffix(self, value):
        self._model.joints_group_suffix = value

    def change_root_group_suffix(self, value):
        self._model.root_group_suffix = value

    def change_auto_group_suffix(self, value):
        self._model.auto_group_suffix = value

    def create_muscle_spline(self):
        muscle_spline_attrs_dict = self._model.get_properties_dict()
        return self._client.create_muscle_spline(**muscle_spline_attrs_dict)
