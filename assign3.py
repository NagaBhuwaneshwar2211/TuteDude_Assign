#Task 1: Calculate a Factorial using a Function

## Method 1
def factorial(num):
    if num == 1:
        return 1
    else:
        fact = 1
        while num > 1:
            fact *= num
            num -= 1
        return fact

print(factorial(5))

##Method 2
def fact_rec(num):
    if num == 1:
        return 1
    else:
        factorial = num*fact_rec(num-1)
        return factorial
print(fact_rec(5))



#Task 2: Using the Math Module for Calculations
from math import sqrt, log, sin
def cal():
    num = int(input('Enter a number: '))
    print(f'Square root: {sqrt(num)}')
    print(f'Logarithm: {log(num)}')
    print(f'Sine: {sin(num)}')

cal()

#Task 3: