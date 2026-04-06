class Estudiante:
    def __init__ (self, nombre, edad,promedio):
        self.nombre = nombre
        self.edad = edad
        self.promedio = promedio

# Método para mostrar información
    def mostrarInfo(self):
        print(f"Estudiante: {self.nombre} | Edad: {self.edad} | Promedio: {self.promedio}")

# Método para modificar el promedio 
def setPromedio():
        if not estudiantes:
            print(">> No hay estudiantes para modificar.")
            return
        try: 
            posicion = int (input ("Ingresa posicion de la fila del estudiante al que le quieras cambiar el promedio (0, 1, 2): "))

            if 0 <= posicion < len(estudiantes):
                entrada = input(f"Ingresa el nuevo promedio para {estudiantes[posicion].nombre}: ")
                nuevoPromedio = float(entrada.replace(",", "."))

                estudiantes[posicion].promedio = nuevoPromedio
            
                print(f">> El promedio de {estudiantes[posicion].nombre} ahora es {nuevoPromedio}.")
            else:
            # Si el usuario mete un número como 8 y solo hay 3 estudiantes
                print(f">> ERROR: La posición {posicion} no existe. Intenta con un número entre 0 y {len(estudiantes)-1}.")
        except ValueError: 
            print("Invalido.")


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
setPromedio()