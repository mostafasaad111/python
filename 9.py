###########################---String Formatting ------################################
name ="mustafa"
age=24
rank=3
print("My name is:" + name )
# print("My name is:" + name + "and my age is:" + age)

#  %s string blaceholder
#  %d int blaceholder
#  %f float blaceholder
# %.2f .2 meaning 2 zero after number 
# %.5s .5 meaning print first five elements 
print("My name is %s " % "mustafa" )
print("My name is %s " % name )
print("My name is : %s  and my age is : %d" % (name , age ) )
print("My name is : %s  and my age is : %d and my rank is : %f" % (name , age ,rank) )

n = "Osama"
l="python"
y=10
print("I am %s my language is %s my expert  is %d" % (n, l, y))

# control floating point numbers
myNumber = 10
print("My number is: %d" %myNumber)
print("My number is: %.2f" %myNumber)  

# Truncate String
myLongString = "Hello people in the world and I will be working "
print("Message is %.5s" %myLongString)
print("Message is %s" %myLongString)

######## ------------------new formatting elements -----------------###########
name = "sad"
age = 50
rank= 2
print("My name is {}" .format(name))
print("My name is {:s} and age is {:d} and rank is {:f}" .format(name, age, rank))
print("My name is {} and age is {} and rank is {}" .format(name, age, rank))


StringLong = "hello world  world world world world world world world world "
print("Message is {}".format(StringLong))
print("Message is {:.5s}".format(StringLong))

#format money
myMoney = 590055849385839485569398038958589388693034887598383885983903038383098395858305833
print("My money in bank is: {}".format(myMoney))
print("My money in bank is: {:_d}".format(myMoney))
print("My money in bank is: {:,d}".format(myMoney))

#ReArrange items

a,b,c = "one", "two","three"
print("hello {} {} {}".format(a,b,c))  # hello one two three
print("hello {1} {2} {0}".format(a,b,c))  #hello two three one 
print("hello {1} {2} {1}".format(a,b,c))  #hello two three two 

x,y,z = 10 , 20 ,30 
print("hello {} {} {}".format(x,y,z)) 
print("hello {1:d} {1:d} {0:d}".format(x,y,z)) 
print("hello {1:.3f} {2:.5f} {0:.2f}".format(x,y,z)) 


# Format in version 3.6+
myName = "Mustafa"
age = 23
print("My name is : {myName} and my age is :{age}")
print(f"My name is : {myName} and my age is :{age}")