while True: 
    triangule = False
    even = False
    sum =0
    num=input("Enter a number: ")
    if num.isalpha(): 
        print("Not valid")
        continue
    elif num.isnumeric(): 
        num = int(num)
        if num%2==0:
            even = True
        for i in range(num):
            consecu = i+1
            consecu < num
            sum += consecu
            if num == sum: 
                triangule = True 
    break
if triangule == True and even == True: 
    print(f"{num} is even and triangular")
if triangule != True and even == True: 
    print(f"{num} is even but not triangular")
if triangule == True and even != True: 
    print(f"{num} is not even but is triangular")
elif triangule!=True and even!= True: 
    print(f"{num} is neither even nor triangular")

