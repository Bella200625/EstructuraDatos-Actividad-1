class Estudiante:
    def __init__ (self, nombre, edad,promedio):
        self.nombre = nombre
        self.edad = edad
        self.promedio = promedio

# Método para mostrar información
    def mostrarInfo(self):
        print(f"Estudiante: {self.nombre} | Edad: {self.edad} | Promedio: {self.promedio}")

# Método para modificar el promedio 
    def setPromedio(self, nuevo_promedio):
        self.promedio = nuevo_promedio

# se han creado 3 instancias y se han almacenado 
# en un arreglo/lista.
estudiantes = [
    Estudiante("Marinet", 19, 4.5),
    Estudiante("Rosita", 18, 3.8),
    Estudiante("Alia", 19, 4.2)
]

# LLamaremos al metodo
print ("-------- Estudiantes --------")
for e in estudiantes:
    e.mostrarInfo()


#modificar con metodo
print("--- Promedio modificado ---")
estudiantes[1].setPromedio(4.0)
estudiantes[1].mostrarInfo()