# ----------set Methods----------#
mySet1 = {"osama", "ahmed", 100}
print(mySet1)

# not slicing and indexing

# clear()
set2 = {"osama", "ahmed", 100}
set2.clear()
print(set2)

# union()
b = {"one", "two", "three", "four", "five", "six"}
c = {1, 2, 3, 4}
print(b | c)
print(b.union(c))

# add()
d = {1, 2, 3, 4, 5}
d.add(3)
d.add(10)
print(d)

# copy()
e = {1, 2, 3, 4, 5}

e.add(6)
f = e.copy()
print(e)
print(f)

# remove()
g = {1, 2, 3, 4, 5}
g.remove(1)
# g.remove(7)

# discard()
h = {1, 2, 3, 4, 5}
h.discard(1)
h.discard(7)
print(h)

# pop()
i = {2, 3, 4, True, "q", 5}
print(i.pop())

# update()
j = {2, 3, 4, True}
k = {5, 6, "b", "c"}
j.update(["html", "css"])
j.update(k)
print(j)

print("=" * 40)
# difference()
a = {1, 2, 3, 4, 5}
b = {1, 2, "a", "b"}
print(a)
print(a.difference(b))  # a - b
print(a - b)
print(a)
print("=" * 40)

# different_update()
c = {1, 2, 3, 4, 5}
d = {1, 2, "a", "b"}
print(c)
c.difference_update(b)  # a - b
print(c)

print("=" * 40)

# intersection() المشترك
e = {1, 2, 3, "m", "v"}
f = {1, "kk", 3, "v", "h"}

print(e)
print(e.intersection(f))  # e&f
print(e & f)
print(e)
print("=" * 40)

# intersection_update()
b = {1, 2, 3, "m", "v"}
v = {1, "kk", 3, "v", "h"}

print(b)
b.intersection_update(v)  # e&f
print(b)
print("=" * 40)

# symmetric difference()  هنا المشترك بينهم نشيله وناخد اللي يفضل
u = {1, 2, 3, "m", "v"}
t = {1, "kk", 3, "v", "h"}

print(u)
print(u.symmetric_difference(t))
print(u)
print("=" * 40)

# symmetric difference_update()
u = {1, 2, 3, "m", "v"}
t = {1, "kk", 3, "v", "h"}

print(u)
u.symmetric_difference_update(t)
print(u)
print("=" * 40)

# issuperset()

a = {1, 2, 3, 4}
b = {1, 2, 4}

print(b.issuperset(a))
print(a.issuperset(b))
print("=" * 40)

# issubset()
d = {1, 2, 3, 4}
e = {1, 2, 3}
f = {11, 2, 4, 5, 6}
print(e.issubset(d))
print(d.issubset(e))
print("=" * 40)
# isdisjoint()
d = {1, 2, 3, 4}
e = {1, 2, 3}
f = {33, 444, 55, 66}
print(d.isdisjoint(e))
print(e.isdisjoint(d))
print(f.isdisjoint(d))
print("=" * 40)

# ----------------------------------------------Dictionary------------------------------#
user = {
    "name": "sad",
    "age": 23,
    "gender": "male",
    "skills": ["html", "javascript", "python", "css"],
    "name": "ahmed",
}
print(user)
print(user["gender"])
print(user.get("name"))

print(user.keys())
print(user.values())
print("=" * 40)

# Two-Dimensional Dictionary
lang = {
    "one": {"name": "Html", "pro": "80%"},
    "two": {"name": "css", "pro": "100%"},
    "three": {"name": "go", "pro": "100%"},
    "four": {"name": "python", "pro": "100%"},
}
print(lang)
print(lang["two"])
print(lang["one"]["name"])
print(len(lang))
print(len(lang["one"]))

# create dictionary from variables
framwork = {"name": "vue.js", "pro": "90%"}
framwork1 = {"name": "react.js", "pro": "90%"}
framwork2 = {"name": "next.js", "pro": "90%"}
framwork3 = {"name": "angular.js", "pro": "90%"}

allframework = {
    "one": framwork,
    "two": framwork1,
    "three": framwork2,
    "four": framwork3,
}

print(allframework)
print("=" * 50)
# --------------------------------------dictionary method--------------------------------#
# clear()
user = {
    "name": "sad",
}
print(user)
user.clear()
print(user)

print("=" * 50)

# update()
member = {"name": "sad"}
print(member)
member["age"] = 23
print(member)
member.update({"country": "egypt ", "gender": "male"})
print(member)
print("=" * 50)

# copy()
main = {"name": "sad"}
b1 = main.copy()
print(b1)
print(main)

main.update({"skills": "fighting"})
print(b1)
print(main)

# keys( ) values()
main = {"name": "sad"}

print(main.keys())
print(main.values())

# setDefault()
user = {
    "name": "sad",
}

print(user)
print(user.setdefault("age", 23))
print(user)
print("=" * 40)


# popitem()
member = {
    "name": "mustafa",
    "age": 23,
}
print(member)
member.update({"skills": " logic of programming"})
print(member.popitem())
print("=" * 40)


# items()
view = {
    "name": "sad",
    "skills": "html & CSS classes",
}
AllItems = view.items()
print(view)
view["age"] = 23
view.update({"country": "Egypt", "gender": "male"})
print(AllItems)
print("=" * 50)

# fromkeys()

a = ("myKeyOne", "myKeyTwo", "myKeyThree")
b = "x"
print(dict.fromkeys(a,b))
