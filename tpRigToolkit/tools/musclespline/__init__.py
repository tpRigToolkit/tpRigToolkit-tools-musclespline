#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Initialization module for tpRigToolkit-tools-musclespline
"""

from __future__ import print_function, division, absolute_import

import os
import logging.config


def create_logger(dev=False):
    """
    Creates logger for current tpRigToolkit-tools-musclespline package
    """

    logger_directory = os.path.normpath(os.path.join(os.path.expanduser('~'), 'tpRigToolkit', 'logs', 'tools'))
    if not os.path.isdir(logger_directory):
        os.makedirs(logger_directory)

    logging_config = os.path.normpath(os.path.join(os.path.dirname(__file__), '__logging__.ini'))

    logging.config.fileConfig(logging_config, disable_existing_loggers=False)
    logger = logging.getLogger('tpRigToolkit-tools-musclespline')
    dev = os.getenv('TPRIGTOOLKIT_DEV', dev)
    if dev:
        logger.setLevel(logging.DEBUG)
        for handler in logger.handlers:
            handler.setLevel(logging.DEBUG)

    return logger


create_logger()


if __name__ == '__main__':
    import tpRigToolkit.loader
    from tpDcc.managers import tools

    tpRigToolkit.loader.init()
    tools.ToolsManager().launch_tool_by_id('tpRigToolkit-tools-musclespline')
