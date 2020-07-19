"""
Unit test base class.
"""
from unittest import TestCase

# Adding the path through this base module takes care of an odd
# issue where the tests were run too early.
import os
tests_path = os.path.dirname(os.path.realpath(__file__))
noca_path = tests_path.rsplit(os.sep, 1)[0]

import sys
if noca_path not in sys.path:
    sys.path.insert(0, noca_path)

import maya.cmds as cmds


class BaseTestCase(TestCase):
    """Base Class for all unittests."""
    @classmethod
    def setUpClass(self):
        """Run for every Test-Class, before methods are executed."""
        cmds.file(new=True, force=True)

    def tearDown(self):
        """Run after every Test-Class method."""
        cmds.file(new=True, force=True)
