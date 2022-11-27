from producto import Product
class Beverage(Product):
    def __init__(self, name, price, type,alcoholic):
        super().__init__(name, price, type)
        self.alcoholic=alcoholic
    def show(self):
        print(f"\nName: {self.name}\nPrice: {(self.price)+((self.price)*0.16)}\nType: {self.type}\nAlcoholic {self.alcoholic}")