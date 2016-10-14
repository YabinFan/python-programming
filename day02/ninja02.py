#!/usr/bin/env python3

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
## 0 Read variable value and type
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