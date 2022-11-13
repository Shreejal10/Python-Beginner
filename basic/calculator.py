def add(a, b):
    sum = a+b
    print("The sum of", a, "and", b, "is: ", sum)


def subtract(a, b):
    difference = a-b
    print("The difference of", a, "and", b, "is: ", difference)


def multiply(a, b):
    multiply = a*b
    print("The product of", a, "and", b, "is: ", multiply)


def divide(a, b):
    divide = a/b
    print("The division of", a, "and", b, "is: ", divide)


def modulo(a, b):
    modulo = a % b
    print("The remaidner of", a, "and", b, "is: ", modulo)


a = input("Enter first number: ")
b = input("Enter second number: ")
print("Available operations:")
print("1. Add (+)")
print("2. Subtract (-)")
print("3. Multiply (*)")
print("4. Divide (/)")
print("5. Modulo (%)")
operator = input("Your choice: ")
if int(operator) == 1:
    add(int(a), int(b))
elif int(operator) == 2:
    subtract(int(a), int(b))
elif int(operator) == 3:
    multiply(int(a), int(b))
elif int(operator) == 4:
    divide(int(a), int(b))
elif int(operator) == 5:
    modulo(int(a), int(b))
else:
    print("Invalid Input")
