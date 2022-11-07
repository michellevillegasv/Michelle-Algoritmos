class Section:
    def __init__(self, name, code, classroom, schedule):
        self.name=name
        self.code=code
        self.classroom=classroom
        self.schedule = schedule
class Prepa(Section):
    def __init__(self, name, code, classroom, schedule, preparador,section):
        super().__init__(name, code, classroom, schedule)
        self.preparador = preparador
        self.section=section
    def show(self):
        print(f"\nAsignature Name: {self.name}\nAsignature Code: {self.code}\nPreparador: {self.preparador}\nClassroom:{self.classroom}\nSchedule: {self.schedule}\nSection:")
        for sections in self.section:
            print(sections,end=",")
class Clase(Section):
    def __init__(self, name, code, classroom, schedule, professor):
        super().__init__(name, code, classroom, schedule)
        self.professor=professor
    def show(self):
        print(f"\nAsignature Name: {self.name}\nAsignature Code: {self.code}\Professor: {self.professor}\nClassroom:{self.classroom}\nSchedule: {self.schedule}")
