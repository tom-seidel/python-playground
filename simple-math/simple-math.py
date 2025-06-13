# Simple addition
a = 7
b = 5
result = a + b

print("The result of", a, "+", b, "is", result)

# Add two numbers entered by the user

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print("Sum:", a + b)

# Perform basic arithmetic operations

x = 10
y = 3

print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)
print("Floor Division:", x // y)
print("Modulo:", x % y)
print("Exponentiation:", x ** y)

# Perform basic arithmetic operations with user input

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)
print("Floor Division:", x // y)
print("Modulo:", x % y)
print("Exponentiation:", x ** y)

# A small interactive calculator

num1 = float(input("First number: "))
op = input("Operator (+, -, *, /): ")
num2 = float(input("Second number: "))

if op == "+":
    print("Result:", num1 + num2)
elif op == "-":
    print("Result:", num1 - num2)
elif op == "*":
    print("Result:", num1 * num2)
elif op == "/":
    print("Result:", num1 / num2)
else:
    print("Unknown operator")

# A small interactive calculator with error handling

num1 = float(input("First number: "))
op = input("Operator (+, -, *, /): ")
num2 = float(input("Second number: "))

try:
    if op == "+":
        print("Result:", num1 + num2)
    elif op == "-":
        print("Result:", num1 - num2)
    elif op == "*":
        print("Result:", num1 * num2)
    elif op == "/":
        print("Result:", num1 / num2)
    else:
        print("Unknown operator")
except ZeroDivisionError:
    print("Cannot divide by zero")