# Tutorial: Control Flow and Decision Making in Python

# 1. Introduction to Control Flow

# Control flow refers to the order in which statements are executed in a program. 
# In Python, decision-making is achieved using if, elif, and else statements, along with comparison and logical operators.


# 2. Comparison Operators

# Comparison operators are used to compare values and return True or False. Here are the most common ones:

# == (equal to)
# !=  (not equal to)
# >   (greater than)
# <   (less than)
# >= (greater than or equal to)
# <= (less than or equal to)

x: int = 10
y: int = 20

print("x == y = ", x == y)  # False
print("x != y = ", x != y)  # True
print("x > y  = ", x > y)   # False
print("x < y  = ", x < y)   # True
print("x >= y = ", x >= y)  # False
print("x <= y = ", x <= y)  # True


name = input('Enter user name: ')
password = int(input('Enter password: '))

if name == 'waqas' and password == 123:
    print('Login! successfully')
    
else:
    print('invalid name or password')


# 3. Logical Operators

# Logical operators combine multiple conditions:

# and (True if both conditions are True)
# or (True if at least one condition is True)
# not (reverses the result of a condition)

age: int = 11
is_student: bool = True

# Check if age is greater than 18 AND is_student is True
if age > 18 and is_student:
    print("You are eligible for a student discount.")

# Check if age is less than 12 OR greater than 60
if age < 12 or age > 60:
    print("You qualify for a special discount.")

# Check if the person is NOT a student
if not is_student:
    print("You are not a student.")



name = input('Enter Your Full Name >> ')

age = input('Enter Your Age >> ')

print(f'Your name is {name.title()}')

print(f'You are {age} years old')


# if, else and elif examples


num1 = int(input('Enter First Number: '))
num2 = int(input('Enter Second Number: '))
operator = input('Select Operator (+ , - , * , / , **, %): ')

if operator == '+':
    print(num1+num2)

elif operator == '-':
    print(num1-num2)  
    
elif operator == '*':
    print(num1*num2) 
     
elif operator == '/':
    print(num1/num2)  

elif operator == '**':
    print(num1**num2)  

elif operator == '%':
    print(num1%num2)     
else:
    print('Select valid operator. Try again')



def func(num1,num2,operator):
    if operator == '+':
        return num1+num2
    elif operator == '-':
        return num1-num2
    elif operator == '*':
        return num1*num2
    elif operator == '/':
        return num1/num2
    else:
        print('Select valid operator. Try again')
    
num1 = int(input('Enter First Number: '))
num2 = int(input('Enter Second Number: '))
operator = input('Select Operator (+, -, *, /)')

result = func(num1,num2,operator)
print(result)


# Nested if else

num = 0

if num >= 0:
    
   if num % 2 == 0:
      print('Number is Positive, Even',num)
   else:
      print('Number is Positive, Odd',num)
     
else:
    print('Number is Negative',num)


total = 150

bio = int(input('Enter Biology Marks: '))
chem = int(input('Enter Chemistry Marks: '))
phy = int(input('Enter Physics Marks: '))
if bio <= 50 and bio >= 25:
    print(bio,'Marks Pass')
else:
    print(bio,'Marks Fail')
    
if chem <= 50 and chem >= 25:
    print(chem,'Marks Pass')
else:
    print(chem,'Marks Fail')

if phy <= 50 and phy >= 25:
    print(bio,'Marks Pass')
else:
    print(phy,'Marks Fail')
print('Obtained Marks:',bio+chem+phy)
print('Total Marks',total)



