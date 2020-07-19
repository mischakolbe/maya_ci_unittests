"""
Unit tests for example tool.
"""
from maya import cmds

from base import BaseTestCase

import example_code


class TestPolyCube(BaseTestCase):
    def test_node_name(self):
        """Test whether node name is correct."""
        name = "ItIsIndeedACube"
        cube = example_code.make_a_cube(name=name)

        # Make sure no attributes were added to this node instance
        self.assertEqual(cube, name)
