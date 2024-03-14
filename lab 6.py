#ex1
import os
path = input("Enter the path: ")
list_directories=[name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))]
list_files=[name for name in os.listdir(path) if os.path.isfile(os.path.join(path, name))]
list_all=os.listdir(path)
print(list_directories)
print(list_files)
print(list_all)

#ex2
import os

file_path = '/Users/ablik/Desktop/PP2'

print('Exists:', os.access(file_path, os.F_OK))
print('Readable:', os.access(file_path, os.R_OK))
print('Writable:', os.access(file_path, os.W_OK))
print('Executable:', os.access(file_path, os.X_OK))

#ex3
import os

path = r'/Users/ablik/Desktop/PP2/new.txt'
print(os.path.exists(path))
print("\nFile name of the path:")
print(os.path.basename(path))
print("\nDir name of the path:")
print(os.path.dirname(path))

#ex4
def file_lengthy(namik):
         with open(namik) as f:
                 for i, l in enumerate(f):
                         pass
         return i + 1
print("Number of lines in the file: ",file_lengthy('/Users/ablik/Desktop/PP2/new.txt'))

#ex6
import string, os
if not os.path.exists("letters"):
    os.makedirs("letters")
for letter in string.ascii_uppercase:
    with open(letter + ".txt", "w") as f:
        f.writelines(letter)


#ex7
from shutil import copyfile
copyfile('/Users/ablik/Desktop/PP2/new.txt', '/Users/ablik/Desktop/PP2/new2.txt')

#ex8
import os
if os.path.exists('/Users/ablik/Desktop/PP2/new.txt'):
  os.remove('/Users/ablik/Desktop/PP2/new.txt')
else:
   print("The file does not exist")

#ex9
from math import *
numbers = input().split()
numbers = [int(num) for num in numbers]  
print(prod(numbers))

#ex10
string=input()
cnt1=0
cnt2=0
for i in string:
    if i.isupper():
        cnt1+=1
    elif i.islower():
         cnt2+=1
print(cnt1,cnt2)

#ex11
string=input()
reversed_str=string[::-1]
if string==reversed_str:
     print("True")
else:
     print("False")

#ex12
from time import sleep
import math

def delay(fn, ms, *args):
  sleep(ms / 1000)
  return fn(*args)

z=int(input())
y=int(input())
print(delay(lambda z: math.sqrt(z),y,z))

#ex13
input_string=input()
tuuple=tuple(input_string.split(','))
if all(tuuple)==True:
    print("True")
else:
   print("False")