renta = int(input("Cuánto es tu renta anual?: €"))
if(renta <10000):
    print("Tu tipo impositivo es 5%")
elif(renta >= 10000 or renta < 20000):
    print("Tu tipo impositivo es 15%")
elif(renta>=20000 or renta<35000):
    print("Tu tipo impositivo es 20%")
elif(renta>=35000 or renta<60000):
    print("Tu tipo impositivo es 30%")
else: 
    print("Tu tipo impositivo es 45%")

#EJERCICIO 2
points = float(input("Score obtained: "))
if(points == 0.0):
    print(f"The score you got is {points}, your perfomance is UNACCEPTABLE, the money you will receive is: {points * 2400}$")
elif(points == 0.4):
    print(f"The score you got is {points}, your perfomance is ACCEPTABLE, the money you will receive is:{points*2400}$")
elif(points >= 0.6): 
    print(f"The score you got is {points}, your perfomance is MERITORIOUS, the money you will receive is:{points*2400}$")
else:
    print("Error")