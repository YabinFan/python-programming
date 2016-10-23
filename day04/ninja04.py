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
## 1 Loop exercise 1
## Please print each element in list:
##    value_list = [1,2,3,4,5,6,7,8]
## Output the following format:
##    1. output the length of value_list:
##        length = 8
##    2. output each element:
##        1,2,3,4,5,6,7,8
##    3. output each even element:
##        2,4,6,8
##    4. output each odd element:
##        1,3,5,7
##    5. output each reversed element
##        8,7,6,5,4,3,2,1
##    6. output the sum of all elements:
##        sum = 36
##    7. output the max element of value_list
##        max_value = 8
##    8. output the min element of value_list
##        min_value = 1

#1
l1 = [1,2,3,4,5,6,7,8]
print (len(l1))

#2
for i in l1:
    print (i)
#3

for i in l1:
    if i%2 ==0:
        print (i)


#4

for i in l1:
    if i%2 !=0:
        print(i)
#5

for i in reversed(l1):
    print (i)

#6


print (sum(l1))

#7
print (max(l1))

#8

print(min(l1))



#################################################################################
## 2 List comprehension exercise 2
##    data = "123,,456,789,,,,34,,,,12"
##Output the following format:
##    1. result = [123,456,789,34,12]

data = "123,,456,789,,,,34,,,,12"
data =data.split()
#print (data)
data = [x.strip(' ') for x in data]

print (data)

#################################################################################
## 3 exercise 3
##    data = [1,3,2,5,4,8,6,7]
##Output the following format
##    1. append a element '9'(use append() function)
##       data = [1,3,2,5,4,8,6,7,9]
##    2. insert a element '10' at index 2(use insert() function)
##       data = [1,3,10,2,5,4,8,6,7,9]
##    3. return final element and delete from list(use pop() function)
##       data = [1,3,10,2,5,4,8,6,7]
##    4. sort elements in list(use sort() function)
##       data = [1, 2, 3, 4, 5, 6, 7, 8, 10]
##    5. reverse elements in list(use reverse() function)
##       data = [10, 8, 7, 6, 5, 4, 3, 2, 1]

data2 = [1,3,2,5,4,8,6,7]
#1
print (data2.append(9))
#2
print(data2.insert(2,10))
#3
print(data2.pop(9))
#4
print(data2.sort())
#5
print(data2.reverse())


##################################################################################
## 4 exercise 4
## use 'while' statement to calculate the sum from 1 to 100
## input:
n = 100

sum = 0
i = 1
while i <= n:
    sum = sum + i
    i = i + 1

print ("Sum of 1 until %d: %d" % (n,sum))
## output:
##    sum = 5050

##################################################################################
## 5 exercise 5
## Please judge the year that you input is leap year
## for example:
##    2000, 1922,2400 is leap year
##    2011, 2013 is not leap year
##

year = int(raw_input('Please enter the year'))

for i in year:
    if i%4 == 0:
        print(year,"is leap year")
## output:
##    for example : 2000 is leap year.
##                  2011 is not leap year

###################################################################################
## 6 exercise 6
## Please find prime number from list

data3 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for i,y in data3:
    if i>=2 and i%y!=0:
        print (i)

## output:
##    result = [2,3,5,7,11,13,17,19]




