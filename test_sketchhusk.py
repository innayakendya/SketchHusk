# test_sketchhusk.py
"""
Tests for SketchHusk module.
"""

import unittest
from sketchhusk import SketchHusk

class TestSketchHusk(unittest.TestCase):
    """Test cases for SketchHusk class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SketchHusk()
        self.assertIsInstance(instance, SketchHusk)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SketchHusk()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
