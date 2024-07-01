print("This is a password checker to see if your password has the minimum requirements.")
print("It must have at least a minimum of 8 characters, at least 1 lowercase, 1 upper case, and 1 digit")
password = input("Enter Password Here : ")
lower = 0
upper = 0
digits = 0

if(len(password) >= 8):
    for letter in password:
        if(letter.islower()):
            lower += 1
        if(letter.isupper()):
            upper += 1
        if(letter.isdigit()):
            digits += 1

if(lower < 1 or upper < 1 or digits < 1):
    print("One of the requirements is not suffice. Try again")       
elif(lower + upper + digits >= 8):
    print("Valid Password")
else:
    print("Invalid Pass")
            
