# Unicode Character

print(r"\u0041 = ", "\u0041")
print(r"\u0042 = ", "\u0042")
print(r"\u0043 = ", "\u0043")

print(dir(str))
print([method for method in dir(str) if '__' not in method])


# Methods of string

# Important methods

a = 'Hel lo Wor ld'
print(a.split()) # break code of peace

b = 'all the '
a = b.join(['Hello ', 'World'])
print(a)


old = ('Hello, World!')
new = old.replace('Hello', 'Hi') 
print(new)


b = 'hello'
c = b.join('world')
print(c)


a = 'hello world, hello pakistan'
b = a.find('world')
print(b)
print(a.find('hello'))
print(a.__len__())
print(a.index('hello'))

a = 'pak istan zin da abad'
b = a.split()
print(b)


a = 'pakistan zinda shad'
b = a.replace('shad', 'abad')
print(b)

a = 'pakistan zindabad'
b = a.count('a')
print(b)


#String Formatting

name: str = 'Waqas'
fisrt_letter: str = 'W'
age: int = 21
weight: int = 40.20

# str.format()
print('My name is {0}, first letter of my name is {1}, I am {2} years old and my weight is {3}'.format(name,fisrt_letter,age,weight))

# % Operator
print('My name is %s, first letter of my name is %c, I am %d years old and my weight is %.3f' %(name,fisrt_letter,age,weight))

# F-string Recommonded
print(f'My name is {name}, first letter of my name is {fisrt_letter}, I am {age} years old and my weight is {weight}')


# Return id
a = 'waqas'
b = 'waqas'
print(id(a))
print(id(b))
c = a+ ''
print(id(c))


# String Interning
import sys

a = sys.intern("waqas")
print(id(a))

a = 'hello'
b = 'hello'
print(id(a is b))


# String Repetition

a = 'hello' * 3
b = '-' * 3
print(a+b)


b = True * 3
print(b)


# Type Casting in Python

# 1️⃣ Implicit Type Casting (Automatic Conversion)
# ✅ Python automatically converts one data type to another when no data loss occurs.
# Implicit me python datatype khud hi infer kr le ta he.

a: int = 10
b: float = 5.5 
print(a+b, type(a+b)) # is exaple me us ne khudhi datatype infer kr li. 

# 2️⃣ Explicit Type Casting (Manual Conversion)

# ✅ Python automatically promotes int to complex, as complex numbers cannot be downgraded.
# Explicit me python ki datatype hum apne hisab se manage kr te he .

num1: int = 5
num2: int = float(num1)
print(num2, type(num2)) # is exaple me hum ne use float datatype di.


num_int: int = 7
num_complex: complex = num_int + 3j  # int + complex → complex
print(num_complex, type(num_complex))


num1 = 2
num2:complex = num1 + 3j + 2
print(num2, type(num2))


a = '123abc'
b: str = a + '45'
print(b, type(b))


num: list = [1,2,3,4,5]
convert = set(num)
print(convert, type(convert))

name = 'waqas'
num:int = name
print(num, type(num))


lst: list = [('name','waqas'),('age',21),('is_married',False)]
d = dict(lst)
print(d, type(d))


a = '5'
b:float = int(a)
print(b, type(b))


# Examle of Implicit
a = True
b = 5
c = a + b
print(c, type(c))


# Examle of Explicit
a = False
b = int(a)
print(b, type(b))



