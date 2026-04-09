#A loop is useed to repeat the block of code multiple times
#Ther are different types of loops they are for loop and while loop 
#for loop works on counting through items \
#while loop workes based on conditions

#for loops
#A for loop allows you to apply the same operation to every item within the loop
# using the for loop avoids the need to manually manage the index
# A for loop can iterate over any iterable object like list,tuple, dictionary,set or custom iterator

#syntax 
# for vavr in iterator:
    #Statements
    ##pass
s = ["hi","hello","bye"]
for i in s:
    print(i ,end = " ")
print("\n")

#iterating over the character of strings

s = "hello"
for ch in s:
    print(ch)

#using the range() function with for loop
#range() function is commonly used with for loops to generate a sequence of numbers it can take one,two or three arguments
# range(stop_value) : generates numbers form 0 to stop_value-1
# range(start_value,stop_value) : generate from start_vlaue to stop_value-1
# range(start_value,stop_value,step_value) : generates from the start_value to stop_value and incrementing by the step_value


#print ing from 0 to n-1 
n = 4
print("single argument range() function")
for i in range(n):
    print(i)

print("two argumebnts range() function")
n = 5
for i in range(1,n):
    print(i)

print("Three arguments range() function")
for i in range(1,n,2):
    print(i)

# Control statement with for loop
print("control statement with for loop -- continue")
for i in "sreenivasulu":
    if i == 's' or i == 'r':
        continue  # if the condition is satified it will skip that loop and goes to next loop to execute but foor loop will do all the iterations \

    print(i)

#break statement in the for loop
print("using the brak in the for loop")
for  i in range(1,20,1):
    if i%2 == 0:
        break  # here it will terminate the loop
    print(i)

#pass statement 
print("passstatement with for loop")
for i in range(6):
    if i==4:
        pass #it will do nothing when the condition is satisfied
    else :
        print(i)

for i in range(5):
    if i == 3:
        pass  # Do nothing when i is 3
    else:
        print(i)

# else statement with for loop
print("else block with for")
for i in range(5):
    print(i)
else:
    print("no breAK")

for i in range(5):
    print(i)
    break
else:
    print("No Break")

#example pprogra : check if an array consists of even numbers

def checkNumbers(lis):
    for i in lis:
        if i%2 == 0 :
            print("list contain even number")
            break
    else:
        print("array does not contain any even number")

checkNumbers([1,2,3,4])
checkNumbers([1,3])

#for loop with enumerate() 
#enumerate function in python is used to loop over an iterable and get both the index and element at the same time
#enumerate() retuns an object that pproduces pairs in the form(index,element)
#rnumerate() will remove the need of manually maintained counter variable during iteration

#internal execution of enumerate()
fruits = ["grapes","orange","apple"]
#step1 : converts the iterable to iterator
it = iter(fruits)
#step2 : store start value default value is 0
count = 0
# or 
enumerate(fruits,start=1)

#step3 : onevery next()
# 1. get next item from iterator
# 2. return tuple(count,item)
# 3. increase count

#actual enumerate()

for i, fruit in enumerate(fruits):
    print(i,fruit)

#actuall implementation

index = 0
for i in fruits:
    print(index,i)
    index = index +1
#some other example with enumerate()

for i,fruit in enumerate(fruits,start = 2):
    print(i,fruit)

#printin in the list format

lis = list(enumerate(fruits))
print(lis)

#prin the elelments like next(e)

e = enumerate(fruits)
print(next(e))
print(next(e))
print(next(e))


#nested for loop

# syntax:
# for var in iterator:
    #for var in iterator:
        #Statements
        #pass

for i in range(1,4):
    for  j in range(1,4):
        print(i,j)

# iterating over list,tuple, string and dictionary

#list
lis = ["sree","nivas","dasari"]
for i in lis:
    print(i)
#tuple
tup = ["sreenivas","dasari"]
for i in tup:
    print(i)

#string 
s = "sreenivas"
for ch in s:
    print(ch)

#dictionary
dic = dict({'x':123,'y':124})
for i in dic:
    print("%s %d" % (i,dic[i]))

s = {1,2,3,5}
for i in s:
    print(i)