# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 23:01:53 2021

@author: mgune
"""

from itertools import combinations
def dongu(arr):
    y=max(arr)
    arr.remove(y)    
    for i in range(1,len(arr)+1):
        x=list(combinations(arr,i))
        for j in range(len(x)):
            if sum(x[j]) == y:
                return 'true'
    return 'false'


arr=[1,2,3,23,5,9,13]
print(dongu(arr))
