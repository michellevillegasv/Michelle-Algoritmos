class Restaurant:
    def __init__(self, name,products) -> None:
        self.name=name
        self.products=products
    def show(self):
        for products in self.products:
            print(products.show())