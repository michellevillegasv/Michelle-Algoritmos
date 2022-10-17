


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
def ambicioso(num, max=10):
    if perfect_numbers(suma(num),num) == True:
        print("Es ambicioso")
    while max!=0 and num!=1:
        if perfect_numbers(suma(num),num) == False:
            num = suma(num)
            max-=1
            if max==0:
                print("No es ambicioso")
        break

ambicioso(num)



