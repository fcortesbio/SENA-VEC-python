# Taller 6 Python - Ciclo While
# Autor: Fabián Andrés Cortés Tróchez
# Fecha: 2024 - 03 - 20

from datetime import date
import time
import random
current = date.today()

def get_number(prompt: str = None, min: int = None, max: int = None) -> int:
    prompt = prompt if prompt is not None else "Enter a number:\n"
    print(prompt)
    while True:
        try:
            number = int(input())
            if (min is not None and number < min) or (max is not None and number > max):
                raise ValueError(f"Number must be between {min} and {max}.")
            else:
                print(f"Saved value is: {number}.")
                return number
        except ValueError as e:
            print(f"Invalid input. {e}. Please enter a number:")

def main()-> None:
    # outputting current date 
    print("Today is: ", current, end="\n")
    print("Taller 6 - Ciclos iterativos usando la sentencia 'while'", end="\n\n")
    
    # Counter-driven cycles.
    print("** Ciclos controlados por contadores **")
    
    i = 15 # stablish a base case
    num1 = get_number()
    while num1 == i:
        print("Por favor elige un número diferente.")
        num1 = get_number("")
    if num1 > i:
        while num1 != i:
            print("i = ", i, ". adding unit (+1)")
            time.sleep(0.4)
            i += 1
    else: 
        while num1 != i:
            print("i = ", i, ". subtracting unit (-1)")
            time.sleep(0.4)
            i -= 1       
    print("i =", i, ". The base case has been reached.\n")

    print("Press 'Enter' to continue.")
    input("\n")
    
    # Event-driven cycles
    print("** Event-driven cycle. **")
    print("Let's play a game.", "Can you guess what's the lucky number?", sep="\n")
    
    attempts = 1  # counter of attempts starts in 1   
    lucky_number = random.choice(range(1,10))
    
    print("Please enter a number between 1 to 10:")
    user_choice = get_number("", 1, 10)
    if user_choice == lucky_number:
        print("Awesome! You guessed the number in your first attempt!")
    else:      
        while user_choice != lucky_number:
            print("Sorry, that's not the lucky number. Let's try again.", "Please enter a number between 1 to 10:", sep="\n\n")
            user_choice = get_number("", 1, 10)
            attempts += 1
        print(f"Congratulations! You've guessed the number after {attempts} attempts.")
        print("Game is over.\n")
    
    print("Press 'Enter' to continue.")
    input("\n")    
    
    # Cycle interruption using keywords    
    print("** Cycle interrupted with 'break' keyword. **")
    friend_name = input("Enter the name of a friend:\n")
    friend_name = friend_name.upper()
    
    for character in friend_name:
        print(character)
        time.sleep(0.5)
        if character == "A":
            print("Interrupted because the letter 'A' was found.")
            break
    
    print("End of the cycle.\n")
    print("End of the program.")
    
if __name__ == "__main__":
    main()