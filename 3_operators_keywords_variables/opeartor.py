# Operator and Operand

# In Python (and programming in general), an operand is a value or variable that an operator acts on. Think of it like this:

# Operator: A symbol that performs an operation (e.g., +, -, *, /).
# Operand: The value(s) or variable(s) that the operator works with.

# x + y = z --> x and y are operand and +,= are operators 


a : int = 8
b : int = 2

# Python Arithmetic Operators

# print(a + b) # addtition
# print(a - b) # subtraction
# print(a * b) # multiplication
# print(a / b) # division

a: int = 7
print(b := 7)



# Python Assignment Operators


a : int = 7
print(a)
a = a + 2
print(a)



a : int = 7
print(a)
a += 2
print(a)



a : int = 7
print(a)
a -= 2
print(a)


# Python Comparison Operators

a : int = 7
b : int = 10
print( a == b )

a : int = 7
b : str = '7'
print(a == b)

a : int = 7
b : int = 7
print( a == b )

a : int = 7
b : int = 7
print( a != b )


a : int = 7
b : int = 8
print( a < b )



# Python Logical Opetator

# and operator

print( 2 < 3 and 4>1 )

exp = 2 > 3 and 4 < 5
print(exp)

name = 'waqas'=='rajput' and 'waqas'=='rajput'
print(name)

# or operator

num = 2 > 5 or 4 < 8
print(num)

a = 5 == 5 or 3 == 4
print(a)


# not operator

name = 'waqas'
print(not(name))


b = 5 > 3
print(not(b))

name = 'waqas'
if name == 'waqas':
    print(not(name))
else:
    print('invalid name')
    
    
a = 3 == 3 and 2 == 3
print(a)

a = 3 == 3 or 2 == 3
print(a)

a = 3 == 3
print(not(a))


password = 12
if password == 123:
    print("countinue", password)
    con = password
    print('Login')
    name = 'Waqas'
    print(name)
    
else:
    print("invalid password", password) 
    print('try again')


a = 5
a += 2
a -= 3
a *= 2
a /= 2
print('The curent value of "a" is',a)


a = '7'
b = 7
print(a==b)

# Python Identity Opetators 

# is operator
a = 2
b = 5
print(a is b) # False

a = 2
b = 5
a = b
print(a is b) # True

# is not operator
a = 2
b = 5
print(a is not b) # True

a = 2
b = 5
a = b
print(a is not b) # False

# Python Membership Opetators

# in operator
text = 'This is a dummy text'
print('dummy' in text) # True


text = 'This is a dummy text'
print('python' in text) # False


# not in operator
text = 'This is a dummy text'
print('dummy' not in text) # False


text = 'This is a dummy text'
print('python' not in text) # True

