
validation_len = False
validation_upper = False
validation_lower = False
validation_num = False
validation_alnum = False
while True:
    password = input("Enter your password:")
    list_password = list(password)
    password_accepted =[]
    if len(list_password) <8:
        print("You have to write 8 or more characters")
        continue
    elif len(list_password)>=8:
        validation_len = True
    for characters in list_password:
        if characters.isupper():
            validation_upper = True
        elif validation_upper:
            continue
    for characters in list_password:
        if characters.islower():
            validation_lower = True
        elif validation_lower:
            continue
    for characters in list_password:
        if characters.isnumeric():
            validation_num = True
        elif validation_num:
            continue
    for characters in list_password:
        if characters.isalnum():
            validation_alnum = True
        elif validation_alnum:
            continue
    if validation_alnum == True and validation_len == True and validation_lower == True and validation_upper == True and validation_num == True:
        password_accepted.append(password)
        print("Your password is valid. Welcome")
        break
    else:
        print("Enter a valid password. Your password have to be compound by: one uppercase and one lowercase letter, an alphanumeric symbol and at least one number")
        continue