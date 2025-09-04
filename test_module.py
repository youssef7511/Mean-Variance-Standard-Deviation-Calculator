import unittest
import mean_var_std
import numpy as np

class TestMeanVarStd(unittest.TestCase):
    
    def test_calculate_valid_input(self):
        """Test calculate function with valid 9-element list"""
        test_input = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        result = mean_var_std.calculate(test_input)
        
        # Check that all expected keys exist
        expected_keys = ['mean', 'variance', 'standard deviation', 'max', 'min', 'sum']
        for key in expected_keys:
            self.assertIn(key, result)
        
        # Check that values are lists
        for value in result.values():
            self.assertIsInstance(value, list)
        
        # Check that each list has 3 elements
        for value in result.values():
            self.assertEqual(len(value), 3)
    
    def test_calculate_invalid_input(self):
        """Test calculate function raises ValueError for invalid input"""
        with self.assertRaises(ValueError):
            mean_var_std.calculate([1, 2, 3, 4, 5])  # 5 elements, not 9
    
    def test_calculate_empty_list(self):
        """Test calculate function with empty list"""
        with self.assertRaises(ValueError):
            mean_var_std.calculate([])
    
    def test_calculate_non_numeric(self):
        """Test calculate function with non-numeric input"""
        with self.assertRaises(ValueError):
            mean_var_std.calculate(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'])

if __name__ == '__main__':
    unittest.main()
