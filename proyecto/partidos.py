class Match:
    def __init__(self, local_team, visitor_team,date,hour,stadium_id,stadium,id,cont_asientos,boletos_vendidos):
        self.local_team=local_team
        self.visitor_team=visitor_team
        self.date= date
        self.hour=hour
        self.stadium_id= stadium_id
        self.stadium=stadium
        self.id=id
        self.cont_asientos=cont_asientos
        self.boletos_vendidos=boletos_vendidos
    def show(self):
        print(f"\nLocal Team:{self.local_team}\nVisitor team: {self.visitor_team}\nDate: {self.date}\nHour: {self.hour}\nStadium: {self.stadium}")
