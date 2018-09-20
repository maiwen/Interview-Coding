# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 20:17:52 2018

@author: Administrator

最优分割
时间限制：C/C++语言 1000MS；其他语言 3000MS
内存限制：C/C++语言 65536KB；其他语言 589824KB
题目描述：
依次给出n个正整数A1，A2，… ，An，将这n个数分割成m段，每一段内的所有数的和记为这一段的权重， m段权重的最大值记为本次分割的权重。问所有分割方案中分割权重的最小值是多少？

输入
第一行依次给出正整数n，m，单空格切分；(n <= 10000, m <= 10000, m <= n) 
第二行依次给出n个正整数单空格切分A1，A2，… ，An  (Ai <= 10000)
输出
分割权重的最小值


样例输入
5 3
1 4 2 3 5
样例输出
5

Hint
分割成 1  4 |   2   3  |   5  的时候，3段的权重都是5，得到分割权重的最小值。
"""

n, m = map(int,input().split())
data = list(map(int,input().split()))

def split(data, m):
    N = len(data)
    if N == m:
        return max(data)
    low, high = max(data), sum(data)
    
    while low <= high:
        mid = (low + high) // 2
        count, cum = 1, 0
        for num in data:
            if cum + num <= mid:
                cum += num
            else:
                count += 1
                cum = num
                if count > m:
                    break
        if count <= m:
            high = mid - 1
        else:
            low = mid + 1
    return low

print(split(data, m))