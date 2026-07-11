"""
LeetCode #2177 - Find Three Consecutive Integers That Sum to a Given Number
找到和为给定整数的三个连续整数
https://leetcode.cn/problems/find-three-consecutive-integers-that-sum-to-a-given-number/

给你一个整数 `num` ，请你返回三个连续的整数，它们的 和 为 `num` 。如果 `num` 无法被表示成三个连续整数的和，请你返回一个 空 数组。

示例 1：
输入：num = 33 输出：[10,11,12] 解释：33 可以表示为 10 + 11 + 12 = 33 。 10, 11, 12 是 3 个连续整数，所以返回 [10, 11, 12] 。
示例 2：
输入：num = 4 输出：[] 解释：没有办法将 4 表示成 3 个连续整数的和。

提示：
`0 <= num <= 10^15`
"""

from typing import List, Optional


class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num % 3 != 0:
            return []
        mid = num // 3
        return [mid - 1, mid, mid + 1]



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Math, Simulation
#
# 解题思路:
# 设三个连续整数为 x-1, x, x+1，它们的和为 3x。因此如果 num 能被 3 整除，则中间的整数
# mid = num // 3，三个连续整数为 [mid - 1, mid, mid + 1]；否则不存在这样的三个连续整数，
# 返回空数组。
#
# 时间复杂度: O(1)
# 空间复杂度: O(1)
#
# 关键点:
# - 三个连续整数之和必定是 3 的倍数：num % 3 == 0 才可能有解
# - 中间数 mid = num // 3，连续三数为 [mid-1, mid, mid+1]
# - 纯数学推导，O(1) 时间，无需任何循环
