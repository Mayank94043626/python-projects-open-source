import re

# function to check whether the password is valid or not.
def validator(password):
    flag = 0
    while True:
        if len(password)<8 or len(password)>16:   #length limiter
            flag = -1
            break
        elif not re.search("[a-z]",password):     #presence of lowercase letter
            flag = -1
            break
        elif not re.search("[A-Z]",password):     #presence of uppercase letter
            flag = -1
            break
        elif not re.search("[0-9]",password):     #presence of digit
            flag = -1
            break
        elif not re.search("[@#$&_]",password):   #presence of special character
            flag = -1
            break
        elif re.search("\s", password):           #check if space present.
            flag = -1
            break
        else: 
            print("This is a valid password") 
            break
        
    if flag ==-1: 
        print("This is not a valid password")

password = input("Enter the password:")
validator(password)