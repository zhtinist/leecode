"""
LeetCode #454 - 4Sum II
中文题名：四数相加 II
https://leetcode.com/problems/4sum-ii/

Given four lists A, B, C, D of integer values, compute how many tuples `(i, j, k,
l)` there are such that `A[i] + B[j] + C[k] + D[l]` is zero.

To make problem a bit easier, all A, B, C, D have same length of N where 0 <= N <= 500.
All integers are in the range of -228 to 228 - 1 and the result is
guaranteed to be at most 231 - 1.

Example:

Input:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

Output:
2

Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0

【中文翻译】
给定四个整数列表 A、B、C、D，计算有多少个四元组 (i, j, k, l) 使得 A[i] + B[j] + C[k] + D[l] = 0。

为了简化问题，A、B、C、D 长度 N 相同，0 <= N <= 500。所有整数在 -2^28 到 2^28-1 之间，
结果保证不超过 2^31-1。

示例：
输入：
A = [1, 2]
B = [-2, -1]
C = [-1, 2]
D = [0, 2]
输出：2
解释：两个四元组为：
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
"""

from typing import List, Optional
from collections import Counter


class Solution:
    def fourSumCount(
        self, nums1: List[int], nums2: List[int],
        nums3: List[int], nums4: List[int]
    ) -> int:
        # Count all sums of pairs from nums1 and nums2
        sum_count = Counter()
        for a in nums1:
            for b in nums2:
                sum_count[a + b] += 1

        # For each pair from nums3 and nums4, look for complement
        count = 0
        for c in nums3:
            for d in nums4:
                complement = -(c + d)
                count += sum_count[complement]

        return count



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 分治+哈希表。将四数之和拆分为两部分：先计算 A[i] + B[j] 的所有可能和，存入哈希表（Counter）。
# 然后遍历 C[k] + D[l] 的所有和，在哈希表中查找其相反数 -(C[k] + D[l])，累加计数。
# 将 O(N^4) 暴力降为 O(N^2)。
#
# 时间复杂度: O(N^2) — 计算 A+B 的和 O(N^2)，遍历 C+D 也是 O(N^2)
# 空间复杂度: O(N^2) — 哈希表存储 A+B 最多 N^2 种和
#
# 关键点:
# - 将 4Sum 降维为 2Sum 的思想：分组处理
# - 使用 Counter/HashMap 存储中间结果
# - 与 #18 4Sum 的区别：本题是四个独立数组，不是单一数组；只需计数无需去重
