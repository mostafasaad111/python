##########--------lists---------------###########
myList = ["one", "two", "one", 1, 100.5, True]

print(myList)
print(myList[1])
print(myList[2])
print(myList[-3])
print(myList[-1])

print(myList[1:4])
print(myList[:4])
print(myList[1:])

print(myList[::1])
print(myList[::2])

myList[-1] = False
myList[3] = 3
myList[0:2] = ["a", "b", "c"]
print(myList)


# ------lists Methods ----------------#
# append()

myFriends = ["Osama", "Ahmed", "Sayed"]
myOldFriends = ["ali", "sad", "alam"]

myFriends.append("Alam")
myFriends.append(100)
myFriends.append(True)
myFriends.append(150.200)
myFriends.append(myOldFriends)

print(myFriends)
print(myFriends[2])
print(myFriends[7][0])

# extend()بضمهم قيمه واحده
a = [1, 2, 3, 4, 5]
b = ["a", "b", "c", "d", "e", "f", "g"]
c = ["one", "two"]
a.extend(b)
a.extend(c)
print(a)


# remove() ببحذف اول واحد
x = [1, 2, 3, 4, 5, 6, "mustafa", True, "mustafa", "mustafa"]
x.remove("mustafa")
print(x)

# sort()  ترتيب
y = [1, 2, 100, 120, -20, 12, 34]
y.sort(reverse=True)
print(y)

# reverse() بيعكس
z = [10, 1, 9, 80, 100, "mustafa", 100]
z.reverse()
print(z)

#clear()بحذف كل عناصر اليست 
a = [ 1,2,3,4]
a.clear()
print(a)

#copy()باخد نسخه من اليست 
b =[1,2,3,4,5,6]
c = b.copy()
print(b)
print(c)

#count()
d=[1,2,3,4,5,5,6]
print(d.count(5))

#index()
e =["a","b","c"]
print(e.index("a"))

#insert()
f = [ 1,2,3,4,5,6,7, "a","b"]
f.insert(0 ,"c")
f.insert(4 ,"sayed")
print(f)

#pop()
g=[1,3,3,4,5,6,"a","b"]
print(g.pop(-1))