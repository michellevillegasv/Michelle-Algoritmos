
while True:
    number = input("Enter a number: ")
    divisores = 0
    primo = True
    if number.isalpha():
        print("Not valid")
        continue
    if number.isnumeric():
        number=int(number)
        operator = ((22*(number))+1)
        for i in range(2,operator):
            if operator%i==0:
                divisores +=1
                primo = False
        break
if primo == True: 
    print(f"{operator} is a Fermat number")
else: 
    print(f"{operator} is not a Fermat number")
    

