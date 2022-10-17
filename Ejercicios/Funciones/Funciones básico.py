def main():
    name = input("Enter your name:")
    name= name.upper()
    print(f"****WELCOME {name}****")
    return 
main()
def factorial(num):
    factorial = 1
    for i in range(num): 
        i=int(i)
        factorial*=i+1        
    
    return factorial
print(factorial(5))
print(factorial(20))