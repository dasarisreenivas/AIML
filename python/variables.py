#Variables
#varaible is name used to refer the values stored in the memory

x = 10
print(x)

#when we call an x it will get the value stored in the reference address of the memory
#variable(x) ----------> reference(1000)-------> value(10)
#in python has two main memory areas 1. heap memory 2. NameSpace

#Heap memory stores the objects and values like Strings, integers, floats, list, dictionaries and class Objects and functions
#each object has the value, type, memory address and references count 
#NameSpace will store the variable names and reference, NameSpace will be like a dictionalry in a python

a = 10 
b = 20
name = "srinivas"
lis = [1,2,3]

#NameSpace                   HEAP MEMORY
#a --> address              add --> 10
#b --> add                  add --> 20
#name--> add                add --> "srinivas"
#lis --> add                add --> [1,2,3]

#how objects are stored in the heap memory
x = 10
#step1 : python creates an object in heap
#  HEAP
#   10

#step2 : stores the memory address of the value in the heap
#   0X1023A (memory address of the heap)

#step3 : variable in the namespace point to the memory address (reference number)
# NAMESPACE                       HEAP
#   x -------------------------> 0X1023A
#                                  10

# actually internal storage of a variable will be 
# NAMESPACE                      HEAP MEMORY
# X --> 0X1023A                  0X1023A --> 10

#when the values of the two variables are same both variables refers to the same object in heap memory
a = 10 
b = 10

print (a is b) # "is" keyword is used to check the address of the two objects are same or not
print(a == b) # "==" is used to compare the valuues of the two variables
print(id(a)) # id() is used to get the memory address of the variable
print(id(b))

#NAMESPACE                            HEAP MEMORY
# a --> 1000                         1000 --> 10 
# b --> 1000

#types of NAME SPACES
# 1. built-in name spce    2. local name sppce   3. global name spce

#built-in name spce contains all predefined names provided by python
#Example : print,len,type,range,int,list,tuple etc.,
#built-in names comes form the module "builtins" when the interpretre starts it will import all the built-in names internally from the module (internally it willl be like import builtins)

#global name space : variables defined outside of fuunction
name = "global"
def outter():
    print(name)
outter()
#local name space : variables defined inside of function
def inner():
    name = "local"
    print(name)
inner()
#enclosing name spce : variables defined inside of outer function and outside of the inner function

def outter1():
	name = "enclosed"
	def inner1():
		print(name)
	inner1()
outter1()

# python follows the LEGB rules 
# initially python will look for the lpcal variables and then enclosed variables and then global variables and then it will go the built in variables
# ii will give the folowing priority orfer to it
# 1. local name space 2. enclosed name space 3. global name spce 4. built-in name spce

#example : comment each pi and check the result
from math import pi # pi = builtin name space

pi = "global name space"
def outter_fun():
    pi = "enclosed name space"
    def inner_fun():
        pi = "local name spce"
        print(pi)
    inner_fun()
outter_fun()