from producto import Product
class Food(Product):
    def __init__(self, name, price, type, mode):
        super().__init__(name, price, type)
        self.mode=mode
    def show(self):
        print(f"\nName: {self.name}\nPrice:{(self.price)+((self.price)*0.16)}\nType: {self.type}\nMode: {self.mode}")

        