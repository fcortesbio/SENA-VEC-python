# Challenge 1 — Pixel Gun Apocalypse 
# Author : Fabián Andrés Cortés Tróchez
# Date: 2024 - 03 - 12

import random
random.seed(1997) # for reproducibility

# List with characters representing a legal weapon in the game
weapons = [".", "-", "+", "*", "T", "Y", "|", "W", "X", "M"]

def legal_select(string: str)-> bool:
    # must validate that each character in a string belongs to the list '0weapons'
    for character in string: # for all characters in string
        if character.casefold() not in [weapon.casefold() for weapon in weapons]:
            return False
    return True

# request user to select 6 weapons
def get_weapon(team:str)->str:
    # must input a string representing a set of 6 'weapons'
    print(f"Select the 6 weapons to be used by {team}.")
    while True:
        weapon_set = input()
        if len(weapon_set) == 6:
            if legal_select(weapon_set):
                return weapon_set
            else: 
                print("One or more of the selected weapons are invalid. Please try again.")
        elif len(weapon_set) < 6:
            print("You are selecting less than 6 weapons. Please try again.")
        else:
            print("You are selecting more than 6 weapons. Please try again.") 

def rand_clock(n: int)->str:
    # must generate a string of 'n' 6 characters from 'weapons'
    clock = ""
    for i in range(n):
        clock.join(i)
    return None 

def input_clock():
    return None

def game_state(a, b):
    return None

    
def main():
    # gather entries for 2 teams with input_weapon(), generates or input the clock and make the match comparisons to make the 
    print("Hello, World!")
    
if __name__ == "__main__":
    main()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            