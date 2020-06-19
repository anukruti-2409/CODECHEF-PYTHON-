# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 20:50:08 2020

@author: ANUKRUTI DAS
"""


x=int(input())
t=list(map(int,input().split()))
d=[]
u=set(t)
if x==1:
    print(1)
else:
    
    for b in range(1,x+1):
        if b not in u:
            d.append(b)
    

print(*d)