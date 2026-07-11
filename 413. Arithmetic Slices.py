"""
LeetCode #413 - Arithmetic Slices
中文题名：等差数列划分
https://leetcode.com/problems/arithmetic-slices/

A sequence of number is called arithmetic if it consists of at least three elements and if
the difference between any two consecutive elements is the same.

For example, these are arithmetic sequence:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9

The following sequence is not arithmetic.

1, 1, 2, 5, 7

A zero-indexed array A consisting of N numbers is given. A slice of that array is any pair of
integers (P, Q) such that 0 <= P < Q < N.

A slice (P, Q) of array A is called arithmetic if the sequence:

A[P], A[p + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this means that P + 1 < Q.

The function should return the number of arithmetic slices in the array A.

Example:

A = [1, 2, 3, 4]

return: 3, for 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4] and [1, 2, 3, 4] itself.

【中文翻译】
如果一个数列至少包含三个元素，并且任意两个相邻元素之差都相同，则称为等差数列。
例如：
    1, 3, 5, 7, 9
    7, 7, 7, 7
    3, -1, -5, -9

以下数列不是等差数列：
    1, 1, 2, 5, 7

给定一个包含 N 个数的零索引数组 A。切片是该数组的任意整数对 (P, Q) 满足 0 <= P < Q < N。
如果序列 A[P], A[P+1], ..., A[Q-1], A[Q] 是等差数列，则称切片 (P, Q) 为等差数列切片。
特别地，这意味着 P + 1 < Q。

函数应返回数组 A 中等差数列切片的数量。

示例：
    A = [1, 2, 3, 4]
    返回：3，对应 3 个等差数列切片：[1, 2, 3]、[2, 3, 4] 和 [1, 2, 3, 4]。
"""

from typing import List, Optional


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0

        total = 0
        cur = 0  # Number of arithmetic slices ending at current position

        for i in range(2, n):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                cur += 1   # Extend all previous slices + this 3-element slice
                total += cur
            else:
                cur = 0    # Reset

        return total


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 动态规划。定义 dp[i] 为以第 i 个元素结尾的等差数列切片的数量。
#
# 当 nums[i] - nums[i-1] == nums[i-1] - nums[i-2] 时，
# 以 i 结尾的等差数列可以由以 i-1 结尾的等差数列延长而来（再加上新的三个元素组成的切片），
# 即 dp[i] = dp[i-1] + 1。
#
# 当差值不等时，dp[i] = 0。
#
# 最终结果是所有 dp[i] 之和。由于 dp[i] 只依赖于 dp[i-1]，我们使用变量 cur 代替数组，
# 将空间优化为 O(1)。
#
# 例如 [1,2,3,4]：
# - i=2: diff(1,2)==diff(2,3), cur=1, total=1 → 切片 [1,2,3]
# - i=3: diff(2,3)==diff(3,4), cur=2, total=3 → 新增 [2,3,4] 和 [1,2,3,4]
#
# 时间复杂度: O(N) — 一次遍历
# 空间复杂度: O(1) — 只使用常数变量
#
# 关键点:
# - cur 表示以当前位置结尾的等差数列切片数量
# - 每次相等时 cur += 1，不等时 cur = 0
# - 累加 cur 到 total 得到最终结果
