#!/usr/bin/env python3
#-*- coding:utf-8 -*-

l1 = list(range(0, 100, 2))
l2 = ['apple', 'banana', 'peach', 'strawberry', 'blueberry', 'mango']

students = [
    {'name':'peter', 'age':1, 'gender':'m'},
    {'name':'vivi', 'age':2, 'gender':'f'},
    {'name':'emma', 'age':3, 'gender':'f'},
    {'name':'david', 'age':4, 'gender':'m'}
]

for student in students:
    for k,v in student.items():
        print('%s: %s'%(k,v))

d = {'name':'peter', 'age':1, 'gender':'m'}
d.items()