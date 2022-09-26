word = str(input("Enter a word: "))
vocal1 = "a", "e","i", "o", "u"
for vocal in range(word):
    vocal = str(vocal)
    if vocal == vocal1:
        vocal = vocal.upper()
print(word)