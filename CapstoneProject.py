import string
import random

'''
#Password Checker Criteria
#8 Character Minimum
#Special Characters
#Lower & Upper Case
#Minimum of 1 Number
'''

def PassChecker(password):
  lowercase = 0
  uppercase = 0
  numbers = 0
  specialCharCheck = 0
  
  specialChars = "()!@#$%^&*_-+={}[]|\:;'<>,.?/~`"
  
  if len(password) >= 8:
    for i in password:
      if i.islower():
        lowercase += 1
      if i.isupper():
        uppercase += 1
      if i.isnumeric():
        numbers += 1
      if i in specialChars:
        specialCharCheck += 1

    if lowercase >= 1 and uppercase >= 1 and numbers >= 1 and specialCharCheck >= 1:
        print("This is a well written password!")
    else:
        print("This is not a well written password! You must have at least one lowercase letter, one uppercase letter, one number, and one special character.")
  else:
    print("Password must be at least 8 characters long")

'''
This is the random pass generator
It does the following:
- It uses the String Library to get all the lowercase letters, digits, and punctuations
- Password Variable will store the password using random choices in the characters variable.
- Prints it out
'''

def RandomPassGen(passwordLength):
  AllCharacterChoices = string.ascii_letters + string.digits + string.punctuation
  password = ''.join(random.choice(AllCharacterChoices) for i in range(passwordLength))
  print("The password you have generated with the length of " + str(passwordLength) + " characters is " + password)


#We're deciding on the name of the program
print("Welcome to SecurePass!")
print("This is your all in one software for passwords!")

#Menu
print("1. Password Checker")
print("2. Random Password Generator")
choice = int(input("Enter what option would you like to do : "))
if choice == 1:
    password = input("Enter the password that you want to check: ")
    print(PassChecker(password))
elif choice == 2:
    passwordLength = int(input("Enter the length of the password: "))
    RandomPassGen(passwordLength)
else:
    print("Invalid Input")
