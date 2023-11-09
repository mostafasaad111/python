from modules1 import calc
import math
import random

x = float(input("enter num1 :"))
y = float(input("enter num2 :"))
z = input("enter Arithmetic coefficient :")


if z == "+":
    result_addition = calc.addition(x, y)
    print("result_addition = ", result_addition)
elif z == "-":
    result_subtraction = calc.subtraction(x, y)
    print("result_subtraction = ", result_subtraction)
elif z == "/":
    result_division = calc.division(x, y)
    print("result_division = ", result_division)
elif z == "*":
    result_multi = calc.multi(x, y)
    print("result_multi = ", result_multi)

if z == "power":
    print("sum = ", math.pow(x, y))
elif z == "sqr":
    print("sum = ", math.sqrt(x))

random_num = random.randint(x, y)
if x >= y:
    print("Random number between", x, "and", y, "is:", random_num)

input("print eny key to exit..............")
