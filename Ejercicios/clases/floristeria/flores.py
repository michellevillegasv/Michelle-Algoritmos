class Flower:
    def __init__(self, type,id, name, stock, colors):
        self.type= type
        self.id= id
        self.name=name
        self.stock=stock
        self.colors=colors
    def actualize(self, stock1):
        self.stock = stock1
    def show(self):
        print(f"\n---{(self.type).upper()}--- \nId: {self.id}\nName: {self.name}\nStock: {self.stock}")
        print('Colors:')
        for colors in self.colors:
            print (colors)


        