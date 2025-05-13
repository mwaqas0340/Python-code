# What is a Module in Python?

# A module in Python is a file that contains Python code (functions, classes, variables, or even runnable code) and is used to organize and reuse code efficiently.

# A module is simply a .py file that can be imported and used in other Python programs.

# Modules help keep the code modular, readable, and maintainable.

# Python has built-in modules (like math, random, os) and also allows users to create custom modules.

# Types of Modules in Python

# 1. Built-in Modules (Standard Library)

# Pre-installed modules in Python.

# Example: math, random, os, sys

# Example usage:

import math

print(math.pi) # 3.141592653589793
print(math.sqrt(25))  # 5.0
print(math.isqrt(25)) # 5
print(math.cbrt(125)) # 5.0
print(math.ceil(2.4667)) # 3
print(math.floor(2.4667)) # 2


import math as m
print(m.pi)

# import with alias

from math import pi as p, sqrt as sr 
print(p)
print(sr(64))



# 2. User-Defined Modules (Custom Modules)

# Any Python file (.py) you create can be used as a module.

# Example:

# Create a file called my_module.py: (use VSCode/Cursor on local computer)

# Import and use it in another script: (use VSCode/Cursor on local computer)

# import mymodule
# print(mymodule.add(5, 3))  # Output: 8


# 3. External Modules (Third-party Libraries)

# Installed via pip (pip install module_name).

# Example: numpy, pandas, requests

# Example usage:

import requests

response = requests.get('https://www.example.com')
print(response.status_code)

req = requests.get('https://jsonplaceholder.typicode.com/todos/2')
print(req.json())

# import qrcode

# data = 'QR code using make function'
# img = qrcode.make(data)
# img.save('qrcode generate')


# 1. Basic Import
import math
print(math.pi)

# 2. Import with Alias (as)
import math as m
print(m.pi)


# 3. Import Specific Functions or Variables (from ... import ...)
from math import pi as p, sqrt as sr 
print(p)
print(sr(64))


# 4. Import Everything (from module import *) (Not recommended for large modules)
from math import*
print(pi)
print(cbrt(125))


import random
a = [1,2,3,4,5]
a = random.choice(a)
print(a)


# Advantages of Using Modules

# ✔ Code Reusability – Write once, use anywhere.

# ✔ Organization – Keep related functions together.

# ✔ Namespace Management – Prevents variable conflicts.

# ✔ Faster Development – Use existing libraries instead of writing everything from scratch.


