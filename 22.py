# -------------- intro for functions ------#
def getDirection():
    print("walk for 5 kms")
    print("Turn right ")
    print("Turn left ")
    print("You have reached your destination ")
    print("=" * 50)
    
# monday
getDirection()
# tuesday
getDirection()
# friday
getDirection()

def printSum(num1 , num2):
    print("sum = ",num1 + num2 )
    
printSum(1,2)
printSum(6,2)
printSum(3,2)


def calc(apparmentPrice , precentage):
    return((precentage/100)*apparmentPrice )- ((10/100)* apparmentPrice )
    
apparmentPrice = 200000

installmentAmount = calc(apparmentPrice ,15)

if((installmentAmount < 0)):
    print("the company owns me " + str( installmentAmount * -1))
else:
    print("I oww money to the company " + str( installmentAmount ))


# -----------The third challenge-------#

def calculate(num1,num2,num3):
    return (num1 + num2) * num3

print(calculate(2,3,4))
print(calculate(4,3,4))
print(calculate(2,9,4))

def compare(): 
    print(5, "is greater than", 6)
