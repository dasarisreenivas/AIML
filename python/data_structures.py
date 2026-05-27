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
