#In python programming, Operators in general are used to perform operations on values and variables
#Operators = Special symbols like -,+,*,/ etc.,
#Operands = value on which the operator is applied
#There are different types of operators they are 
#Arthimetic operators : Arthimetic operators are used to perfomr the basuc mathematical operation between two variables
a = 10
b = 20
print("Additon ",(a+b))
print("Subbtraction ",(a-b))
print("Multiplication ",(a*b))
print("Division ",(a/b))
print("Floor Division ",(a//b))
print("Modular Division ",(a%b))
print("Power of a Number ",(a**b))

#Comparision Operator : thses operators are used to compare the values and return true or false which are used in the conditional statements along with the logical operators
a = 10
b = 20

print(a>b)
print(a<b)
print(a==b)
print (a>=b)
print(a<=b)
print(a!=b)

#logical operators: thse operators are used with in the conditions
x = True
y = False

print(x and y)
print(x or y)
print( not y)
print(not x)

#Assignment operators : these opperators are used to assign the values to the variables
a = 10
a +=5  # a = a + 5
a -= 5 # a = a - 5
a *= 5 # a = a * 5
a /=5 # a = a / 5
a %=5 # a = a % 5
a **=5 # a = a ** 5
print (a)

#bitwise operator : these operators are used to operate at binary level
a = 5
b = 3

print(a & b)
print(a^b)
print(~a)
print(a<<b)
print(a<<b)

a = [1,2]
b = [1,2]

print(a is b) #compare the address
print(a is not b) #compare the address
print(a==b) #compare the values

#Memory Allocation 

a = 10
b = 10 #both a and b 
