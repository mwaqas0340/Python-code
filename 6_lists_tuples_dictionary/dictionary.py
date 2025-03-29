# Dictionaries in Python

# 1. Introduction to Dictionaries

# A dictionary is a collection of key-value pairs. It is:

# Ordered (since Python 3.7): Items are stored in the order they were inserted.

# Mutable: Items can be added, removed, or modified after the dictionary is created.

# Un-indexed: Items are accessed using keys, not indices.

# Without duplicates: Keys must be unique, but values can be duplicated.

# A dictionary is written with curly brackets.


# 2. Creating a Dictionary

person = {
    'first_name': 'Muhammad',
    'last_name': 'Waqas',
    'age': 21,
    'is_married': False
}
# value add or update in dictionary
person['hobby'] = 'Playing cricket'
print(person)

# 3. Accessing Values

person = {
    'first_name': 'Muhammad',
    'last_name': 'Waqas',
    'age': 23,
    'is_married': False
}

# First method to access dictionary value
print(person.get('first_name'))
print(person.get('last_name'))


# Second method to access dictionary value
x = person['first_name']
y = person['last_name']
print(x)
print(y)

# 4. Modifying a Dictionary

person = {
    'first_name': 'Muhammad',
    'last_name': 'Waqas',
    'age': 21,
    'is_married': False
}
person["age"] = 22
print(person)


# 5. Deleting Items

person = {
    'first_name': 'Muhammad',
    'last_name': 'Waqas',
    'age': 21,
    'is_married': False
}
# person.pop('age')
del person['is_married']

person = [{
    'first_name': 'Muhammad',
    'last_name': 'Waqas',
    'age': 21,
    'is_married': False
},{
    'first_name': 'Muhammad',
    'last_name': 'Fahham',
    'age': 19,
    'is_married': False
}
]
person.pop()
print(person)


# 6. Nested dictionary

students={
    'student1':{
        'first_name': 'Muhammad',
        'last_name': 'Waqas',
        'age': 21,
    },
    'studen2':{
        'first_name': 'Muhammad',
        'last_name': 'Fahham',
        'age': 19,
    }
}
print(students)


person = {
  'student1': {
    'name': 'Waqas',
    'cast': 'Rajput',
    'age': 23
    },
  'student2': {
    'name': 'Ahmer',
    'cast': 'Malik',
    'age': 19
    }
}
for person in person:
    print(person)


# 7. Dictionary Methods
# Python provides several useful methods for working with dictionaries.

# Method	Description	
# keys()	Returns a list of all keys in the dictionary.	
# values()	Returns a list of all values in the dictionary.	
# items()	Returns a list of key-value pairs as tuples.	
# clear()	Removes all items from the dictionary.	
# update()	Adds or updates multiple key-value pairs from another dictionary.	

person = {
    'first_name': 'Muhammad',
    'last_name': 'Waqas',
    'age': 21,
    'is_married': False
}
print(person.key())
print(person.items())


# 8. Iterating Over a Dictionary
# You can loop through a dictionary using for loops.

person = {
    'first_name': 'Muhammad',
    'last_name': 'Waqas',
    'age': 21,
    'is_married': False
}
for key in person:
    print(key)

for key,value in person.items():
    print(key ,':',value)


# 8. Practical Examples

phonebook: dict = {
    "Alice": "123-456-7890",
    "Bob": "987-654-3210",
    "Charlie": "555-555-5555"
}

# Add a new contact
phonebook["David"] = "111-222-3333"

# Search for a contact
name: str = input("Enter a name to search: ")
if name in phonebook:
    print(f"{name}'s phone number is {phonebook[name]}.")
else:
    print(f"{name} is not in the phonebook.")

phonebook = {
    "Alice": "123-456-7890",
    "Bob": "987-654-3210",
    "Charlie": "555-555-5555"
}
    

    
    