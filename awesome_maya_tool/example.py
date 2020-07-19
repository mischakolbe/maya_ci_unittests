"""Simple test function.

:author: Mischa Kolbe <mischakolbe@gmail.com>
"""
from maya import cmds


def make_a_cube(name="test"):
    cube = cmds.polyCube(name=name)

    return cube
