#Begimkulov Abylaikhan lab 4 solutions

#1 Write a Python program to convert degree to radian.
import math

a=int(input())
print(math.radians(a))

#2 Write a Python program to calculate the area of a trapezoid.

height=int(input())
base=int(input())
sec_base=int(input())
def area():
    area=0.5*(base+sec_base)*height
    return area

print(area())

#3 Write a Python program to calculate the area of regular polygon.

num_side=int(input())
len_side=int(input())
def area():
    apothem= (len_side/2*(math.tan(math.radians(180/num_side))))
    area=(num_side*len_side*apothem)/2
    return area
print(area())

#4 Write a Python program to calculate the area of a parallelogram.

length= int(input())
height = int(input())

def area():
    area=length*height
    return area
print(area())

#5 Write a Python program to subtract five days from current date

import datetime
from datetime import date, timedelta,datetime,time

sub= date.today() - timedelta(5)
print(date.today())
print(sub)

#6 Write a Python program to print yesterday, today, tomorrow.

today=date.today()
yesterday= date.today()-timedelta(1)
tomorrow= date.today()+timedelta(1)
print(yesterday)
print(today)
print(tomorrow)

#7 Write a Python program to drop microseconds from datetime.
import datetime

mic=datetime.datetime.today().replace(microsecond=0)
print(mic)

#8 Write a Python program to calculate two date difference in seconds.
yesterday= date.today()-timedelta(1)
tomorrow= date.today()+timedelta(1)
def raznica():
    time= yesterday-tomorrow
    return time.days * 24 * 3600 + time.seconds
print(raznica()*-1)

#9 Create a generator that generates the squares of numbers up to some number N.
def square_generator(n):
    for i in range(1, n+1):
        yield i**2
n = int(input())
for i in square_generator(n):
    print(i)

#10 Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.

def even_numbers_generator(N):
    for i in range(2, N+1, 2):
        yield i
n=int(input())
even_numbers = even_numbers_generator(n)
print(','.join(map(str,even_numbers)))


#11 Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.

def divisible_by_3_and_4_generator(n):
    for i in range(n+1):
        if i % 3 ==0 and i%4==0:
            yield i
def print_divisible_by_3_and_4(n):
    generator = divisible_by_3_and_4_generator(n)
    for number in generator:
        print(number)
n=int(input())
print(n)
print_divisible_by_3_and_4(n)

#12 Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.

def squares(a,b):
    for i in range(a, b+1):
        yield i*i
a=int(input())
b=int(input())
for square in squares(a,b):
    print(square)

#13 def countdown(n):
    while n >=0:
        yield n 
        n-=1
n=int(input())
for number in countdown(n):
    print(number)

#14 Json Using data file sample-data.json, create output that resembles the following by parsing the included JSON file.
import json

file_path = "/Users/balzhanbatyrbaeva/Downloads/sample-data.json" # Update the file path with the correct file name and extension

with open(file_path, "r") as my_file:
    json_string = my_file.read()

data = json.loads(json_string)

interfaces = data.get('imdata', [])
print("Interface Status")
print("=" * 80)
print("{:<50} {:<20} {:<8} {:<6}".format("DN", "Description", "Speed", "MTU"))
print("-" * 50, "-" * 20, "-" * 8, "-" * 6)

for i in interfaces:
    l1physif = i.get('l1PhysIf', {})
    att = l1physif.get('attributes', {})
    
    dn = att.get('dn', '')
    descr = att.get('descr', '')
    speed = att.get('speed', 'inherit')
    mtu = att.get('mtu', '')
    
    print("{:<50} {:<20} {:<8} {:<6}".format(dn, descr, speed, mtu))
