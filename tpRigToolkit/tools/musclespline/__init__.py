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


if __name__ == '__main__':
    import tpDcc
    import tpRigToolkit.loader

    tpRigToolkit.loader.init()
    tpDcc.ToolsMgr().launch_tool_by_id('tpRigToolkit-tools-musclespline')
