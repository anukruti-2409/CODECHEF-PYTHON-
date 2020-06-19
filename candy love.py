# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 20:57:43 2020

@author: ANUKRUTI DAS
"""


t=int(input())
for i in range(t):
    n=int(input())
    c=input().split()
    e=0
    for x in c:
        e+=int(x)
        
    
    if e%2!=0:
       print('YES')
    else:
       print('NO')