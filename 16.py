# --------------Assignments For Lessons 24 To 25 -----------#
myTuple = ("Sad",)
print(myTuple)
print(myTuple[0])
print(len(myTuple))
print(type(myTuple))

# ---------------2--------------#
friends = ("Osama", "Ahmed", "Sayed")
friendsList = list(friends)
friendsList[0:1] = ["Elzero"]
friends = tuple(friendsList)
print(friends)
print(len(friends))
print(type(friends))
# Needed Output

# ("Elzero", "Ahmed", "Sayed")
# <class 'tuple'>
# 3 Elements


# -----------------3----------------#
Tuple1 = (1, 2, 3)
Tuple2 = ("a", "b", "c")
Tuple3 = Tuple1 + Tuple2
print(Tuple3)
print(type(Tuple1))
print(type(Tuple3))
print(len(Tuple3))

# -----------------4--------------#
Tuple4 = (1, 2, 3, 4, 5)
x, c, v, _, b = Tuple4
print(x)
print(c)
print(b)
