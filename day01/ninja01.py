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
## 0 Hello world
## (This is an example of how you going to finish this practice)
## Output the following line:
##   Hello world

print('Hello', 'world')  # read instruction above and write this code
                         # run this script to see the results yourself

################################################################################
## 1 Hello python
## Take your name as input and output the following line:
##   Hello <NAME>. Welcome to the world of python.



################################################################################
## 2 Arithmetic computation
## Output the results (and fomula) of following problems
##   1. (1+2)*3/4-5/(6+7)*8-9 = ?
##   2. 2**5 = ?
##   3. Consider rolling a standard dice, what's the probablity of getting 1?
##   4. Consider a rectangle: width=10, height=15, what's the circumference of it?
##   5. If you deposit $7500 in a bank with annual interest rate of 5%, how much
##      you can get after 5 years.



################################################################################
## 3 Bit operations
## Output the results (and fomula) of following problems
##   1. Bit shift 5 left for 3 steps
##   2. 5*(2**3) = ? (Does it equal to the result above?)
##   3. Bit shift 1024 right for 3 steps
##   4. 1024/(2**3) = ? (Does it equal to the result above? Found something?)
##   5. 15 | 9 = ?
##   6. 15 & 9 = ?
##   7. 15 ^ 9 = ?
##   8. 9 | 10 | (11 & 12) = ?



################################################################################
## 4 More input and output
## Take the following information as inputs:
##   name, gender, age, company and title
## Output the following lines:
##   I'm <NAME>
##   I'm a <GENDER>
##   I work at <COMPANY> as a <TITLE>



################################################################################
## 5 Explore new knowledge
## What's the largest integer (unsigned) can 8-bit data can hold?
## As you can imagine, largest 8-bit data is 0xFF (hex) or 1111 1111b (binary),
## when all bits are set to 1, but what's it in decimal form. We use following
## way to find out.
##   1111 1111b = 1 0000 0000b - 1b
## We already know 1 0000 0000b is simply 1 shifted left by 8 steps.
## So we compute
##   1111 1111b = 1<<8 - 1 = 15
##
## Use the same method to find out the largest integers (unsigned) which 16-bit, 32-bit and
## 64-bit data can hold.