opening_balance = 3480
print(f"2020/04/10: Your opening balance is ${opening_balance}")
spent1 = float(input(print("Enter how many you spent: ")))
print(f"2020/04/11: You have spent ${spent1}, now you have ${opening_balance - spent1}")
charged1 = 1200
print(f"2020/04/17: You charged ${charged1} of your salary, now you have {opening_balance - spent1 + charged1} ")
interest = (opening_balance - spent1 + charged1)*3/100
print(f"2020/04/30: 3% interest is charged of your current balance, now your balance is ${interest} ")
spent2 = float(input(print("Enter hoy many you spent: ")))
print(f"2020/05/02: You have spent ${spent2}, your current balance is ${interest - spent2}")


