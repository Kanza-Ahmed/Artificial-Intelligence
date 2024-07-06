#Kinza Iftikhar
#BCS21016

#While Loop
count = 1
while ( count < 3):
    count = count + 1
    print("Hello world!")

#Single Statement While Block
count = 0
while(count != 0):print("Hello World!")

#for in loop
#Iterating over a list 
print("List Iteration") 
l = ["geeks", "for", "geeks"] 
for i in l: 
    print(i) 
#Iterating over a tuple (immutable) 
print("\nTuple Iteration") 
t = ("geeks", "for", "geeks") 
for i in t: 
    print(i)
#Iterating over a String 
print("\nString Iteration") 
s = "Geeks" 
for i in s : 
    print(i)
    
#Iterating by Index
list = ['geeks', 'for', 'geeks']
for i in range(len(list)):
    print(i)
   
#Loop Control
s = "geeksforgeeks"
for letter in s:
    if letter == 'e' or letter == 's':
        continue
    print ('current letter: ', letter)

#Functions
def my_function():
    print("Hello from a function")
my_function()

#Function with Parameters
def my_function(fname):
    print(fname + " was the parameter that you passed to the function")
my_function("Hello")

#Default Parameter Value
def my_function(country = "Norway"):
    print("I am from :", country)
my_function("Pakistan")
my_function()

#Passing a List as a Parameter
def my_function(country):
    for x in country:
        print(x)
cities = ['Karachi', 'Lahore', 'Gujranwala', 'Hunza']
my_function(cities)

#Function with return values
def my_function(x):
    return 2*x
print(my_function(10))

#Functions with keyword arguments
def my_function(child1, child2, child3):
    print("The youngest child is:", child2)
my_function (child1 = "Hamza", child2 = "Azka", child3 = "Imran")

#Classes and Objects
class Box:
    z = 5

x = Box()
print(x.z)

#init function
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)