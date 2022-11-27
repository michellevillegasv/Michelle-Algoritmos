from bebida import Alcoholic,NonAlcoholic
from invoice import Invoice
bebidas = [{"name": "Cocacola", "price": 2, "type": "non-alcoholic", "temperature": "15°"},
{"name": "Beer","price": 1.5,"type": "alcoholic", "alcoholic percent": "4%"},
{"name": "Redbull", "price": 3, "type": "non-alcoholic", "temperature": "14°"}
]
bebidas_obj=[]
clients=[]
bebidas_alcoholic_count=[]
bebidas_nonalcoholic_count=[]
def register_beverage(bebidas):
    new_beverage={}
    key_name="name"
    key_price="price"
    key_type="type"
    key_alcoholic="alcoholic percent"
    key_temp="temperature"
    name=input("Enter beverage's name: ")
    price=input("Enter the price:")
    type=input("\n1.Alcoholic\n2.Non-alcoholic\n->")
    while type.isalpha(): input("ENTER A VALID OPTION\n1.Alcoholic\n2.Non-alcoholic\n->")
    if int(type)==1: 
        beverage_type="alcoholic"
        alcoholic_percent=input("Enter the alcoholic percent:")
        new_beverage[key_name]=name
        new_beverage[key_price]=price
        new_beverage[key_type]=beverage_type
        new_beverage[key_alcoholic]=alcoholic_percent
    elif int(type)==2: 
        beverage_type="non-alcohlic"
        temp=input("Enter the temperature of the beverage:")
        new_beverage[key_name]=name
        new_beverage[key_price]=price
        new_beverage[key_type]=beverage_type
        new_beverage[key_temp]=temp
    else: input("ENTER A VALID OPTION\n1.Alcoholic\n2.Non-alcoholic\n->")
    bebidas.append(new_beverage)
def bebidas_register_obj(bebidas,bebidas_obj):
    for bebida in bebidas:
        if bebida["type"].lower()=="non-alcoholic":
            bebidas_obj.append(NonAlcoholic(bebida["name"], bebida["price"],bebida["type"],bebida["temperature"]))
        elif bebida["type"]=="alcoholic":
            bebidas_obj.append(Alcoholic(bebida["name"],bebida["price"],bebida["type"],bebida["alcoholic percent"]))
def register_client(bebidas_obj,bebidas_acoholic,bebidas_nonalcoholic):
    name_client=input("Name:")
    id_client=input("ID: ")
    while id_client.isalpha():id_client=input("ID: ")
    age = input("Age: ")
    while age.isalpha(): age =input("Age: ")
    if int(age)<18: 
        for bebida in bebidas_obj:
            if bebida.type=="non-alcoholic":
                bebida.show()
    elif int(age)>=18: 
        for bebida in bebidas_obj:
            bebida.show()
    subtotal=[]
    select_drink_list=[]        
    while True:
        select_drink= input("\nSelect Beverage:").title()
        select_drink_list.append(select_drink)
        for bebida in bebidas_obj:
            if (bebida.name).title()==select_drink:
                subtotal_beverage=bebida.price
                subtotal.append(subtotal_beverage)
                if bebida.type=="alcoholic":
                    bebidas_acoholic.append(select_drink)
                elif bebida.type=="non-alcoholic":
                    bebidas_nonalcoholic.append(select_drink)
        exit=input("Do you want to buy another beverage? \n1.Yes\n2.No\n->")
        if int(exit)==1: continue
        elif int(exit)==2: break
    return name_client,id_client,select_drink_list,sum(subtotal)
def primo_number(info_client):
    cont=0
    primo=False
    for divisor in range(2,int(info_client[3])):
        if info_client[3]%divisor==0:
            cont+=1
    if cont==0: primo=True
    elif cont>0: primo=False
    return primo
def get_invoice(info_client,primo,clients):
    if primo==True:
        discount=0.10
    total=(info_client[3]*0.16)-discount+info_client[3]
    invoice= Invoice(info_client[0],info_client[1],info_client[2],info_client[3], total)
    clients.append(invoice)
    print(invoice.show())
def statistics(clients,bebidas_acoholic,beverage_nonalcoholic):
    total_price_compras=[]
    print("---STATISTICS---")
    print(f"TOTAL CLIENTS: {len(clients)}")
    for invoice in clients:
        total_price_compras.append(invoice.total)
    if len(clients)==0: print("AVERAGE SALES: 0")
    else:
        print(f"AVERAGE SALES: {sum(total_price_compras)/len(clients)}")
    print(f"TOTAL ALCOHOLIC BEVERAGES SOLD: {len(bebidas_acoholic)}")
    print(f"TOTAL NON-ALCOHOLIC BEVERAGES SOLD: {len(beverage_nonalcoholic)}")
    
def main():
    print("----WELCOME----")
    bebidas_register_obj(bebidas,bebidas_obj)
    while True: 
        menu=input("\n1.Register beverage\n2.Register shop\n3.Statistics\n4.Exit\n->")
        while menu.isalpha(): ("ENTER A VALID OPTION\n1.Register beverage\n2.Register shop\n3.Statistics\n4.Exit\n->")
        if int(menu)==1: 
            register_beverage(bebidas)
        elif int(menu)==2:
            client_get = register_client(bebidas_obj,bebidas_alcoholic_count,bebidas_nonalcoholic_count)
            get_invoice(client_get,primo_number(client_get),clients)
        elif int(menu)==3:
            statistics(clients,bebidas_alcoholic_count,bebidas_nonalcoholic_count)
        elif int(menu)==4: break
        
main()