from dataclasses import dataclass

# Declaración 
@dataclass
class Estudiante:
    nombre: str
    edad: int
    promedio: float

# Inicialización 
E1 = Estudiante("Marino", 19, 4.6)
E2 = Estudiante("Nino", 21, 4.8)
E3 = Estudiante("Yuleka", 20, 3.2)


# Guardar en arreglo
estudiantes = [E1, E2, E3] 

# Recorrido
print("--- Lista de Estudiantes ---")

for e in estudiantes:

    print(f"Nombre: {e.nombre}, Edad: {e.edad}, Promedio: {e.promedio}")

# Modificación 
estudiantes [2].promedio = 5.0
print (f"El promedio del {estudiantes [2].nombre} ha sido modificado: {estudiantes[2].promedio} ")

print("--- Lista de Estudiantes ---")

for e in estudiantes:

    print(f"Nombre: {e.nombre}, Edad: {e.edad}, Promedio: {e.promedio}")