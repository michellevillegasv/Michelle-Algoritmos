class Person:
    def __init__(self,charge, name, last_name,sections):
        self.name= name
        self.last_name = last_name
        self.sections = sections
        self.charge=charge
class Professor(Person): 
    def __init__(self, charge, name, last_name, sections,ci):
        super().__init__(charge, name, last_name, sections)
        self.ci=ci
    def show(self):
        print(f"\nName: {self.name}\nLast Name: {self.last_name}\nStatus: {self.charge}\nID: {self.ci}\nSections: {self.sections}")
class Student(Person): 
    def __init__(self, charge, name, last_name, sections,carnet, preparador):
        super().__init__(charge, name, last_name, sections)
        self.carnet = carnet
        self.preparador=preparador
    def show(self):
        print(f"\nName: {self.name}\nLast Name: {self.last_name}\nStatus: {self.charge}\nPreparador: {self.preparador}\nID: {self.carnet}\nSections: {self.sections} ")