#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains tpRigToolkit-tools-musclespline server implementation for Maya
"""

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

import tpDcc as tp
from tpDcc.core import server

from tpRigToolkit.dccs.maya.core import musclespline

LOGGER = tp.LogsMgr().get_logger('tpRigToolkit-tools-musclespline')


class MuscleSplineServer(server.DccServer, object):

    PORT = 19231

    def _process_command(self, command_name, data_dict, reply_dict):
        if command_name == 'create_muscle_spline':
            self.create_muscle_spline(data_dict, reply_dict)
        else:
            super(MuscleSplineServer, self)._process_command(command_name, data_dict, reply_dict)

    @tp.Dcc.undo_decorator()
    def create_muscle_spline(self, data, reply):

        muscle_spline = musclespline.MuscleSpline(**data)
        muscle_spline.create()

        reply['success'] = True
