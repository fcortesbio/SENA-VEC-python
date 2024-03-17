# Challenge 1 — Pixel Gun Apocalypse 
# Author : Fabián Andrés Cortés Tróchez
# Date: 2024 - 03 - 17

# Removing all extra items and keep only the bear minumum for the challenge
# Hopefully, I"ll figure out why tests are not passing

import unittest
from unittest.mock import patch

weapons = list(".-+*TY|WXM") # Valid characters representing weapons

def report_score(V, F): # adopting convention as in challenge document
    return "≈" if V == F else ("V" if V > F else "F")

def main() -> str:
    vg_weapons = input()
    fs_weapons = input()
    clock = input()
    # define starting values for scores
    vg_score = 0
    fs_score = 0 
    output = [] # empty list
    for effective_weapon in clock: 
        if effective_weapon in vg_weapons:
            vg_score += 1 # add 1 to score1 if this turn"s character is in team1_weapons
        if effective_weapon in fs_weapons:
            fs_score += 1 # I realized I had an increment of 2 instead of one; Vampires apparently had a huge handycap!!
        output.append(report_score(vg_score, fs_score))
        string = "".join([letter for letter in output])
    return string   

# Now let"s test:
class TestMainFunction(unittest.TestCase):
    @patch("builtins.input", side_effect=["+XMY*|", "+XWY.-", "WWX.-.+M-M||+..+XM|XM"])
    def test_scenario_1(self, mock_input):
        expected_output = "FFFFFFFFFFFFFFFFFFFFF"
        self.assertEqual(main(), expected_output)
    # So far, so good;
    
    @patch("builtins.input", side_effect=["+Y.X-|", "WMT*|-", "|*Y+-*|-|Y-X|+|YM-*T+-X-**W-XY"])
    def test_scenario_2(self, mock_input):
        expected_output = "≈F≈VV≈≈≈≈VVVVVVVVVVVVVVVVV≈≈VV"
        self.assertEqual(main(), expected_output)
    # It"s working; let"s build the remaining tests :D
    
    @patch("builtins.input", side_effect=["MX.+T", "+TX-W", "M-+.|M*++*Y-W+|M-|YXW."])
    def test_scenario_3(self, mock_input):
        expected_output = "V≈≈VVVVVVVVV≈≈≈V≈≈≈≈F≈"
        self.assertEqual(main(), expected_output)

    @patch("builtins.input", side_effect=["MX.+T", "+TX-W", "M-+.|M*++*Y-W+|M-|YXW."])
    def test_scenario_4(self, mock_input):
        expected_output = "V≈≈VVVVVVVVV≈≈≈V≈≈≈≈F≈"
        self.assertEqual(main(), expected_output)

    @patch("builtins.input", side_effect=["*W+|.", "-+TXY", "XW*|M+T*YXW+X*.+MW*|"])
    def test_scenario_5(self, mock_input):
        expected_output = "F≈VVVVVVV≈VV≈VVVVVVV"
        self.assertEqual(main(), expected_output)
    
if __name__ == "__main__":
    # unittest.main(argv=["", "TestMainFunction"], verbosity=3, exit=False) # There we go!! tests are going through!
    # The problem is likely an issue in the main function, as all other modules work as expected when testing; 
    # I"ll try building an alternate function and add complements as the test are passed again 
    main()