products ={
    "Q":1000,
    "F": 2500,
    "B": 4000
}
def client():
    clients ={
        "RIF": input("Please enter the client's RIF: "),
        "PRODUCT": input("Select the product you'r going to buy: \nQuimico(Q) \nBiologico(B) \nFarmaceutico(F) \n->"),
        "PAYMENT METHOD": input("Select the payment method: \nContado(C) \nCredito(R) \n->")
    }
    return clients
def price(clients,products):
    for products1, price in products.items():
        if clients['PRODUCT'] == products1:
            return price
def primo(clients):
    primo1 = False
    divisores1 =0
    ultimos_numeros = (clients['RIF'])[-1]
    ultimos_numeros=int(ultimos_numeros)
    for divisores in range(2,ultimos_numeros):
        if ultimos_numeros%divisores==0:
            divisores1+=1
    if divisores1==0:
        primo1=True
        return primo1
    if divisores1!=0:
        return primo1
def discounts(client,price,primo):
    discounts_list=[]
    if client["PAYMENT METHOD"] == "C":
        price2= price*0.03
        discounts_list.append(price2)
    if primo == True:
        price3 = price*0.05
        discounts_list.append(price3)
    return sum(discounts_list)
def recharges(client,price):
    recharges_list=[]
    if client['PRODUCT']== "F": 
        price1 = price*0.12
        recharges_list.append(price1)
    if client["PAYMENT METHOD"] == "C":
        price2= price*0.03
        recharges_list.append(price2)
    return sum(recharges_list)
def total_amount1(price,recharges,discounts):
    total_amount = price + recharges - discounts
    return total_amount
def IVA(client):
    if client['PRODUCT']== "Q": 
        return "IVA: 12%" 
    if client["PAYMENT METHOD"] == "R":
        return "IVA: 10%"
    if client['PRODUCT']=="F": 
        return "NO IVA"
def discounts_declaration(client,primo):
    if client["PAYMENT METHOD"] == "C" and primo == True:
        return "3%, 5%"
    if client["PAYMENT METHOD"] == "C":
        return "3%"
    if primo == True:
        return "5%"
def main():
    clients_count=[]
    prices_list=[]
    count_Q=0
    count_F=0
    count_B=0
    count_C=0
    count_R=0
    print("***WELCOME***")
    while True:
        menu = input("Choose an option: \n1.Register a client \n2.See the report \n3.EXIT \n->")
        if menu=="1":
            client_get=client()
            price_get = price(client_get,products)
            clients_count.append(client_get)
            if client_get['PRODUCT'] == "Q":
                count_Q+=1
            if client_get['PRODUCT'] == "F":
                count_F+=1
            if client_get['PRODUCT'] == "B":
                count_B+=1
            if client_get['PAYMENT METHOD'] == "C":
                count_C+=1
            if client_get['PAYMENT METHOD'] == "R":
                count_R+=1    
            print("***INVOICE***")
            for keys,data in client_get.items():
                print(f"{keys}: {data}")
            total_get = total_amount1(price_get,(recharges(client_get,price_get)),discounts(client_get,price_get,primo(client_get)))
            print(IVA(client_get))
            if total_get%2==0:
                definitivo_total = total_get - (total_get*0.02)
                print(f"DISCOUNT: {discounts_declaration(client_get,primo(client_get))}"+" and 2%")
                print(f"TOTAL: {definitivo_total}")
                key_dic = "TOTAL"
                client_get[key_dic]=definitivo_total
            else:
                print(f"DISCOUNT: {discounts_declaration(client_get,primo(client_get))}")
                print(f"TOTAL: {total_get}")
                key_dic = "TOTAL"
                client_get[key_dic]=total_get
            prices_list.append(client_get['TOTAL'])
        if menu == "2":
            print("***END OF DAY***")
            print(f"TOTAL CLIENTS: {len(clients_count)}")
            print(f"TOTAL QUIMICO CLIENTS: {count_Q}")
            print(f"TOTAL FARMACEUTICO CLIENTS: {count_F}")
            print(f"TOTAL BIOLOGICO CLIENTS: {count_B}")
            print(f"TOTAL DE DESCUENTOS POR PAGO AL CONTADO: {count_C}")
            print(f"TOTAL DE IVAS APLICADOS POR PAGOS A CREDITOS: {count_R}")
            max = float(prices_list[0])
            for x in prices_list:
                x=float(x)
                if x>max:
                    max=x
            if max == float(client_get['TOTAL']):
                print(f"CLIENT WITH THE BIGGEST SHOP: {client_get['RIF']}")
            print(f"TOTAL AMOUNT FACTURADO: {sum((prices_list))}")
        if menu=="3":
            break
main()
