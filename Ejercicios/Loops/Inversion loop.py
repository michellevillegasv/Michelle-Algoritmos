
amount = float(input("Please enter the amount you're going to invest:$ "))
interest = float(input("Please enter the annual interes: % "))
years = int(input("Please enter how many years are you going to be investing: "))
for i in range(years):
    years = i+1
    amount1 = amount*(interest/100)*years
    print(f"\nYear {years}: {amount1}", end="$")