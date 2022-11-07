from flores import Flower
from semillas import Seed
from vendedores import Vendedor
products1 = [
    {"id":1, "name": "Rose","type":"flower", "stock": 160, "colors": ["red","white","pink"]},
    {"id":2, "name": "Tulip","type":"flower", "stock": 34, "colors": ["white","yellow"]},
    {"id":3, "name": "Sunflower seeds","type":"seeds", "stock": 50},
    {"id":4, "name": "Sunflower","type":"flower", "stock": 77, "colors": ["yellow"]},
    {"id":5, "name": "Lavender seeds","type":"seeds", "stock": 100, "colors": ["purple"]},
    {"id":6, "name": "Carnation","type":"flower", "stock": 89, "colors": ["yellow","burgundy","purple", "pink", "red", "white"]}
]
vendor_1 =[
    {"product_id":5, "customer_id": 333, "amnt":1},
    {"product_id":5, "customer_id": 1010, "amnt":2},
    {"product_id":3, "customer_id": 1111, "amnt":3},
    {"product_id":2, "customer_id": 222, "amnt":6},
    {"product_id":6, "customer_id": 444, "amnt":7},
    {"product_id":1, "customer_id": 1111, "amnt":20}
]
vendor_2 =[
    {"product_id":6, "customer_id": 888, "amnt":10},
    {"product_id":1, "customer_id": 123, "amnt":5},
    {"product_id":2, "customer_id": 321, "amnt":4},
    {"product_id":4, "customer_id": 555, "amnt":2},
    {"product_id":1, "customer_id": 777, "amnt":1},  
]
products_obj=[]
vendedores_obj =[]
def products_object_add(list_products_obj, list_products):
    for dic in list_products:
        if dic["type"] == "flower": 
            obj = Flower(dic["type"], dic["id"], dic["name"], dic["stock"], dic["colors"])
        elif dic["type"] == "seeds":
            obj= Seed(dic["type"], dic["id"], dic["name"], dic["stock"])
        list_products_obj.append(obj)
def show_products(products_list):
    for products in products_list:
        products.show()
def register_vendedor(list_vendedores, vendedor1, vendedor2):
    for dic in vendedor1:
        vendedor1_obj = Vendedor(dic["product_id"], dic["customer_id"], dic["amnt"])
        list_vendedores.append(vendedor1_obj)
    for dic in vendedor2:
        vendedor2_obj = Vendedor(dic["product_id"], dic["customer_id"], dic["amnt"])
        list_vendedores.append(vendedor2_obj)
def show_salers(list_salers):
    list_salers.sort(key=lambda sale: sale.amount)
    for salers in list_salers:
        salers.show()

def main():
   products_object_add(products_obj,products1)
   print("****WELCOME****")
   while True:
    menu = input("\nChoose an option: \n1. See the list of products \n2, List sales \n3. Exit \n->")
    if menu.isalpha():
        continue
    if menu.isnumeric():
        if int(menu)==1:
            show_products(products_obj)
        if int(menu) == 2:
            register_vendedor(vendedores_obj,vendor_1,vendor_2)
            show_salers(vendedores_obj)
      
        if int(menu)==3:
            print("***GOODBYE!***")
            break
main()