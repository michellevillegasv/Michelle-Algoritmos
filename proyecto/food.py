from producto import Product
class Food(Product):
    def __init__(self, name, price, type, quantity, mode,sold):
        super().__init__(name, price, type, quantity)
        self.mode=mode
        self.sold=sold
    def show(self):
        print(f"\nName: {self.name}\nQuantity: {self.quantity}\nPrice:{(self.price)+((self.price)*0.16)}\nType: {self.type}\nMode: {self.mode}")
    def show_menu(self):
        print(f"-----------\nName: {self.name}\nPrice: {self.price}\n-----------")
        