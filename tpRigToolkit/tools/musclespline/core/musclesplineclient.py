#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains tpRigToolkit-tools-musclespline client implementation
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

from tpDcc.core import client


class MuscleSplineClient(client.DccClient, object):

    PORT = 19231

    # =================================================================================================================
    # BASE
    # =================================================================================================================

    def create_muscle_spline(self, **kwargs):
        cmd = {
            'cmd': 'create_muscle_spline'
        }
        cmd.update(kwargs)

        reply_dict = self.send(cmd)

        if not self.is_valid_reply(reply_dict):
            return False

        return reply_dict['success']
