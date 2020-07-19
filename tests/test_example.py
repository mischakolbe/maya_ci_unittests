"""
Unit tests for example tool.
"""
from maya import cmds

from base import BaseTestCase

import awesome_maya_tool.example


class TestPolyCube(BaseTestCase):

    def test_node_name(self):
        """Test whether node name is correct."""
        name = "ItIsIndeedACube"
        cube = awesome_maya_tool.example.make_a_cube(name=name)

        # Make sure no attributes were added to this node instance
        self.assertEqual(cube, name)
