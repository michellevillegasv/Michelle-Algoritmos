class Ticket:
    def __init__(self,name_client,code,seat,subtotal,discount,total):
        self.name=name_client
        self.code=code
        self.seat=seat
        self.subtotal=subtotal
        self.discount=discount
        self.total=total
    def confirmation_show(self):
        print("---TICKET---")
        print(f"\nNAME: {self.name}\nSEAT: {self.seat}\nSUBTOTAL: {self.subtotal}\nDISCOUNT: {self.discount}\nTOTAL: {self.total}")