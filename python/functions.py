#Python functions are a block of statements that does a specific task.
#we put all together which has common behavior and task that are used to perform repeatedly.
#Instead of writing the same code again and again we can just call the function
#Functions will help in the code resuability,Modularity,readability and Maintainability


#def keyword is used to define a function. Functions are logical blocks of code that can be reused multiple times

#Syntax :
# def function_ name(parameters):
#     statements
# #     return expression
# def fun():
#     print("Hello World")
# fun()

#Example perfom the Calculator operations using the methods

def fun_cal():
    a = int(input("Enter the number1"))
    b = int(input("Enter the numnber2"))

    operation = input("ch0ose the operation add,sub,mul and div")

    match operation:
        case "add":
            return print(add(a,b))
        case "mul":
            return print(mul(a,b))
        case "sub":
            return print(sub(a,b))
        case "div":
            return print(sub(a,b))

def add(*objects):
    sum = 0
    for obj in objects:
        sum +=obj
    return sum
def sub(a,b):
    return a-b
def mul(*objects):
    product = 0
    for obj in objects:
        product *=  obj
    return product
def div(a,b):
    if(b==0):
        return "Invalid input"
    return a/b

fun_cal()

#Function Arguments 
# Arguments are the values passed inside the parenthesis of the function when function is called. A funtion can have any number of arguments
# syntax:
# 
# def function(parameters): # parameters are the variables in the function definition
#       """Doc String """ #  to describe the function
#       #body of the function
#       return expression
# function(arguments) # function call (actual values are passed during the function call)

#parameters and  arguments are different but they are related.

# FEATURE          PARAMETERS              ARGUMENTS
# where used       function defination     function call
# what they are    variables               Actual values
# Example          def fun(a,b)            fun(5,2)

#Example :

def add(a,b):
    """this is the addition of two numbers function"""
    return (a+b)
print (add(5,6))

#There are different types of arguments they are :
#1. positional arguments
#2. keyword arguments
#3. Default arguments
#4. variable-length arguments (*args, **kwargs)

#1. positional arguments : values are assigned to parameters based on their order in the function call
# syntax : 
# def function(parameter1,paremeter2):
#   statemets
#   return
# function(value of parameter1, value of parameter2)
 
def nameage(name,age):
    for i in range(1,3):
        match i:
            case 1:
                print("I am ",name)
                print("My age ",age)
            case 2:
                print("I am ", age)
                print("My age ",name)
nameage("srinivas",19)

#Memory view of positional arguments

#Python uses "call by Object reference" also "call by sharing"
#which means varibles don't store values directly
#They store the refernces(address) to object in memory
#here the order must be correct wwe cant palce the name value in the age and vice versa

def nameage(name_parameter,age):
    print(id(name_parameter)) #to check the memory address
    for i in range(1,3):
        match i:
            case 1:
                print("I am ",name_parameter)
                print("My age ",age)
            case 2:
                print("I am ", age)
                print("My age ",name_parameter)
name = "Srinivas"
nameage(name,19)
print(id(name)) #to check the address of the name 
#here name refernce to object "Srinivas" in the memory
# name_parameter points to same object

#another example
def fun(x):
    print(id(x))
    x = x +5
a = 10
fun(a)
print(id(a))

#2. Keyword arguments : values are passed by explicitly specifying the parameter names, so the order does'nt matter

def fun_ka(name ,age ):
    print(f" name : {name}  and age : {age}")
fun_ka(name = "sreenivas", age= "20")
fun_ka(age = "20",name = "chanti") # order is does'nt matter here unlike positional arguments

# 3. Default Argument : A default argument is a parameter that assumes a default value if the value is not provided in the function call for that argument
# we assign the default value in the fumction definition
def fun_def(name,age = 18):
    """Here the age is default value"""
    print(f"name {name} age {age}")
fun_def("sreenivas") # here one parameter is missing the here default value is assigned to the age
fun_def("sreenivas",20) # here no default value is assigned

#another example for the default argument
def fun_defar(name = "sreenivas",age = 21):
    print(f"name : {name} age : {age}")
fun_defar()