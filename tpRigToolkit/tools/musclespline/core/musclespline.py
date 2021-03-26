#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Python based Maya Muscle Spline rig builder
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

import os
import logging
import importlib

from tpDcc import dcc
from tpDcc.core import tool
from tpDcc.libs.qt.widgets import toolset

from tpRigToolkit.tools.musclespline.core import musclesplineclient

LOGGER = logging.getLogger('tpRigToolkit-tools-musclespline')

# Defines ID of the tool
TOOL_ID = 'tpRigToolkit-tools-musclespline'


class MuscleSplineTool(tool.DccTool, object):
    def __init__(self, *args, **kwargs):
        super(MuscleSplineTool, self).__init__(*args, **kwargs)

    @classmethod
    def config_dict(cls, file_name=None):
        base_tool_config = tool.DccTool.config_dict(file_name=file_name)
        tool_config = {
            'name': 'Muscle Spline',
            'id': TOOL_ID,
            'supported_dccs': {'maya': ['2017', '2018', '2019', '2020']},
            'logo': 'musclespline',
            'icon': 'musclespline',
            'tooltip': 'Python based Maya Muscle Spline rig builder',
            'tags': ['tpRigToolkit', 'muscle', 'spline'],
            'logger_dir': os.path.join(os.path.expanduser('~'), 'tpRigToolkit', 'logs', 'tools'),
            'logger_level': 'INFO',
            'is_checkable': False,
            'is_checked': False,
            'menu_ui': {'label': 'Muscle Spline', 'load_on_startup': False, 'color': '', 'background_color': ''},
            'size': [450, 840]
        }
        base_tool_config.update(tool_config)

        return base_tool_config

    def launch(self, *args, **kwargs):
        return self.launch_frameless(*args, **kwargs)


class MuscleSplineToolset(toolset.ToolsetWidget, object):
    ID = TOOL_ID

    def __init__(self, *args, **kwargs):
        super(MuscleSplineToolset, self).__init__(*args, **kwargs)

    def setup_client(self):

        self._client = musclesplineclient.MuscleSplineClient()
        self._client.signals.dccDisconnected.connect(self._on_dcc_disconnected)

        if not dcc.is_standalone():
            dcc_mod_name = '{}.dccs.{}.musclesplineserver'.format(TOOL_ID.replace('-', '.'), dcc.get_name())
            try:
                mod = importlib.import_module(dcc_mod_name)
                if hasattr(mod, 'MuscleSplineServer'):
                    server = mod.MuscleSplineServer(self, client=self._client, update_paths=False)
                    self._client.set_server(server)
                    self._update_client()
            except Exception as exc:
                LOGGER.warning(
                    'Impossible to launch Muscle Spline server! Error while importing: {} >> {}'.format(
                        dcc_mod_name, exc))
                return
        else:
            self._update_client()

    def contents(self):

        from tpRigToolkit.tools.musclespline.core import model, view, controller

        muscle_spline_model = model.MuscleSplineModel()
        muscle_spline_controller = controller.MuscleSplineController(client=self._client, model=muscle_spline_model)
        muscle_spline_view = view.MuscleSplineView(
            model=muscle_spline_model, controller=muscle_spline_controller, parent=self)

        return [muscle_spline_view]
