from recordatorio import Reminder
from tarea import Chore
reminders_list=[]
def reminders_register(reminders_list_obj):
    name=input("Reminder's name: ")
    date= input("Set the reminder's date: ")
    hour=input("Set the reminder's time: ")
    while True:
        chores_obj=[]
        print("CHORES:")
        name_chore=input("Name:")
        body_chore=input("Description:")
        chores_obj.append(Chore(name_chore,body_chore))
        choice= input("Do you want to add another chore? \n-Yes(Y) \n-No(N) \n->").upper()
        while choice.isnumeric():input("ENTER A VALID OPTION \nDo you want to add another chore? \n-Yes(Y) \n-No(N) \n->")
        if choice=="Y": continue
        elif choice=="N": break
    reminder= Reminder(name,hour,date,chores_obj)
    reminder.show() and reminders_list_obj.append(reminder)
    print("---REMINDER REGISTER---")
def list_reminders_show(reminders_obj):
    for numbers,reminders in enumerate(reminders_obj):
        print(f"---REMINDER {numbers+1}")
        reminders.show()
def delete_reminder(reminders_obj):
    delete= input("Select the number of the reminder you want to delete:")
    while delete.isalpha(): input("Select the number of the reminder you want to delete:")
    for number,reminder in enumerate(reminders_obj):
        print(f"{number+1}: {reminder.name}")
        if int(delete)==(number-1): reminders_obj.remove(reminder)
        else: print("REMINDER NOT FOUND")
def actualize_reminder(reminder_list_obj):
    actualize= input("Select the number of the reminder you want to actualize:")
    while actualize.isalpha(): input("Select the number of the reminder you want to delete:")
    for number,reminder in enumerate(reminder_list_obj):
        print(f"{number+1}: {reminder.name}")
        if int(actualize)==(number-1):
            menu=input("What do you want to change? \n1.Name\n2.Date\n3.Hour\n4.Chores\n5.Back")
            while menu.isalpha(): input("ENTER VALID OPTION\nWhat do you want to change? \n1.Name\n2.Date\n3.Hour\n4.Chores\n5.Back")
            if int(menu)==1:
                pass
            if int(menu)==5:
                break
        else: print("REMINDER NOT FOUND")
def main():
    print("---WELCOME---")
    while True:
        menu=input("\n1.Set a reminder\n2.List of reminders\n3.Actualize reminder\n4.Delete a reminder\n5.Exit\n->")
        while menu.isalpha(): input("ENTER A VALID OPTION\n1.Set a reminder\n2.List of reminders\n3.Actualize reminder\n4.Delete a reminder\n5.Exit\n->")
        if int(menu)==1:
            reminders_register(reminders_list)
        elif int(menu)==2:
            list_reminders_show(reminders_list)
        elif int(menu)==3:
            pass
        elif int(menu)==4:
            delete_reminder(reminders_list)
        elif int(menu)==5: break
main()