# The Frozenset

# In Python, a frozenset is an immutable (unchangeable) version of a set. It is a collection of unique elements, just like a set, but it cannot be modified after it is created.

# Here are the key features of a frozenset:

# Immutable: A frozenset cannot be modified after it is created. You cannot add, remove, or change elements in a frozenset.

# Unordered: In Python, frozenset objects are unordered collections of unique, immutable, and hashable elements.

# Hashable: frozensets are hashable, meaning they can be used as keys in dictionaries or elements in other sets.

# Unique elements: A frozenset can only contain unique elements, just like a set.


my_frozenset: frozenset = frozenset([1,2,3, "Hello! World"])
my_frozenset2 = my_frozenset
print("my_frozenset  = ", my_frozenset2)

frozenset1: frozenset = ([1, 2, 3, 4, 5,'John'])
frozenset2: frozenset = ([1, 2, 3, 4, 5, 'John'])
frozenset2 = frozenset1
print('frozenset2 =',frozenset2)

# Frozensets Methods

frozen_set1: frozenset = frozenset([1, 2, 3, 4])
frozen_set2: frozenset = frozenset([3, 4, 5, 6])
print('difference() :',frozen_set1.difference(frozen_set2))
print('intersection() :',frozen_set1.intersection(frozen_set2))
print('unioin() :',frozen_set1.union(frozen_set2))
print('symmetric_difference() :',frozen_set1.symmetric_difference(frozen_set2))
print('isdisjoint() :',frozen_set1.isdisjoint(frozen_set2))
print('issubset() :',frozen_set1.issubset(frozen_set2))


