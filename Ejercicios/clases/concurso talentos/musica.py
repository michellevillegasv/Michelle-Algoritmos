from participante import Participante
class Musica(Participante):
    def __init__(self, name, type, category, number, register, instrument):
        super().__init__(name, type, category, number, register)
        self.instrument= instrument
    def show(self):
        print(f"\nName: {self.name}\nSolo or Group: {self.type}\nCategory: {self.category}\nCellphone number: {self.number_cellphone}\nRegister Number: {self.register_number}\nInstrument(s): {self.instrument}")