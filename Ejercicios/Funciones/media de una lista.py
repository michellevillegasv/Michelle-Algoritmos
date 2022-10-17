list_numbers = []
while True:
    num = float(input("Enter a number: "))
    list_numbers.append(num)
    if (input("Do you want to enter another number?: \nYes \nNo \n- ")) == "No":
        break
    else: 
        continue
def media(list_numbers):
    suma =0
    for i in list_numbers:
        i=float(i)
        suma+=i
    mediatotal = suma/(len(list_numbers))
    return mediatotal
print(f"La media de {list_numbers} es{media(list_numbers)}")

