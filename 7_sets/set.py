# The Set Data Type

# Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

# A set is:

# unordered
# unchangeable
# unindexed
# mutable

# An object cannot appear more than once in a set, whereas in List and Tuple, same object can appear more than once.

# A set is created by round brackets{}.


my_set: set = {123, 452, 5, 6}
my_set2: set = set([123, 452, 5, 6])
unknown: set = {} # set or dectionary
empty_set: set = set()

print("my_set            = ", my_set)
print("my_set2           = ", my_set2)
print("type(my_set)      = ", type(my_set))
print("type(my_set2)     = ", type(my_set2))
print("type(unknown)     = ", type(unknown))
print("type(empty_set)   = ", type(empty_set))
print("my_set == my_set2 = ", my_set == my_set2)

# The set is unordered

set1: set = {'Java', 'Python', 'JavaScript', 'java'}
print(set1)

# The set is Unchangeable

set2: set = {1,2,3,4,5}
print(set2)

try:
    set2[1] = 10
except TypeError as e:
    print("*TypeError ", e)
print("Program execution continues as normal because we handle the error condition in try except block")   


# Using the union() method or | operator:
# In Python, the union() method or the | operator is used to combine two sets into a single set. This operation returns a new set containing all unique elements from both sets.

# Using the union() method:
# The union() method is a built-in method of the set data type in Python. It takes an iterable (such as a set, list, or tuple) as an argument and returns a new set containing all unique elements from both the original set and the iterable.

set1 = {1, 2, 3, 5, 3}
set2 = {1, 5, 3, 6, 7}
set3 = set1.union(set2)
print(set3)


# Using the | operator:
# The | operator is a binary operator that can be used to combine two sets into a single set. It has the same effect as the union() method, but is often more concise and readable.

set1 = {1, 2, 3, 5, 3}
set2 = {1, 5, 3, 6, 7}
set3 = set1 | set2
print(set3)


# Unique Elements
# Note that sets only store unique elements, so if you try to add a duplicate item, it will be ignored. For example:

a = {1, 2, 'waqas', 2}
print(a)


fruits = {'mango','banana','orange'}
print(fruits)  # {'banana', 'mango', 'orange'}

# Other way create Set
fruits = (('mango','banana','orange'))
print(fruits)  # ('mango', 'banana', 'orange')

# Set Methods

# Adding Items to a Set
fruits = {'mango','banana','orange'}
fruits.add('greaps')
print(fruits)  # {'banana', 'greaps', 'mango', 'orange'}

# Removing an Item
fruits = {'mango','banana','orange'}
fruits.remove('banana')
print(fruits)  # {'mango', 'orange'}

# Checking if an Items Exists 
fruits = {'mango','banana','orange'}
print('mango' in fruits)  # True

# Combine Two Sets
x = {1,2,3}
y = {4,5,6}
x.update(y)
print(x)  # {1, 2, 3, 4, 5, 6}

# Accessing Item
fruits = {'mango','banana','orange'}
for fruit in fruits:
    print(fruits)


fruits = {'mango','banana','orange'}
fruits.discard('banana')
print(fruits)  # {'orange', 'mango'}

fruits = {'mango','banana','orange'}
fruits.pop()
print(fruits)  # {'mango', 'banana'}

