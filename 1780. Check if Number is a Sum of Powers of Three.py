"""
LeetCode #1780 - Check if Number is a Sum of Powers of Three
中文题名：判断一个数字是否可以表示成三的幂的和
https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/

Given an integer `n`, return `true` if it is possible to represent `n` as the sum of distinct powers of three. Otherwise, return `false`.

An integer `y` is a power of three if there exists an integer `x` such that `y == 3x`.

Example 1:

Input: n = 12
Output: true
Explanation: 12 = 31 + 32

Example 2:

Input: n = 91
Output: true
Explanation: 91 = 30 + 32 + 34

Example 3:

Input: n = 21
Output: false

Constraints:

`1 <= n <= 107`

【中文翻译】
给定一个整数 n，判断 n 是否可以表示为若干个不同的 3 的幂次之和（即每个幂最多使用一次）。
例如 3^0、3^1、3^2 等。

示例 1：
输入: n = 12
输出: true
解释: 12 = 3^1 + 3^2 = 3 + 9

示例 2：
输入: n = 91
输出: true
解释: 91 = 3^0 + 3^2 + 3^4 = 1 + 9 + 81

示例 3：
输入: n = 21
输出: false
解释: 21 = 3^0 + 3^0 + 3^1? 不允许重复使用。21 的二进制/三进制表示中有系数2。
"""

from typing import List, Optional


class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        # 转换为三进制，检查是否有数字 2
        while n > 0:
            if n % 3 == 2:
                return False
            n //= 3
        return True
# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 将 n 转换为三进制表示。每个 3 的幂只能使用 0 次或 1 次。
# 三进制中，如果某位出现 2 则说明需要两个该幂次，不符合要求。
# 如果只有 0 和 1 则返回 true。
#
# 时间复杂度: O(log N)
# 空间复杂度: O(1)
#
# 关键点:
# - 转换为三进制是最简洁的解法
# - 三进制位为 2 意味着需要两个相同的 3 的幂
# - 本质上是判断 n 的三进制表示中是否只有 0 和 1
