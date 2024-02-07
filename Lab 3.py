# Begimkulov Abylaikhan Lab 3 Exersice solutions

#1 Write a function called calculate_factorial that takes a positive integer as a parameter and returns its factorial (use recursion)

def calculate_factorial():
    a=int(input())
    result=1
    for i in range(1, a+1):
        result=result*i
    return result
print(calculate_factorial())

#2 Write a function called reverse_string that takes a string as a parameter and returns its reverse.

def reverse_string():
    a=str(input())
    return a[::-1]
print(reverse_string())

#3 Write a function called get_max that takes three parameters (a, b, and c) and returns the maximum of the three.

def get_max():
    a=int(input())
    b=int(input())
    c=int(input())
    if a>b>c:
        return a
    elif b>a>c:
        return b
    else:
        return c
print(get_max())

#4 Write a function called is_even that takes an integer as a parameter and returns True if it's even and False otherwise.

def is_even():
    a=int(input())
    if a%2==0:
        return True
    else:
        return False
print(is_even())

#5 You are given list of numbers separated by spaces. Write a function filter_prime which will take list of numbers as an argument and returns only prime numbers from the list.

def filter_prime(arr):
    primes = []
    for num in arr:
        if num < 2:
            continue
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num%i==0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

a = int(input())
arr = [int(input()) for i in range(a)]
prime_numbers = filter_prime(arr)
print(prime_numbers)
            
#6 Write a function find_common_elements that takes two lists as parameters and returns a new list containing common elements between them.
def find_common_elements(first, second):
    done_arr = []
    for i in first:
        if i in second:
            done_arr.append(i)
    return done_arr

a = int(input())
first = [int(input()) for i in range(a)]
second = [int(input()) for i in range(a)]
done = find_common_elements(first, second)
print(done)

#7 Write a function word_frequency that takes a string as input and returns a dictionary where keys are unique words, and values are their frequencies

def word_frequency():
    a=int(input())
    words=[str(input()) for i in range(a)] 
    word_freq={}
    for i in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    return word_freq
print(word_frequency())

#8 Write a recursive function fibonacci that returns the nth Fibonacci number

def fibonacci(a):
	if a <= 1:
		return a
	return fibonacci(a-1) + fibonacci(a-2)
a = int(input())
print(fibonacci(a))

#9 Write a function calculate_running_average that takes a series of numbers as input and returns a list containing the running average at each position.

def calculate_running_average(number,sum,average):
    for id, number in enumerate(number, 1):
        sum+=number
        average.append(sum / id)
    return average
sum=0
average=[]
a=int(input())
numbers=[int(input()) for i in range(a)]
print(calculate_running_average(numbers,sum,average))

#10 Create class My_shape with params color(String) and is_filled (boolean)

class My_shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

shape = My_shape(str(input()), True)
print(shape.color)
print(shape.is_filled)

#11 create __init__() method with default values for color and is_filled (choose your own default values)

class My_shape:
    def __init__(self, color="red", is_filled=True):
        self.color = color
        self.is_filled = is_filled

shape = My_shape()
print(shape.color)
print(shape.is_filled)

#12 override __str__() method (choose your own logic of string generating which includes inner fields values)

class Car:
    def __init__(self, brand, age):
        self.brand = brand
        self.age = age
    def __str__(self):
        return {self.name}, {self.age}
car = (str(input()), int(input()))
print(car)

#13 create method getArea() which returns 0;

def getArea():
    return 0
print(getArea())

# 14, 15, 16, 17, 18 and 19 Create child classes Rectangle and Circle which extend My_shape class.

import math

class My_shape:
    def getArea(self):
        return 0

    def __str__(self):
        return "Ne pon che tut sdelat, no dobavil new str"

class Rectangle(My_shape):
    def __init__(self, x_top_left, y_top_left, length, width):
        self.x_top_left = x_top_left
        self.y_top_left = y_top_left
        self.length = length
        self.width = width

    def getArea(self):
        return self.length * self.width

    def __str__(self):
        return {self.x_top_left}, {self.y_top_left}, {self.length}, {self.width}

class Circle(My_shape):
    def __init__(self, x_center, y_center, radius):
        self.x_center = x_center
        self.y_center = y_center
        self.radius = radius

    def getArea(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return {self.x_center}, {self.y_center}, {self.radius}
    
x_top_left = float(input())
y_top_left = float(input())
length = float(input())
width = float(input())
rectangle = Rectangle(x_top_left, y_top_left, length, width)

print(rectangle)
