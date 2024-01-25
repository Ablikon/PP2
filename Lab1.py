#LAB 1 SOLUTIONS Begimkulov Abylaikhan

#Syntax1
print("Hello world")

#Syntax2
if 5>2:
    print("YES")

#Comments1
#This is a comment

#Comments2
"""
This is comment 
written in 
more tham one line
"""

#Variables1
carname = "Volvo"

#Variables2 
x = 50

#Variables3
x = 5
y = 10
print(x+y)

#Variables4
x = 5
y = 10 
z = x+y
print(z)

#Variables5
a, b, c = "Orange", "Banana", "Cherry"

#Variables6
a=b=c= "Orange"

#Variables7
def myfunc():
    global g
    g = "fantastic"

#Data_Types1
x = 5
print(type(x))

#Data_Types2
a = "Hello World"
print(type(a))

#Data_Types3
f = 20.5
print(type(f))

#Data_Types4
l = ["apple", "banana", "cherry"]
print(type(l))

#Data_Types5
t = ("apple", "banana", "cherry")
print(type(t))

#Data_Types6
d = {"name" : "John", "age" : "36"}
print(type(d))

#Data_Types7
bo = True
print(type(bo))

#Numbers1 
x = 5
x = float(x)

#Numbers2
x = 5.5
x = int(x)

#Numbers3
x = 5
x = complex(x)

#Strings1
a = "Hello World"
print(len(a))

#Strings2
txt = "Hello World"
x = txt[0]

#Strings3
txt = "Hello World"
x = txt[2:5]

#Strings4
txt = "Hello World"
x = txt.strip()

#Strings5
txt = "Hello World"
txt = txt.upper()

#Strings6
txt = "Hello World"
txt = txt.lower()

#Strings7
txt = "Hello World"
txt = txt.replace("H", "J")

#Strings8
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))