#!/usr/bin/env python
#
# License: BSD
#   https://raw.githubusercontent.com/stonier/py_trees_ros/devel/LICENSE
#
##############################################################################
# Documentation
##############################################################################
"""
Generic launcher for one of the tutorial entry points. Saves us having to
write and install multiple no-brainer scripts.
"""
##############################################################################
# Imports
##############################################################################

import argparse
import importlib
import py_trees.console as console
import rospy
import sys

##############################################################################
# Main
##############################################################################

if __name__ == '__main__':
    # parser = argparse.ArgumentParser(description='Start of the rex-tree')
    # parser.add_argument('name', action='store', nargs='?',
    #                     default='rex_tree',
    #                     choices=['rex_tree'],
    #                     help='name of the tutorial to start')
    # command_line_args = rospy.myargv(argv=sys.argv)[1:]
    # args = parser.parse_args(command_line_args)

    module_name = "sa_rex.main_script"

    try:
        module_itself = importlib.import_module(module_name)
    except ImportError:
        console.logerror("Could not import this module [{0}]".format("main_script"))
        sys.exit(1)
    main_itself = getattr(module_itself, "main")
    main_itself()