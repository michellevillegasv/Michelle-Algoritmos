num=(input("Please enter a number:"))
num2 = input("Please enter another number:")
num3 = input("Please enter another number:")
num4 = input("Please enter another number:")
num5 = input("Please enter another number:")
if num.isnumeric():
    num=int(num)
    suma1 = 0
    for divisor in range(2, num):
        if num%divisor==0:
            suma1+=divisor
        else:
            continue
if num2.isnumeric():
    num2=int(num2)
    suma2=0
    for divisor1 in range(2,num2):
        if num2%divisor1==0:
            suma2+=divisor1
        else:
            continue
if num3.isnumeric():
    num3=int(num3)
    suma3=0
    for divisor3 in range(2,num3):
        if num3%divisor3==0:
            suma3+=divisor3
        else:
            continue
if num4.isnumeric():
    num4=int(num4)
    suma4=0
    for divisor4 in range(2,num3):
        if num4%divisor4==0:
            suma4+=divisor4
        else:
            continue
if num5.isnumeric():
    num5=int(num5)
    suma5=0
    for divisor5 in range(2,num5):
        if num5%divisor5==0:
            suma5+=divisor5
        else:
            continue
    if suma1 ==num2 and suma2 ==num3 and suma3 ==num4 and suma4 ==num5 and suma5 ==num:
        print(f"{num},{num2},{num3},{num4} and {num5} are friends numbers")
    else: 
        print(f"The numbers are not friends number")
