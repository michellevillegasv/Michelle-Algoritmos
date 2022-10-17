list_numbers = []

while True:
    num = float(input("Enter a number: "))
    list_numbers.append(num)
    if (input("Do you want to enter another number?: \nYes \nNo \n- ")) == "No":
        break
    else: 
        continue
def squares(list_numbers):
    list_squares=[]
    for i in list_numbers:
        i=float(i)
        cuadrado = i**2
        list_squares.append(cuadrado)
    return list_squares
print(f"Los cuadrado de {list_numbers} are {squares(list_numbers)}")
