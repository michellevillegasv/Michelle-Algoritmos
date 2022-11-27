class Vehicle:
    def __init__(self, placa,marca,puesto,hora_entrada):
        self.placa = placa
        self.marca=marca
        self.puesto=puesto
        self.hora_entrada=hora_entrada
        self.hora_salida= None
class Car(Vehicle):
    def __init__(self, placa, marca, puesto, hora_entrada, misnuvalido):
        super().__init__(placa, marca, puesto, hora_entrada)
        self.minusvalido=misnuvalido
    def show(self):
        print(f"\nPlaca: {self.placa}\nMarca: {self.marca}\nPuesto: {self.puesto}\nEntrada: {self.hora_entrada}\nSalida: {self.hora_salida}\nMinusvalido: {self.minusvalido}")
class Motorcycle(Vehicle):
    def __init__(self, placa, marca, puesto, hora_entrada):
        super().__init__(placa, marca, puesto, hora_entrada)
    def show(self):
        print(f"\nPlaca: {self.placa}\nMarca: {self.marca}\nPuesto: {self.puesto}\nEntrada: {self.hora_entrada}\nSalida: {self.hora_salida}")
        