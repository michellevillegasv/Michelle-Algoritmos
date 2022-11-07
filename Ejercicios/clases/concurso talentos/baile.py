from participante import Participante
class Baile(Participante):
    def __init__(self, name, type, category, number, register, style):
        super().__init__(name, type, category, number, register)
        self.style=style
    def show(self):
        print(f"\nName: {self.name}\nSolo or Group: {self.type}\nCategory: {self.category}\nCellphone number: {self.number_cellphone}\nRegister Number: {self.register_number}\nStyle: {self.style}")