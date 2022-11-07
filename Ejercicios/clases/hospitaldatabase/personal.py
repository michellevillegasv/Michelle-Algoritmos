from re import A


class Personal:
    def __init__(self, type, name, age, instruccion):
        self.type_personal  = type
        self.name = name
        self.age = age
        self.grado_instruccion = instruccion
class Doctor(Personal):
    def __init__(self, name, age, instruccion, especializacion, turno, consultorio):
        super().__init__("Doctor", name, age, instruccion)
        self.especializacion = especializacion
        self.turno = turno
        self.consultorio = consultorio
class Enfermera(Personal):
    def __init__(self, name, age, instruccion, turno):
        super().__init__("Enfermera", name, age, instruccion)
        self.turno_enfermera = turno
class Vigilancia(Personal):
    def __init__(self, name, age, instruccion, turno):
        super().__init__("Vigilancia", name, age, instruccion)
        self.turno_vigilancia = turno
class Limpieza(Personal):
    def __init__(self, name, age, instruccion, turno):
        super().__init__("Limpieza", name, age, instruccion)
        self.turno_limpieza = turno
