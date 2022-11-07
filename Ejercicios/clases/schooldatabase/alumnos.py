class Student:
    def __init__(self, name, year, average, direction, parents_name, parents_cellphone, scholarship):
        self.name= name
        self.year= year
        self.average= average 
        self.direction= direction
        self.parents_name= parents_name
        self.parents_cellphone= parents_cellphone
        self.scholarship = scholarship
    def show(self):
        print(f"\nName: {self.name}\nYear: {self.year}\nAverage: {self.average}\nDirection: {self.direction}\nParent's Name: {self.parents_name}\nParent's Cellphone: {self.parents_cellphone}\nScholarship: {self.scholarship}")