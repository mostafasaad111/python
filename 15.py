# --------- Tuple -------#
# Tuple format
myTupleOne = ("mustaf", "sad")
myTupleTwo = "mustaf", "sad"

print(myTupleOne)
print(myTupleTwo)

print(type(myTupleOne))
print(type(myTupleTwo))

# Tuple Indexing

myTupleThree = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
print(myTupleThree[0])
print(myTupleThree[-1])
print(myTupleThree[3])

# Tuple Assign Values
# myTupleFour = (1,2,3,4,5,6,7,8,9,10,11,12)
# myTupleFour[2]="two"
# print(myTupleFour)

myList = ["sad", "sad"]
print(myList[0:])

# Tuple Items
myTupleTest = ("Osama", "Osama", 1, 2, 3, 4, 100.3, True)
print(myTupleTest[1])

# Tuple with one element
myTuple1 = ("osamma",)
myTuple2 = ("osamma",)

print(type(myTuple1))
print(len(myTuple1))

# Tuple concatenation
a = (1, 2, 3, 4, 5)
b = (2, 3)
c = a + b
print(c)

# tuple , list , string Repeat(*)

myString ="Osama"
myList= [1,2]
myTuple=("a","b")

print(myString * 5)
print(myList * 5)
print(myTuple * 5)

# Method => count()

a = ( 1,2,3,3,3,3,3,4,5,6,7,8)
print(a.count(3))


# Method => Index()

a = ( 1,2,3,3,3,3,3,4,5,6,7,8)
print(f"The position of Index is: {a.index(3)} ")

# tuple Destruct
a = ("a","b",4,"c")
x,y,_,z = a
print(x)
print(y)
print(z)

