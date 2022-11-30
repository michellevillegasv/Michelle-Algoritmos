import requests 
import pickle
from itertools import permutations
from equipo import Team
from estadio import Stadium
from partidos import Match
from cliente import Client
from beverage import Beverage
from food import Food
from restaurante import Restaurant
from boleto import Ticket
from invoice import Invoice
teams_obj=[]
matches_obj=[]
stadium_obj=[]
client_obj=[]
boleto_register = []
spent_vip_client={}
product_count={}
def get_info_api(): #En esta función importé todas las API, y returne la información en una tupla.
    url_team = "https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/teams.json"
    response_team = requests.get(url_team)
    team_content = response_team.json()
    url_stadiums_restaurant = "https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/stadiums.json"
    response_stadium_restaurant = requests.get(url_stadiums_restaurant)
    stadium_restaurant = response_stadium_restaurant.json()
    url_matches = "https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/matches.json"
    response_matches = requests.get(url_matches)
    matches_cont = response_matches.json()
    return team_content,stadium_restaurant,matches_cont

def register_teams(teams_obj,info):
    for teams in info[0]:
        teams_obj.append(Team(teams["name"],teams["fifa_code"], teams["group"], int(teams["id"])))

def product_register(info):
    product_obj={}
    cont_beverage=0
    cont_food=0
    for stadiums in info[1]:
        for dics_restaurant in stadiums["restaurants"]:
            products_list=[]
            for products in dics_restaurant["products"]:
                name=products["name"]
                price=products["price"]
                quantity=products["quantity"]
                if (products["type"]).title() == "Beverages":
                    if (products["adicional"]).lower() == "non-alcoholic":
                        alcoholic = False
                    elif (products["adicional"]).lower() == "alcoholic":
                        alcoholic = True
                    products_list.append(Beverage(name,price,products["type"],quantity,alcoholic,cont_beverage))
                elif(products["type"]).title() == "Food":
                    products_list.append(Food(name,price,products["type"],quantity, products["adicional"],cont_food)) 
            key=stadiums["name"]
        product_obj[key]=products_list
    return product_obj
def restaurant_register(info,product_obj):
    restaurant_obj={}
    for stadiums in info[1]:
        for dics_restaurant in stadiums["restaurants"]:
            restaurant_list=[]
            for key,product in product_obj.items():
                if key.title()==stadiums["name"]:
                    name_restaurant=dics_restaurant["name"]
                    products_register=product
                    restaurant_list.append(Restaurant(name_restaurant,products_register))
        key=stadiums["name"]
        restaurant_obj[key]=restaurant_list
    return restaurant_obj

def stadium_register(stadium_obj,restaurant_obj,info):
    for stadiums in info[1]:
        stadium_obj.append(Stadium(int(stadiums["id"]), stadiums["name"],stadiums["capacity"],stadiums["location"],restaurant_obj))

def matches_register(matches_obj,teams_obj,stadium_obj, info):
    cont_asientos=0
    cont_tickets_sold=0
    for matches in info[2]:
        for teams in teams_obj:
            if matches["home_team"]==teams.country:
                local_team= teams  #En esta variable estoy almacenando el objeto Equipo
            elif matches["away_team"]==teams.country:
                visitor_team=teams
        for stadiums in stadium_obj:
            if int(matches["stadium_id"])==int(stadiums.id):
                stadium_match=stadiums
            else:
                continue
        date_hour= matches["date"].split(" ")
        matches_obj.append(Match(local_team.country,visitor_team.country,date_hour[0], date_hour[1], stadium_match.id, stadium_match.name,int(matches["id"]),cont_asientos,cont_tickets_sold))

def show_teams(teams_obj):
    new_list_teams = sorted(teams_obj,key=lambda team: int(team.id))
    for teams in new_list_teams:
        print(f"{teams.id}. {teams.country}")

def show_stadium(stadium_obj):
    for stadium in stadium_obj:
        print(f"{stadium.id}. {stadium.name}")

def show_date(match_obj):
    new_list_matches = sorted(match_obj,key=lambda x: x.id)
    for date in new_list_matches:
        print(f"{date.id}. {date.date}")
def register_client(matches_obj,client_obj):
    print("---------------------------------------------\n\tREGISTER CLIENT\n---------------------------------------------")
    name=input("Client's name: ")
    id=input("Client's ID: ")
    while id.isalpha(): id=input("ENTER A VALID OPTION\nClient's ID: ")
    if id is id.isnumeric(): int(id) 
    for client in client_obj:
        if int(client.id)==int(id) and len(client_obj)>0:
            return client.name,client.id,client.age,client.match_client,client.ticket_selected,client.vampiro_id,client.perfect_id
    else:
        age=input("Client's age: ")
        while age.isalpha() and age<0 and age>118: input("ENTER A VALID OPTION\nClient's age: ")
        new_list_matches = sorted(matches_obj,key=lambda match: match.id)
        for matches in new_list_matches:
            print(f"-----{matches.id}-----")
            print(f"\n\t{matches.show()}")
        select_match=input("Select the match: ")
        while select_match.isalpha(): input("ENTER A VALID OPTION\nSelect the match: ")
        for matches in new_list_matches:
            if int(select_match)==matches.id: match_client=matches.id
        ticket=input("\n1. General --> 50$\n2. VIP -->120$\n->")
        while ticket.isalpha(): ("ENTER A VALID OPTION\n1. General --> 50$\n2. VIP -->120$\n->")
        if int(ticket)==1: ticket_selected="General"
        elif int(ticket)==2: ticket_selected="VIP"
        else: input("ENTER A VALID OPTION\n1. General --> 50$\n2. VIP -->120$\n->")
        vampiro_id=False
        if len(id)%2==0:
            combinations_list = permutations(id)
            for combination in combinations_list:
                vampiro = ("".join(combination[int(len(id)/2):]))*int("".join(combination[:int(len(id)/2)]))
                if vampiro==int(id):
                    vampiro_id=True
                    break
        perfect_id=False
        count = 1
        for divisores in range(1,int(id)+1):
            if int(id)%divisores==0:
                count+=1
                suma = 0
                suma+=divisores
            if suma == int(id):
                perfect_id =True
        return name,id,age,match_client,ticket_selected,vampiro_id,perfect_id
def boleto(info_client, fila_get, columna_get,client_list, boleto_register,matches_obj):
    cont_compras=0
    client_list.append(Client(info_client[0],info_client[1],info_client[2],info_client[3],info_client[4],info_client[5],info_client[6],cont_compras))
    cont_client=0
    cont_sold=0
    for client in client_list:
        cont_client+=1
    if info_client[4]=="General": subtotal = 50
    elif info_client[4]=="VIP": subtotal=120
    if info_client[5]==True: 
        discount=0.50
        discount_print = "YOU HAVE 50% DISCOUNT"
    elif info_client[5]==False: 
        discount = 0
        discount_print="NO DISCOUNT"
    total = subtotal - discount + (subtotal*0.16)
    boleto = Ticket(info_client[0],info_client[1],info_client[3], cont_client,fila_get,columna_get,subtotal,discount_print,total,cont_sold) 
    print(f"\n{boleto.confirmation_show()}")
    decision = input("\n----------------\nCONFIRM PURCHASE\n1.Confirm\n2.Delete\n->")
    while not decision.isnumeric(): decision =input("ENTER A VALID OPTION\n1.Confirm\n2.Delete\n->")
    if int(decision)==1:
        boleto_register.append(boleto)
        for matches in matches_obj:
            if info_client[3]==int(matches.id):
                for boleto_cofirmed in boleto_register:
                    boleto_cofirmed.sold+=1
                    matches.boletos_vendidos+=1
                    for client in client_list:
                        client.compra+=1
        print("----TICKET BOUGTH----")
    elif int(decision)==2: print("---PURCHASE DELETE---")
    elif int(decision)!=1 or int(decision)!=2: decision =input("ENTER A VALID OPTION\n1.Confirm\n2.Delete\n->")
def boleto_check(boleto_register, info_client):
    code_list=[]
    for boletos in boleto_register:
        code_list.append(boletos.code)
    verify_code = input("Enter the ticket code: ")
    while verify_code.isalpha(): input("ENTER A VALID OPTION\nEnter the code of the ticket: ")
    for code_ticket in code_list:
        if int(verify_code)==int(code_ticket):
            code_list.remove(code_ticket)
            for matches in matches_obj:
                if info_client[3]==int(matches.id):
                    matches.cont_asientos+=1
            print("----TICKET VERIFIED!----")
    else: print("---- THE TICKET IS NOT IN THE SYSTEM. YOU'RE NOT ALLOWED ----")  #### ESTO SE ME IMPRIME VARIAS VECES

def stadium_choice(client_info,matches_obj, stadium_obj):
    map_stadium=[]
    for matches in matches_obj:
        if client_info[3] == int(matches.id):
            selected = int(matches.stadium_id)
        else: continue
    for stadiums in stadium_obj:
        if selected==int(stadiums.id):
            x=stadiums.capacity[1]
            y=stadiums.capacity[0]
    for i in range(y):
        seat=[]
        for j in range(x):
            seat.append(False)
        map_stadium.append(seat)
    return map_stadium
def restaurant_show(dic_restaurant):
    for key,restaurant in dic_restaurant.items():
        print(f"-{key}")
    select_restaurant = input("Enter the name of the restaurant: ").title()
    menu_restaurant = input("---------------------\n1.Look for a product\n2.Look for type of product\n3.Look for price\n->")
    while menu_restaurant.isalpha(): input("ENTER A VALID OPTION\n------------------\n1.Look for a product\n2.Look for type of product\n3.Look for price\n->")
    if int(menu_restaurant) ==1:
        select_product= input("Enter the product you want to search: ").title()
        while select_product.isnumeric(): input("ENTER A VALID OPTION\nEnter the product you want to search:").title()
        for key,restaurants in dic_restaurant.items():
                if select_restaurant == key.title():
                    for restaurant in restaurants:
                        for products in restaurant.products:
                            if select_product==(products.name).title():
                               print(f"\n----------------\n{products.show()}\n----------------")
                        #else: continue
    elif int(menu_restaurant)==2:
        type_food= input("Enter the type of food you want to search:").title()
        while not type_food.isalpha(): input("ENTER A VALID OPTION\nEnter the type of food you want to search:").title()
        for key,restaurants in dic_restaurant.items():
                if select_restaurant == key.title():
                    for restaurant in restaurants:
                        for products in restaurant.products:
                            if type_food==(products.type).title():
                                print(f"{products.show()}")
        if type_food!=(products.type).title():
            print("Type not found")
    elif int(menu_restaurant)==3:
        price_search=input("Enter the price you want to look: ")
        while price_search.isalpha(): input("ENTER A VALID OPTION\nEnter the price you want to look: ")
        for key,restaurants in dic_restaurant.items():
            if select_restaurant == key.title():
                    for restaurant in restaurants:
                        for products in restaurant.products:
                            if float(price_search)==float(products.price):
                                print(f"{products.show()}")
    else:
        print("Restaurant not found")
def valid_stadium(fila,columna,client_info,matches_obj, stadium_obj):
    for matches in matches_obj:
        if client_info[3] == int(matches.id):
            selected = int(matches.stadium_id)
            break
    for stadiums in stadium_obj:
        if selected==int(stadiums.id):
            if int(fila) in range(stadiums.capacity[1]) and int(columna) in range(stadiums.capacity[0]):
                fila =input("Enter the number of the row: ")
                columna = input("Enter the number of the column: ")
                break
    return fila,columna
            
def stadium_view(stadium_map):
    order = "    "
    for numbers,seats in enumerate(stadium_map[1]):
        if numbers>8: order+=str(numbers+1)+"|    "
        else: order+=str(numbers+1)+" |  "
    print(order)
    for numbers,seats in enumerate(stadium_map):
        if numbers>8: indicador =str(numbers+1)
        else: indicador=str(numbers+1)+" "
        for spaces in seats:
            if spaces==True:
                indicador+="| X "
            else: indicador+="|    "
        print("   "+"_"*len(stadium_map[1]*5))
        print(indicador)
def restaurant_management(client_list, match_obj, stadium_obj, invoice_dic, boleto_list,product_count):
    id_validation= input("Enter the client's ID: ")
    while id_validation.isalpha(): id_validation=input("ENTER A VALID OPTION\nEnter the client's ID: ")
    for client in client_list:
        if int(id_validation)==int(client.id):
            if client.type_tickets== "VIP":
                for match in match_obj:
                    if client.match == match.id:
                        for stadium in stadium_obj:
                            if match.stadium==stadium.name:
                                for name,value in (stadium.restaurants).items():
                                    if name==stadium.name:
                                        for restaurant in value:
                                            print(f"-{restaurant.name}")
            
                select_restaurant=input("Select the restaurant: ").title()
                for client in client_list:
                    if id_validation==client.id:
                        if client.type_tickets== "VIP":
                            for match in match_obj:
                                if client.match == match.id:
                                    for stadium in stadium_obj:
                                        if match.stadium==stadium.name:
                                            for name,value in (stadium.restaurants).items():
                                                    if name==stadium.name:
                                                        for restaurant in value:
                                                            if select_restaurant == (restaurant.name).title():
                                                                for products in restaurant.products:
                                                                    if int(client.age)<18:
                                                                        if products.type=="beverages":
                                                                            if products.alcoholic=="alcoholic":
                                                                                (restaurant.products).remove(products)
                                                                        print(products.show_menu()) 
                                                                    elif int(client.age)>=18: 
                                                                        print(products.show_menu())
                prices_list=[] 
                compra={}                                                                                    
                while True:
                    select_products=input("Select the product: ").title()
                    amount= input("How many of this product you want?: ")
                    while select_products.isnumeric(): input("ENTER A VALID OPTION\nSelect the product: ")
                    repeat_product=False
                    for key,value in compra.items(): 
                        if select_products==key.title():
                            compra[select_products]+=amount
                            repeat_product=True
                            break
                    if repeat_product:    
                        compra[select_products]=amount
                    menu=input("\n1.Select another product \n2.Finalize shop \n->")
                    while not menu.isnumeric(): ("ENTER A VALID OPTION\n1.Select another product \n2.Finalize shop \n->")
                    if int(menu)==2:break
                    elif int(menu)==1: continue
                for client in client_list:
                    if id_validation==client.id:
                        if client.type_tickets== "VIP":
                            for match in match_obj:
                                if client.match == match.id:
                                    for stadium in stadium_obj:
                                        if match.stadium==stadium.name:
                                            for name,value in (stadium.restaurants).items():
                                                    if name==stadium.name:
                                                        for restaurant in value:
                                                            if select_restaurant == restaurant.name:
                                                                for product in restaurant.products:
                                                                    for product_bought,amount in compra.items():
                                                                        if (product.name).title()==product_bought:
                                                                            prices_list.append((float(product.price)*float(amount))+(float(product.price)*0.16))
                print("-----------INVOICE-----------")
                product_shop=[]
                for products_confirmed,amount in compra.items(): 
                    product_shop.append(products_confirmed)
                    print(f"-{products_confirmed}")
                for client in client_list: 
                    if client.id ==id_validation:
                        name_invoice_client = client.name
                        if client.perfect_id == True: 
                            discount = sum(prices_list)*0.15
                            print_discount ="DISCOUNT: 15%" 
                        else:
                            discount = 0
                            print_discount="NO DISCOUNT"   
                print(f"TOTAL: {sum(prices_list)-discount}")
                confirm = input("\n1.Confirm your shop\n2.Cancel your shop\n->")
                while confirm.isalpha(): confirm= ("ENTER A VALID OPTION\n1.Confirm your shop\n2.Cancel your shop\n->")
                if int(confirm)==1:
                    #for products_registered,amount_inicial in compra.items(): 
                    invoice_get = Invoice(name_invoice_client,id_validation,product_shop,print_discount,sum(prices_list),(sum(prices_list)-discount))
                    print("----SHOP CONFIRMED!----")
                    print(invoice_get.show())
                    for client in client_list:
                        if id_validation==client.id:
                            if client.type_tickets== "VIP":
                                for match in match_obj:
                                    if client.match == match.id:
                                        for stadium in stadium_obj:
                                            if match.stadium==stadium.name:
                                                for name,value in (stadium.restaurants).items():
                                                        if name==stadium.name:
                                                            for restaurant in value:
                                                                if select_restaurant == restaurant.name:
                                                                    for product in restaurant.products:
                                                                        for amount,product_bought in compra.items():
                                                                            if (product.name).title()==product_bought:
                                                                                product.quantity= int(product.quantity)-int(amount)
                    list_spent=[]
                    list_spent.append(((sum(prices_list)-discount)))
                    for client in client_list:
                        if id_validation==client.id:
                            if client.type_tickets== "VIP":
                                for boleto in boleto_list:
                                    if int(boleto.id_client)==int(client.id):
                                        list_spent.append(boleto.total)
                    invoice_dic[client.id]=list_spent                                                            
                elif int(confirm)==2: print("----SHOP CANCELED----")
            elif client.type_tickets=="General": print("---NOT ALLOWED TO BUY IN THE RESTAURANT---")
def statistics(spent_list,matches_obj,boletos_list,client_list):
    print("\n-----STATISTICS-----")
    spent_sum=[]
    for id,spent in spent_list.items():
        spent_sum.append(spent)
    if len(spent_list)==0:
        average_spent=0
    else:
        average_spent=sum(spent_sum)/len(spent_list)
    print(f"AVERAGE SPENT CLIENT VIP: {average_spent}")
    new_list_matches = sorted(matches_obj,key=lambda match: int(match.cont_asientos))
    print("----------------------------------------------------------------------------------------------------------------")
    print(f"|        PARTIDO           |       ESTADIO       |      BOLETOS VENDIDOS      |     ASISTENCIA     |      RELACIÓN     |")
    print("----------------------------------------------------------------------------------------------------------------")
    for match in new_list_matches: 
        for boletos in boletos_list:
            if boletos.sold !=0:
                relacion = int(match.cont_asientos)/int(boletos.sold)
            else:
                relacion=0
            print(" ----------------------------------------------------------------------------------------------------------------")
            print(f"|  {match.local_team}vs.{match.visitor_team}  |   {match.stadium}   |       {boletos.sold}   |         {match.cont_asientos}   |       {relacion}    |")
    print(f"MOST ATTENDED MATCH:")
    print(f"{new_list_matches[0].show()}")
    new_list_sold=sorted(matches_obj,key=lambda match: int(match.boletos_vendidos))
    print(f"MATCH WITH THE MOST TICKETS SOLD:")
    print(f"{new_list_sold[0].show()}")
    new_list_client_order = sorted(client_list, key=lambda client: int(client.compra))
    if len(new_list_client_order)<3:
        None
    else:
        print(f"TOP 3 CLIENTS:\n1.{(new_list_client_order[0]).name}\n2.{(new_list_client_order[1]).name}\n3.{(new_list_client_order[2]).name}")
def main(teams_obj,matches_obj,stadium_obj,client_obj,boleto_register,spent_vip_client,product_count):
    try:
        with open("teams_obj.txt", "rb") as archivo:
            teams_obj=pickle.load(archivo)
    except:
         get_info_api()
    try:
        with open("matches_obj.txt", "rb") as archivo:
            matches_obj=pickle.load(archivo)
    except:
         get_info_api()
    try:
        with open("stadium_obj.txt","rb") as archivo:
            stadium_obj=pickle.load(archivo)
    except:
        get_info_api()
    try:
        with open("client_obj.txt","rb") as archivo:
            client_obj=pickle.load(archivo)
    except:
        get_info_api()
    try:
        with open("boleto_register.txt", "rb") as archivo:
            boleto_register=pickle.load(archivo)
    except:
        get_info_api()
    try:
        with open("spent_vip_client.txt","r") as archivo:
            archivo1=archivo.read()
            spent_vip_client= eval(archivo1)
    except:
        get_info_api()
    try:
        with open("product_count.txt", "r") as archivo:
            archivo1=archivo.read()
            product_count=eval(archivo1)
    except:
        get_info_api()
    
    register_teams(teams_obj,get_info_api())
    product_register(get_info_api())
    restaurant_register(get_info_api(),product_register(get_info_api()))
    stadium_register(stadium_obj,restaurant_register(get_info_api(),product_register(get_info_api())),get_info_api())
    matches_register(matches_obj,teams_obj,stadium_obj,get_info_api())
    print("---------------WELCOME---------------")
    while True: 
        menu = input("\n1. Matches\n2. Tickets\n3. Check Tickets\n4. Restaurants\n5. Statistics\n6. Exit \n->")
        while menu.isalpha(): input("CHOOSE A VALID OPTION\n1. Matches\n2. Tickets\n3. Check Tickets\n4. Restaurants\n5. Statistics\n6. Exit \n->")
        if int(menu)==1: 
            menu2= input("\n1.By Country\n2.By Stadium\n3.By Date\n4.Back to the main menu\n->")
            while menu2.isalpha(): ("CHOOSE A VALID OPTION\n1.By Country\n2.By Stadium\n3.By Date\n4.Back to the main menu\n->")
            if int(menu2)==1: 
                show_teams(teams_obj)
                selected_country= input("Select the country you want to look for: ")
                while selected_country.isalpha(): input("ENTER A VALID OPTION\nSelect the country you want to look for: ")
                for teams in teams_obj:
                    for matches in matches_obj:
                        if int(selected_country)==int(teams.id):
                            if teams.country == matches.local_team or teams.country == matches.visitor_team:
                                print(matches.show())              
            elif int(menu2)==2:
                show_stadium(stadium_obj)
                selected_stadium=input("Select the stadium you want to look for: ")
                for stadium in stadium_obj:
                    for matches in matches_obj:
                        if int(selected_stadium)== int(stadium.id):
                            if stadium.name == matches.stadium:
                                print(matches.show())
            elif int(menu2)==3:
                show_date(matches_obj)
                selected_stadium=input("Select the date you want to look for: ")
                for stadium in stadium_obj:
                    for matches in matches_obj:
                        if int(selected_stadium)== int(matches.id):
                                print(matches.show())
        elif int(menu)==2:
            
            register_client_get = register_client(matches_obj,client_obj)
            selected_stadium=stadium_choice(register_client_get,matches_obj,stadium_obj)
            stadium_view(selected_stadium)
            fila_get=input("Enter the number of the row:")
            columna_get = input("Enter the number of the column: ")
            while fila_get.isalpha(): fila_get = input("Enter the number of the row:") 
            while columna_get.isalpha(): columna_get = input("Enter the number of the column: ")
            x,y = valid_stadium(fila_get,columna_get,register_client_get,matches_obj, stadium_obj)
            selected_stadium[int(x)-1][int(y)-1]=True
            stadium_view(selected_stadium)
            boleto(register_client_get,fila_get,columna_get,client_obj,boleto_register,matches_obj)
        elif int(menu)==3:
            boleto_check(boleto_register,register_client_get)
        elif int(menu)==4:
            menu_4 = input("\n1.Look for products\n2.Register a shop\n->")
            while menu_4.isalpha(): input("ENTER A VALID OPTION\n1.Look for products\n2.Register a shop\n->")
            if int(menu_4)==1:
                restaurant_show(restaurant_register(get_info_api(),product_register(get_info_api())))
            elif int(menu_4)==2:
                restaurant_management(client_obj,matches_obj,stadium_obj, spent_vip_client,boleto_register,product_count)
        elif int(menu)==5:
            statistics(spent_vip_client,matches_obj,boleto_register,client_obj)
        elif int(menu)==6: 
            pickle.dump(teams_obj,open("teams_obj.txt","wb"))
            pickle.dump(matches_obj, open("matches_obj.txt","wb"))
            pickle.dump(stadium_obj, open("stadium_obj.txt","wb"))
            pickle.dump(client_obj, open("client_obj.txt","wb"))
            pickle.dump(boleto_register,open("boleto_register.txt","wb"))
            with open("spent_vip_client.txt","wt") as archivo:
                spent_vip_client=str(spent_vip_client)
                archivo.write(spent_vip_client)
            with open("product_count.txt", "wt") as archivo:
                product_count=str(product_count)
                archivo.write(product_count)
            break
main(teams_obj,matches_obj,stadium_obj,client_obj,boleto_register,spent_vip_client,product_count)


