# Challenge 1 — Pixel Gun Apocalypse 
# Author : Fabián Andrés Cortés Tróchez
# Date: 2024 - 03 - 17
# https://github.com/fcortesbio/SENA-VEC-python/blob/main/Pixel/main.py

import random
import unittest
from unittest.mock import patch
random.seed(1997)

weapons = list(".-+*TY|WXM") # Valid characters representing weapons
random_mode = False # When True, main() uses rand_clock() rather than get_clock() for clock weapons
# strikes = 3 # amount of permitted attempts during input validation

def check_select(string: str)-> bool:
    # Returns True only if all characters in the passed string belongs to weapons
    return all(letter.upper() in weapons for letter in string)

def get_weapon(strikes = 3)->str:
    # Returns a string representing a list of weapons after passing input lenght and characters validation
    try:
        while strikes > 0:
            string = input()
            if len(string) in range(4,7): # lenght must be 6
                if check_select(string): # input character validation
                    return string
                else:
                    print("Selección inválida, intenta nuevamente.") # error message for illegal characters
                    strikes -= 1
            else:
                print("Debes seleccionar de 5 a 6 armas.") # error message for illegal lenght
                strikes -= 1
        raise ValueError("Too many invalid inputs.")
    except ValueError:
        string = "".join([random.choice(weapons) for _ in range(6)])
        print(f"Sobrepasaste la cantidad de intentos fallidos. La computadora ha seleccionado automáticamente las siguientes armas: {string}")
        return string
        
def rand_clock(times: int)->str:
    # returns a times-lenght string with characters from weapons
    return "".join([random.choice(weapons) for _ in range(times)])

def get_clock()-> str:
    """ 
    Prompt the user to input a string representing a custom set of weapons that will be effective through each clock cycle
    If any inputted character is not in `weapons`, user is prompted to enter a new value
    Returns: 
        string: a string validated to contain only legal characters
    """
    while True:
        string = input()
        if check_select(string):
            return string
        else:
            print("Selección inválida, por favor intenta nuevamente.")

def report_score(V, F): # adopting convention as in challenge document
    return "≈" if V == F else ("V" if V > F else "F")
    
def match()-> str:
    vg_weapons = get_weapon()
    fs_weapons = get_weapon()
    clock = get_clock()
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
 
# def main() -> str:
#     # getting weapons for each team from inputs
#     print("Selecciona las armas para el Equipo 1")
#     team1_weapons = get_weapon()
#     print("Selecciona las armas para el Equipo 2")
#     team2_weapons = get_weapon()
#     # getting a clock from input, or generate 20 if Global random is True
#     clock = get_clock() if not random_mode else rand_clock(20)
#     # define starting values for scores
#     score1 = 0
#     score2 = 0 
#     # empty list
#     output = [] 
#     # iterate on clock to get and report scores
#     for character in clock: # runs the following for each character in clock
#         if character in team1_weapons:
#             score1 += 1 # add 1 to score1 if this turn's character is in team1_weapons
#         if character in team2_weapons:
#             score2 += 2 # add 1 to score2 if this turn's character is in team2_weapons
#         output.append(report_score(score1, score2))
#         string = "".join([letter for letter in output])
#     return string   

# Including testing units for match()

class TestMatchFunction(unittest.TestCase):
    @patch("builtins.input", side_effect=["+XMY*|", "+XWY.-", "WWX.-.+M-M||+..+XM|XM"])
    def test_scenario_1(self, mock_input):
        expected_output = "FFFFFFFFFFFFFFFFFFFFF"
        self.assertEqual(match(), expected_output)
    # So far, so good;
    
    @patch("builtins.input", side_effect=["+Y.X-|", "WMT*|-", "|*Y+-*|-|Y-X|+|YM-*T+-X-**W-XY"])
    def test_scenario_2(self, mock_input):
        expected_output = "≈F≈VV≈≈≈≈VVVVVVVVVVVVVVVVV≈≈VV"
        self.assertEqual(match(), expected_output)
    # It"s working; let"s build the remaining tests :D
    
    @patch("builtins.input", side_effect=["MX.+T", "+TX-W", "M-+.|M*++*Y-W+|M-|YXW."])
    def test_scenario_3(self, mock_input):
        expected_output = "V≈≈VVVVVVVVV≈≈≈V≈≈≈≈F≈"
        self.assertEqual(match(), expected_output)

    @patch("builtins.input", side_effect=["MX.+T", "+TX-W", "M-+.|M*++*Y-W+|M-|YXW."])
    def test_scenario_4(self, mock_input):
        expected_output = "V≈≈VVVVVVVVV≈≈≈V≈≈≈≈F≈"
        self.assertEqual(match(), expected_output)

    @patch("builtins.input", side_effect=["*W+|.", "-+TXY", "XW*|M+T*YXW+X*.+MW*|"])
    def test_scenario_5(self, mock_input):
        expected_output = "F≈VVVVVVV≈VV≈VVVVVVV"
        self.assertEqual(match(), expected_output)

if __name__ == "__main__":
    game = match()
    print(game)
    
    # unittest.main(argv=["", "TestMatchFunction"], verbosity=2, exit=False)
    
    # (pixel) fcortesbio@aspire:~/Code/SENA/SENA-VEC-python/Pixel$ python3 main.py 
    # test_scenario_1 (__main__.TestMatchFunction.test_scenario_1) ... ok
    # test_scenario_2 (__main__.TestMatchFunction.test_scenario_2) ... ok
    # test_scenario_3 (__main__.TestMatchFunction.test_scenario_3) ... ok
    # test_scenario_4 (__main__.TestMatchFunction.test_scenario_4) ... ok
    # test_scenario_5 (__main__.TestMatchFunction.test_scenario_5) ... ok

    # ----------------------------------------------------------------------
    # Ran 5 tests in 0.002s

    # OK
    