


num = int(input("Please enter a number:"))
  
def suma(num):
        num=int(num)
        suma1=0
        for number in range(2,num):
            if num%number == 0:
                suma1+=number
        return suma1
def perfect_numbers(suma,num):
    perfect = False
    if suma!=num:
        return perfect
    if suma == num:
        perfect = True
        return perfect
    if suma==1:
        return perfect
def ambicioso(num):
    ambicioso_verificador = False
    while suma(num) !=num:
        num= suma(num)
        if perfect_numbers(suma(num),num) == True:
            ambicioso_verificador=True
            break
    if ambicioso_verificador== True:
        print(f"The number is an aspiring number")
    else:
        print("The number is not an aspiring number")
ambicioso(num)



