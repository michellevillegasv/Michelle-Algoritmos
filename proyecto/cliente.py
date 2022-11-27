class Client:
    def __init__(self, name,id,age,match,type_ticket,vampiro_id,perfect_id):
        self.name=name
        self.id=id
        self.age=age
        self.match=match
        self.type_tickets=type_ticket
        self.vampiro_id= vampiro_id
        self.perfect_id=perfect_id
    def confirmation_client(self):
        print("---TICKET---")
        print(f"\nSeat: {self.seat}\nMatch {self.match}\n Ticket: {self.type_tickets}\nSubtotal: {self.total}\nDiscount:{self.discount} \nIVA: 16%\nTotal: {self.total-{self.total*self.discount}+{self.total*0.16}}")
        