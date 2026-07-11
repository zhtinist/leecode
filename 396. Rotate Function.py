"""
LeetCode #396 - Rotate Function
中文题名：旋转函数
https://leetcode.com/problems/rotate-function/

Given an array of integers `A` and let n to be its length.

Assume `Bk` to be an array obtained by rotating the array
`A` k positions clock-wise, we define a "rotation function" `F`
on `A` as follow:

`F(k) = 0 * Bk[0] + 1 * Bk[1] + ... + (n-1) * Bk[n-1]`.

Calculate the maximum value of `F(0), F(1), ..., F(n-1)`.

Note:

n is guaranteed to be less than 105.

Example:

A = [4, 3, 2, 6]

F(0) = (0 * 4) + (1 * 3) + (2 * 2) + (3 * 6) = 0 + 3 + 4 + 18 = 25
F(1) = (0 * 6) + (1 * 4) + (2 * 3) + (3 * 2) = 0 + 4 + 6 + 6 = 16
F(2) = (0 * 2) + (1 * 6) + (2 * 4) + (3 * 3) = 0 + 6 + 8 + 9 = 23
F(3) = (0 * 3) + (1 * 2) + (2 * 6) + (3 * 4) = 0 + 2 + 12 + 12 = 26

So the maximum value of F(0), F(1), F(2), F(3) is F(3) = 26.

【中文翻译】
给定一个整数数组 A，设 n 为它的长度。

假设 Bk 是通过将数组 A 顺时针旋转 k 个位置得到的数组，我们在 A 上定义一个"旋转函数" F 如下：

F(k) = 0 * Bk[0] + 1 * Bk[1] + ... + (n-1) * Bk[n-1]。

计算 F(0), F(1), ..., F(n-1) 中的最大值。

注意：

n 保证小于 10^5。

示例：

A = [4, 3, 2, 6]

F(0) = (0 * 4) + (1 * 3) + (2 * 2) + (3 * 6) = 0 + 3 + 4 + 18 = 25
F(1) = (0 * 6) + (1 * 4) + (2 * 3) + (3 * 2) = 0 + 4 + 6 + 6 = 16
F(2) = (0 * 2) + (1 * 6) + (2 * 4) + (3 * 3) = 0 + 6 + 8 + 9 = 23
F(3) = (0 * 3) + (1 * 2) + (2 * 6) + (3 * 4) = 0 + 2 + 12 + 12 = 26

所以 F(0), F(1), F(2), F(3) 中的最大值是 F(3) = 26。
"""

from typing import List, Optional


class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)
        cur = sum(i * num for i, num in enumerate(nums))
        res = cur
        for i in range(1, n):
            cur = cur + total - n * nums[n - i]
            res = max(res, cur)
        return res











# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 推导 F(k) 与 F(k-1) 的递推关系。
# 设 sum = A[0] + A[1] + ... + A[n-1]
# F(0) = 0*A[0] + 1*A[1] + ... + (n-1)*A[n-1]
# 向右旋转一次后，每个元素的系数加 1（最后一个元素系数从 n-1 变为 0）：
# F(1) = F(0) + sum - n*A[n-1]
# 一般公式：F(k) = F(k-1) + sum - n*A[n-k]
# 先计算 F(0) 和 sum，然后迭代计算每个 F(k)，记录最大值。
#
# 时间复杂度: O(n) - 第一遍计算 sum 和 F(0)，第二遍迭代计算所有 F(k)
# 空间复杂度: O(1) - 仅使用常数额外空间
#
# 关键点:
# - 推导 F(k) 与 F(k-1) 的递推关系是核心
# - 每次旋转相当于：所有系数 +1，最后一个元素系数从 n-1 回退到 0
# - F(k) = F(k-1) + sum - n * A[n-k]
# - 无需实际旋转数组，纯数学推导即可 O(1) 空间完成
