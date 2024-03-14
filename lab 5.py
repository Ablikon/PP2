#lab 5 solutions BEGIMKULOV ABYLAIKHAN

#1 1 - Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
import re

def file_watch(filename):
    with open(filename) as f:
        content = f.read()
        return content

def match(filename):
    pattern='ab*'
    if re.fullmatch(pattern, filename):
        print("Match")
    else:
        print("Not match")

result=match(file_watch("row.txt"))

#2 Write a Python program that matches a string that has an 'a' followed by two to three 'b'

def file_watch(filename):
    with open(filename) as f:
        content = f.read()
        return content

def match(filename):
    pattern='ab{2,3}'
    if re.fullmatch(pattern, filename):
        print("Match")
    else:
        print("Not match")

#3 Write a Python program to find sequences of lowercase letters joined with a underscore.

def file_watch(filename):
    with open(filename) as f:
        content = f.read()
        return content
    
def match(filename):
    pattern='[a-z]+_[a-z]+'
    if re.fullmatch(pattern, filename):
        print("Match")
    else:
        print("Not match")

#4 Write a Python program to find the sequences of one upper case letter followed by lower case letters.

def file_watch(filename):
    with open(filename) as f:
        content = f.read()
        return content
    
def match(filename):
    pattern='[A-Z][a-z]+'
    if re.fullmatch(pattern, filename):
        print("Match")
    else:
        print("Not match")

#5 Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.

def file_watch(filename):
    with open(filename) as f:
        content = f.read()
        return content
    
def match(filename):
    pattern=r'a.+b'
    if re.fullmatch(pattern, filename):
        print("Match")
    else:
        print("Not match")

#6 Write a Python program to replace all occurrences of space, comma, or dot with a colon.

def file_watch(filename):
    with open(filename) as f:
        content = f.read()
        return content
    
def match(filename):
    pattern= '[ ,.]'
    if re.fullmatch(pattern, filename):
        filename.sub(pattern, )

#7 Write a python program to convert snake case string to camel case string.

def file_watch(filename):
    with open(filename) as f:
        content = f.read()
        return content
    
def snake_to_camel(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

#8 Write a Python program to split a string at uppercase letters.

def file_watch(filename):
    with open(filename) as f:
        content = f.read()
        return content

def split_at_uppercase(s):
    return re.findall('[A-Z][^A-Z]*', s)

#9 Write a Python program to insert spaces between words starting with capital letters.

def file_watch(filename):
    with open(filename) as f:
        content = f.read()
        return content
    
def insert_spaces(s):
    return re.sub(r"(\w)([A-Z])", r"\1 \2", s)

#10 Write a Python program to convert a given camel case string to snake case.

def file_watch(filename):
    with open(filename) as f:
        content = f.read()
        return content
    
def camel_to_snake(camel_str):
    str1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', camel_str)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', str1).lower()