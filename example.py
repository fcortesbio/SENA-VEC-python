# example for explaining classes and methods in Python

# Obtener la longitud de una lista
frutas = ["mango", "banana", "manzana"]
longitud = len(frutas)
print("La longitud de la lista es: ", longitud)

# Convertir una cadena en Mayúsculas
nueva_cadena = frutas[0].upper()
print("Esta es una fruta mayúscula: ", nueva_cadena)

class Persona:
# Aquí se definen los atributos de la clase Persona
    def __init__(self, nombre, edad):
        self.nombre = nombre 
        self.edad = edad
        self.pasos = 0 # Este atributo representa los pasos que ha recorrido una 'Persona' 

# Definir el método 'caminar'que .
    def caminar(self):
        self.pasos += 10
        print(f"{self.nombre} acaba de dar 10 pasos. Pasos totales: {self.pasos}")

# Crear un objeto de la clase Persona, nombre: "Andres", edad: 30 
andres = Persona("Andres", 30) 

# Invocar el método caminar para el objeto Andres
andres.caminar()