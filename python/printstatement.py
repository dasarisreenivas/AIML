#print() function : it is a inbuilt function in python which prints the arguments that are passsed to the function
print("hello world")

#syntax of the print statement
#print(arguments)

#internal implementation of the print 
#print(objects,sep = " ",end = "\n",flush = True)

#print() function will always consider the arguments that are passed are considerd as the objects and there is seperator as sep = " " and  there is a end line parameter end = "\n" here the sep = " " and end = "\n" are the default parameters and we can overdife the values of the sep and end and there is a one more parameter called fulsh it will be the reason for the immediate output on the console in the terminal

#overwritting the sep value  from " "(space) to  "-"(hyphen)
print("HELLO","WORLD", sep = "-")

#overwritting the end value from "\n" to ","
print("Hello", end = ",")
print("world") # output will be  "Hello, world" 

#different approaches same output
print("hello",end = " ")
print("world",end = " ")
print("srinivas",end = "\n")

print("hello","world","srinivas", sep = " ",end ="")

#combination of sep and end 

print("hello","world","D",sep = " ",end = ".")
print("srinivas")

#Internal Implementation of print() function
import sys

def myprint(*Objects, sep = "-",end = "!"):
	output = sep.join(str(obj) for obj in Objects)
	sys.stdout.write(output+"\n")
myprint("hello",10)

#so in print function it will consider the each parameter as a object 
#internally print function will join them using the sep 
#before joining it will conver the objects into strings and then it will join

#tricky question on internal implementation question

def myprint1(object1,object2):
	lis = []
	lis.append(object1)
	lis.append(object2)
	sep = " "
	end = "!"
	output = sep.join(str(obj) for obj in lis)
	sys.stdout.write(output+end)

myprint1("Hello",10)

#this is the debugging question 

# def myprint2(*Objects,sep = "-",end="!"):
# 	output = sep.join(str(obj) for obj in Objects)
# 	sys.stdout.write(output+end+"\n")

# def myprint3(*Objects):
# 	lis = [(obj for obj in Objects)] 
# 	myprint2(lis)
# 
# myprint3("hello","world","get","ready")
#
#output should be "hello world get ready"
print("")
# solution is 

def myprint2(*Objects,sep = "-",end="!"):
	output = sep.join(str(obj) for obj in Objects)
	sys.stdout.write(output+end+"\n")

def myprint3(*Objects):
	lis = [obj for obj in Objects]
	myprint2(*lis,sep = " ")

myprint3("hello","world","get","ready")

# def myprint2(*Objects,sep = "-",end="!"):
# 	output = sep.join(str(obj) for obj in Objects)
# 	sys.stdout.write(output+end+"\n")

# def myprint3(*Objects):
# 	lis = [(obj for obj in Objects)]  here it is the generated expression which stores collection of all objects into single object
									# [(....)] it treated as a generated expression
									# in list it contains only single object that is (....) it is the generated expression
									# (....) is a generated object
# 	myprint2(lis)
# 
# myprint3("hello","world","get","ready")
#
#output should be "hello world get ready"