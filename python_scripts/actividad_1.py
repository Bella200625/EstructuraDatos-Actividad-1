from dataclasses import dataclass

# Declaración 
@dataclass
class Estudiante:
    nombre: str
    edad: int
    promedio: float

# Inicialización 
E1 = Estudiante("Bella", 19, 4.5)
E2 = Estudiante("Juan", 21, 3.8)
E3 = Estudiante("Maria", 20, 4.2)
