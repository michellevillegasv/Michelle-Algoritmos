
products ={
    "Quimico": 10,
    "Farmaceutico":25,
    "Biologicos":40
}

prices_list=[]
discounts_C=[]
ivas_credit=[]
def client():
    client_dic={
    "RIF": input("Please enter your RIF: "),
    "PRODUCT": input("Please select the product you'r going to buy: \n1. Quimico \n2. Farmaceutico \n3.Biologicos \n->").title(),
    "PAYMENT METHOD": input("Please select the payment method: \n1. Contado \n2. Credito \n->").title()
    }
    return client_dic
def clasification_payment(client,discountsC,ivasC,price):
    if client['PAYMENT METHOD'] =="Contado":
        discountsC.append(price*0.03)     
    if client['PAYMENT METHOD'] =="Credito":
        ivasC.append(price*0.10)
def price(client,products):
    if client['PRODUCT'] == "Quimico":
        return products['Quimico']
    if client['PRODUCT'] == "Farmaceutico":
        return products['Farmaceutico']
    if client['PRODUCT'] == "Biologicos":
        return products['Biologicos']
def primo_rif(client):
    divisores=0
    last_number=(client['RIF'])[-1]
    last_number=int(last_number)
    for numbers in range(2,last_number):
        if last_number%numbers==0:
            divisores+=1
    if divisores==0:
        return True
    if divisores!=0:
        return False
def discounts(client,price, primo):
    discounts_list=[]
    if client['PAYMENT METHOD'] =="Contado":
        discounts_list.append(price*0.03)
    if primo== True:
        discounts_list.append(price*0.05)
    else:
        discounts_list.append(0)
    return sum(discounts_list)
def ivas(client,price):
    ivas_list=[]
    if client['PRODUCT'] == "Quimico":
        ivas_list.append((price*0.16))
    if client['PRODUCT'] == "Biologicos":
        ivas_list.append((price*0.16))
    if client['PAYMENT METHOD'] =="Credito":
        ivas_list.append(price*0.10)
    else:
        ivas_list.append(0)
    return sum(ivas_list)
def price_max(prices_list,client):
    max = float(prices_list[0])
    for x in prices_list:
        x=float(x)
        if x>max:
            max=x
    if max == float(client['TOTAL']):
        return client['RIF']
def main():
    Q_count=0
    B_count=0
    F_count=0
    total_invoice=0
    print("***WELCOME***")
    while True:
        menu = int(input("Select an option: \n1. Register a client \n2. See the report of the day \n3. Exit \n->"))
        if menu ==1:
            client_get = client()
            print("***INVOICE***")
            for keys,data in client_get.items():
                print(f"{keys}: {data}")
            print(f"TOTAL DISCOUNTS: {discounts(client_get,price(client_get,products),primo_rif(client_get))}")
            print(f"TOTAL IVA: {ivas(client_get,price(client_get,products))}")
            total = price(client_get,products) - discounts(client_get,price(client_get,products),primo_rif(client_get)) + ivas(client_get,price(client_get,products))
            if total%2==0:
                final_total = total-(total*0.02)
            elif total%2!=0:
                final_total = total
            key_dic = "TOTAL"
            client_get[key_dic]= final_total
            prices_list.append(final_total)
            total_invoice+=final_total
            print(f"TOTAL: {final_total}")
            if client_get['PRODUCT'] == "Quimico":
                Q_count+=1
                return products['Quimico']
            elif client_get['PRODUCT'] == "Farmaceutico":
                B_count+=1
                return products['Farmaceutico']
            elif client_get['PRODUCT'] == "Biologicos":
                F_count+=1
        if menu ==2:
            clasification_get=clasification_payment(client_get,discounts_C,ivas_credit,price(client_get,products))
            max_get=price_max(prices_list,client_get)
            print("***REPORT OF THE DAY***")
            print(f"QUIMICO CLIENTS: {Q_count}")
            print(f"FARMACEUTICO CLIENTS: {F_count}")
            print(f"BIOLOGICO CLIENTS: {B_count}")
            print(f"TOTAL DISCOUNTS FOR CASH PAYMENT: {sum(discounts_C)}")
            print(f"TOTAL IVAS FOR CREDIT PAYMENT:: {sum(ivas_credit)}")
            print(f"THE CLIENT WITH THE BIGGEST SHOP: {max_get} ")
            print(f"TOTAL AMOUNT INVOICED: {total_invoice}")
        if menu==3:
            print("***GOODBYE!***")
            break
main()