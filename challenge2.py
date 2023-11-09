
print( "-----------the favorites list------------ ")
furits = ["apples", "banana", "grapes", "mangos", "nectarines", "pears"]

for furit in furits:
    print(furit.capitalize())
    
print("=" * 50)

# solve 1 
for x in furits:
    if x != "nectarines":
        print(x.capitalize())
        
print("=" * 50)
# solve 2 
i = 0 
while i < len(furits):
    if furits[i] != "nectarines":
        print(furits[i])
    i += 1
# solve 3
print("=" * 50)
for v in furits:
     if v == "nectarines":
         continue
     print(v)
input("print eny key to exit..............")