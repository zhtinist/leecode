"""
LeetCode #1574 - Shortest Subarray to be Removed to Make Array Sorted
中文题名：删除最短的子数组使剩余数组有序
https://leetcode.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted/


Given an integer array `arr`, remove a subarray (can be empty)
from `arr` such that the remaining elements in `arr` are
non-decreasing.

A subarray is a contiguous subsequence of the array.

Return the length of the shortest subarray to remove.

Example 1:

Input: arr = [1,2,3,10,4,2,3,5]
Output: 3
Explanation: The shortest subarray we can remove is [10,4,2] of length 3. The remaining elements after that will be [1,2,3,3,5] which are sorted.
Another correct solution is to remove the subarray [3,10,4].

Example 2:

Input: arr = [5,4,3,2,1]
Output: 4
Explanation: Since the array is strictly decreasing, we can only keep a single element. Therefore we need to remove a subarray of length 4, either [5,4,3,2] or [4,3,2,1].

Example 3:

Input: arr = [1,2,3]
Output: 0
Explanation: The array is already non-decreasing. We do not need to remove any elements.

Example 4:

Input: arr = [1]
Output: 0

Constraints:

`1 <= arr.length <= 10^5`

`0 <= arr[i] <= 10^9`

【中文翻译】
给定一个整数数组 arr，删除一个连续子数组后，使得剩余元素非递减排列。
返回需要删除的最短子数组的长度。

示例 1：
输入：arr = [1,2,3,10,4,2,3,5]
输出：3
解释：删除 [10,4,2] 后得到 [1,2,3,3,5]。

示例 2：
输入：arr = [5,4,3,2,1]
输出：4

示例 3：
输入：arr = [1,2,3]
输出：0
"""

from typing import List, Optional


class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        # Find longest non-decreasing prefix
        left = 0
        while left + 1 < n and arr[left] <= arr[left + 1]:
            left += 1
        if left == n - 1:
            return 0
        # Find longest non-decreasing suffix
        right = n - 1
        while right > 0 and arr[right - 1] <= arr[right]:
            right -= 1
        # Either remove prefix or suffix
        result = min(n - left - 1, right)
        # Try to merge prefix and suffix
        i, j = 0, right
        while i <= left and j < n:
            if arr[i] <= arr[j]:
                result = min(result, j - i - 1)
                i += 1
            else:
                j += 1
        return result



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 找到最长的非递减前缀（arr[0..left]）和最长的非递减后缀（arr[right..n-1]）。
# 答案最小值是删除中间部分全部（n-left-1）或删除前缀全部（right）的最小值。
# 然后尝试保留前缀的一部分和后缀的一部分：用双指针，对于前缀中的每个位置 i，
# 找到后缀中第一个 arr[j] >= arr[i] 的位置 j，删除 (i, j) 之间的部分。
# 取所有可能方案的最小值。
#
# 时间复杂度: O(N) — 双指针线性扫描
# 空间复杂度: O(1)
#
# 关键点:
# - 删除一个子数组 = 保留一个前缀 + 一个后缀
# - 先找最长非递减前后缀
# - 双指针合并前后缀












