class Participante:
    def __init__(self, name, type, category, number, register):
        self.name = name
        self.type = type
        self.category = category
        self.number_cellphone= number
        self.register_number = register
    def show(self):
        print(f"\nName: {self.name}\nSolo or Group: {self.type}\nCategory: {self.category}\nCellphone number: {self.number_cellphone}\nRegister Number: {self.register_number}")