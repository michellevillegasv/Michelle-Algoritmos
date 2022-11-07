from participante import Participante
class Libre(Participante):
    def __init__(self, name, type, category, number, register, talent):
        super().__init__(name, type, category, number, register)
        self.talent= talent
    def show(self):
        print(f"\nName: {self.name}\nSolo or Group: {self.type}\nCategory: {self.category}\nCellphone number: {self.number_cellphone}\nRegister Number: {self.register_number}\nTalent: {self.talent}")