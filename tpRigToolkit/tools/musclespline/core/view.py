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
        self._insertion_type_cbx = combobox.BaseComboBox(parent=self)
        num_driven_lbl = label.BaseLabel('N. Driven:', parent=self)
        num_driven_lbl.setToolTip('Number Driven Joints')
        self._num_driven_spn = spinbox.BaseSpinBox(parent=self)
        self._num_driven_spn.setMinimum(1)
        self._num_driven_spn.setMaximum(64)
        num_driven_type_lbl = label.BaseLabel('Type:')
        self._num_driven_type_cbx = combobox.BaseComboBox(parent=self)
        extras_layout = layouts.HorizontalLayout(spacing=2, margins=(2, 2, 2, 2))
        self._cns_mid_ctrls_cbx = checkbox.BaseCheckBox('Constraint Mid Controls', parent=self)
        self._lock_ctrls_scale_cbx = checkbox.BaseCheckBox('Lock Controls Scale', parent=self)
        extras_layout.addStretch()
        extras_layout.addWidget(self._cns_mid_ctrls_cbx)
        extras_layout.addWidget(self._lock_ctrls_scale_cbx)
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
        muscle_setup_base_layout.addWidget(self._insertion_type_cbx, 4, 1)
        muscle_setup_base_layout.addWidget(dividers.Divider(), 5, 0, 1, 2)
        muscle_setup_base_layout.addWidget(num_driven_lbl, 6, 0, Qt.AlignRight)
        muscle_setup_base_layout.addWidget(self._num_driven_spn, 6, 1)
        muscle_setup_base_layout.addWidget(num_driven_type_lbl, 7, 0, Qt.AlignRight)
        muscle_setup_base_layout.addWidget(self._num_driven_type_cbx, 7, 1)

        advanced_setup_widget = QWidget()
        advanced_setup_layout = layouts.VerticalLayout(spacing=2, margins=(2, 2, 2, 2))
        advanced_setup_widget.setLayout(advanced_setup_layout)
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
        muscle_set_lbl = label.BaseLabel('Main Muscle Set Name:', parent=self)
        self._main_set_line = lineedit.BaseLineEdit(parent=self)
        set_suffix_lbl = label.BaseLabel('Muscle Set Suffix:', parent=self)
        self._set_suffix_line = lineedit.BaseLineEdit(parent=self)
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
        advanced_setup_layout.addLayout(advanced_setup_base_layout)
        advanced_setup_layout.addLayout(advanced_setup_set_layout)
        advanced_setup_base_layout.addWidget(ctrl_suffix_lbl, 0, 0, Qt.AlignRight)
        advanced_setup_base_layout.addWidget(self._ctrl_suffix_line, 0, 1)
        advanced_setup_base_layout.addWidget(joint_suffix_lbl, 1, 0, Qt.AlignRight)
        advanced_setup_base_layout.addWidget(self._joint_suffix_line, 1, 1)
        advanced_setup_base_layout.addWidget(grp_suffix_lbl, 2, 0, Qt.AlignRight)
        advanced_setup_base_layout.addWidget(self._grp_suffix_line, 2, 1)
        advanced_setup_base_layout.addWidget(drv_suffix_lbl, 3, 0, Qt.AlignRight)
        advanced_setup_base_layout.addWidget(self._drv_suffix_line, 3, 1)
        advanced_setup_base_layout.addWidget(dividers.Divider(), 4, 0, 1, 2)
        advanced_setup_set_layout.addWidget(muscle_set_lbl, 0, 0, Qt.AlignRight)
        advanced_setup_set_layout.addWidget(self._main_set_line, 0, 1)
        advanced_setup_set_layout.addWidget(set_suffix_lbl, 1, 0, Qt.AlignRight)
        advanced_setup_set_layout.addWidget(self._set_suffix_line, 1, 1)
        advanced_setup_set_layout.addWidget(muscle_spline_name_lbl, 2, 0, Qt.AlignRight)
        advanced_setup_set_layout.addWidget(self._muscle_spline_name_line, 2, 1)
        advanced_setup_set_layout.addWidget(dividers.Divider(), 3, 0, 1, 2)
        advanced_setup_set_layout.addWidget(controls_group_suffix_lbl, 4, 0, Qt.AlignRight)
        advanced_setup_set_layout.addWidget(self._controls_group_suffix_line, 4, 1)
        advanced_setup_set_layout.addWidget(joints_group_suffix_lbl, 5, 0, Qt.AlignRight)
        advanced_setup_set_layout.addWidget(self._joints_group_suffix_line, 5, 1)
        advanced_setup_set_layout.addWidget(root_group_suffix_lbl, 6, 0, Qt.AlignRight)
        advanced_setup_set_layout.addWidget(self._root_group_suffix_line, 6, 1)
        advanced_setup_set_layout.addWidget(auto_group_suffix_lbl, 7, 0, Qt.AlignRight)
        advanced_setup_set_layout.addWidget(self._auto_group_suffix_line, 7, 1)

        expander.addItem('Advanced Setup', advanced_setup_widget)
        expander.addItem('Muscle Setup', muscle_setup_widget)

        self.main_layout.addWidget(expander)
        self.main_layout.addWidget(dividers.Divider())
        self.main_layout.addLayout(create_layout)

    def setup_signals(self):
        pass
