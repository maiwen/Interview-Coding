# -*- coding: utf-8 -*-
"""
Created on 2018/7/9 10:28

@author: vincent
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


class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        lo, hi = 0, n - 1
        lo_index = self.searchLeft(nums, target)
        hi_index = self.searchRight(nums, target)
        return [lo_index, hi_index]

    def searchLeft(self, nums, target):
        n = len(nums)
        lo, hi = 0, n - 1
        left = -1
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
        left = -1
        while lo <= hi:
            mid = int((lo + hi) / 2)
            if nums[mid] == target and (mid == n - 1 or nums[mid + 1] != target):
                return mid
            elif nums[mid] <= target:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1