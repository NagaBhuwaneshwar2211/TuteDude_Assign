#Task 1: Check if a Number is Even or Odd
print("Task 1: Check if a Number is Even or Odd")
s1 = int(input('enter a number: '))
print('even') if s1 % 2 == 0 else print('odd')

#Task 2: Sum of Integers from 1 to 50 Using a Loop
print("Task 2: Sum of Integers from 1 to 50 Using a Loop")
total = 0
for i in range(1, 51):
    total += i
print("Sum of numbers from 1 to 50 is:", total)