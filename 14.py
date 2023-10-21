#-----------------Assignments For Lessons 21 To 23 ----------#
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

print(friends[::2])
print(friends[1::2])

print(friends[0])
print(friends.pop(0))
print(friends[-1])
print(friends.pop(-1))


friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

print(friends[1:-1])
print(friends[-2:])

#---------------4---------------#
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
friends[-2:] =["Elzero","Elzero"]
print(friends)
# Needed Output
# ["Osama", "Ahmed", "Sayed", "Elzero", "Elzero"]

#---------------5---------------#
friends = ["Osama", "Ahmed", "Sayed"]
friends.insert(0,"Nasser")
friends.insert(-1,"Sayed")
print(friends)
# Needed Output
# ["Nasser", "Osama", "Ahmed", "Sayed"]
# ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]

#----------------6-----------#
friends = ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]
friends[0:2] =[]
print(friends)

friends[-1:] = []
print(friends)
# Needed Output
# ["Ahmed", "Sayed", "Salem"]
# ["Ahmed", "Sayed"]

#-------------7-----------#
friends = ["Ahmed", "Sayed"]
employees = ["Samah", "Eman"]
school = ["Ramy", "Shady"]

friends.extend(employees)
friends.extend(school)
print(friends)
# Needed Output
# ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]

#---------------8------------------#
friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
friends.sort()
print(friends)

friends.sort(reverse= True)
print(friends)
# Needed Output
# ['Ahmed', 'Eman', 'Ramy', 'Samah', 'Sayed', 'Shady']
# ['Shady', 'Sayed', 'Samah', 'Ramy', 'Eman', 'Ahmed']

#------------------9-------------------#
friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
print(len(friends))
# Needed Output
# 6

#----------------9--------------_#
technologies = ["Html", "CSS", "JS", "Python", ["Django", "Flask", "Web"]]
print(technologies[-1][0])
print(technologies[-1][-1])
# Needed Output
# Django
# Web
