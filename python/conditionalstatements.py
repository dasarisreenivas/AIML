# conditional statement in python are used to execute certain blocks of code based on condition
# These statements help control the flow of a program
# making it behave differently in different situation

# If Conditional statement
# Syntax :  if condition is true it will execute the block other wise it will not
# if(condition):
#   exection block

from sys import stdout

age = 20
if age>=18 :
    stdout.write("this block is executed because the conditoin is true")

if True:
    print("this will not throw any exception or error")

#short hand if statement

age = 20
if age==20 : print(f"your age is {age}")

#if - else statement
#in if - else either of if block or else block will execute
# if block condition is satisfied then it will execute the if block otherwise else block will execute
#syntax :
# if <condotion> : 
#       # condition satified this line will execute
# else :
#       # condition not satisfied this line will execute

age = 21
if age>=18:
    stdout.write("you are eligible to vote"+"\n")
else:
    stdout.write("you are not eligible to vote"+"\n")

#shorthand if-else
marks =  45
res = "pass" if marks>=40 else "fail"
stdout.write(res+"\n")

#elif satement 
#elif stateement in python stands for "else if". it allows us to
#check multiple conditions
# if <condition>:
#     if true this block will execute
#     if false control goes to next Block
# elif <conditoin>:
#     if true this block will execute
#     if false control goes to next Block
# elif <conditoin>:
#     if true this block will execute
#     if false control goes to next Block
# else:
#     if no condition is satisfied control will come to else block

#consider an example 

age = 113

if age < 10:
    print("kid")
elif age < 12:
    print("child")
elif age <= 18:
    print("teenage")
elif age <=35:
    print("young adult")
else:
    print("Adult")

#Nested if..else conditional statement
#Nested if..else means if-ellse statement inside another if statement. we can use nested if statement to check condition with in the condition
#syntax:

# if <condition>:
#     if<condition>:
#         execute this line
#     else:
#         execute this line
# else:
#     if <condition>:
#         execute this line
#     else:
#         execute this line

#example

age = 70
is_member = True
if age>=70:
    if is_member:
        print("30% discount")
    else:
        print("20% discount")
else:
    print("you are not eligible")

#Ternary condition statement is a compact way to write an if-else condition in a single line it sometimes also called as ternary exppression
#above shorthand if-else statements are the kind of ternary expressions
#example :
age = 20
res = "Adult" if age>20 else "Minor"
print(age)

#Match case statemet : in python version of a switch-case found in other languages. it allows us to match a variable's value aganist the set of patterns
#syntax

# match <matching pattern>:
#     case 1:
#         execute this case of Block
#     case 2:
#         execute this case of block
#     case 3:
#         execute this case of block
#     .
#     .
#     . 
#     .
#     case n:
#         execute this case of block

#example
number = 2
match number:
    case 1:
        print(f"the number is {number}")
    case 2:
        print(f"the number is {number}")
    case _:
        print("other number")

#Internal execution of conditional statements
#let us consider an example

x = 10

if x > 5:
    print("Greater")
else:
    print("Smaller")

#step1: code is converted to byte code and that byte code is executed by the PVM(Python virtual Machine)
    #Load x
    #Load 5
    #Compare >
    #JUMP_IF_FALSE To else

#Step2 : condition is evaluated
    #Fetch value of X(10)
    #compare with 5
    #Result -> True
    #Note : in python always converts condition into boolean(True or False)
#Step3 : Truth Value Testing
 #True --> execute the block
 #False --> skip the block
 #Note : 0,None,"",[] -> treated as False and Non-zero and non-empty are treated as True

#Stepp4 : Control flow jumping
    #if Condition is True execute print("Greater") and skips the else block
    #if Coondition id False Python jumps to else block
    #above things will be done using the instructions in bytecode
    # POP_JUMP_IF_FALSE
    # JUMP_FORWARD
#Internal flow diagram
# Start
#   ↓
# Evaluate Condition (x > 5)
#   ↓
# True? ─── Yes ───→ Execute IF block
#   │
#   No
#   ↓
# Execute ELSE block
#   ↓
# End

#Behind the Code exceutinn\
#Python uses the Stack Based Execution
   #values pushed to stack
   #operation performed
   #result popped

   #Example 
   #Push 10
   #Push 5
   #Compare >
   #Push True
   #POP the result