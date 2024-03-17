# Challenge 1 — Pixel Gun Apocalypse 
# Author : Fabián Andrés Cortés Tróchez
# Date: 2024 - 03 - 12

import random
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
            if len(string) == 6: # lenght must be 6
                if check_select(string): # input character validation
                    return string
                else:
                    print("Selección inválida, intenta nuevamente.") # error message for illegal characters
                    strikes -= 1
            else:
                print("Debes seleccionar 6 armas.") # error message for illegal lenght
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

def report_score(V, F):
    if V == F: 
        return "≈"
    elif V > F:
        return "V"
    else:
        return "F" 
    
def main() -> str:
    # getting weapons for each team from inputs
    print("Selecciona las armas para el Equipo 1")
    team1_weapons = get_weapon()
    print("Selecciona las armas para el Equipo 2")
    team2_weapons = get_weapon()
    # getting a clock from input, or generate 20 if Global random is True
    clock = get_clock() if not random_mode else rand_clock(20)
    # define starting values for scores
    score1 = 0
    score2 = 0 
    # empty list
    output = [] 
    # iterate on clock to get and report scores
    for character in clock: # runs the following for each character in clock
        if character in team1_weapons:
            score1 += 1 # add 1 to score1 if this turn's character is in team1_weapons
        if character in team2_weapons:
            score2 += 1 # add 1 to score2 if this turn's character is in team2_weapons
        output.append(report_score(score1, score2))
        string = "".join([letter for letter in output])
    return string   

if __name__ == "__main__":
    match = main()
    print(match)                                                                                                                                     
