# ----------------- the introduction -----------------------#

print("'hello 'world' ")

print("Hi!")
name = input("What's your name?")

print("It's nice to meet you, ", name)
answer = input("Are you enjoying the course?")

if answer == "yes":
    print("that's good to heart!")
else:
    print("oh no! that's bad!")

print("Challenge 1:")
message = "This is going to be tricky ;)"
Message = "Very tricky!"
print(message)
result = 3**2
print("3**2 =", result)
result = 3 - 5
print(result)
print("Challenge complete!")

# -----------intro for if condition --------#
print( 5 == 5)
print( 4 != 5)
print( 4 < 5)
print( 4 > 5)

# example 1
if 5 > 6:
    print("5 is greater than 6.")
else:
    print("5 is not greater than 6.")

# example 2

today = input("enter today: ")
if today == "friday":
    print(today , "is the weekend")
else :
    print(today, "is not the weekend")

# example 3

today = input("enter today: ")
if today == "friday":
    print(today , "is the weekend")
elif today == "saturday":
    print(today," I visit my calendar")
else :
    print(today, "is not the weekend")

# example 4

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


# example 5 
if (num>=0):
    print(num)
else:
    print(-1 * num)