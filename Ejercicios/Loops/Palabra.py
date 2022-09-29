
word = input("Enter a word:")
count = 0
if word.isalpha():
    for letter in range(len(word)):
        count+=1
        print(word[len(word)-count])      
else:
    print("Error")
