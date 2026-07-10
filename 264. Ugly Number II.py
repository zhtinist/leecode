"""
LeetCode #264 - Ugly Number II
https://leetcode.com/problems/ugly-number-ii/

Write a program to find the `n`-th ugly number.

Ugly numbers are positive numbers whose prime factors only include `2,
3, 5`.

Example:

Input: n = 10
Output: 12
Explanation: `1, 2, 3, 4, 5, 6, 8, 9, 10, 12` is the sequence of the first `10` ugly numbers.

Note:

`1` is typically treated as an ugly number.

`n` does not exceed 1690.
"""

from typing import List, Optional


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [1]
        # 三个指针分别指向下一个乘以 2、3、5 的 ugly 数
        p2 = p3 = p5 = 0

        for _ in range(1, n):
            next_ugly = min(ugly[p2] * 2, ugly[p3] * 3, ugly[p5] * 5)
            ugly.append(next_ugly)

            # 移动指针（注意可能同时移动多个，因为有重复值如 2*3=6, 3*2=6）
            if next_ugly == ugly[p2] * 2:
                p2 += 1
            if next_ugly == ugly[p3] * 3:
                p3 += 1
            if next_ugly == ugly[p5] * 5:
                p5 += 1

        return ugly[-1]


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路：
# 使用三指针法动态生成 ugly 数序列。维护三个指针 p2, p3, p5，
# 分别指向下一个待乘以 2、3、5 的 ugly 数位置。每轮取三个乘积中的
# 最小值作为下一个 ugly 数，并将对应指针后移。注意当有重复值时
# （如 6 = 2*3 = 3*2），多个指针都需要移动，以避免重复。
#
# 时间复杂度: O(n)
# 空间复杂度: O(n) — 存储 ugly 序列
#
# 关键点：
# - 三指针合并有序序列，类似合并 K 有序链表
# - 处理重复值：多个 if 而非 elif，同时移动所有匹配的指针
# - 初始 ugly[0] = 1
