# Ask the user: "Insert your first number: "
number1 = input("Enter your first number: ")

# Ask the user: "Insert your second number: "
number2 = input("Enter your first number2: ")

# Ask the user: "Insert the operation: "
operation = input("Insert the operation: ")

if operation == "+":
    print(int(number1) + int(number2))
elif operation == "-":
    print(int(number1) - int(number2))
elif operation == "*":
    print(int(number1) * int(number2))
else:
    print("We don’t support this operation")

print("Thanks for using our software")
