print("Calculator")

# Input numbers
num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

# Operations
print("Press + for Addition")
print("Press - for Subtraction")
print("Press * for Multiplication")
print("Press / for Division")

# User choice
choice = input("Enter your operation from above: ")

# Perform calculation based on user choice
if choice == '+':
    print("Result:", num1 + num2)
elif choice == '-':
    print("Result:", num1 - num2)
elif choice == '*':
    print("Result:", num1 * num2)
elif choice == '/':
    # Handle division by zero
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Enter a valid operator.")
