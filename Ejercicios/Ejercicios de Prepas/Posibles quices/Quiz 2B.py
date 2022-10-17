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
id_pathologie_dicc = {}
new_patient = {}
key1_patient = "Name"
key2_patient = "last name"
key3_patient = "ID"
count=0
while True:
    menu= input("CHOOSE YOUR OPTION (Enter 1, 2 or 3): \n-1 Register a pacient \n-2 Search a pacient \n-3 Exit \n->")
    if menu.isalpha():
        print("Enter a valid option.")
    elif menu.isnumeric():
        menu=int(menu)
        if menu == 1:
            while True:
                name = input("REGISTER THE PATIENT \n- Enter the patient's name: ")
                last_name = input("- Enter the patient's last name: ")
                id_patient = input("- Enter the patient's ID: ")
                id_pathologie = input("-Enter the id of the pathologie: ")
                new_patient[key1_patient] =name
                new_patient[key2_patient] =last_name
                new_patient[key3_patient] =id_pathologie
                #new_patient[key4_patient] =id_pathologie

                for type_system, systems_pathologies in pathologies.items():
                    for types in systems_pathologies:
                            id_pathologie = int(id_pathologie)
                            if types["id"] == id_pathologie: 
                                print("***** INVOICE *****")
                                for patient_data, value_patient in new_patient.items():
                                    print(f"\t{patient_data}: {value_patient}")
                                print(f"\tPatient's pathologie: {types['name']}")
                                print(f"\tMONTO A PAGAR: {types['price']}")

                exit =input("Do you want to register another patient? (Enter 1 or 2) \n1- Yes \n2- No \n->")
                if exit == "1":
                    continue
                elif exit == "2":
                    break
                else:
                    print("Not valid")


        elif menu == 2:
            pathologie_search = input("Enter the pathologie you're searching for: ")
            pathologie_search = pathologie_search.lower()
            pathologie_search = pathologie_search.capitalize()
            for type_system, systems_pathologies in pathologies.items():
                if type_system == pathologie_search:
                    print(f"{pathologie_search}: ")
                    for patients in systems_pathologies:
                        for data, value_data_patiens in patients.items():
                            print(f"\t {data}: {value_data_patiens} ")
                else:
                    print("Pathologie not found")
        elif menu == 3: 
            break