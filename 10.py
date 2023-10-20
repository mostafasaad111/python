##  Lesson assignments from Lesson 011 to 018
name = "Mustafa"
age = 23
country = "Egypt"
print(
    f'Hello \'{name}\', How you Doing \\ """ YOU age is "{age}""  and your country is: {country}'
)

########------2----------#########
print(
    f'hello \'{name}\',How you Doing \\ \n """ your age is "{age}"" +\n and your country is : {country}'
)

#--------3--------#
name="Elzero"
print(name[1:2])
print(name[2:3])
print(name[5:6])

#---------4--------#
print(name[1:3])
print(name[0:1] + name[2:3] + name[4:5])
print(name[4:5] + name[2:3] + name[0:1])
#-------5---strip------_#
name = "#@#@Elzero#@#@"
print(name.strip("#@"))

#--------6----------#

num1 = "9"
num2 = "15"
num3= "130"
num4 = "950"
num5 = "1500"

print(num1.zfill(4))
print(num2.zfill(4))
print(num3.zfill(4))
print(num4.zfill(4))
print(num5.zfill(4))

#----------7-------#
name_one = "Osama"
name_two = "Osama_Elzero"

print(name_one.rjust(20,"@"))
print(name_two.rjust(30,"@"))

#----------8-------#

name_one = "OSamA"
name_two = "osaMA"

print(name_one.swapcase())
print(name_two.swapcase())

#----------9---count method----#
msg = "I Love Python And Although Love Elzero Web School"
print(msg.count("Love"))
#----------10-------#
name = "Elzero"
print(name.index("z"))
#----------11-------#
msg = "I <3 Python And Although <3 Elzero Web School"
print(msg.replace("<3","love",1))
#----------12-------#
msg = "I <3 Python And Although <3 Elzero Web School"

print(msg.replace("<3","love"))

#---------13------#
name = "Osama"
age = 38
country = "Egypt"

print(f"My name is {name}, and my age is {age}, and my country is {country}")

#---------14------#
