"""
LeetCode #33 - Search in Rotated Sorted Array
https://leetcode.com/problems/search-in-rotated-sorted-array/

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly left rotated at an
unknown pivot index k (1 <= k < nums.length) such that the resulting array is
[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]].

For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become
[4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return
the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
    Input: nums = [4,5,6,7,0,1,2], target = 0
    Output: 4

Example 2:
    Input: nums = [4,5,6,7,0,1,2], target = 3
    Output: -1

Example 3:
    Input: nums = [1], target = 0
    Output: -1

Constraints:
    1 <= nums.length <= 5000
    -10^4 <= nums[i], target <= 10^4
    All values of nums are unique.
    nums is an ascending array that is possibly rotated.
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        # 循环数组：先找「断点」pivot（最小值下标，即旋转起点）
        left, right = 0, n - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        pivot = left

        # 展开后有两段有序区间：[pivot, n-1] 和 [0, pivot-1]
        if target >= nums[pivot] and target <= nums[n - 1]:
            return self._binary_search(nums, pivot, n - 1, target)
        return self._binary_search(nums, 0, pivot - 1, target)

    def _binary_search(self, nums: List[int], left: int, right: int, target: int) -> int:
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
