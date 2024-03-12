# Challenge 1 — Pixel Gun Apocalypse 
# Author : Fabián Andrés Cortés Tróchez
# Date: 2024 - 03 - 12

import random
random.seed(2024)

# List with characters representing a legal weapon in the game
weapons = [".", "-", "+", "*", "T", "Y", "|", "W", "X", "M"]

# for helping input validation
def selection_is_legal(string: str)-> bool:
    """ Validates if all elements in a sequence belong to our 'weapons' list """
    for character in string: # for all characters in string
        if character.casefold() not in [weapon.casefold() for weapon in weapons]:
            return False
    return True

# request user to select 6 weapons
def select_weapon(team:str)->str:
    """ gather a set of 6 weapons for a given team """
    print(f"Select the 6 weapons used by {team}.")
    while True:
        weapon_set = input()
        if len(weapon_set) == 6:
            if selection_is_legal(weapon_set):
                return weapon_set
            else: 
                print("One or more of the selected weapons are invalid. Please try again.")
        elif len(weapon_set) < 6:
            print("You are selecting less than 6 weapons. Please try again.")
        else:
            print("You are selecting more than 6 weapons. Please try again.") 

def blinded_watchmaker(shifts: int)->str:
    """ 
    Returns a sequence of random weapons for each clock change
    
    Arguments:
        shifts: will set the amount of turns (the lenght of the resulting string)
    """
    "".join()


def testing():
    team_1 = select_weapon("team_1")
    print(team_1,)
    
    
    
    # print("Hello, World!")
    
def main():
    print("Hello, World!")
    
if __name__ == "__main__":
    testing()
    # main()


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               

