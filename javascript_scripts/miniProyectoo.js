class Heroe {
    constructor(nombre, miraculous, concepto, fase) {
        this.nombre = nombre;
        this.miraculous = miraculous;
        this.concepto = concepto;
        this.fase = fase;
    }

    listaMaestra() {
        console.log("==o==o===||====o===o===o====||====o===o===o====||====o===o==");
        console.log(" ")
        console.log(`Nombre de heroe: ${this.nombre}`);
        console.log(`Miraculous: ${this.miraculous}`);
        console.log(`Concepto del Kwami: ${this.concepto}`);
        // Indexación doble [fila][columna] para limpiar la salida
        console.log(`Fase : ${this.fase[0][1]} (Nivel ${this.fase[0][0]})`);
        console.log(`Estado: ${this.fase[1][1]} (${this.fase[1][0]}% confianza)`);
    }
}

// Creamos el Arreglo de Objetos
const ListaHeroe = [
    new Heroe("Ladybug", "Tikki", "Creacion", [[4, "Experta"], [95, "Activo"]]),
    new Heroe("Cat Noir", "Plagg", "Destrucion", [[3, "Avanzada"], [85, "Activo"]]),
    new Heroe("Bunnix", "Fluff", "Evolucion", [[5, "Maestra"], [100, "Estable"]]),
    new Heroe("Viperion", "Sass", "Intuicion", [[3, "Avanzada"], [0, "Inactivo"]]),
    new Heroe("Rena Rouge", "Trixx", "Ilusion", [[3, "Avanzada"], [90, "Activo"]]),
    new Heroe("Vesperia", "Pollen", "Accion", [[2, "Intermedia"], [70, "Activo"]])
];

// El Recorrido Usando forEach 
ListaHeroe.forEach(prodigio => {
    prodigio.listaMaestra();
});