#########------------Lesson assignments from Lesson 019 to 020 --------###
print(type(10))
print(type(10.5))
print(type(10 + 10j))


e = 1 + 2j
print("{}".format(e.real))
print("{}".format(e.imag))

#قم بتحويل الرقم 10 ل Floating Point Number مع وضع عشر أرقام بعد العلامة العشرية
num = 10
print("{:.10f}".format(float(num)))


#قم بتحويل الرقم 159.650 ل Integer ثم قم بطباعته في أول سطر ثم في تاني سطر تقوم بطباعة نوعه والـاكد أنه Integer
num = 159.650

print(int(num))
print(type(int(num)))

#قم بوضع العلامة الحسابية المناسبة بدل علامة الإستفهام لتكون النتيجة صحيحة في الأمثلة التالية
print(100 - 115) 
print(50 * 30) 
print(21 % 4) 
print(int(110 / 11))
print(97 // 20)