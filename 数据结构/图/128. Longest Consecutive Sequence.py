# -*- coding: utf-8 -*-
"""
Created on 2018/8/24 17:42

@author: vincent
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
"""
class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums) # turn list into set take O(n)
        best = 0
        for x in nums: # this iteration takes O(n)
            if x - 1 not in nums:
                y = x + 1
                while y in nums:
                    y += 1
                best = max(best, y - x)
        return best


class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Initialize max subsequence length and set of available numbers to pick from
        max_subsequence = 0
        available = set(nums)

        # Let's iterate through the array and "grow" a subsequence for each number
        # that isn't already part of a subsequence. Once we can no longer do so, the
        # max subsequence for that number has been found.
        #
        # Note: it is impossible for a number to be in two separate subsequences
        # By contradiction, if it can be in two separate subsequences, then those
        # subsequences should be a single subsequence because they're consecutive
        for n in nums:
            # Grow a subsequence if this number hasn't been used yet
            if n in available:
                # Initialize needed variables and discard seed from available nums.
                available.discard(n)
                seed = n
                subsequence_length = 1
                left = 1
                right = 1

                # Grow subsequence to left and discard as necessary
                while seed - left in available:
                    available.discard(seed - left)
                    left += 1
                    subsequence_length += 1

                # Grow subsequence to right and discard as necessary
                while seed + right in available:
                    available.discard(seed + right)
                    right += 1
                    subsequence_length += 1

                # Update max_subsequence
                max_subsequence = max(max_subsequence, subsequence_length)

        return max_subsequence
