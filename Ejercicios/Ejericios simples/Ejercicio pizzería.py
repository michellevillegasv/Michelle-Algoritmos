option = input("Enter a valid option \n1- Vegetarian \n2- Non Vegetarian \n3-> ")
is_valid = True
if option.isnumeric(): 
    option = int(option)
else: 
    is_valid == False
if is_valid:
    if option == 1:
        ingrediente1 = input("Choose an ingredient: \n1-Pimiento \n2-Tofu \n3-")
        if ingrediente1.isnumeric():
            ingrediente1 = int(ingrediente1)
            if ingrediente1 == 1:
                ingrediente1 = "Pimiento"
                print(f"You chose a Vegetarian pizza with tomato, mozzarella cheese and {ingrediente1}")
            elif ingrediente1 == 2:
                ingrediente1 = "Tofu"
                print(f"You chose a Vegetarian pizza with tomato, mozzarella cheese and {ingrediente1}")
            else: 
                print("No valid option")
        else: 
            is_valid == False
        
    elif option ==2: 
        ingrediente2 = input("Choose an ingrediente: \n1-Peperoni \n2-Jam \n3- Salmon \n4-> ")
        if ingrediente2.isnumeric():
            if ingrediente2 == "1":
                ingrediente2 = "Peperoni"
                print(f"You chose a Non Vegetarian with tomato, mozzarella cheese and {ingrediente2}")
            elif ingrediente2 == "2":
                ingrediente2 = "Jam"
                print(f"You chose a Non Vegetarian with tomato, mozzarella cheese and {ingrediente2}")
            elif ingrediente2 == "3":
                ingrediente2 = "Salmon"
                print(f"You chose a Non Vegetarian with tomato, mozzarella cheese and {ingrediente2}")
            else:
                print("No valid option")
        else:
            is_valid == False 
        
    else:
        print("No valid option")
                



