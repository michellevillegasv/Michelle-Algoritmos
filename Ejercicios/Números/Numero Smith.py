num=(input("Please enter a number: "))
def divisores(num):
    num = int(num)
    divisores_list = []
    for divisores in range(2,int(num)):
        if num%divisores==0:
            divisores_list.append(divisores)
    return divisores_list
def digitos(num,suma=0):
    for digitos in num:
        digitos=int(digitos)
        
        suma+=digitos
    return suma
def multiplicidad(divisores,num,multiplicidad2=0):
    num=int(num)
    count_divisores=0
    for num1 in divisores:
        num1=int(num1)
        for divisores2 in range(2,num1):
            if num1%divisores2==0:
                count_divisores+=1
                divisores.remove(num1)
                break
    for divisores_primos in divisores:
        divisores_primos=int(divisores_primos)
        multiplicidad1= num/divisores_primos
        multiplicidad2+=multiplicidad1
    return multiplicidad2
if multiplicidad(divisores(num),num) == digitos(num):
    print(F"{num} is a Smith number")
else:
    print(f"{num} is not a smith number")