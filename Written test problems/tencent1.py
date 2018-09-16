# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 15:44:23 2018

@author: Administrator
"""

import sys
if __name__ == "__main__":
    # 读取第一行的k
    k = int(input())
    a = input()
    b = input()
    if not k or not a or not b or k > len(a):
        print(0)
    subs = []
    for i in range(len(a)):
        if i+k <= len(a):
            sub = a[i:i+k]
            if sub not in subs:
                subs.append(sub)
    ans = 0
    for sub in subs:
        ans += b.count(sub)
    print(ans)