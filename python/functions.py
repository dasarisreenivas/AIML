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
    a = int(input("Enter the number1 "))
    b = int(input("Enter the numnber2 "))

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