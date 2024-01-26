#LAB1 2 WEEK EXERSICE SOLUTIONS Begimkulov Abylaikhan

#Booleans1
print(10>9)
True

#Booleans2
print(10==9)
False

#Booleans3
print(10<9)
False

#Booleans4
print(bool("abc"))
True

#Booleans5
print(bool(0))
False

#Operators1
print(10*5)

#Operators2
print(10/2)

#Operators3
fruits = ["apple", "banana"]
if "apple" in fruits:
  print("Yes, apple is a fruit!")

#Operators4
if 5 != 10:
  print("5 and 10 is not equal")

#Operators5
if 5 == 10 or 4 == 4:
  print("At least one of the statements is true")
#Lists1
fruits = ["apple", "banana", "cherry"]
print(fruits[1])

#lists2
fruits = ["apple", "banana", "cherry"]
fruits[0]="kiwi"

#lists3
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")

#lists4
fruits = ["apple", "banana", "cherry"]
fruits.insert(1,"lemon")

#lists5
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")

#lists6
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])

#lists7
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])

#lists8
fruits = ["apple", "banana", "cherry"]
print(len(fruits))

#while loops1
i = 1
while i < 6:
  print(i)
  i += 1

#while loops2
i = 1
while i < 6:
  if i == 3:
    break
  i += 1

#while loops3
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

#while loops4
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
#for loops1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#for loops2
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#for loops3
for x in range(6):
  print(x)

#for loops4
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

#Arrays нет на w3schools

#tuples1
fruits = ("apple", "banana", "cherry")
print(fruits[0])

#tuples2
fruits = ("apple", "banana", "cherry")
print(len(fruits))

#tuples3
fruits = ("apple", "banana", "cherry")
print(fruits[-1])

#tuples4
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])

#sets1
fruits = {"apple", "banana", "cherry"}
if "apple"  in fruits:
  print("Yes, apple is a fruit!")

#sets2
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")

#sets3
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)

#sets4
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")

#sets5
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")

#dictionaries1
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("mdoel"))

#dictionaries2
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"]=2020

#dictionaries3
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"]="red"

#dictionaries4
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")

#dictionaries5
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()

#ifelse1
a = 50
b = 10
if a > b:
  print("Hello World")

#ifelse2
a = 50
b = 10
if a != b:
  print("Hello World")

#ifelse3
a = 50
b = 10
if a == b:
  print("Yes")
else:
  print("No")

#ifelse4
a = 50
b = 10
if a == b:
  print("1")
elif a > b:
  print("2")
else:
  print("3")

#ifelse5
if a == b and c == d:
  print("Hello")

#ifelse6
if a == b or c == d:
  print("Hello")

#ifelse7
if 5>2:
  print("YES")

#ifelse8
a = 2
b = 5
print("YES") if a==b else print("NO")

#ifelse9
a = 2
b = 50
c = 2
if a==c or b == c:
  print("YES")