# -*- coding: utf-8 -*-
"""
Created on 2018/7/9 9:34

@author: vincent

Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2
"""

class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l , h = 0, x
        while l <= h:
            mid = (h+l) /2
            sqrt = x / mid
            if mid == sqrt:
                return mid
            elif mid > sqrt:
                h = mid -1
            else:
                l = mid +1
        return h