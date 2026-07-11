"""
LeetCode #1031 - Maximum Sum of Two Non-Overlapping Subarrays
中文题名：两个非重叠子数组的最大和
https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/

Given an array `A` of non-negative integers, return the maximum sum of elements in
two non-overlapping (contiguous) subarrays, which have lengths `L` and
`M`.  (For clarification, the `L`-length subarray could occur
before or after the `M`-length subarray.)

Formally, return the largest `V` for which `V = (A[i] + A[i+1] +
... + A[i+L-1]) + (A[j] + A[j+1] + ... + A[j+M-1])` and either:

`0 <= i < i + L - 1 < j < j + M - 1 < A.length`,
or

`0 <= j < j + M - 1 < i < i + L - 1 < A.length`.

Example 1:

Input: A = [0,6,5,2,2,5,1,9,4], L = 1, M = 2
Output: 20
Explanation: One choice of subarrays is [9] with length 1, and [6,5] with length 2.

Example 2:

Input: A = [3,8,1,3,2,1,8,9,0], L = 3, M = 2
Output: 29
Explanation: One choice of subarrays is [3,8,1] with length 3, and [8,9] with length 2.

Example 3:

Input: A = [2,1,5,6,0,9,5,0,3,8], L = 4, M = 3
Output: 31
Explanation: One choice of subarrays is [5,6,0,9] with length 4, and [3,8] with length 3.

Note:

`L >= 1`

`M >= 1`

`L + M <= A.length <= 1000`

`0 <= A[i] <= 1000`

【中文翻译】
给定一个非负整数数组 A，返回两个不重叠（连续）子数组的最大元素和，这两个子数组的长度分别为 L 和 M。（说明：长度为 L 的子数组可以出现在长度为 M 的子数组之前或之后。）

形式化地，返回最大的 V，使得 V = (A[i] + A[i+1] + ... + A[i+L-1]) + (A[j] + A[j+1] + ... + A[j+M-1])，且满足以下条件之一：

0 <= i < i + L - 1 < j < j + M - 1 < A.length，或
0 <= j < j + M - 1 < i < i + L - 1 < A.length。

示例 1：

输入：A = [0,6,5,2,2,5,1,9,4], L = 1, M = 2
输出：20
解释：一种子数组选择是长度为 1 的 [9] 和长度为 2 的 [6,5]。

示例 2：

输入：A = [3,8,1,3,2,1,8,9,0], L = 3, M = 2
输出：29
解释：一种子数组选择是长度为 3 的 [3,8,1] 和长度为 2 的 [8,9]。

示例 3：

输入：A = [2,1,5,6,0,9,5,0,3,8], L = 4, M = 3
输出：31
解释：一种子数组选择是长度为 4 的 [5,6,0,9] 和长度为 3 的 [3,8]。

注意：

L >= 1
M >= 1
L + M <= A.length <= 1000
0 <= A[i] <= 1000
"""

from typing import List, Optional


class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        def max_sum(L: int, M: int) -> int:
            # L-length subarray comes before M-length subarray
            best = 0
            max_L = 0
            for i in range(L + M, n + 1):
                # max L-length sum ending before position i-M
                max_L = max(max_L, prefix[i - M] - prefix[i - M - L])
                # current M-length sum ends at i
                cur_M = prefix[i] - prefix[i - M]
                best = max(best, max_L + cur_M)
            return best

        return max(max_sum(firstLen, secondLen), max_sum(secondLen, firstLen))










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用前缀和数组和滑动窗口思想。考虑两种情况：
# 1. L 长度子数组在 M 长度子数组之前
# 2. M 长度子数组在 L 长度子数组之前
# 对于每种情况，从左到右扫描，维护到目前为止遇到的最大第一个子数组的和，
# 然后与当前位置的第二个子数组求和，取全局最大值。
# 两种情况分别计算后取较大值。
#
# 时间复杂度: O(N) - 遍历两次
# 空间复杂度: O(N) - 前缀和数组
#
# 关键点:
# - 两种情况分别计算：L在前M在后，或者M在前L在后
# - 使用前缀和快速计算任意子数组的和
# - 滑动窗口维护左侧最大子数组和，一次遍历即可得到答案
