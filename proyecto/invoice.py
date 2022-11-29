class Invoice: 
    def __init__(self, name, id, products, discount, subtotal, total):
        self.name=name
        self.id=id
        self.products=products
        self.discount=discount
        self.subtotal=subtotal
        self.total=total
    def show(self):
        print("---INVOICE---")
        print(f"\nName: {self.name}\nID: {self.id}\nProducts:")
        for products in self.products:
            print(f"-{products}")
        print(f"Subtotal: {self.subtotal}\nDiscount: {self.discount}\nTotal: {self.total}")