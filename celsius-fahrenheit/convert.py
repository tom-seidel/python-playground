# Convert celsius to fahrenheit
def convert_celsius_to_fahrenheit(celsius):
    
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit

# Convert fahrenheit to celsius
def convert_fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) / 1.8
    return celsius

# Enter your choice (1 or 2):
print("What would you like to do?")
print("1. Convert Celsius to Fahrenheit")
print("2. Convert Fahrenheit to Celsius")
choice = int(input("Enter your choice (1 or 2): "))

# Call the appropriate conversion function
if choice == 1:
    celsius = float(input("Enter the temperature in Celsius: "))
    fahrenheit = convert_celsius_to_fahrenheit(celsius)
    print("Temperature in Fahrenheit:", fahrenheit)
else:
    fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
    celsius = convert_fahrenheit_to_celsius(fahrenheit)
    print("Temperature in Celsius:", celsius)
