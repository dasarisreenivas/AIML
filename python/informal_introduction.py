#comments are the non executable statements in python 
#when a statement starts with the character '#' that statement 
#will not execute at the time of execution

#This is the first comment



spam = 1 # this is the secomd comment
text = "# this is not a comment"
#any thing with in the single 0r double quotes is considerd as a string
print(spam)
print(text)

#using the python we can perform the mathematical operation like calculator

a = 10 
b = 20

print(f"the addition of two number is : {a+b}")
print(f"the subtraction of two number is : {a-b}")
print(f"the multiplication of two number is : {a*b}")
print(f"the division  of two number is : {a/b}")
print(f"the floor division of two number is : {a//b}")
print(f"the remainder of two number is : {a%b}")

#In python we use the  operator '**' for calculating powers

a = 2
b = 5
print(2**5)

# In python '=' is used to assign the values to the variable
# consider an example a  = 10
# here 10 is the value where 10 is assigned to a 
# consider example 
# 10 is the physical appearence of a person 
# a is the name of the person
# declaring the variable without initializing the value will
# lead to an error
try:
    d=10 # remove the value and check the error
    print(d)
except:
    print(f"variable {d} is not initialized with any value")
