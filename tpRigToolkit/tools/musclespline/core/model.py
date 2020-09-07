#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Muscle Spline widget model class implementation
"""

from __future__ import print_function, division, absolute_import

from Qt.QtCore import *


class MuscleSplineModel(QObject, object):

    nameChanged = Signal(str)
    sizeChanged = Signal(float)
    insertionControlsChanged = Signal(int)
    drivenJointsChanged = Signal(int)
    constraintMidControlsChanged = Signal(bool)
    lockControlsScaleChanged = Signal(bool)
    enableAdvancedChanged = Signal(bool)
    controlSuffixChanged = Signal(str)
    jointSuffixChanged = Signal(str)
    groupSuffixChanged = Signal(str)
    drivenSuffixChanged = Signal(str)
    mainMuscleSetNameChanged = Signal(str)
    muscleSetSuffixChanged = Signal(str)
    muscleSplineNameChanged = Signal(str)
    controlsGroupSuffixChanged = Signal(str)
    jointsGroupSuffixChanged = Signal(str)
    rootGroupSuffixChanged = Signal(str)
    autoGroupSuffixChanged = Signal(str)

    def __init__(self):
        super(MuscleSplineModel, self).__init__()

        self._insertion_types = ['cube', 'circleY', 'null']
        self._driven_types = 'joint', 'circleY', 'null'

        self._name = 'Char01_Spine'
        self._size = 1.0
        self._insertion_controls = 3
        self._driven_joints = 5
        self._constraint_mid_controls = False
        self._lock_controls_scale = True
        self._enable_advanced = False
        self._control_suffix = 'ctrl'
        self._joint_suffix = 'jnt'
        self._group_suffix = 'grp'
        self._driven_suffix = 'drv'
        self._main_muscle_set_name = 'setMUSCLERIGS'
        self._muscle_set_suffix = 'RIG'
        self._muscle_spline_name = 'muscleSpline'
        self._controls_group_suffix = 'ctrls'
        self._joints_group_suffix = 'joints'
        self._root_group_suffix = 'root'
        self._auto_group_suffix = 'auto'

    @property
    def insertion_types(self):
        return self._insertion_types

    @property
    def driven_types(self):
        return self._driven_types

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = str(value)
        self.nameChanged.emit(self._name)

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = float(value)
        self.sizeChanged.emit(self._size)

    @property
    def insertion_controls(self):
        return self._insertion_controls

    @insertion_controls.setter
    def insertion_controls(self, value):
        self._insertion_controls = int(value)
        self.insertionControlsChanged.emit(value)

    @property
    def driven_joints(self):
        return self._driven_joints

    @driven_joints.setter
    def driven_joints(self, value):
        self._driven_joints = int(value)
        self.drivenJointsChanged.emit(self._driven_joints)

    @property
    def constraint_mid_controls(self):
        return self._constraint_mid_controls

    @constraint_mid_controls.setter
    def constraint_mid_controls(self, flag):
        self._constraint_mid_controls = bool(flag)
        self.constraintMidControlsChanged.emit(self._constraint_mid_controls)

    @property
    def lock_controls_scale(self):
        return self._lock_controls_scale

    @lock_controls_scale.setter
    def lock_controls_scale(self, flag):
        self._lock_controls_scale = bool(flag)
        self.lockControlsScaleChanged.emit(self._lock_controls_scale)

    @property
    def enable_advanced(self):
        return self._enable_advanced

    @enable_advanced.setter
    def enable_advanced(self, flag):
        self._enable_advanced = bool(flag)
        self.enableAdvancedChanged.emit(self._enable_advanced)

    @property
    def control_suffix(self):
        return self._control_suffix

    @control_suffix.setter
    def control_suffix(self, value):
        self._control_suffix = str(value)
        self.controlSuffixChanged.emit(self._control_suffix)

    @property
    def joint_suffix(self):
        return self._joint_suffix

    @joint_suffix.setter
    def joint_suffix(self, value):
        self._joint_suffix = str(value)
        self.jointSuffixChanged.emit(self._joint_suffix)

    @property
    def group_suffix(self):
        return self._group_suffix

    @group_suffix.setter
    def group_suffix(self, value):
        self._group_suffix = str(value)
        self.groupSuffixChanged.emit(self._group_suffix)

    @property
    def driven_suffix(self):
        return self._driven_suffix

    @driven_suffix.setter
    def driven_suffix(self, value):
        self._driven_suffix = str(value)
        self.drivenSuffixChanged.emit(self._driven_suffix)

    @property
    def main_muscle_set_name(self):
        return self._main_muscle_set_name

    @main_muscle_set_name.setter
    def main_muscle_set_name(self, value):
        self._main_muscle_set_name = str(value)
        self.mainMuscleSetNameChanged.emit(self._main_muscle_set_name)

    @property
    def muscle_set_suffix(self):
        return self._muscle_set_suffix

    @muscle_set_suffix.setter
    def muscle_set_suffix(self, value):
        self._muscle_set_suffix = str(value)
        self.muscleSetSuffixChanged.emit(self._muscle_set_suffix)

    @property
    def muscle_spline_name(self):
        return self._muscle_spline_name

    @muscle_spline_name.setter
    def muscle_spline_name(self, value):
        self._muscle_spline_name = str(value)
        self.muscleSplineNameChanged.emit(self._muscle_spline_name)

    @property
    def controls_group_suffix(self):
        return self._controls_group_suffix

    @controls_group_suffix.setter
    def controls_group_suffix(self, value):
        self._controls_group_suffix = str(value)
        self.controlsGroupSuffixChanged.emit(self._controls_group_suffix)

    @property
    def joints_group_suffix(self):
        return self._joints_group_suffix

    @joints_group_suffix.setter
    def joints_group_suffix(self, value):
        self._joints_group_suffix = str(value)
        self.jointsGroupSuffixChanged.emit(self._joints_group_suffix)

    @property
    def root_group_suffix(self):
        return self._root_group_suffix

    @root_group_suffix.setter
    def root_group_suffix(self, value):
        self._root_group_suffix = str(value)
        self.rootGroupSuffixChanged.emit(self._root_group_suffix)

    @property
    def auto_group_suffix(self):
        return self._auto_group_suffix

    @auto_group_suffix.setter
    def auto_group_suffix(self, value):
        self._auto_group_suffix = str(value)
        self.autoGroupSuffixChanged.emit(self._auto_group_suffix)
