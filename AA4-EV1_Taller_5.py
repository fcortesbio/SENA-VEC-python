# Taller 5 Python
# Autor: Fabián Andrés Cortés Tróchez
# Fecha: 2024 - 03 - 20

from datetime import date
import time
current = date.today()
global_delay = 0.034

def snap(seconds:float = None)-> None:
    seconds = seconds if seconds is not None else global_delay 
    time.sleep(seconds)

def puts(prompt: str)-> None:
    """ A funny use of for loops in scripted programs """
    for char in prompt:
        print(char, end='', flush=True)  
        snap()
    print()

def get_number(prompt: str = None) -> int:
    puts("Ingresa un número:\n" if prompt is None else f"{prompt}\n")
    while True:
        try:
            return int(input())
        except ValueError:
            puts("Por favor ingresa un número.")
    
def main()-> None:
    # Displaying today's date
    puts(f"Hoy es el día: {current}.")
    
    # getting num1 from input
    num1 = get_number("Ingresa el valor de a:")
    puts("Ahora ingresa el valor de b:")
    
    # getting num2 from input; num2 must be higher than num1 
    while True:
        num2 = get_number("")
        if num2 <= num1: 
            puts(f"Por favor ingresa un valor mayor que {num1}:")
        else: 
            break
    
    # displaying gathered values
    puts(f"Nuestros valores serán: a = {num1} y b = {num2}.")
    puts("Presiona 'Enter' para continuar.")
    input("\n")

    # for i in range(a)
    puts(f"Ciclo para los números del 1 hasta {num1}:")
    for i in range(num1): 
        print(i+1)  # adding one because range list are 0-based
        snap(0.5)
    puts("Fin del ciclo.")
    puts("Presiona 'Enter' para continuar.")
    input("\n")
    
    # for i in range(a, b)
    puts(f"Ciclo para los números entre el {num1} y el {num2}")
    for i in range (num1, num2): # cicle with inner and outer limits
        print(i)
        snap(0.5)
    puts("Fin del ciclo.")
    puts("Presiona 'Enter' para continuar.")
    input("\n")

    # for i in range(a, b, steps)
    puts("Ciclo desde a hasta b con saltos de 2:")
    for i in range(num1, num2, 2):
        print(i)
        snap(0.5)
    puts("Fin del ciclo.")

    puts("Presiona 'Enter' para continuar.")
    input("\n")

    # for element in iterable:
    puts("Digita el nombre de la empresa:")
    empresa = input()
    for char in empresa.upper():
        print(char)
        snap(0.5)
    puts("Fin del ciclo.")

    puts("FIN.")

if __name__ == "__main__":
    main()