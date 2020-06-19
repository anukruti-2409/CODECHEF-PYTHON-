# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 21:30:33 2020

@author: ANUKRUTI DAS
"""


t=int(input())
for i in range(t):
    x=list(map(int,input().split()))
    r=x[0]%x[1]
    print(r)