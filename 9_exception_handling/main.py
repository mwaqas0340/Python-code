# Exception Handling with try, except, else, and finally

# Exception handling is a crucial part of writing robust Python programs. It allows you to handle errors gracefully and ensure
# your program doesn't crash unexpectedly. In this tutorial, we'll cover the try, except, else, and finally blocks with examples.


# 1. The try Block

# The try block is used to test a block of code for errors. If an error occurs within the try block, the program will immediately jump to the except block (if provided).

# try:
#     convert = 10 / 0  # This will raise a ZeroDivisionError
#     print('If 10 divided by any positive number Exicute try block')
# except:
#     print("An error occurred!")
    
  
  
# 2. The except Block

# The except block is used to handle specific errors that occur in the try block. You can specify the type of error to catch, or use a generic except to catch all errors.  
  
# try:
#     convert = 10 / 0
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
# except Exception as e:
#     print(f"An unexpected error occurred: {e}")
    

# 3. The else Block

# The else block is executed if no errors occur in the try block. It is optional and is used for code that should only run when the try block is successful.

# try:
#     convert = 10 / 0
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
# else:
#     print(f"Division successful. Result: {convert}")


# 4. The finally Block

# The finally block is executed regardless of whether an error occurred or not. It is often used for cleanup operations, such as closing files or releasing resources.

# try:
#     convert = 10 / 0
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
# else:
#     print(f"Division successful. Result: {convert}")
# finally:
#     print('This will always execute.')
    

# 5. Putting It All Together

# Here’s an example that combines all four blocks:
    
# def myfunc(a,b):
#     try:
#         convert = a / b
#     except:
#         print('Error: Cannot divide by zero!')
#     else:
#         print(f'Division successfull. Result: {convert}')
#     finally:
#         print('Operation compeleted!')
# myfunc(10,2)


# Key Points Covered:

# try Block: Used to test a block of code for errors.
# except Block: Used to handle specific or generic errors.
# else Block: Executes when no errors occur in the try block.
# finally Block: Executes regardless of whether an error occurred.



# Practice Problem:
# Write a Python program that asks the user for two numbers and divides them. Use exception handling to catch any errors that might occur (e.g., division by zero or invalid input).

# try:
#     num1 = float(input("Enter the first number: "))
#     num2 = float(input("Enter the second number: "))
#     convert = num1 / num2
#     print(convert)
# except ValueError:
#     print('Error: Invalid input. Please enter numbers.')
# except ZeroDivisionError:
#     print('Error! Cannot devide by zero')
# else:
#     print(f'The convert is: {convert}')
# finally:
#     print('Thank you for using the program!')


# def divide(a, b):
#     if b == 0:
#         raise ValueError("Division by zero is not allowed!")  # Raising an exception
#     return a / b

# print(divide(10, 2))  # Output: 5.0
# print(divide(5, 0))   # Raises: ValueError: Division by zero is not allowed!



# How a Function Throws an Exception in Python?

# In Python, a function can throw an exception using the raise keyword. This is used to indicate that an error has occurred, and it interrupts the normal flow of the program.

# When an exception is raised:


# def func(a,b):
#   if b == 0:
#    raise ValueError('Value Error') 
#   return a / b
# print(func(10,0))


# a = 10
# b = 0
# if b == 0:
#  raise ValueError('value Error!')
# print(a/b)


# name = input('Enter your name: ')
# password = int(input('Enter your password: '))
# if name == 'waqas' and password == 12345:
#  print('Login successfully!')

# if not name == 'waqas' or not password == 12345:
#     raise TypeError('Envalid name or pasword')

# def func(a,b,oper):
   
#  if oper == '+':
#   print(a+b)
#  elif oper == '-':
#     print(a-b)
#  elif oper == '*':
#     print(a*b)
#  elif oper == '/':
#     print(a/b)
#     if oper == 0:
#         raise ZeroDivisionError('Division by zero is not allowed!')
#  elif oper == '%':
#     print(a%b)
#  else:
#     print('Select valid operator! Try again')
    
# a = int(input('Enter first number :'))
# b = int(input('Enter second number :'))
# oper = input('Select operator :')
# convert = func(a,b,oper)

# def func(select, convert):
#  select = (input('Select Currency : '))
#  convert = int(input('Convert money in Pakistan currency :'))
#  one_dollar = 270
#  one_pound = 245
 
#  if one_dollar == 270:
#       print(select == convert,'Dollars = Rs',one_dollar * convert)
#  if one_pound == 245:
#    # print(convert,'Dollars = Rs',one_dollar * convert)
#   print( select == convert,'Pounds = Rs',one_pound * convert)
#  result = func(select,convert)
#  print(result)


# import random 

# a = random.choice([{'name':'waqas'},{'name':'fahham'},{'name':'huraira'},{'name':'rohan'}])
# print(a)







    
