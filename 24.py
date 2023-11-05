color1 = "yellow"
color3 = "red"
color4 = "blue"
color4 = "black"

print(color1)
colorList = ["yellow", "red", "blue", "black"]
print(colorList[0])
print(colorList[1])
print(colorList[2])
print(colorList[3])

spices = [
    "salt",
    "pepper",
    "cumin",
    "turmeric",
]

for spice in spices :
    uppercase = str(spice).capitalize()
    print(uppercase)
print("Mix ingredients")
print("Done!")

## iteration التكرار
print("Counting to 100 by fives:")
counter = 5
while counter <= 100:
    print(counter)
    counter += 5
print("counting is done!")  

print("=" * 50)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  
print("=" * 50)
#هنا طبع كل حروف الكلمه اللي هي banana
for x in "banana":
  print(x)
  

# example 4
# هنا طبع الكلام اللي الليست لحد ماوصل للبنانا وعمل بريك
print("=" * 50)
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

## example 5
# هنا الفرق لانه طبع طلع قبل ما يكبع البانانا
print("=" * 50)
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

## example 6
print("=" * 50)
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#example 7 
# هنا الرنج بيتدا من 0 وتنتهي عند الرقم قبل الرقم المكتوب
print("=" * 50)
for x in range(6):
  print(x)

#example 8
# هنا انا محدد ليه البدايه تكون 2 والنهايه تكون 5
print("=" * 50)
for x in range(2, 6):
  print(x)
  
# example 9
#هنا محدد ليه البدايه 2 والنهايه 29  والاستيب بتاعت كل خطوه 3 
print("=" * 50)
for x in range(2, 30, 3):
  print(x)

## example 10
#هنا بطبع الحروف من 0 الي 5 وفي النهايه بعد نلاللوب يخلص بطبع اللي موجوج في الالس
print("=" * 50)
for x in range(6):
  print(x)
else:
  print("Finally finished!")
  
## example 11
#هنا هيطبع الارقام من 0 الي 2وهيعمل خروج خالص من الليوب
print("=" * 50)
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")
  
## example 12
#هنا طبع كل عنصر من عاصر الليست الاولي مع عناصرر الليست التانيه 
print("=" * 50)
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

## example 12
#هنا الباص مش بتعمل ايرور
print("=" * 50)
for x in [0, 1, 2]:
  pass

## example 12
#هنا بدا العد من 1 وهيزود لحد ال 5 
print("=" * 50)
i = 1
while i < 6:
  print(i)
  i += 1

## example 13
#هنا هيطلع بره اللوب ويوقفقيمه توصل الي 3 لما ال
print("=" * 50)
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
  
## example 14
#هنا قفزز من فوق التلاته 
print("=" * 50)
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

## example 15
#هنا هيكمل اللوب وببعدها هيطبع الاليس
print("=" * 50)
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

