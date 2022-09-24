from ast import Mult


num = int(input("Enter a intger positive number:"))
for i in range(num):
    for j in range(i+1):
        print("*", end="")
    print("")
