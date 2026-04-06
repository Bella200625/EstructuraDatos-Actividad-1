class Heroe: 
    def __init__(self, nombre, miraculous, concepto, fase):
        self.nombre = nombre
        self.miraculous = miraculous
        self.concepto = concepto
        self.fase = fase

    def listaMaestra (self):
        print ("==o==o===||====o===o===o====||====o===o===o====||====o===o==")
        print (" ")
        print(f"Nombre de herore: {self.nombre} ")
        print(f"Miraculous: {self.miraculous} ")
        print(f"Concepto del Kwamis : {self.concepto} ")
        print(f"Fase : {self.fase[0][1]} (Nivel {self.fase[0][0]})")
        print(f"Estado: {self.fase[1][1]} ({self.fase[1][0]}% confianza)")
        print (" ")
        

ListaHeroe = [
    Heroe("Ladybug", "Tikki", "Creacion", [[4, " Experta"], [90, "Activo"]]),
    Heroe("Cat Noir", "Plagg", "Destrucion", [[3, " Avanzada"], [85, "Activo"]]),
    Heroe("Bunnix", "Fluff", "Evolucion", [[5, " Maestra"], [100, "Estable"]]),
    Heroe("Viperion", "Sass", "Intuicion", [[3, " Avanzada"],[0, "Inactivo"]]),
    Heroe("Rena Rouge", "Trixx", "Ilusion", [[3, " Avanzada"], [80, "Activo"]]), 
    Heroe("Vesperia", "Pollen", "Accion", [[2, " Intermedia"], [65, "Activo"]])
]

#llamemos metodo lista_Maestra 
for prodigio in ListaHeroe:
    prodigio.listaMaestra()