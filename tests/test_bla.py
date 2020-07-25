"""Example unittests.

Note:
    Visit unittest documentation page for all assert options:
    https://docs.python.org/2.7/library/unittest.html#module-unittest
"""
from base import MayaBaseTestCase

import example_code


class TestMakeTransform(MayaBaseTestCase):
    def test_node_name(self):
        """Test whether returned name is correct."""
        name = "TestTransform"
        self.assertEqual(example_code.make_transform(name=name), "boba")
