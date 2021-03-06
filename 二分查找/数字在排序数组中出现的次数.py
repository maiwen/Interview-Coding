# -*- coding: utf-8 -*-
"""
Created on 2018/8/7 10:48

@author: vincent
题目描述
统计一个数字在排序数组中出现的次数。

此题与 Find First and Last Position of Element in Sorted Array 相同
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""
# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        lo_index = self.searchLeft(data, k)
        hi_index = self.searchRight(data, k)
        if lo_index == -1 and hi_index == -1:
            return 0
        return hi_index - lo_index + 1

    def searchLeft(self, nums, target):
        n = len(nums)
        lo, hi = 0, n - 1
        while lo <= hi:
            mid = int((lo + hi) / 2)
            if nums[mid] == target and (mid == 0 or nums[mid - 1] != target):
                return mid
            elif nums[mid] >= target:
                hi = mid - 1
            else:
                lo = mid + 1
        return -1

    def searchRight(self, nums, target):
        n = len(nums)
        lo, hi = 0, n - 1
        while lo <= hi:
            mid = int((lo + hi) / 2)
            if nums[mid] == target and (mid == n - 1 or nums[mid + 1] != target):
                return mid
            elif nums[mid] <= target:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1