// Declaramos la Clase
class Estudiante {
    constructor(nombre, edad, promedio) {
        this.nombre = nombre;
        this.edad = edad;
        this.promedio = promedio;
    }

    // Creamos metodo para mostrar informacion
    mostrarInfo() {
        console.log(`Estudiante: ${this.nombre} | Edad: ${this.edad} | Promedio: ${this.promedio}`);
    }

    // Creamos el método para modificar el promedio 
    setPromedio(new_promedio) {
        this.promedio = new_promedio;
    }
}

// Inicializamos e instanciamos en un arreglo
const estudiantes = [
    new Estudiante("Lila", 19, 4.5),
    new Estudiante("Kloe", 21, 2.1),
    new Estudiante("Viperion", 20, 4.2)
];

// llamamos el metodo mostrarInfo
console.log("--- Listado de Estudiantes ---");
estudiantes.forEach(e => e.mostrarInfo());

// Modificación con el metodo setPromedio
console.log("\n--- Actualizando nota ---");
estudiantes[1].setPromedio(4.0);
estudiantes[1].mostrarInfo();