medications = {
        "prescription": {
            "antibiotics": {
                "skin": [
                    {
                        "id": 1,
                        "name": "Clindamicine",
                        "price": 300
                    },
                    {
                        "id": 2,
                        "name": "Cefadroxil",
                        "price": 350
                    },
                    {
                        "id": 3,
                        "name": "Amoxicillin",
                        "price": 320
                    }
                ],
                "respiratory-system":[
                    {
                        "id": 4,
                        "name": "Citromicine",
                        "price": 380
                    },
                    {
                        "id": 5,
                        "name": "Levofloxacine",
                        "price": 125
                    },
                    {
                        "id": 6,
                        "name": "Azitromicine",
                        "price": 740
                    }
                ]
            },
            "analgesic": {
                "anti-inflammatories": [
                    {
                        "id": 7,
                        "name": "HYDROCODONE-IBUPROFEN",
                        "price": 150
                    },
                    {
                        "id": 8,
                        "name": "IBUDONE",
                        "price": 180
                    }
                ]
            }
        },
        "non-prescription": {
            "analgesic": {
                "general": [
                    {
                        "id": 9,
                        "name": "Acetaminophen",
                        "price": 15
                    },
                    {
                        "id": 10,
                        "name": "Ibuprofen",
                        "price": 20
                    }
                ]
            },
            "antihistamine": {
                "antiallergic": [
                    {
                        "id": 11,
                        "name": "Loratadine",
                        "price": 12
                    },
                    {
                        "id": 12,
                        "name": "Desler M",
                        "price": 8
                    },
                    {
                        "id": 13,
                        "name": "Allegra",
                        "price": 21
                    },
                    {
                        "id": 14,
                        "name": "Fexofenadine",
                        "price": 18
                    }
                ]
            }
        }
    }

def inventario(medications):
    print("***INVENTARY***")
    for types, category in medications.items():
        types=str(types)
        print(f"\n{types.upper()}:")
        for types_category, data in category.items():
            types_category = str(types_category)
            print(f"{types_category.title()}")
            for types2, data2 in data.items():
                print(f"Type:{types2}")
                for medicamentos in data2: 
                    print(f"\t-Name: {medicamentos['name']} \n\t-Price: {medicamentos['price']}")

def client_data(medications):
    client = {
        "Name": input("Please enter your first name: "),
        "Last name" : input("Please enter the last name: "),
        "ID": input("Enter your ID number: "),
        "Product": input("Please enter the product you want:").title()
    }
    return client
def search(medications,client):
    for types, category in medications.items():
        for types_category, data in category.items():
            for types2, data2 in data.items():
                for medicamentos in data2: 
                    medicaments1 = medicamentos['name']
                    if medicaments1 == client['Product']:
                        numero_medicamentos = medicamentos['id']
    return numero_medicamentos
def price(client):
    for types, category in medications.items():
        for types_category, data in category.items():
            for types2, data2 in data.items():
                for medicamentos in data2: 
                    medicamentos1=medicamentos['name']
                    if client['Product'] == medicamentos1:
                        price_medicine1 = medicamentos['price']
    return price_medicine1 
def invoice(client,price,search):
    print("**INVOICE**")
    for key,value in client.items():
        print(f"{key}: {value}")
    print(f"ID product:{search}")
    print(f"TOTAL: {price}$")
    
def main():
    print("***WELCOME***")
    while True:
        menu = input("1.See the inventary \n2.Register a shop \n3.Exit \n->")
        if menu == "1":
            inventario_get = inventario(medications)
        if menu == "2":
            client_get = client_data(medications)
            search_get = search(medications, client_get)
            price_get=price(client_get)
            invoice_get = invoice(client_get,price_get,search_get)
        if menu == "3": 
            print("***BYE!***")
            break
main()
