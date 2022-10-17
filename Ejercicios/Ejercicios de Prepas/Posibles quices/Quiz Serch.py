list_numbers = ([313, 153, 370], [], [31, 515, 78593, 3819, 12],
[407, 9041], [371, 706], [407,153, 1, 2],
[41, 4], [5], [1, 2, 3, 4, 5, 6, 7, 8, 9],
[313, 54748, 370], [], [31, 515, 432, 313, 45],
[313, 88, 407], [153, 370], [1634, 8208, 9474],)

def narcisistas(list_numbers):
    narcisists=[]  
    for lists in (list_numbers):
        for numbers in lists:
            numbers=str(numbers)
            suma=0
            for digits in numbers:        
                digits=int(digits)
                digits1 = digits**(len(numbers))
                suma+=digits1                    
            if suma== int(numbers):
                narcisists.append(numbers)
            if suma!=numbers:
                continue
    return narcisists
narcisist = narcisistas(list_numbers)
print(f"Some narcisist number are:")
for numbers in narcisist:
    print(f"{numbers}",end="; ")


            
        