from canto import Canto
from baile import Baile
from musica import Musica
from libre import Libre
participants = []
def register_participant(participants_list):
    name = input("Participant's Name: ").title()
    type = input("Type:\n1.Solo\n2.Group \n-> ")
    if type.isalpha():
        type = input("ENTER A VALID OPTION\n1.Solo\n2.Group\n-> ")
    if type.isnumeric():
        if int(type)==1:
            type = "Solo"
        elif int(type)==2:
            type="Group"
        else:
            type = input("ENTER A VALID OPTION\n1.Solo\n2.Group\n-> ")
    cellphone= input("Participant's cellphone number: ")
    if cellphone.isalpha():
        cellphone= input("ENTER A VALID OPTION \nParticipant's cellphone number: ")
    register = input("Participant's register number: ")
    if register.isalpha():
        register= input("ENTER A VALID OPTION \nParticipant's rgister number: ")
    category = input("Category:\n1.Canto\n2.Baile\n3.Musica\n4.Libre\n->")
    if category.isalpha(): 
        category = input("ENTER A VALID OPTION\n1. Canto\n2. Baile\n3.Musica\n4.Libre\n->")
    if category.isnumeric():
        if int(category)==1:
            category = "Canto"
            song = input("Enter the name of the song: ").title()
            author = input("Enter the author of the song: ").title()
            participant = Canto(name, type, category,cellphone,register, song, author)
        elif int(category)==2:
            category = "Baile"
            style = input("Enter the style you'r going to dance: ").title()
            participant = Baile(name, type,category,cellphone,register,style)
        elif int(category)==3:
            category = "Musica"
            instrument= input("Enter the instrument(s): ").title()
            participant = Musica(name, type, category,cellphone,register, instrument)
        elif int(category)==4:
            category = "Libre"
            talent = input("Enter the talent you'r going to show: ").title()
            participant = Libre(name, type, category, cellphone, register, talent)
    participants_list.append(participant)
    print("\n\t---REGISTER DONE---")
    participant.show()
def show_participants_list(participants_list):
    print("---PARTICIPANTS---")
    for participants_obj in participants:
        participants_obj.show()
def main():
    print("---WELCOME---")
    while True:
        menu = input("\nChoose an option (Enter a number)\n1. Register a participant \n2. See al the participants \n3. Exit \n->")
        if menu.isalpha(): continue
        if menu.isnumeric():
            if int(menu) == 1:
                register_participant(participants)
            if int(menu)==2:
                show_participants_list(participants)
            if int(menu)==3:
                print("---GOOBYE!---")
                break
main()
