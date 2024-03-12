# TALLER 1 PYTHON
# AUTOR (A): Fabian Andres Cortes Tróchez
# FECHA: 2024-03-11

from datetime import date

print("¿Cómo te llamas?")  #   
while True:
    username = input()
    if username == "":  # user cannot be empty
        print("El nombre no puede estar vacío, por favor intenta nuevamente", end="\n")
    else:
        username = username.capitalize()
        print(f"¡Gusto conocerte {username}!")
        break

current_date = date.today() 
print(f"La fecha de hoy es: {current_date}.") # mostrar fecha actual

print("Digita el primer número:") 
while True: # input validation; n1 has to be an int value
    try: 
        n1 = int(input(""))
        break
    except ValueError:
        print("Este valor no es valido. Por favor ingresa un número entero.")
        
print("Digita el segundo número:")
while True:  # input validation; n2 has to be an int, non-zero value
    try: 
        n2 = int(input())
        if n2 == 0: # if input value is 0
            print("Por favor ingresa un valor diferente de cero.")
        else:
            break
    except ValueError: # if input can't be converted to 'int'
        print("Por favor ingresa un número entero.")

# Python numeric operators
results = {
    "suma": n1 + n2,
    "concatenación": str(n1) + str(n2),
    "resta": n1 - n2,
    "inversión de signo": -n1,
    "producto": n1 * n2,
    "division": n1 / n2,
    "multiplicación de cadenas": username * n1,  # In case n1 is used as a string
    "división de enteros": n1 // n2,
    "module": n1 % n2
}

# Print results
print("Gracias. Ahora realicemos algunas operaciones con estos datos:", end = "\n\n")
for operation, result in results.items():
    print(f"El resultado de la operación '{operation}' es: {result}", end="\n")
    
print("FIN")