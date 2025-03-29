# Python Variables
# In Python, variables are used to store data that can be referenced and manipulated during program execution.
# A variable is essentially a name that is assigned to a value. Unlike many other programming languages, Python 
# variables do not require explicit declaration of type. The type of the variable is inferred based on the value assigned.

# Rules for Naming Variables

# Valid variable names
name = "Alice"
_age = 25
salary2024 = 50000
my_variable = "Python"

# Invalid variable names
# 2name = "Bob"          # ❌ Starts with a digit
# my-variable = "Error"  # ❌ Contains a hyphen
# class = "CS101"        # ❌ Uses a reserved keyword


# Here are the naming conventions in Python with their respective names:

# CapWords or PascalCase: Class names
# snake_case: Variable names, function names, method names, module names, package names
# UPPER_CASE: Constant names
# dunder (double underscore): Special method names (e.g. __init__, __str__)


# Assigning Different Values
x, y, z = 1, 2.5, "Python"
print(x,y,z)


# Delete a Variable Using del Keyword
x: int = 10
del x
print(x)

# Explanation:
# del x removes the variable x from memory. After deletion, trying to access the variable x results in a NameError, indicating that the variable no longer exists.