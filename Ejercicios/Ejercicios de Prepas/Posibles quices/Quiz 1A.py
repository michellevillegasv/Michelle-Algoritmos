
count_infractions = 0
count_officers = 0
count_erase =0
key1_infraction = "name"
key2_infraction = "last name"
key3_infraction = "ID"
key4_infraction = "Infraction's type"
key5_officers ="name"
key6_officers ="last name"
key7_officers ="ci"


infraction = {
    1:{"name":"Choque", "cost":50},
    2:{"name":"Semáforo", "cost":30},
    3:{"name":"Falta de documentos", "cost":100}
}
officers={
    1:{"name":"Luis", "lastName":"Bello","ci":13452224},
    2:{"name":"Jose", "lastName":"Quevedo","ci":44235611},
    3:{"name":"Antonio", "lastName":"Guerra","ci":12345678},
}
db ={}
while True:
    
    menu = input("What do you want to do?(eg:1,2,3...) \n1- Register an infraction \n2- Consult the infractions \n3- Erase an infraction \n4- Exit \n- Enter your option: ")
    if menu.isalpha(): 
        print("Enter a valid option")
        continue
    elif menu.isnumeric():
        if menu == "1":
            while True:
                name = input("REGISTER THE INFRACTION \n- Enter the infractor's name:")
                last_name = input("- Enter the infractor's last name: ")
                id = input("- Enter the infractor's ID: ")
                type_infraction = input("-Enter the type of the infraction: ")
                officer = input("REGISTER THE OFFICER \n- Officer's name: ")
                lastname_officer = input("-Officer's last name: ")
                id_officer = input("-Officer's ID: ")

                new_infractor = {}
                new_infractor[key1_infraction] =name
                new_infractor[key2_infraction] =last_name
                new_infractor[key3_infraction] =id
                new_infractor[key4_infraction] =type_infraction

                new_officer = {}
                new_officer[key5_officers]=officer
                new_officer[key6_officers]=lastname_officer
                new_officer[key7_officers]=id_officer

                for infractions in range(len(infraction)):
                    count_infractions +=1
                    key_infractions = count_infractions+1
                infraction[key_infractions]=new_infractor
                for officers_for in range(len(officers)): 
                    count_officers+=1
                    key_officers = count_officers+1
                officers[key_officers]=new_officer
                exit =input("Do you want to enter another infraction? (Enter 1 or 2) \n1- Yes \n2- No \n->")
                if exit == "1":
                    continue
                elif exit == "2":
                    break
                else:
                    print("Not valid")
        
        elif menu == "3":
            while True:
                validate_erase = True
                erase = list(infraction.keys())
                infraction_erase = input("\n- Enter the number of the infraction you want to remove or write Exit to go to the menu: ")
                if infraction_erase.isnumeric():
                    infr_num = int(infraction_erase)
                    for keys_erase in erase:
                        if keys_erase == infr_num:
                            validate_erase = False
                            infraction.pop(int(infraction_erase))
                            print("Infraction deleted")
                            break
                    if validate_erase:
                        print("Its not in the system") 
                elif infraction_erase == "Exit":
                    break
                else: 
                    print("Not valid")  
        elif menu == "2":
            for keys, values in infraction.items():
                print(f"Infraction {keys}: {values}")
            menu1 = input("Enter 'Menu' to go back to de Menu \n-")
            menu1 = menu1.title()
            if menu1 == "Menu":
                continue
            else: 
                print("Not valid")
        elif menu == "4":
            break
        else:
            print("Not valid option. Enter again")
            continue