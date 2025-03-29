# Loops and Iteration in Python

# 1. Introduction to Loops

# Loops are used to repeat a block of code multiple times. Python supports two types of loops:

# for loops: Used to iterate over a sequence (e.g., lists, strings, or ranges).
# while loops: Used to repeat a block of code as long as a condition is True.
# When to use scenario:

# A. For Loop:

# Grading a class of students: You have a list of 30 students and you want to calculate the average score for each student. You use a for loop to iterate over the list of students and calculate the average score for each one.

# Washing Machine(number spins), Microwave Oven e.t.c.

# B. While Loop:

# Filling up a gas tank: You want to fill up your gas tank until it's full. You don't know how many times you'll need to fill up the tank, but you'll keep filling it up until it's full. You use a while loop to fill up the tank until it's full.

# Air Conditioner, Refigrator, Heater, Washing Machine(filling water) e.t.c.


# 2. The for Loop
# The for loop iterates over a sequence (like a list, string, or range) and executes a block of code for each item for a specified or fixed number of times.

# Example Code:

fruits: list = ["apple", "banana", "cherry"]
for fruit in fruits:
  print(fruit)

for _ in range(1,5):
 print(_)


# Example 1: for loop with else (No break)
for i in range(5):
    i+=1
    print(i)
else:
    print('The end')


# Example 2: for loop with break (Skipping else)
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    print(num)
    if num == 3:
        print("Breaking the loop!")
        break
else:
    print("Loop completed successfully!") 


for i in range(int(input('Enter Value: '))):
    
  print(i)
  if i <= 10 and i >=20:
   print(i) 
   break
else:
    print('Loops Completed')


# Example 3: Searching with else
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num == 3:
        print("Number Found!")
        break
else:
    print("Number Not Found!") 


# Print even numbers from 2 to 10
for i in range(2,11,2):
 print(i)
 
 
# Print odd numbers from 1 to 9
for i in range(1,10,2):
 print(i)


# 3. The while Loop
# The while loop repeats a block of code as long as a condition is True.


# Example Code:

count: int = 1
while count <= 5:
    print(count)
    count += 1

j = 10
while j > 5:
    j-=1
    print(j)
else:
    print('Exicution End')


i = int(input('Enter Value: '))

while i < 20:
    i += 1
    print(i)
    if i == 10:
     print('Loop is break') 
     break
else:
    print('While Loops End')
    
    
odd = 1
while odd <= 20:
    print(odd,'= odd number')
    odd+=2
    
# print('#/////////////////////#')

even = 2
while even <= 20:
    print(even,'= even number')
    even+=2



# 4. Controlling Loops
# Python provides two keywords (break & continue) to control loops:

# break: Exits the loop immediately.
# continue: Skips the rest of the code in the current iteration and moves to the next iteration.

for i in range(97, 123):
    if i == 105:
       break
    print(chr(i))


for i in range(97, 123):
    if i == 105:
        continue
    print(chr(i))


# 5. Nested Loops

# What are nested loops?
# Nested loops, also known as inner loops or nested iterations, refer to the process of placing one loop inside another loop. The inner loop will iterate through its entire cycle for each iteration of the outer loop.


# Multiplication table
for outer in range(1, 6): # outer loop
    print(f"Multiplication table for {outer}:")
    for inner in range(1, 6): # nested inner loop
        print(f"{outer} * {inner} = {outer * inner}")
    print()  # Add a blank line after each row


# Use Cases for Nested Loops

# Nested loops are useful in various scenarios, such as:

# Matrix operations: When working with matrices, you often need to iterate over each element in a two-dimensional array. Nested loops can help you achieve this.

# Iterating over multiple lists: If you have multiple lists and want to perform operations on each combination of elements, nested loops can be used.

# Games and simulations: Nested loops can be used to create game boards, simulate complex systems, or iterate over multiple levels of data.

# Data processing: When dealing with large datasets, nested loops can help you process and analyze the data by iterating over ea


import string

for alphabet in string.ascii_uppercase:
 print(alphabet)

i = 96
while i < 112:
 i += 1
 print(chr(i))

for i in range(96,112):
    i += 1
    print(chr(i))

for a in range(1,11,8):
    for b in range(1,11):
     print(f'{a} * {b} = {a*b}')
    print('----')

    

# 6. Practical Examples
total = 0
for i in range(1, 10):
  total += i
print("Sum of numbers from 1 to 10:", total) # 1+2+3+4+5+6+7+8+9=45


    

