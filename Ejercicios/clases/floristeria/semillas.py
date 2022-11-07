class Seed:
    def __init__(self,type, id, name, stock):
        self.type=type
        self.id=id
        self.name=name
        self.stock=stock
    def actualize(self, stock1):
        self.stock= stock1
    def show(self):
        print(f"\n---{(self.type).upper()}---\nId: {self.id}\nName: {self.name}\nStock: {self.stock}")
        