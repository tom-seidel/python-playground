num1 = float(input("Enter the first number: "))
op = input("Enter the operator (+, -, *, /): ")
num2 = float(input("Enter the second number: "))

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
