num = int(input("Please enter a number: "))
def sucesion(num):
    numbers_list=[]
    for numbers in range(num):
        numbers_list.append(numbers)
    if (numbers_list[-1] + numbers_list[-2])== num:
        return True
    else: 
        return False
if sucesion(num) == True:
    print(f"{num} pertenece a la Sucesión de Fibonacci")
if sucesion(num) == False:
    print(f"{num} no pertenece a la Sucesión de Fibonacci")
