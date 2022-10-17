tarifas = {
    "A":2500,
    "S": 3500
}
clients = []
clients_A = []
clients_S=[]
clients_discount=[]
facturacion_total=[]
def client():
    client = {
        "ID": input("Please enter your ID number: "),
        "Type of car": input("Please enter the type of car you drive: \n\tAutomatic \n\tSyncronic \n\t-> ").title(),
        "Hours": input("Enter how many hours are you going to drive: ")
    }
    return client
def categories(client, tarifas,clients_A, clients_S):
    if client['Type of car'] == "Automatic":
        price = tarifas['A']
        clients_A.append(client)
        return price
    elif client['Type of car'] == "Syncronic":
        price1 = tarifas['S']
        clients_S.append(client)
        return price1
def total(categories,client,clients_discount):
    if int(client['Hours']) <=3:
        total_amount = int(client['Hours'])* categories
        return total_amount
    if int(client['Hours']) > 3:
        total_amount1 = int(client['Hours'])* categories
        discount = total_amount1*0.15
        clients_discount.append(client)
        return discount

def invoice(client,total,facturacion):
    print("\n\t***INVOICE***")
    print(f"\tID: {client['ID']}")
    print(f"\tTYPE OF CAR: {client['Type of car']}")
    print(f"\tTOTAL AMOUNT: {total}")
    facturacion.append(total)
def promedio(facturacion):
    for totals in facturacion:
        promedio=0
        promedio+=totals
    return promedio
def main():
    print("***WELCOME***")
    while True: 
        menu = input("\nChoose an option(Enter 1 2 or 3): \n1. Register a client \n2. See the report of the day \n3. Exit \n->")
        if menu == "1":
            client_get = client()
            price_get = categories(client_get,tarifas,clients_A, clients_S)
            total_get = total(price_get, client_get,clients_discount)
            invoice_get = invoice(client_get,total_get,facturacion_total)
            clients.append(client_get)
        if menu == "2":
            promedio_get = promedio(facturacion_total)
            print("***REPORT OF THE DAY***")
            print(f"TOTAL CLIENTS: {len(clients)}")
            print(f"\t- CLIENTS AUTOMATIC: {len(clients_A)} \n\t- CLIENTS SYNCRONIC: {len(clients_S)}")
            print(f"CLIENTS WITH DISCOUNT: {len(clients_discount)}")
            print(f"FACTURATION TOTAL: {promedio_get/(len(clients))}")
    
        if menu == "3":
            break
main()