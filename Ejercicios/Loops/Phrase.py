phrase = input("Enter a phrase: ")
letter = input("Enter a letter: ")
cont = 0
if phrase.isnumeric():
    ("Not valid phrase")
elif letter.isnumeric():
    print("Not valid letter")
else:
    for letters in phrase:
        if letters == letter: 
            cont+=1
    print(f"The letter appears {cont} times in phrase")          

            
