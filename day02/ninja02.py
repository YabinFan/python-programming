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
v = 1.23456  # float
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