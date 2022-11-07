class Chore:
    def __init__(self, name, body):
        self.name=name
        self.body_chore = body
    def actualize(self,new_name,new_description):
        self.name=new_name
        self.body_chore=new_description
    def show(self):
        print(f"\nName: {self.name}\nDescription: {self.body_chore}")