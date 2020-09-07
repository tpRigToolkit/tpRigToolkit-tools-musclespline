#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Muscle Spline widget view class implementation
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

from Qt.QtCore import *
from Qt.QtWidgets import *

from tpDcc.libs.qt.core import base
from tpDcc.libs.qt.widgets import layouts, expandables, label, lineedit, spinbox, dividers, combobox, checkbox, buttons


class MuscleSplineView(base.BaseWidget, object):
    def __init__(self, model, controller, parent=None):

        self._model = model
        self._controller = controller

        super(MuscleSplineView, self).__init__(parent=parent)

        self.refresh()

    def get_main_layout(self):
        return layouts.VerticalLayout(spacing=0, margins=(0, 0, 0, 0))

    def ui(self):
        super(MuscleSplineView, self).ui()

        expander = expandables.ExpanderWidget()

        muscle_setup_widget = QWidget()
        muscle_setup_layout = layouts.VerticalLayout(spacing=2, margins=(2, 2, 2, 2))
        muscle_setup_widget.setLayout(muscle_setup_layout)
        muscle_setup_base_layout = layouts.GridLayout(spacing=5, margins=(2, 2, 2, 2))
        name_label = label.BaseLabel('Name:', parent=self)
        self._name_line = lineedit.BaseLineEdit(parent=self)
        size_label = label.BaseLabel('Size:')
        self._size_spn = spinbox.BaseDoubleSpinBox(parent=self)
        self._size_spn.setMinimum(1.0)
        insertion_ctrls_lbl = label.BaseLabel('N. Controls:', parent=self)
        insertion_ctrls_lbl.setToolTip('Number Insertion Controls')
        self._insertion_ctrls_spn = spinbox.BaseSpinBox(parent=self)
        self._insertion_ctrls_spn.setMinimum(2)
        self._insertion_ctrls_spn.setMaximum(24)
        insertion_type_lbl = label.BaseLabel('Type:', parent=self)
        self._insertion_type_combo = combobox.BaseComboBox(parent=self)
        num_driven_lbl = label.BaseLabel('N. Driven:', parent=self)
        num_driven_lbl.setToolTip('Number Driven Joints')
        self._num_driven_spn = spinbox.BaseSpinBox(parent=self)
        self._num_driven_spn.setMinimum(1)
        self._num_driven_spn.setMaximum(64)
        num_driven_type_lbl = label.BaseLabel('Type:')
        self._num_driven_type_combo = combobox.BaseComboBox(parent=self)
        extras_layout = layouts.HorizontalLayout(spacing=2, margins=(2, 2, 2, 2))
        self._cns_mid_ctrls_cbx = checkbox.BaseCheckBox('Constraint Mid Controls', parent=self)
        self._lock_ctrls_scale_cbx = checkbox.BaseCheckBox('Lock Controls Scale', parent=self)
        self._lock_jiggle_attrs_cbx = checkbox.BaseCheckBox('Lock Jiggle Attributes', parent=self)
        extras_layout.addStretch()
        extras_layout.addWidget(self._cns_mid_ctrls_cbx)
        extras_layout.addWidget(self._lock_ctrls_scale_cbx)
        extras_layout.addWidget(self._lock_jiggle_attrs_cbx)
        extras_layout.addStretch()

        muscle_setup_layout.addLayout(muscle_setup_base_layout)
        muscle_setup_layout.addWidget(dividers.Divider())
        muscle_setup_layout.addLayout(extras_layout)
        muscle_setup_base_layout.addWidget(name_label, 0, 0, Qt.AlignRight)
        muscle_setup_base_layout.addWidget(self._name_line, 0, 1)
        muscle_setup_base_layout.addWidget(size_label, 1, 0, Qt.AlignRight)
        muscle_setup_base_layout.addWidget(self._size_spn, 1, 1)
        muscle_setup_base_layout.addWidget(dividers.Divider(), 2, 0, 1, 2)
        muscle_setup_base_layout.addWidget(insertion_ctrls_lbl, 3, 0, Qt.AlignRight)
        muscle_setup_base_layout.addWidget(self._insertion_ctrls_spn, 3, 1)
        muscle_setup_base_layout.addWidget(insertion_type_lbl, 4, 0, Qt.AlignRight)
        muscle_setup_base_layout.addWidget(self._insertion_type_combo, 4, 1)
        muscle_setup_base_layout.addWidget(dividers.Divider(), 5, 0, 1, 2)
        muscle_setup_base_layout.addWidget(num_driven_lbl, 6, 0, Qt.AlignRight)
        muscle_setup_base_layout.addWidget(self._num_driven_spn, 6, 1)
        muscle_setup_base_layout.addWidget(num_driven_type_lbl, 7, 0, Qt.AlignRight)
        muscle_setup_base_layout.addWidget(self._num_driven_type_combo, 7, 1)

        advanced_setup_widget = QWidget()
        advanced_setup_layout = layouts.VerticalLayout(spacing=2, margins=(2, 2, 2, 2))
        advanced_setup_widget.setLayout(advanced_setup_layout)

        self._advanced_widgets_widget = QWidget()
        advanced_widgets_layout = layouts.VerticalLayout(spacing=0, margins=(0, 0, 0, 0))
        self._advanced_widgets_widget.setLayout(advanced_widgets_layout)
        advanced_setup_base_layout = layouts.GridLayout(spacing=5, margins=(2, 2, 2, 2))
        self._advanced_enable_cbx = checkbox.BaseCheckBox('Enable', parent=self)
        ctrl_suffix_lbl = label.BaseLabel('Control Suffix:', parent=self)
        self._ctrl_suffix_line = lineedit.BaseLineEdit(parent=self)
        joint_suffix_lbl = label.BaseLabel('Joint Suffix:', parent=self)
        self._joint_suffix_line = lineedit.BaseLineEdit(parent=self)
        grp_suffix_lbl = label.BaseLabel('Group Suffix:', parent=self)
        self._grp_suffix_line = lineedit.BaseLineEdit(parent=self)
        drv_suffix_lbl = label.BaseLabel('Driven Suffix:', parent=self)
        self._drv_suffix_line = lineedit.BaseLineEdit(parent=self)
        advanced_setup_set_layout = layouts.GridLayout(spacing=5, margins=(2, 2, 2, 2))
        self._create_sets_cbx = checkbox.BaseCheckBox('Create Sets', parent=self)
        muscle_set_lbl = label.BaseLabel('Main Muscle Set Name:', parent=self)
        self._main_muscle_set_name_line = lineedit.BaseLineEdit(parent=self)
        set_suffix_lbl = label.BaseLabel('Muscle Set Suffix:', parent=self)
        self._muscle_set_suffix_line = lineedit.BaseLineEdit(parent=self)
        muscle_spline_name_lbl = label.BaseLabel('Muscle Spline Name:', parent=self)
        self._muscle_spline_name_line = lineedit.BaseLineEdit(parent=self)
        controls_group_suffix_lbl = label.BaseLabel('Controls Group Suffix:', parent=self)
        self._controls_group_suffix_line = lineedit.BaseLineEdit(parent=self)
        joints_group_suffix_lbl = label.BaseLabel('Joints Group Suffix:')
        self._joints_group_suffix_line = lineedit.BaseLineEdit(parent=self)
        root_group_suffix_lbl = label.BaseLabel('Root Group Suffix:', parent=self)
        self._root_group_suffix_line = lineedit.BaseLineEdit(parent=self)
        auto_group_suffix_lbl = label.BaseLabel('Auto Group Suffix:', parent=self)
        self._auto_group_suffix_line = lineedit.BaseLineEdit(parent=self)
        create_layout = layouts.HorizontalLayout(spacing=0, margins=(0, 0, 0, 0))
        self._create_btn = buttons.BaseButton('Create', parent=self)
        create_layout.addStretch()
        create_layout.addWidget(self._create_btn)
        create_layout.addStretch()

        advanced_setup_layout.addWidget(self._advanced_enable_cbx)
        advanced_setup_layout.addWidget(dividers.Divider())
        advanced_setup_layout.addWidget(self._advanced_widgets_widget)
        advanced_widgets_layout.addLayout(advanced_setup_base_layout)
        advanced_widgets_layout.addLayout(advanced_setup_set_layout)
        advanced_setup_base_layout.addWidget(ctrl_suffix_lbl, 0, 0, Qt.AlignRight)
        advanced_setup_base_layout.addWidget(self._ctrl_suffix_line, 0, 1)
        advanced_setup_base_layout.addWidget(joint_suffix_lbl, 1, 0, Qt.AlignRight)
        advanced_setup_base_layout.addWidget(self._joint_suffix_line, 1, 1)
        advanced_setup_base_layout.addWidget(grp_suffix_lbl, 2, 0, Qt.AlignRight)
        advanced_setup_base_layout.addWidget(self._grp_suffix_line, 2, 1)
        advanced_setup_base_layout.addWidget(drv_suffix_lbl, 3, 0, Qt.AlignRight)
        advanced_setup_base_layout.addWidget(self._drv_suffix_line, 3, 1)
        advanced_setup_base_layout.addWidget(dividers.Divider(), 4, 0, 1, 2)
        advanced_setup_set_layout.addWidget(self._create_sets_cbx, 0, 0)
        advanced_setup_set_layout.addWidget(muscle_set_lbl, 1, 0, Qt.AlignRight)
        advanced_setup_set_layout.addWidget(self._main_muscle_set_name_line, 1, 1)
        advanced_setup_set_layout.addWidget(set_suffix_lbl, 2, 0, Qt.AlignRight)
        advanced_setup_set_layout.addWidget(self._muscle_set_suffix_line, 2, 1)
        advanced_setup_set_layout.addWidget(dividers.Divider(), 3, 0, 1, 2)
        advanced_setup_set_layout.addWidget(muscle_spline_name_lbl, 4, 0, Qt.AlignRight)
        advanced_setup_set_layout.addWidget(self._muscle_spline_name_line, 4, 1)
        advanced_setup_set_layout.addWidget(dividers.Divider(), 5, 0, 1, 2)
        advanced_setup_set_layout.addWidget(controls_group_suffix_lbl, 6, 0, Qt.AlignRight)
        advanced_setup_set_layout.addWidget(self._controls_group_suffix_line, 6, 1)
        advanced_setup_set_layout.addWidget(joints_group_suffix_lbl, 7, 0, Qt.AlignRight)
        advanced_setup_set_layout.addWidget(self._joints_group_suffix_line, 7, 1)
        advanced_setup_set_layout.addWidget(root_group_suffix_lbl, 8, 0, Qt.AlignRight)
        advanced_setup_set_layout.addWidget(self._root_group_suffix_line, 8, 1)
        advanced_setup_set_layout.addWidget(auto_group_suffix_lbl, 9, 0, Qt.AlignRight)
        advanced_setup_set_layout.addWidget(self._auto_group_suffix_line, 9, 1)

        expander.addItem('Advanced Setup', advanced_setup_widget)
        expander.addItem('Muscle Setup', muscle_setup_widget)

        self.main_layout.addWidget(expander)
        self.main_layout.addWidget(dividers.Divider())
        self.main_layout.addLayout(create_layout)

    def setup_signals(self):
        self._name_line.textChanged.connect(self._controller.change_name)
        self._size_spn.valueChanged.connect(self._controller.change_size)
        self._insertion_ctrls_spn.valueChanged.connect(self._controller.change_insertion_controls)
        self._insertion_type_combo.currentTextChanged.connect(self._controller.change_control_type)
        self._num_driven_spn.valueChanged.connect(self._controller.change_number_driven_joints)
        self._num_driven_type_combo.currentTextChanged.connect(self._controller.change_driven_type)
        self._cns_mid_ctrls_cbx.toggled.connect(self._controller.change_constraint_mid_controls)
        self._lock_ctrls_scale_cbx.toggled.connect(self._controller.change_lock_controls_scale)
        self._lock_jiggle_attrs_cbx.toggled.connect(self._controller.change_lock_jiggle_attributes)
        self._advanced_enable_cbx.toggled.connect(self._controller.change_enable_advanced)
        self._ctrl_suffix_line.textChanged.connect(self._controller.change_control_suffix)
        self._joint_suffix_line.textChanged.connect(self._controller.change_joint_suffix)
        self._grp_suffix_line.textChanged.connect(self._controller.change_group_suffix)
        self._drv_suffix_line.textChanged.connect(self._controller.change_driven_suffix)
        self._create_sets_cbx.toggled.connect(self._controller.change_create_sets)
        self._main_muscle_set_name_line.textChanged.connect(self._controller.change_main_muscle_set_name)
        self._muscle_set_suffix_line.textChanged.connect(self._controller.change_muscle_set_suffix)
        self._muscle_spline_name_line.textChanged.connect(self._controller.change_muscle_spline_name)
        self._controls_group_suffix_line.textChanged.connect(self._controller.change_controls_group_suffix)
        self._joints_group_suffix_line.textChanged.connect(self._controller.change_joints_group_suffix)
        self._root_group_suffix_line.textChanged.connect(self._controller.change_root_group_suffix)
        self._auto_group_suffix_line.textChanged.connect(self._controller.change_auto_group_suffix)

        self._model.nameChanged.connect(self._on_name_changed)
        self._model.sizeChanged.connect(self._size_spn.setValue)
        self._model.insertionControlsChanged.connect(self._insertion_ctrls_spn.setValue)
        self._model.controlTypeChanged.connect(self._insertion_type_combo.setCurrentText)
        self._model.drivenJointsChanged.connect(self._num_driven_spn.setValue)
        self._model.drivenTypeChanged.connect(self._num_driven_type_combo.setCurrentText)
        self._model.constraintMidControlsChanged.connect(self._cns_mid_ctrls_cbx.setChecked)
        self._model.lockControlsScaleChanged.connect(self._lock_ctrls_scale_cbx.setChecked)
        self._model.lockJiggleAttributesChanged.connect(self._lock_jiggle_attrs_cbx.setChecked)
        self._model.enableAdvancedChanged.connect(self._on_enable_advanced_changed)
        self._model.controlSuffixChanged.connect(self._ctrl_suffix_line.setText)
        self._model.jointSuffixChanged.connect(self._joint_suffix_line.setText)
        self._model.groupSuffixChanged.connect(self._grp_suffix_line.setText)
        self._model.drivenSuffixChanged.connect(self._drv_suffix_line.setText)
        self._model.createSetsChanged.connect(self._create_sets_cbx.setChecked)
        self._model.mainMuscleSetNameChanged.connect(self._main_muscle_set_name_line.setText)
        self._model.muscleSetSuffixChanged.connect(self._muscle_set_suffix_line.setText)
        self._model.muscleSplineNameChanged.connect(self._muscle_spline_name_line.setText)
        self._model.controlsGroupSuffixChanged.connect(self._controls_group_suffix_line.setText)
        self._model.jointsGroupSuffixChanged.connect(self._joints_group_suffix_line.setText)
        self._model.rootGroupSuffixChanged.connect(self._root_group_suffix_line.setText)
        self._model.autoGroupSuffixChanged.connect(self._auto_group_suffix_line.setText)

        self._create_btn.clicked.connect(self._controller.create_muscle_spline)

    def refresh(self):
        self._insertion_type_combo.clear()
        self._num_driven_type_combo.clear()
        self._name_line.setText(self._model.name)
        self._size_spn.setValue(self._model.size)
        self._insertion_type_combo.addItems(self._model.insertion_types)
        self._num_driven_type_combo.addItems(self._model.driven_types)
        self._insertion_ctrls_spn.setValue(self._model.insertion_controls)
        self._insertion_type_combo.setCurrentText(self._model.control_type)
        self._num_driven_spn.setValue(self._model.driven_joints)
        self._num_driven_type_combo.setCurrentText(self._model.driven_type)
        self._cns_mid_ctrls_cbx.setChecked(self._model.constraint_mid_controls)
        self._lock_ctrls_scale_cbx.setChecked(self._model.lock_controls_scale)
        self._lock_jiggle_attrs_cbx.setChecked(self._model.lock_jiggle_attributes)
        self._advanced_enable_cbx.setChecked(self._model.enable_advanced)
        self._ctrl_suffix_line.setText(self._model.control_suffix)
        self._joint_suffix_line.setText(self._model.joint_suffix)
        self._grp_suffix_line.setText(self._model.group_suffix)
        self._drv_suffix_line.setText(self._model.driven_suffix)
        self._create_sets_cbx.setChecked(self._model.create_sets)
        self._main_muscle_set_name_line.setText(self._model.main_muscle_set_name)
        self._muscle_set_suffix_line.setText(self._model.muscle_set_suffix)
        self._muscle_spline_name_line.setText(self._model.muscle_spline_name)
        self._controls_group_suffix_line.setText(self._model.controls_group_suffix)
        self._joints_group_suffix_line.setText(self._model.joints_group_suffix)
        self._root_group_suffix_line.setText(self._model.root_group_suffix)
        self._auto_group_suffix_line.setText(self._model.auto_group_suffix)

        self._check_ui()

    def _check_ui(self):
        self._create_btn.setEnabled(not self._model.name == '')
        self._advanced_widgets_widget.setEnabled(self._model.enable_advanced)

    def _on_name_changed(self, value):
        self._name_line.setText(value)
        self._check_ui()

    def _on_enable_advanced_changed(self, flag):
        self._advanced_enable_cbx.setChecked(flag)
        self._check_ui()
