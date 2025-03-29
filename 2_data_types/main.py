# Python Data Types

# 1. Numeric
# a.Integer
# b.Float
# c.Complex Number

# 2. Sequence Type 
# a.String
# b.Tuple
# c.List

# 3. Boolean

# 4. Set 

# 5. Dictionary


# 1. Numeric

# a.Integer
num_int: int = 42
print(type(num_int)," num_int = ",num_int,)  # <class 'int'>

# b.Float
num_float: float = 3.14
print(type(num_float), " num_float = ", num_float)  # <class 'float'>

# c.Conmpex
num_complex: complex = 2 + 3j
print(type(num_complex), " num_complex = ", num_complex)  # <class 'complex'>


# 2. Sequence Type

# a.String
text_single: str  = 'Hello, Python!' # Strings with Single Quotes (')
text_multi: str   = '''Hello, Python!''' # Multi-Line Strings with Triple Quotes (''')
print(text_single,text_multi)

# b. List (list)
my_list: int = [1, 2, 3, "Java", 3.14, True] #Type hinting is not enforced in python, but you should mention appropriate data type in this case 'list'
print(type(my_list), " my_list_1 = ", my_list)  # <class 'list'>

# c. Tuple (tuple)
my_tuple: tuple = (1, 2, 3, "AI", 2.71, False, .3 , 3+2j )
print(type(my_tuple), " my_tuple = ", my_tuple )  # <class 'tuple'>

# d. Range (range)
num_range: range = range(1, 10, 2) # range(start, stop, step)
print(type(num_range), " num_range = ", num_range.step) 

# 3. Boolean (bool)
is_python_fun: bool = True #False
print(is_python_fun)

# 4. Set Types

# a. Set
my_set: set = {1, 2, 33, 4, 4, 5}
print(type(my_set), "my_set = ", my_set)  # <class 'set'>

# b. Frozenset
frozen_set = frozenset([11, 2, 3, 4, 4, 5])
#frozen_set = frozenset(my_set)
print(type(frozen_set), " frozen_set = ", frozen_set)  


byte_data: bytes = "Hello"
print(type(byte_data), " byte_data = ", byte_data) 


# 5. Binary Types

byte_data: bytes = b"Hello"
print(type(byte_data), " byte_data = ", byte_data)  # <class 'bytes'>


# Number Systems
# ASCII:

# The American Standard Code for Information Interchange (ASCII) is a character encoding standard that represents text in computers using numeric codes. It maps 128 characters (letters, digits, punctuation, and control characters) to values from 0 to 127.

# Decimal:

# The decimal system is the standard numerical system used in everyday life, based on 10 digits (0 through 9). It's a base-10 system, where each digit's position represents a power of 10.

# Hexadecimal:

# The hexadecimal system is a base-16 numbering system, using 16 symbols: 0–9 to represent values 0 to 9, and A–F (or a–f) to represent values 10 to 15. It's widely used in computing for compact representation of binary data.

# Octal:

# The octal system is a base-8 numbering system, using digits 0 through 7. It was more commonly used in older computer systems and is still occasionally used in modern computing, especially for file permissions in Unix/Linux.

# Binary:

# The binary system is a base-2 numbering system that uses only two digits: 0 and 1. It's the fundamental language of computers, where each binary digit (bit) represents a state of off or on.