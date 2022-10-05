pathologies = {
    "Respiratory system": [
        {"id": 1,
        "name": "Cystic Fibrosis",
        "price": 300 },
        {"id": 2,
        "name": "Emphysema",
        "price": 500},
        {"id": 3,
        "name": "Tuberculosis",
        "price": 450}
    ],
    "Nervous system": [
        {"id": 4,
        "name": "Parkinson",
        "price": 800 },
        {"id": 5,
        "name": "Epilepsy",
        "price": 600}
    ],
    "Endocrine system": [
        {"id": 6,
        "name": "Diabetes",
        "price": 350 },
        {"id": 7,
        "name": "Acromegaly",
        "price": 700},
        {"id": 8,
        "name": "Hashimoto’s thyroiditis",
        "price": 900}
    ],   
}
new_patient = {}
key1_patient = "name"
key2_patient = "last name"
key3_patient = "ID"
key4_patient = "pathologie's ID"
count=0
while True:
    menu= input("CHOOSE YOUR OPTION (Enter 1, 2 or 3): \n-1 Register a pacient \n-2 Search a pacient \n-3 Exit \n->")
    if menu.isalpha():
        print("Enter a valid option.")
    elif menu.isnumeric():
        menu=int(menu)
        if menu == 1:
            while True:
                name = input("REGISTER THE PATIENT \n- Enter the patient's name:")
                last_name = input("- Enter the patient's last name: ")
                id_patient = input("- Enter the patient's ID: ")
                id_pathologie = input("-Enter the id of the pathologie: ")
                new_patient[key1_patient] =name
                new_patient[key2_patient] =last_name
                new_patient[key3_patient] =id_pathologie
                new_patient[key4_patient] =id_pathologie

                
                for keys1, values1 in new_patient.items():
                    print(f"\n -        {keys1}: {values1}")    
                exit =input("Do you want to enter another infraction? (Enter 1 or 2) \n1- Yes \n2- No \n->")
                if exit == "1":
                    continue
                elif exit == "2":
                    break
                else:
                    print("Not valid")

            

            print()
        elif menu == 2:
            for keys1, values1 in pathologies.items():
                print(f"\n- {keys1.upper()}:")
                for list in values1:
                    for keys2, values2 in list.items():
                        print(f"\n -        {keys2}: {values2}")
            pathologie_search = input("Enter the pathologie you're searching for: ")
        elif menu == 3: 
            break