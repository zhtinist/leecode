"""
LeetCode #80 - Remove Duplicates from Sorted Array II
https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

Given an integer array nums sorted in non-decreasing order, remove some
duplicates in-place such that each unique element appears at most twice. Return
k after placing the final result in the first k slots of nums.

Example 1:
    Input: nums = [1,1,1,2,2,3]
    Output: 5, nums = [1,1,2,2,3,_]

Example 2:
    Input: nums = [0,0,1,1,1,1,2,3,3]
    Output: 7, nums = [0,0,1,1,2,3,3,_,_]

Constraints:
    1 <= nums.length <= 3 * 10^4
    -10^4 <= nums[i] <= 10^4
    nums is sorted in non-decreasing order.
"""

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)

        write = 2
        for read in range(2, len(nums)):
            if nums[read] != nums[write - 2]:
                nums[write] = nums[read]
                write += 1

        return write
