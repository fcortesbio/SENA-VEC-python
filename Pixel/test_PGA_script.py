import unittest
from PGA_script import * # import all fuctions
# weapons = [".", "-", "+", "*", "T", "Y", "|", "W", "X", "M"]

class Test_legal_select(unittest.TestCase):
    def test_valid_selection(self):
        # Test a valid selection
        self.assertTrue(legal_select('TWTMWM'))

    def test_invalid_selection(self):
        # Test an invalid selection
        self.assertFalse(legal_select('TWTMWM!'))  # Special characte r
        self.assertFalse(legal_select('TWTMWMN'))  # Extra character
        self.assertFalse(legal_select(''))  # Empty selection

    def test_case_insensitive(self):
        # Test case insensitivity
        self.assertTrue(legal_select('twtmwm'))  # Lowercase
        self.assertTrue(legal_select('TWTMwM'))  # Mixed case

class Test_select_weapon(unittest.TestCase):
    def test_valid_input(self):
        # Test for valid input
        # Assuming we're providing input interactively, we can use unittest.mock.patch
        with unittest.mock.patch('builtins.input', side_effect=['TWTMWM']):
            self.assertEqual(select_weapon("team_1"), 'TWTMWM')

    def test_invalid_input(self):
        # Test invalid input
        # Assuming we're providing input interactively, we can use unittest.mock.patch
        with unittest.mock.patch('builtins.input', side_effect=['TWTM!M', 'TWTMWM']):
            self.assertEqual(select_weapon("team_1"), 'TWTMWM')  # Input with special character should be rejected


if __name__ == '__main__':
    unittest.main()
