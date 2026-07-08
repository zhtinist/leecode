"""
LeetCode #88 - Merge Sorted Array
https://leetcode.com/problems/merge-sorted-array/

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
and two integers m and n, representing the number of elements in nums1 and nums2
respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order in
nums1. To accommodate this, nums1 has a length of m + n.

Example 1:
    Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
    Output: [1,2,2,3,5,6]

Example 2:
    Input: nums1 = [1], m = 1, nums2 = [], n = 0
    Output: [1]

Example 3:
    Input: nums1 = [0], m = 0, nums2 = [1], n = 1
    Output: [1]

Constraints:
    nums1.length == m + n
    nums2.length == n
    0 <= m, n <= 200
    1 <= m + n <= 200
    -10^9 <= nums1[i], nums2[j] <= 10^9
"""

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i, j, write = m - 1, n - 1, m + n - 1

        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[write] = nums1[i]
                i -= 1
            else:
                nums1[write] = nums2[j]
                j -= 1
            write -= 1
