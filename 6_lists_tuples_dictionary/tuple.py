
# 4. Tuples in Python
# A tuple is an ordered, immutable (unchangeable) sequence of elements. Tuples are useful for fixed data collections.

# In Python, a tuple is an immutable data type. This means that once a tuple is created, its elements cannot be changed, added, or removed.

# 1. Cannot Modify Elements:
# Once a tuple is created, you cannot change its elements.

# 2. Cannot Add or Remove Elements:
# You cannot add new elements to a tuple or remove existing ones.

# Why Use Tuples?

# 1.Immutable: Since tuples cannot be changed, they are safer to use when you want to ensure that the data remains constant.
# 2.Hashable: Tuples can be used as keys in dictionaries because they are immutable.
# 3.Performance: Tuples are generally faster than lists because of their immutability.

# When to Use Tuples vs Lists

# * Use tuples when you want to store data that should not change (e.g., coordinates, constants).
# * Use lists when you need a collection that can be modified (e.g., adding or removing elements).

# Create a Tuple
fruits = ('mango','banana','orange')
print(fruits) # ('mango', 'banana', 'orange')

# Other way create Tuple
fruits = (('mango','banana','orange'))
print(fruits) # ('mango', 'banana', 'orange')

# Indexing
fruits = ('mango','banana','orange')
print(fruits[1])  # banana

# Negative Indexing
fruits = ('mango','banana','orange')
        #   -3       -2       -1
print(fruits[-3])  # mango

# Range of Indexing
fruits = ('mango','banana','orange')
print(fruits[0:2]) # ('mango', 'banana')
 
# Checking of an Item Exists
fruits = ('mango','banana','orange')
print('mango' in fruits) # True

# Combine Tuple
fruits1 = ('mango','banana')
fruits2 = ('orange','greaps')
print(fruits1+fruits2)  # ('mango', 'banana', 'orange', 'greaps')

# Looping Through a Tuple 
fruits = ('mango','banana','orange')
for fruit in fruits:
 print(fruits)




