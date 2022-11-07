class Reminder:
    def __init__(self,name,hour,date,chores):
        self.name = name
        self.hour=hour
        self.date=date
        self.chores=chores
    def actualize(self, new_name,new_hour,new_date,new_chore_list):
        self.name = new_name
        self.hour=new_hour
        self.date=new_date
        self.chores=new_chore_list
    def show(self):
        print(f"\nName: {self.name}\nDate: {self.date}\nHour: {self.hour}\nChores:")
        for chores_list in self.chores:
            print(f"-{chores_list.show()}")