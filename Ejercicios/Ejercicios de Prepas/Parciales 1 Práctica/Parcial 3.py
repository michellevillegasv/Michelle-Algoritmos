
Quimico=[]
Farmaceutico=[]
Totales = []
def client():
    clients = {
        "ID": input("Please enter the client's ID number: "),
        "Product": input("Choose the product you'r going to buy: \n1.Quimico(Q) \n2.Farmaceutico(F) \n->"),
        "Pay": input("Choose the way you'r going to pay: \n1.Contado(C) \n2.Crédito(R) \n->"),
        "Price": input("Please enter the price of the product:")
    }
    return clients
def impuesto(client,quimico,farmaceutico,totales):
    if client['Product']== "Q":
        new_price= int(client['Price'])+(int(client['Price'])*0.12)
        quimico.append(client)
        totales.append(new_price)
        return new_price
    elif client['Product']== "F":
        farmaceutico.append(client)
        totales.append(client['Price'])
        return int(client['Price'])
def IVA(client):
    if client['Product']== "Q": 
        return "IVA: 12%" 
    if client['Product']=="F": 
        return "NO IVA"
def invoice(client,total,IVA):
    print("\n***NEW CLIENT***")
    for keys,data in client.items():
        print(f"{keys}: {data}")
    print(IVA)
    print(f"TOTAL:{total}")
    client['Price']=total
def mayor_list(totales,client):
    max = float(totales[0])
    for x in totales:
        x=float(x)
        if x>max:
            max=x
    if max == float(client['Price']):
        return client['ID']
def facturacion_total(totales):
    prices1=0
    for prices in totales:
        prices=float(prices)
    prices1+=prices
    return prices1
def main():
    while True:
        clients =[]
        client_get = client()
        clients.append(client_get)
        invoice(client_get,impuesto(client_get,Quimico,Farmaceutico,Totales), IVA(client_get))
        print("\n\t***REPORT OF THE DAY***")
        print(f"Total of chemical products sold:{len(Quimico)}")
        print(f"Total of farmaceutico products sold:{len(Farmaceutico)}")
        print(f"The client with the biggest shop is {mayor_list(Totales,client_get)}")
        print(f"FACTURACIÓN TOTAL: {facturacion_total(Totales)}")
        menu=input("Do you want to register another client?: \n1. Yes \n2.No \->")
        if menu=="1":
            continue
        if menu=="2":
            break
main()
    
