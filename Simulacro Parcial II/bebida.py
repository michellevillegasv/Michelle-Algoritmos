class Beverage():
    def __init__(self,name,price,type):
        self.name=name
        self.price=price
        self.type=type
class Alcoholic(Beverage):
    def __init__(self, name, price, type, percent):
        super().__init__(name, price, type)
        self.alcoholic_percent=percent
    def show(self):
        print(f"---{self.name}\nPrice: {self.price}\Type: {self.type}\nAlcoholic Percent: {self.alcoholic_percent}")
class NonAlcoholic(Beverage):
    def __init__(self, name, price, type,temp):
        super().__init__(name, price, type)
        self.temperature=temp
    def show(self):
        print(f"---{self.name}\nPrice: {self.price}\nType: {self.type}\nTemperature: {self.temperature}")
