# Taller 4 - Python
# Autor: Fabián Andrés Cortés Tróchez
# Fecha 2024 - 03 - 18

from datetime import date
current = date.today()
print("Hoy es el día, ", current, end="\n\n")

def get_number(prompt: str = None) -> int:
    """ Validación de datos de entrada para números enteros """
    while True:
        try:
            return int(input("Ingresa un número:\n" if prompt is None else f"{prompt}\n"))
        except ValueError:
            print("Por favor ingresa un número.")

def triangle_class(a: int,b: int,c: int)-> str:
    """ Clasifica un triangulo dadas las relaciones de longitudes de sus 3 lados """
    if a == b == c: # all sides are equal
        return "equilatero"
    else: 
        if a == b or c == b or a == c:
            return "isoceles"
        else:
            return "escaleno"

triangle = triangle_class(get_number(),get_number(),get_number())
print(f"El triangulo es {triangle}.\n")

animal = input("Nombra tu animal favorito:\n").upper()
if animal == "PERRO":
    print("Este animal es el mejor amigo del hombre:", animal)
elif animal == "GATO": 
    print("Este animal tiene unos reflejos increíbles: ", animal)
elif animal == "OSO":
    print("Este animal es peligroso, pero hermoso: ", animal)
else: 
    print("Este animal no es PERRO, no es GATO, ni es OSO", animal)
    
print("\nFIN.")