while True:
    primo1 = True
    primo2 = True
    suma1=0
    suma2=0
    num1 = input("Enter a number: ")
    num2 = input("Enter another number: ")
    if num1.isalpha() or num2.isalpha():
        print("Not valid")
    if num1.isnumeric() and num2.isnumeric():
        num1=int(num1)
        num2=int(num2)
        for divisores in range(1,num1):
            if num1%divisores==0:
                suma1+=divisores
                primo = False
                
        for divisores2 in range(1,num2):
            if num2%divisores2==0:
                suma2+=divisores2
                primo2 = False
                
        if suma1== num2: 
            print(f"{num1} and {num2} are friends numbers")
        elif suma2== num1: 
            print(f"{num1} and {num2} are friends numbers")
        else: 
            print(f"{num1} and {num2} are not friends numbers")
        break


