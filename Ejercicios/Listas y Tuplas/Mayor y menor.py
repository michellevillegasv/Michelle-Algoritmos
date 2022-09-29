
lottery = input("Enter the number of the lottery: ")
while True: 
    if lottery.isnumeric():
        exit = (input("Do you want to add another number?: \n1-> Yes \n2-> No \n3->"))
        if exit.isalpha():
            if exit == "Yes":
                lottery = input("Enter the number of the lottery: ")
            elif exit == "No":
                break
            else:
                print("No valid option")
                break
        elif exit.isnumeric() or exit.isalnum():
            print("Error")
    else:
        print("Not valid")
lottery_list = list(lottery)
for i in lottery_list:
    lottery_list.sort()
    print(lottery_list)