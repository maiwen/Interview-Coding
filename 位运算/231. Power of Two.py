# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 22:28:49 2018

@author: Administrator
Given an integer, write a function to determine if it is a power of two.

Example 1:

Input: 1
Output: true 
Explanation: 20 = 1
Example 2:

Input: 16
Output: true
Explanation: 24 = 16
Example 3:

Input: 218
Output: false

二进制表示只有一个 1 存在。
"""

class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and list(bin(n)).count('1') == 1