#!/usr/bin/env python3
#-*- coding:utf-8 -*-
## !NOTE! It's good to write shell bang for your script, remember how to write it!

## INSTRUCTIONS:
##
## Finish the following ninja practices
## To run this script make sure to add execute permission to the script, e.g.
##
##   $ chmod u+x <filename>.py
##
## Then run with this script with
##
##   $ ./<filename>.py
##

################################################################################
## 0 Variable value and type
## What is the variable with different value and type look like

v = 123  # int in decimal
print('v =', v, '\ttype(v) =', type(v))
v = 0x123  # int in hexical
print('v =', v, '\ttype(v) =', type(v))
v = 0o123  # int in octal
print('v =', v, '\ttype(v) =', type(v))
v = 1.23456  # float  3/7
print('v =', v, '\ttype(v) =', type(v))
v = 1.23e5  # float in scientific representation
print('v =', v, '\ttype(v) =', type(v))
v = True  # bool true
print('v =', v, '\ttype(v) =', type(v))
v = False  # bool false
print('v =', v, '\ttype(v) =', type(v))
v = None  # none
print('v =', v, '\ttype(v) =', type(v))
v = 'I\'m a string'  # string
print('v =', v, '\ttype(v) =', type(v))
v = "I'm a string"  # string
print('v =', v, '\ttype(v) =', type(v))
v = """
I'm a
multiline string
"""  # string
print('v =', v, '\ttype(v) =', type(v))

################################################################################
## 1 Logical Operater
## Determine True of false or following expression
print(True and False) # False
print(False or True) # True
print((1 < 2) and (0 > 3)) # False
print((2+8 == 10) or (1*6 > 5)) # True
print((1*3+4 > 10) and (2**4 == 16) or (3*6 > 17)) # True
print(not (75-5>100) or (2**4+4 == 20) and (-2 >= 0)) # True

################################################################################
## 2 If-else
## Tax calculation
##   Tax =
##          if 0<income<800, rate = 0.1
##          if 800<=income<1600, rate = 0.2
##          if income >= 1600, rate = 0.3
## Fill in the lines

income = 1450
rate = 0
if 0<income<800:
    rate = 0.1
elif 800<=income<1600:
    rate = 0.2
else:
    rate = 0.3
tax = income*rate
print('Your income is %s, your tax is %s'%(income, tax))

################################################################################
## 3 Create more arithmetic computation operations
## If the first operand of a arithmetic computation is variable itself, e.g.
##   a = a + 5  (assign value of a+5 back to a)
## You can replace the above computation as:
##   a += 5
## They are the same in effect, but it's simpler in coding. Your task is to compute
## the following lines with combined operator, such as +=, -=, *=, /=, **=, |=, &=, ^=, %=
##   1. x = x + 5  (already given)
##   2. x = x - 5
##   3. x = x * 16
##   4. x = x / 16
##   5. x = x ** 5
##   6. x = x | 5
##   7. x = x & 4
##   8. x = x ^ 7
##   9. x = x % 2  # div mod operation
## Feel free to print each intermediate result after each computation.

x = 2
x += 5

################################################################################
## 4 Find more built-in functions
## Python provide a bunch of built-in functions for your convenience, we've seen
## some of them:
##   int(), float(), str(), bool()  # convert variable type to int/float/string/bool
##   len()  # get length of a list or string
##   type()  # get type of a variable
##   input()  # get user input (stdin)
##   print()  # print object to standard output (stdout)
##
## Now we are going to meet more of them
##   bin(), oct(), hex()  # convert a integer to binary/octal/hexical representation string
##   abs()  # get absolute value
##   max(), min()  # get max/min value of two object or a list
##
## You can find the information at:
##   https://docs.python.org/3.5/library/functions.html
## Your task in the part, use the built-in function to find out the following information
##   1. Convert number 123 to float/string/bool, print the value and type of each variable
##   2. Convert number 1.234567e3 to int, print value and type of variable
##   3. Find binary/octal/hexical representation of integer 123 (decimal)
##   4. Find absolute value of -7, 0, 13
##   5. Find max/min value among 13, 22, -5, 73, 0, 3, -17



################################################################################
## 5 If-else weird number
## Given an integer, n, perform the following conditional actions:
## If n is odd, print Weird
## If n is even and in the inclusive range of 2 to 5, print Not Weird
## If n is even and in the inclusive range of 6 to 20, print Weird
## If n is even and greater than 20, print Not Weird

n = 19

################################################################################
## 6 Format string
## Format string is used to determine a format while the content is filled in later.
## A typical format string:
name = 'david'
age = 20
city = 'Seattle'
salary = 8500.14
s = 'I\'m %s. I am %d years old. I live in %s, and earn %f each month.'%(
name, age, city, salary)
print(s)
## This gives you the following line
##   I'm david, I am 20 years old. I live in Seattle, and earn 8500.14 each month
##
## Your task is to use format string to output the following information
##   1. Date format MM/DD/YYYY, e.g. 02/07/2016  (format: '%02d/%02d/%04d')
##   2. Time format HH:mm:ss, e.g. 21:08:13
##   3. Use %s for all, if there is no special requirement for output format
##      of numbers, use %s for all of them is most simple way, just try:
##      'int: %s  float: %s  string: %s  bool: %s  none: %s'%(
##      123, 123.001, 'apple', True, None)