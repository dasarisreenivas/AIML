#Input function() :
#we use the different datatypes like int,float,character,String etc..


#how code will execute it 
#start the program
#program reached to the input() function
#program paused at input() function
#program take the iput and treat it as a string
#input value stores in a variable which can used later based on the type of input sppecified
print(intput("Enter your name"))

#storing the value that take input from the user in the variable
name = input("Enter your name")
print(name)

#Different types of input

#String  input
#we can take the input of the string from the user using the input() function

string1 =  input("enter the string type data")
print(string1)

#integer type input
#we can take the input of the integer from the user by specifying the int type data

integer1 = int(input("enter the integer type data"))
print(integer1)

#float type input
#we can take the inout of the float from the user by specifying the input as float

float1 = float(input("enter the float value"))
print(float1)

#complex number type input
#first we need to take the input as string  consisting of numbers and i or j along with the numbers
#after then we convert the string to the complex number using the function complex() function 
complex_number_string =  input("enter the complex number")
complex_number = complex(complex_number_string)
print(complex_number)

#taking mulltiple string inputs
#here we use the split() function to seperate the multiple inputs
firstname,secondname = input("enter the firstname and second name").split(" ")
print(f"first name : {firstname} and second name : {secondname}")
# we can also use the map() function which maps the input values to the resppective variable for taking the multiple inputs  of integer data we use the map() function
a,b = map(int(input("enter the a and b values").split()))
