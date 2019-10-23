#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 19:50:02 2019

@author: rajeev
"""
#%%
#immutable 
num1=10
#memory location
id(num1)
num1=200
print(id(num1))
print(type(num1))
p=list()
p1=[1,2,3]
print(p,p1,type(p),type(p1))
q=tuple()
t1=(1,2)
print(q,t1,type(q),type(t1))
num2=200
print(id(num1)==id(num2))
num3=256
num4=256
print(id(num1)==id(num2))
l1=[1,2,3]
print("check value is present in l1")
print(2 in l1)
print(num1 == num2)
print(num1 is num2)
num3=400
num4=400
print(num3==num4)
print(num3 is num4)
num4=256
num5=256
print(num4 is num5)