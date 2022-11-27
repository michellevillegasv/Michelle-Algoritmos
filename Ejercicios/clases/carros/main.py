from carro import Car,Motorcycle
vehiculos = [ 
    { "tipo": "AUTOMOVIL", "placa": "ABC12D", "marca": "Chevrolet", "puesto": "A12", "entrada": "10:00:36", "minusvalido": False},
    { "tipo": "AUTOMOVIL", "placa": "IJK56M", "marca": "Mazda", "puesto": "A33", "entrada": "11:48:22", "minusvalido": False},
    { "tipo": "MOTOCICLETA", "placa": "EFG34H", "marca": "Suzuki", "puesto": "B10", "entrada": "10:20:15"},
]
vehicle_obj =[]
def register_vehicles(vehiculos_list, vehicle_obj):
    for diccionaries in vehiculos_list:
        if diccionaries["tipo"] == "AUTOMOVIL":
            vehicle_obj.append(Car(diccionaries["placa"],diccionaries["marca"],diccionaries["puesto"], diccionaries["entrada"], diccionaries["minusvalido"]))
        elif diccionaries["tipo"] == "MOTOCICLETA":
            vehicle_obj.append(Motorcycle(diccionaries["placa"],diccionaries["marca"],diccionaries["puesto"], diccionaries["entrada"]))
def vehicle_list_show(vehicle_obj):
    print("---CARS IN THE PARKING LOT---")
    for vehicles in vehicle_obj:
        vehicles.show()
def check_out_parking(vehicle_obj):
    salida = input("Enter the plate of the car you're going to check out: ")
    hora_salida = input("Enter the departure time: ")
    for vehicles in vehicle_obj:
        if salida==vehicles.placa:
            vehicles.hora_salida = hora_salida
            vehicles.puesto = None
        else:
            print("VEHICLE NOT FOUN IN THE PARKINGLOT")
def main():
    print("---WELCOME---")
    register_vehicles(vehiculos, vehicle_obj)
    while True: 
        
        menu=input("\n1.See all the parked cars\n2.Check out\n3.Exit\n-> ")
        while menu.isalpha(): input("ENTER A VALID OPTION\n1.See all the parked cars\n2.Check out\n3.Exit\n-> ")
        if int(menu)==1:
            vehicle_list_show(vehicle_obj)
        elif int(menu)==2:
            check_out_parking(vehicle_obj)
        elif int(menu)==3: break
main()