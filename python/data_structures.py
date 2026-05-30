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

