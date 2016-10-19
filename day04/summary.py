#!/usr/bin/env python3
#-*- coding:utf-8 -*-

l = ['apple', 'banana', 'peach', 'pineapple','strawberry']

for fruit in l:
    print('I love %s.'%(fruit))

l1 = [1,2,3,4,5,6,7,8,9,0,0,9,8,7,6,5,4,3,2,1]
print('sum = %d'%(sum(l1)))

s = 0
for n in l1:
    s = s + n
print('s = %d'%(s))

i = 0
s = 0
while i <= 100:
    # s = s + i
    s += i
    i += 1

for n in l1:
    if n%3 == 0 and n>0:
        print(n)

print('====================')
for n in l1:
    if n == 0:
        break
    else:
        print(n)

print('====================')
s = 0
for n in l1:
    if n%2 == 0:
        continue
    s+=n

print('====================')
for i in range(0, len(l1), 2):
    l1[i] *= 3
print(l1)

print('====================')
l2 = [3*x if x%2==0 else 0 for x in l1 if x%8==0]
print(l2)






