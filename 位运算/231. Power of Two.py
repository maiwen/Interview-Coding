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

如果一个数是2的次方数的话，根据上面分析，那么它的二进数必然是最高位为1，
其它都为0，那么如果此时我们减1的话，则最高位会降一位，其余为0的位现在都为变为1，那么我们把两数相与，就会得到0，用这个性质也能来解题
"""

class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and list(bin(n)).count('1') == 1

class Solution1:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and not n & (n - 1)