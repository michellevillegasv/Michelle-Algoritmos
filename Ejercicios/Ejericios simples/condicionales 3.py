age = int(input("How old are you:"))
if(age < 4):
    print("Your ticket is free")
elif(age < 18): 
    print("You have to pay 5$ to play")
else: 
    print("You have to pay 10$ for the ticket")