class Ticket:
    def __init__(self,name_client,id_client, code,fila_seat,columna_seat,subtotal,discount,total):
        self.name=name_client
        self.id_client=id_client
        self.code=code
        self.fila_seat = fila_seat
        self.columna_seat = columna_seat
        self.subtotal=subtotal
        self.discount=discount
        self.total=total
    def confirmation_show(self):
        print("\t---TICKET---")
        print(f"Name: {self.name}\nID: {self.id_client}\nCODE: {self.code}\nSeat: {self.fila_seat}-{self.columna_seat}\nSubtotal: {self.subtotal}\nDiscount: {self.discount}\nIVA: 16%\nTotal: {self.total}")