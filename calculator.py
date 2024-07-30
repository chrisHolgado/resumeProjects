def add(x,y):
    return x + y
def subtract(x,y):
    return x - y
def mult(x,y):
    return x * y
def divide(x,y):
    return x / y

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
choice = int(input("Choose your selection : "))

if(choice == 1):
    num1 = int(input("Enter your first number : "))
    num2 = int(input("Enter your second number : "))
    print(add(num1,num2))

elif(choice == 2):
    num1 = int(input("Enter your first number : "))
    num2 = int(input("Enter your second number : "))
    print(subtract(num1,num2))

elif(choice == 3):
    num1 = int(input("Enter your first number : "))
    num2 = int(input("Enter your second number : "))
    print(mult(num1,num2))

elif(choice == 4):
    num1 = int(input("Enter your first number : "))
    num2 = int(input("Enter your second number : "))
    print(divide(num1,num2))

else:
    print("invalid input")
