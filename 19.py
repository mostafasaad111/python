# ---------Boolean-----------

name =(" ")
print(name.isspace())
print("=" * 50)
print(100 > 200)

print("=" * 50)
print(bool("osama"))
print(bool(100))
print(bool(100.345))
print(bool(True))
print(bool([1,2,3,4,5,6])) 
print("=" * 50)

print(bool(0))
print(bool(""))
print(bool(''))
print(bool(False))
print(bool([]))
print(bool(None))
print("=" * 50)

#----------Boolean Operators---#
age = 23
country = "egypt"
rank = 10 

print(age > 25)
print(country == "egypt" )

print( age > 21 and country == "egypt" and rank == 10  )

age2 = 22
country2 = "ksa"
rank2 = 12 

print( age2 > 12 or country2 == "egypt" or rank2 == 12)
print( age2 > 12 or country2 == "egypt" or  rank2 == 2)
print( age2 > 22 or country2 == "kba" or rank2 == 2)

age3 = 22
country3 = "ksa"
rank3 = 12 
print(not age3 > 22 )


# ----------Assignment Operators ------#
x = 10
y = 20 
z = x + y 
print(z)

x += y
y += y 

print(y)
print(x)

x -= y 
y -= y 
print(y)
print(x)

x *= x
print(x)

#-------comparison operator ----------#
# [ == ] Equal 
# [ != ] Not Equal


# [ equal + not equal ]
print("=" * 50)
print( 100 == 100 )
print( 100 == 100.00)
print( 100 == 200)
print("=" * 50)
print( 100 != 100 )
print( 100 != 100.00)
print( 100 != 200)

# [>] greater than 
# [<] less than  
print("=" * 50)
print( 100 > 100 )
print( 100 > 100.00)
print( 100 > 200)

#[>=]
#[<=]

# type Conversion

a = 10 
print( type(a))
print( type(str(a)))

print("=" * 50)
c = "osama"
d = [1,2,3,4,5]
e ={ "a" , "b" , "c" , "d" }
f = {"a" :1 , "b" :2 }
t = 200

print(tuple(c))
print(tuple(d))
print(tuple(e))
print(tuple(f))
# print(tuple(t))

print("=" * 50)
c = "osama"
d = (1,2,3,4,5)
e ={ "a" , "b" , "c" , "d" }
f = {"a" :1 , "b" :2 }
t = 200
print(list(c))
print(list(d))
print(list(e))
print(list(f))


print("=" * 50)
c = "osama"
d = (1,2,3,4,5)
e =[ "a" , "b" , "c" , "d" ]
f = {"a" :1 , "b" :2 }
t = 200
print(set(c))
print(set(d))
print(set(e))
print(set(f))

print("=" * 50)
# c = "osama"
d = (("a", 1), ("b", 2), ("c", 3))
e =[ ["a",1 ], ["b",2]]
# t ={ "a" , "b" , "c" , "d" }

# print(dict(c))
print(dict(d))
print(dict(e))
