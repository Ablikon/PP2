#LAB1 2 WEEK EXERSICE SOLUTIONS Begimkulov Abylaikhan

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
