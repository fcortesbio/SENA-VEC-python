# Taller 3 - Python
# Autor: Fabián Andrés Cortés Tróchez
# Fecha: 2024 - 03 - 18

from datetime import date
current = date.today()

print("Hoy es", current)

def get_number():
    while True:
        try: 
            number = int(input())
            return number
        except ValueError:
            print("Por favor ingresa un número.")

print("Ingresa el valor de A:")
a = get_number()
print("Ingresa el valor de B:")
b = get_number()

print("A es mayor o igual a B" if a >= b else "A es menor que B", sep="\nn")

cursos = {1: "Requerimientos", 2:"Algoritmos"}

for clave, curso in cursos.items():
    print(f"el curso {clave} es: {curso}")

if (cursos[1], cursos[2]) == ("Requerimientos", "Algoritmos"):
    print("Usted estudia Desarrollo de Software.")
else:
    print("Usted estudia un programa distinto a Desarrollo de Software", end="\n\n")
    
print("*** Fin del Análisis del Programa de Formación SENA ***", end="\n\n")

print("Digita una oración:")
phrase = input()

def evaluate_lenght(string)->str:
    return "menos de 10" if len(string) < 10 else ("más de 20" if len(string) > 20 else "entre 10 y 20")

print(f"\nLa frase en mayúsculas es: {phrase.upper()}")
print(f"Esta frase contiene {evaluate_lenght(phrase)} caracteres.")
print(f"Esta  frase tiene exactamente {len(phrase)} caracteres.\n")

print()
print("FIN.")