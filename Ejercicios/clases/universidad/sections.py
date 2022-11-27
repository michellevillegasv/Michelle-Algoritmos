class Section:
    def __init__(self, name, code, classroom, schedule,day,section):
        self.name=name
        self.code=code
        self.classroom=classroom
        self.schedule = schedule
        self.day=day
        self.number_section=section
class Prepa(Section):
    def __init__(self, name, code, classroom, schedule, day, section,preparador):
        super().__init__(name, code, classroom, schedule, day, section)
        self.preparador = preparador
    def show(self):
        print(f"\nAsignature Name: {self.name}\nAsignature Code: {self.code}\nPreparador: {self.preparador}\nClassroom:{self.classroom}\nSchedule: {self.day}-{self.schedule}\nSection:")
        for sections in self.section:
            print(sections,end=",")
class Clase(Section):
    def __init__(self, name, code, classroom, schedule, day, section,professor):
       super().__init__(name, code, classroom, schedule, day, section)
       self.professor=professor
    def show(self):
        print(f"\nAsignature Name: {self.name}\nAsignature Code: {self.code}\Professor: {self.professor}\nClassroom:{self.classroom}\nSchedule: {self.day}-{self.schedule}")
