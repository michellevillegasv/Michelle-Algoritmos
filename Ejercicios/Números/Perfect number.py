num=int(input("Please enter a number:"))
count = 1
for divisor in range(1, num+1):
    if num%divisor==0:
        count+=1
        suma = 0
        suma+=divisor
    if suma == num:
        print(f"{num} is a perfect number")
    else: 
        print(f"{num} is not a perfect number")

        