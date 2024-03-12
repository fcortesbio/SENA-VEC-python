# Challenge 1 — Pixel Gun Apocalypse 
# Author : Fabián Andrés Cortés Tróchez
# Date: 2024 - 03 - 12

weapons = [".", "-", "+", "*", "T", "Y", "|", "W", "X", "M"]

def selection_is_legal(string: str)-> bool:
    """ check if all weapons selected by a team are in the list of allowed weapons """
    for character in string:
        if character not in weapons:
            return False
    return True

def select_weapon()->str:
    """ gather a set of 6 weapons for a given time """
    print("Enter your selection of weapons.")
    while True:
        weapon_set = input()
        if len(weapon_set) == 6:
            if selection_is_legal:
                return weapon_set
            else: 
                print("One or more of the selected weapons are invalid. Please try again.")
        else: 
            print("The amount of weapons has to be 6 in total.")

def blinded_watchmaker(shifts: int):
    """ generate a random sequence of effective weapons for each clock change """
    

           


def testing():
    print("Hello, World!")
    
    
    
def main():
    print("Hello, World!")
    
if __name__ == "__main__":
    testing()
    # main()


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               

