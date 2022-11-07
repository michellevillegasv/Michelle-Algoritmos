estudios ={
    "U": 8900, 
    "T": 12640,
    "R": 15600
}
def client():
    client_data={
        "ID number": input("Please enter your ID number: "),
        "Age": (input("Please enter your age: ")),
        "Gender": input("Please select your gender: \nFemale(F) \nMan(M) \n->"),
        "Study type": input("Please select the stuyd type you need: \nUltrasound(U) \nTomography(T) \nRadiography(R) \n->")
    }
    return client_data
def price(client,estudios):
    if client['Study type'] == "U":
        return estudios['U']
    if client['Study type'] == "T":
        return estudios['T']
    if client['Study type'] == "R":
        return estudios['R']
def discount(client,price):
    if client['Gender'] == "F" and int(client['Age']) >55:
        new_price = price-(price*0.25)
        return new_price
    elif client['Gender'] == "M" and int(client['Age']) >65:
        new_price = price-(price*0.25)
        return new_price
    else:
        return price
def main():
    
    print("***WELCOME***")
    client_list=[]
    prices_U=[]
    prices_T=[]
    prices_R=[]
    count_U=0
    count_T=0
    count_R=0
    count_discount=0
    count_total=0
    
    while True:
        menu= input("Choose an option: \n1. Register a patient \n2. See the report of the day \n3. Exit \n->")
        if menu=="1":
            client_get = client()
            client_list.append(client_get)
    
            print("***INVOICE***")
            for keys,data in client_get.items():
                print(f"{keys}: {data}")
            key_dic = "TOTAL"
            total = discount(client_get,price(client_get,estudios))
            client_get[key_dic]=total
            count_total+=total
            print(f"TOTAL: {total}")
            price_get= price(client_get,estudios)
            if client_get['Study type'] == "U":
                count_U+=1
                prices_U.append(client_get['TOTAL'])
            if client_get['Study type'] == "T":
                count_T+=1
                prices_T.append(client_get['TOTAL'])
            if client_get['Study type'] == "R":
                    count_R+=1
                    prices_R.append(client_get['TOTAL'])
            if client_get['Gender'] == "F" and int(client_get['Age']) >55:
                new_price1 =(price_get*0.25)
                count_discount+=new_price1
            elif client_get['Gender'] == "M" and int(client_get['Age']) >65:
                new_price1 =(price_get*0.25)
                count_discount+=new_price1
        if menu =="2":
            print("\n\t***REPORT OF THE DAY***")
            print(f"ULTRASOUND CLIENTS: {count_U}")
            print(f"TOMOGRAPHY CLIENTS: {count_T}")
            print(f"RADIOGRAPHY CLIENTS: {count_R}")
            print(f"TOTAL AMOUNT OF DISCOUNTS: {count_discount}")
            print(f"TOTAL FACTURADO: {count_total}")
            print(f"AVERAGE PAYMENT CLIENTS: {count_total/len(client_list)}")
            if count_U !=0:
                print(f"AVERAGE FOR ULTRASOUND: {sum(prices_U)/count_U}")
            elif count_U==0: 
                print("AVERGAE FOR ULTRASOUND: 0")
            if count_T !=0:
                print(f"AVERAGE FOR TOMOGRAPHY: {sum(prices_T)/count_T}")
            elif count_T==0: 
                print("AVERGAE FOR TOMOGRAPHY: 0")
            if count_R!=0:
                print(f"AVERAGE FOR RADIOGRAPHY: {sum(prices_R)/count_R}")
            elif count_R==0: 
                print("AVERGAE FOR RADIOGRAPHY: 0")
        if menu == "3":
            print("***GOODBYE***")
            break
main()