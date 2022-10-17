while True: 
    suma=0
    cuadrado = False
    repunit = False
    numx = int()
    number = (input("Enter a number: "))
    if number.isalpha():
        print("Not valid")
    elif number.isnumeric():
        number2= number[::-1]
        for digits in number: 
            digits=int(digits)
            suma+=digits
            if suma**(1/2) == int((suma)**(1/2)):
                cuadrado=True
                break
        if number2==number:
            repunit = True
            break
        elif number2!=number: 
            repunit = False
            break
if repunit == True and cuadrado != True: 
    print(f"{number} is a repunit number but the sum of its digits is not a square number")
elif repunit != True and cuadrado == True:
    print(f"{number} is not a repunit number but the sum of its digits is a square number")
elif repunit == True and cuadrado == True: 
    print(f"{number} is a repunit number and the sum of its digits is a square number")
else: 
    print(f"{number} is not a repunit number and the sum of its digits is not a square number")
