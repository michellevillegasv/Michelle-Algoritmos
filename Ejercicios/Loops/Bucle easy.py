#age = int(input("How old are you?: "))
#for i in range(age): 
#   age = i+1
#    print(i+1)
#number = int(input("Please enter a positive integer: "))
#for i in range(1, number+1, 2):
#    print(f"The odd numbers until {number} are: "+ str(i))
#
# number = int(input("Enter a positive integer number:"))
#while number > 0: 
 #   number-=1
  #  print(number, end= ",")
    
#NUMERO COMPUESTO 
number = int(input("Enter a number:"))
aux = number - 1
if number == 1:
    print("The number 1 is neither primer nor composite")
else: 
    while number%aux!= 0 and number>1:
        aux-=1
        if aux == 1:
            print(f"{number} is a not composite number")
        elif number%aux ==0:
            print(f"{number} is a composite number")





