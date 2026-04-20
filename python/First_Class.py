#In python functions are treated as first-class objects. This means they can be used just like numbers,Strings,or any other varuable
#we can
#   1. Assign functions to variables
#   2. Pass them as arguments to other functions
#   3. Return them from functions
#   4. Store them in data structures such as lists or dictionaries

#Assign the Functions to variables
#here the functions can be assigned to a variable
#example :
def a():
    return "this is the function"
fun_var = a
print(fun_var())

#memory allocation

#step 1
# a -------> [function object]
#                 |
#                 --------- "this is a function"
#step 2

#after the assigning the function to another variabke no new object is created it will points to same function object
# a -------
#          |
#          |-------> [function_object]
#          |
# fun_var--

print(id(a))
print(id(fun_var)) 

# above both the address id are equal but 

print(id(a()))
print(id(fun_var))  # here both have the different address because id(a()) will give the address of return value but the id(a) gives the address of the function object

# | Expression | What it refers to | Memory               |
# | ---------- | ----------------- | -------------------- |
# | `a`        | function          | function object      |
# | `fun_var`  | function          | same function object |
# | `a()`      | return value      | string object        |

#Function with local and global variable
global x,y
x = 123 #global variable 
y = 10
y = 20
def display():
    # global x
    x = 98 #local variable
    print(x) #access global x
    print(globals()['x'])
    print(globals()['y'])

a = display
a()
a()

# Assigning a Function with parameters and return values

def fun(num):
    res = "even" if num%2 == 0 else "odd"
    return res
a = fun
ans = [lambda arg = x : a(arg) for x in range(1,11)]
print([i() for i in ans])

def func_variable (num):
    res = []
    res.append(num)
    return res
a = func_variable

res = [lambda x : a(x) for x in range(1,20)]
print([i(9) for i in res ])
