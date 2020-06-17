# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 20:14:29 2020

@author: ANUKRUTI DAS
"""


i=input().split()
p=[]
j=[]
for k in range(int(i[0])):
    l=int(input())
    p.append(l)
for m in p:
    if m%int(i[1])==0:
        j.append(m)
print(len(j))