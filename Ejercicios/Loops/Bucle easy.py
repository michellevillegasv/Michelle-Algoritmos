age = int(input("How old are you?: "))
for i in range(age): 
    age = i+1
    print(i+1)

number = int(input("Please enter a positive integer: "))
for i in range(1, number+1, 2):
    print(f"The odd numbers until {number} are: "+ str(i))