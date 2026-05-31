#String Data SStructure:
"""Strings are the sequence of characters written inside quotes, it can include the letters number and any other special characters"""
'''A single letter in python cannot be treared as a character like other languages it is treated as a String length of 1'''
#Creating the String
'''Strings can be created using the singlle or double quotes ('' or " ")'''
a = 'GFG'
print(a)
b = "Geeks for Geeks"
print(b)

''' By using the triple quotes (''' ''' or """ """) for multiple line where the new lines are perserved'''
s = '''I am Learnig 
the python programming language'''

print (s)

s = """ I am Learning the 
String in python
"""
print(s)

#indexing and Slicing
'''Indexing (grabbing a single character)'''
'''In python String uses the 0 based Index and also supports the negative indexing which with -1 from the the end of the String '''
s = "python"
#positive indexing
print(s[0])
print(s[1])
print(s[2])
print(s[3])
#negative Indexing

print(s[-1])
print(s[-2])
print(s[-3])

#If we try to acces the character out of the string length it will throw an IndexError Exception

#Slicing 
'''slicing is the Extraction of a substring using the index values from the Existing string'''
'''Syntax for slicing : String[start:stop:step]'''
'''start : The index where the slice begins( start is a inclusive value) default value is 0
   stop  : The index wher the slice ends just before the one step value default value is length of the String len(String)
   step  : Here the step value decides the How many characters to jump forwad default value will be 1
'''
'''we can also slice the string with negative index value also'''
word = "PYTHON PROGRAMMING"
print(word[0:len(word)])
print(word[7:10: ])
print(word[:6:])
print(word[0:10:2])
print(word[-4:-1:2])
print(word[::-1])
#String Immutability
'''In Pythoin Strings are the immutable which means we cannot the change the stirng one it is created
we cannot add,delete,remove or change the character of the string if we cahange the String new String object is Created
'''
word = "Python"
# word[0] = "J" here it will throw an Exception no new Object is Created we cannot change the existing String we can change the String Inderictly where the new Object is Created
# print (word)

'''Indirectly changing the String '''
word = "J"+ word[1::]  #here the new string object is created
print(word)

"""
NameSpace                           HeapArea
word -> 1000                    1000 -> "python"

                                    100 -> "J"

word -> 2000                    2000 -> "Jython"  after concating the String "J" and SubString word[1::]
"""
#Common String Oppperation
#1. Concatenation and repetition 
'''we can concatenete the two Strings using the '+' operator after concatenating the two Stirings a new String Object is Created'''
first = "hello"
second = "world!"
print(first+" "+second)
print(first * 3)

# 'in' membership operator in the strings
'''The in Operator checks if a specific substring exists anywhere inside another String. it evaluates an Expresion and returns a boolean value'''
'''eg ; '''
text = "The Quick brown Fox"
print("Text"  in text)
print("Quick" in text)

#Why 'in' not .find() function?
'''The in Operator reads liek Plain English and Strictly returns the True/False which prevents logical bugs with checking -1'''
if text.find("brown"):
    print("Found it")
if "brown" in text:
    print("Found it")

#'not in' operator 

'''the Not in operator works quite exactly opposite to the 'in' opperator it returns True if the SUbstring or String is not present in the target String '''
def process_email(emailaddress):
    if '@' not in emailaddress:
        return "Invalid Email Address format"
    return "Valid email Address format"
print(process_email("adbkajdbf@gmail.com"))

#String Methods
#common String Methods
#1> len(String) : 
'''len() function is the built-in function in python, it works on the diifferent data types like list,tuple,set,sets,dictionary aand String
when the len() function is applied to the String it will count the total number of characters
'''
s = "Hello"
print(len(s))

'''len() funvtion counts everthing not only the visible characters it will consider the white spaces 
escape characters and special charaters
'''
sentence = "hello, World"
print(len(sentence)) #here as we observe space is also consider as the the charcters

spaces = "     "
print(len(spaces))

empty = ""
print(len(empty))

'''python uses the backslash(/) to the special escape character like "\n" even though we type the two characters for 
the escape character python will interprets them as a single character'''
sentence = "ab\nc"
print(len(sentence))
sentence = "ab\n c"
print(len(sentence))

#Function vs method
'''AS we discuss earlier len() is abuilt in function not a string method
    * we dont use the period notation eg sentence.len()
    * we wrap the function around the string eg len(sentence)
Python Strings are the objects that track their own scale.len() never count the characters manually
it simply queries the objects internal size meta data

   size = 5     #this is the metadata of an Stirng object
   =========
   "HELLO"      #this is the String Object

   time complexity for the len() will be the O(1) because it will not traverse the entire String it will get the data from the metadata 
   for manual iteration it takes the O(n)
'''
#upper() 
'''upper() method will take the String and transform the all lower case charaters to the Uppercase
upper() will not take any arguments simply we can call it on the existing String(a vriable holding a String) using the dot notation
here non-alphabetical and Existing Uppercase letters will be ignored or they will be in the by-pass track.
'''
name = "Sreenivasulu123-"
print(name.upper())

'''as String are immutable means they cannot be changed once the upper() method is applied new String Object is created by holding the uppercase characters after that 
we need a variable to store the transformed String if the transformed string object is not reference to any variable garbage collector will clean the uppper() String Object
'''
name = "Sreenivasulu123-"
name.upper() 
print(name)

name = "Sreenivasulu123-"
upper_name = name.upper()
name = name.upper()
print(upper_name)

'''
befor : 
NameSpace              heap memory
-----------------------------------
name --- 1000       1000--- "Sreenivasulu123-"


inprocess : name.upper()

NameSpace              heap memory
-----------------------------------
name --- 1000       1000--- "Sreenivasulu123-"

                    2000 --- "SREENIVAULU123-"
after 
NameSpace              heap memory
-----------------------------------
name --- 2000       1000--- "Sreenivasulu123-"

                    2000 --- "SREENIVAULU123-"
'''
#upper() vs isUpper()
'''upper is used to transform the entire string to the uppercase
isupper is used to check the string where all the characters of the String are uppercase the return value is boolean value
'''
sentence = "Hello"
print(sentence.isupper()) #False
print(sentence.upper())  #HELLO
print((sentence.upper()).isupper()) #TRUE

#lower() : it is  quite opoposite to the upper() method and islower() method is quite opposite to the isupper()
# lower() method will do the same operations what ever the upper() method do in the opposite manner
#strip() / Strip(args)
'''The strip() method primary job is to trim the unwanted characters from the extrem end of the String
very begining of the String and very ending of the string.
strip() method will allow passing the arguments if we does not pass the arguments the default argument eill be the ehitespace
strip() method will remove the special characters like "\n and \t" without arguments

''' 
text = "    Hello World    "
print(text.strip())
text = "\n     Hello world    \t"
print(text.strip())

'''as String is immutable string will not change the existing string python will create a new String object after 
removing the extrem end and begining charaters and that object need to be referenced to the variable if not garbage 
collector will remove the newly created string object'''

#eg with parameter
text = "...!!!Python???!!!"
print(text)
text = text.strip("!.?nP")
print(text)

'''sometimes it will remove the whole word instead of the only specified word to remove safely we can use the method removeprefix(prefix that to be remove passed as argument)
and removesuffix(suffix that to be removed passed as the argument)'''
sentence = "www.google.com"
print(sentence.strip("www.com"))

print((sentence.removeprefix("www.")).removesuffix(".com"))

'''sometimes we only want to remove on leftside of the string or right side of the string so python provides the 
two companion methods they are lstrip() and rstrip() here also we can pass arguments and the default value will be the white space
'''
text = "0000240000"
print(text.lstrip("0"))
print(text.rstrip("0"))

#real world use case

user_input = "  alice " 

if user_input.strip()=="alice":
    print("correct input")
else:
    print("check youe input")

#join(Iterable):
'''The .join() method job is to take a collection(list,tuple,sets etc,.) of seprated Strings
and stich them into a single string
Syntax = result_string = seperator.join(iterable)
'''
words = ["python", "is","good"]
res = " ".join(words)
print(res)
res = ''.join(words)
print(res)
res  = '-'.join(words)
print(res)

'''the join method is very strict about one thing that a collection(list,tuple, etc ..) elements must be a String other if we
try to join the numericals it will throw an error Type Error'''

numbers = ["one",2,"Three"]
# print(" ".join(numbers))    this will throw an error

#we can overcome the error by using the generator expression

res = " ".join(str(x) for x in numbers)
print(res)

'''in terms of performance .join() is better than + 

using + is perfectly fine for two or three strings however every time we use +  repeatedly brand new Strig Object will be created because of strings are immutable
suppose there are 10000 thousand Strings in the iterable use + it will slow down the performance but where as in the .join() is highly optimized in C under hood 
.join() method will calculate thre total memory needed exactly once and place all the strings inside and return it instantly
.join(0 works in two Phases

Phase 1 : The Measurement Phase
instead of building the String away python will loop through the iterable to measure everything
    * it checks the every single item in the iterable whether it is a String or not if not it will throw an TYPE ERROR
    * it count the exact lelngth of each String in the iterable
    * it count the how many times the seperator will be used
    * it calculates the exact total number of bytes that final string will be required
Now Python knows the final size it wil ask the operating system and asks for a single block of memory exactly the string needed or required

phase 2 : Python loops through the list second time,using first c level memory copy command(memcpy) where all the characters will be droped into the perfectly sized memory block
'''