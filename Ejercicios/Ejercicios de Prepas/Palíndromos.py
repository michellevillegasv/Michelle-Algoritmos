variable = (input("Enter a number: "))
variable2 = variable[::-1]
if variable != variable2:
    print(f"{variable} is not a palindrome")
else:
    print(f"{variable2} is a palindrome")
