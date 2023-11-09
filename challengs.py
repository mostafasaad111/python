# Strings_output = open("strings_output.txt", "wt")
# stringInput = open("strings.txt")

# phrase = ""
# for line in stringInput:
#     if line.strip() == "I":
#         phrase += " " + line.strip().lower()
#     elif line.strip() == "Almadrasa":
#         phrase += " " + line.strip().lower()
#     else:
#         phrase += " " + line.strip()

# print(phrase)
# print(phrase, file=Strings_output)

a, b, c = map(int, input("Enter the Numbers : ").split())
print("The Numbers are : ", end=" ")
print(a, b, c)