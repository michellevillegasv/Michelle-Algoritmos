#EJERCICIO 1
from re import M, S


num1 = float(input("Enter a number:"))
num2 = float(input("Enter another number:"))
if(num2 == 0):
    print("Error, divisor is 0")
else:
    print(f"the result of {num1} out of {num2} is {num1/num2}")

#EJERCICIO 2
num = float(input("Enter a number: "))
if(num % 2 == 0): 
    print("Even number")
else:
    print("Odd number")

#EJERCICIO 3
age = int(input("What's your age?: "))
income = float(input("How much is your income?: $"))
if(age > 16 and income >= 1000):
    print("You meet the requirements to pay taxes")
else: 
    print("You don't have to pay taxes")

#EJERCICIO 4
name = input("What's your name?:")
gender = input("Enter your gender (Male or Female):")
if(gender == "Female" or gender =="female" and name[0] <"M"):
    print("You're group A")
elif(gender == "Male" or gender == "male" and name[0] > "N"):
    print("You're group A")
else:
    print("You're group B")
        

