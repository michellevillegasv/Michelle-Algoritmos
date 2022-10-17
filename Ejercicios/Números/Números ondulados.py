num = (input("Enter a number: "))
for i in range(0, len(num)):
    ondulado = False
    index = i
    if num[index] == num[index+2] and num[index+1]==num[index+3]:
        ondulado=True
        break
    else:
        ondulado=False
        break
if ondulado==True:
    print(f"{num} es un numero ondulado")
else:
    print(f"{num} no es ondulado")
