# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 16:05:54 2018

@author: Administrator
"""
sub = []
result = []
def find(target, n):
    if n <= 0 or target <= 0:
        return
    if target == n:
        slist = [n]
        for i in sub:
            slist.append(i)
        result.append(slist)
    sub.insert(0,n)
    find(target-n, n-1)
    sub.pop(0)
    find(target, n-1)
    

q, niu = list(map(int, input().split()))
s = q + niu
n, l, r = 0, 0, s
while l < r:
    m = l + (r-l)//2
    print('left', l)
    print('middle', m)
    print('right', r)
    if m*(m+1) == 2*s:
        n = m
        break
    elif m*(m+1) > 2*s:
        r = m
    else:
        l = m + 1
print(n)
if q <= n:
    print(1)
else:
    find(q, n)
    print(min(list(map(len,result))))
        
