from participante import Participante
class Canto(Participante):
    def __init__(self, name, type, category, number, register, song, author):
        super().__init__(name, type, category, number, register)
        self.song = song
        self.author = author
    def show(self):
        print(f"\nName: {self.name}\nSolo or Group: {self.type}\nCategory: {self.category}\nCellphone number: {self.number_cellphone}\nRegister Number: {self.register_number} \nSong: {self.song}-{self.author}")