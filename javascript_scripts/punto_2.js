const prompt = require('readline-sync').question;

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

function setPromedio() {
    if (estudiantes.length === 0) {
        console.log(" No hay estudiantes para modificar.");
        return;
    }
    // Pedimos la posición
    let inputPos = prompt("Ingresa posicion de la fila (0, 1, 2): ");
    let posicion = parseInt(inputPos);

    // Validamos la posición
    if (!isNaN(posicion) && posicion >= 0 && posicion < estudiantes.length) {
        
        // Pedimos el nuevo promedio
        let newP = prompt(`Ingresa el nuevo promedio para ${estudiantes[posicion].nombre}: `);
        let nuevoPromedio = parseFloat(newP.replace(",", "."));

        if (!isNaN(nuevoPromedio)) {
            
            estudiantes[posicion].promedio = nuevoPromedio;
            
            console.log(`El promedio de ${estudiantes[posicion].nombre} ahora es ${nuevoPromedio}.`);
            console.log(" ");
            console.log("--- Listado actualizada ---");
            estudiantes.forEach(e => e.mostrarInfo());
        } else {
            console.log("ERROR: El promedio ingresado no es un número válido.");
        }
    } else {
        console.log(`ERROR: La posición ${inputPos} no es válida.`);
    }
}

// Modificación con el metodo setPromedio
console.log("\n--- Actualizando nota ---");
setPromedio()
