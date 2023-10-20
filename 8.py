# String  Methods

MyStringOne = "This is my string one "
MyStringTwo = "This is my string two "
MyStringThree = 'This is my string "test" '

print(MyStringOne)
print(MyStringTwo)
print(MyStringThree)

MyStringFour = """test 
one 
two 
three
"""
MyStringFive = """test 
one 
two 
three
"""
print(MyStringFour)
print(MyStringFive)

# String Indexing & Slicing


# indexing# (Access single item  هنا بطبع حرف معين
myString = "I love python"
print(myString[0])  # I
print(myString[2])  # l
print(myString[-3])  # o


# Slicing # (Access multiple items)
# [start:end]  هنا عاوز اطبع الحروف من كذا لكذا
print(myString[8:11])  # yth
print(myString[2:11])  # love pyth
print(myString[:11])  # I love pyth
print(myString[3:])  # ove python
print(myString[:])  # I love python

# [start:end:steps] هنا عاوز اطبع الحروف من كذا لكذا واعمل استيب
print(myString[0::1])  # I love python
print(myString[::1])  # I love python
print(myString[::3])  # Io tn

################### String Methods ############################
a = "I love python"
b = "I   love python"
print(len(a))

# strip() rstrip() lstrip()  هنا بحذف المسافات من اليمين او الشمال او الاثنين معا
a = "   I love python     "
print(len(a.strip()))
print(len(a.rstrip()))
print(len(a.lstrip()))

a = "##$I love python####"
print(a.strip("#$"))
print(a.rstrip("#"))
print(a.lstrip("$#"))

# title() هنا بخلي اول حرف كبير
c = "I love 2d and front 3g Technologies and c++"
print(c.title())

# capitalize  هنا الحروف اللي بعد الارقام مش هيحصل ليها حاجه
b = "I love 2d and front 3g Technologies and c++"
print(b.capitalize())


# zfill  هنا بيحط اص
a, b, c = "1", "11", "111"
print(a)
print(b)
print(c)

print(a.zfill(3))
print(b.zfill(3))
print(c.zfill(3))

# upper
g = "mustafa"
print(g.upper())

# lower
h = "oSama"
print(h.lower())

# split() rsplit()
a = "I love python and javascript"
print(a.split())
print(type(a.split()))

b = "I0love0python0and0javascript"
print(b.split("0"))

b = "I0love0python0and0javascript"
print(b.split("0", 2))

b = "I0love0python0and0javascript"
print(b.rsplit("0", 2))

# center
e = "osama"
print(e.center(9, "#"))

# count()
f = "I love python and javascript"
print(f.count("a"))
print(f.count("a", 0, 20))

# swapcase()
g = "I love python"
h = "I love javascript"
print(g.swapcase())
print(h.swapcase())

#startswith()
i = "I love python "
print(i.startswith("i"))
print(i.startswith("I"))
print(i.startswith("I",7,12))

#endswith()
j = "I love python "
print(j.endswith("i"))
print(j.endswith("I"))
print(j.endswith("I",7,12))


#index(subString , Start , end)
a="I love python"
print(a.index("p"))
print(a.index("p",0,12))
# print(a.index("p",0,3))   Error


#find(subString , Start , end)
a="I love python"
print(a.find("p"))
print(a.find("p",0,12))

#rjust()  ljust()
c="sad"
print(c.rjust(10))
print(c.rjust(10,"#"))

print(c.ljust(10))
print(c.ljust(10,"#"))

#splitlines()
e=""" first line
second line
third line"""
print(e.splitlines())

f="first line\nsecond line\nthird line"
print(f.splitlines())

#expandtabs()
g="hello\tworld\ti\tlove\tpython"
print(g.expandtabs(4))

one="I love python and 3g"
two="I love python and 3g"
print(one.title())
print(one.istitle())
print(two.istitle())


three=" "
four=""
print(three.isspace())
print(four.isspace())

five='I love Python'
print(five.islower())


seven="mustafa_sad"
eight="mustafaSad200"
nine = "mustafa--Sad300"
print(seven.isidentifier())
print(eight.isidentifier())
print(nine.isidentifier())


x="aaabbccc"
z="aaabb23232ccc"
print(x.isalpha())
print(z.isalpha())

x="aaabbccc"
z="aaabb23232ccc"
print(x.isalnum())
print(z.isalnum())

#replace(old value, new value , count)
a ="Hello one two three one one "
print(a.replace("one" ,"1"))
print(a.replace("one" ,"1",1))
print(a.replace("one" ,"1",2))

#join(iterable)
myList=["one","two","three","four","five","six"]
print(myList)
print("-".join(myList))
print("  ".join(myList))
print(type(", ".join(myList)))