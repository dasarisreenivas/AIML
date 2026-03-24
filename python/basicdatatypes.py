#Data Types
#As we know python variables do not store the value they store the reference to the objects
#Data types will say us what kind of data is stored in the memory area
#There are different types of Data types they are 
# 1. Numeric 2.Boolean 3.String 4. character 5. set 6.Sequence type 7. Dictionary

#Note : here we the function called type() which gives the what typpe of data the variable is holding
#1. Numeric data type 
# numeric data type contain differnt types of numeric data like integers,decimals complex number etc .,
#In python they called as integer as positive and negative non-decimal numbers (whole numbers without fractions and decimals) float which are decimal numbers and complex number

#integer : .... -3,-2,-1,0,1,2,3,...
#float : 1.2, 1.3333, 1.456, 1.325 ....
#complex number : 2+j, 1+j, .... (real part + imaginary  part)

#In python there is no range for integers and numric data types 
#In python as the range of the number increases the memory also increases as needed because there ia no range for the integer
#example : 
a = 10
b = -20
c = 999999999999999999999999999999
result = type(a)
print(type(result)) # type id type
print(result) # type is <class 'int'>


# #float value is represented by a float class. it is a realnumber 
# with a flaoting point representation it is spepcified by a decimal point.optionally character e or E
# followed by a positive or negative integer may be appended to specify sciebtific notation
#floats are stored in binary format
#justification for the above statement
#computers only understand binary (0s and 1s)
x = 5.75
#computers does not store 5.75 directlly
#computer split the floating numeric dat
# 5.75 = 5 + 0.75
# Binary rep of 5 = 101
# 0.75 is converted by multiplying the two repeatedly 
# 0.75 X 2 =  1.5 here the decimal part is 
# 1.5 = 1 + 0.5
#0.5 X 2 = 1
#hence 5.75 = 101.11
x = 0.1 + 0.2
print(x)
print(type(x))
y = -0.1222
print("type of y is ",type(y))

#complex Number  : real nubmer + imaginary number
c = 2j+111111111j #in python we should take only j character as the imaginary paart in comppplex number otherthan j it will throw an error
print(type(c))
print(c.real) #it will print real part of complex number
print(c.imag) #it will print the imaginary part of complex number