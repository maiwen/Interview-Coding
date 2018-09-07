# -*- coding: utf-8 -*-
"""
Created on 2018/9/7 13:54

@author: vincent

给你一个01串，定义答案=该串中最长的连续1的长度，现在有k次机会将某个0改为1，现在问最大可能答案

输入：第一行 n k

第二行 n个数

样例：

输入：
10 2
1 0 0 1 0 1 0 1 0 1
输出：

5
"""


def max_length(k, nums):
    n = len(nums)
    start, end, ans = 0, 0, 0
    while k and end < n:
        if not nums[end]:
            k -= 1
        end += 1
        ans += 1

    while end < n:
        ans = max(ans, end - start)
        if not nums[end]:
            while start < end and nums[start] == 1:
                start += 1
            start += 1
        end += 1
    ans = max(ans, end - start)
    return ans


data = [1, 0, 0, 1, 0, 1, 0, 1, 0, 1]
print(max_length(2, data))


