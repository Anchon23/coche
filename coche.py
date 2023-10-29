class Vehiculo():
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return "Color {}, {} ruedas".format(self.color, self.ruedas)

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return super().__str__() + ", {} km/h, {} cc".format(self.velocidad, self.cilindrada)

def catalogar(vehiculos, ruedas=None):
    if ruedas is None:
        print("Catálogo de vehículos:")
    else:
        print("Se han encontrado {} vehículos con {} ruedas:".format(
            sum(1 for vehiculo in vehiculos if vehiculo.ruedas == ruedas), ruedas))
    for vehiculo in vehiculos:
        if ruedas is None or vehiculo.ruedas == ruedas:
            print("Clase: {} - Descripción: {}".format(type(vehiculo).__name__, str(vehiculo)))

vehiculo1 = Vehiculo("rosa", 4)
coche1 = Coche("Azul", 4, 250, 2200)
vehiculo2 = Vehiculo("Verde", 4)
coche2 = Coche("Amarillo", 4, 180, 1400)

vehiculos = [vehiculo1, coche1, vehiculo2, coche2]

catalogar(vehiculos)

catalogar(vehiculos, 4)
