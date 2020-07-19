"""Simple test function.

:author: Mischa Kolbe <mischakolbe@gmail.com>
"""
from maya import cmds

# IMPORTS ---
# Python imports
import copy
import itertools
import numbers
import os
import re
import sys

# Third party imports
from maya import cmds
from maya.api import OpenMaya

def make_a_cube(name="test"):
    cube = cmds.polyCube(name=name)

    return cube

