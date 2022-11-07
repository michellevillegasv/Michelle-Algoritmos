class Vendedor:
    def __init__(self, product_id, customer_id, amnt):
        self.product_id = product_id
        self.customer_id = customer_id
        self.amount = amnt
    def show(self):
        print(f"\nAmount: {self.amount}\nCustomer ID: {self.customer_id}\nProduct ID: {self.product_id}")