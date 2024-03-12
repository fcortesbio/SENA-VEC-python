# TALLER 2 PYTHON
# AUTOR: Fabián Andrés Cortés Tróchez
# Fecha: 2024 - 03 - 12

from datetime import date
current_date = date.today()
print(f"El día de hoy es", current_date)

def get_int(prompt: str)-> int:
    """ Para facilitar la validación de datos de entrada """
    print(prompt)
    while True:
        try: 
            number = int(input()) 
            return number
        except ValueError:  # Si el valor ingresado no se puede almacenar como 'int'
            print("Entrada invalida. Por favor ingresa un número entero.")

a = get_int("Digite el primer número entero: ")
b = get_int("Digite el segundo número entero: ")
c = get_int("Digite el tercer número entero: ")

x = [a, b, c]
if a == b == c: 
    print(f"Todos los valores en la lista son iguales, la suma de los valores es {sum(x)}")
else: 
    print(f"El valor máximo es {max(x)}, mientras que el valor mínimo es {min(x)}")
    print(f"La lista tiene {len(x)} elementos, que suman un total de: {sum(x)}")
    print(f"El valor promedio de la lista es: {round(sum(x)/len(x), 3)}") 

print("Ahora ingresa un número decimal:")
while True:
    try: 
        z = float(input())
        print(f"El valor de z redondeado es: {round(z)}")
        break
    except ValueError:
        print("El valor que ingresaste no es válido. Por favor ingresa un número decimal.") 

print("Escribe una oración:")
frase = input()

variants = {
    'letras mayúsculas': frase.upper(),
    'letras minúsculas': frase.upper(),
    'letras codificadas': frase.encode(),
    'letra títular': frase.title(),
    'letra capitular': frase.capitalize(),
    'letras intercambiadas': frase.swapcase()
}

for variant, result in variants.items():
    print(f"Así luce tu frase convertida a {variant}: {result} ")

print("Fin.")