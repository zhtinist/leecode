"""
LeetCode #2929 - Distribute Candies Among Children II
给小朋友们分糖果 II
https://leetcode.cn/problems/distribute-candies-among-children-ii/

给你两个正整数 `n` 和 `limit` 。
请你将 `n` 颗糖果分给 `3` 位小朋友，确保没有任何小朋友得到超过 `limit` 颗糖果，请你返回满足此条件下的 总方案数 。

示例 1：
输入：n = 5, limit = 2 输出：3 解释：总共有 3 种方法分配 5 颗糖果，且每位小朋友的糖果数不超过 2 ：(1, 2, 2) ，(2, 1, 2) 和 (2, 2, 1) 。
示例 2：
输入：n = 3, limit = 3 输出：10 解释：总共有 10 种方法分配 3 颗糖果，且每位小朋友的糖果数不超过 3 ：(0, 0, 3) ，(0, 1, 2) ，(0, 2, 1) ，(0, 3, 0) ，(1, 0, 2) ，(1, 1, 1) ，(1, 2, 0) ，(2, 0, 1) ，(2, 1, 0) 和 (3, 0, 0) 。

提示：
`1 <= n <= 10^6`
`1 <= limit <= 10^6`
"""

from typing import List, Optional


class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        def C2(k: int) -> int:
            if k < 2:
                return 0
            return k * (k - 1) // 2

        ans = C2(n + 2)
        ans -= 3 * C2(n - limit + 1)
        ans += 3 * C2(n - 2 * limit)
        ans -= C2(n - 3 * limit - 1)
        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Math, Combinatorics, Enumeration
#
# 解题思路:
# 使用容斥原理。总数 = C(n+2, 2)（三个非负整数之和为n的组合数）。
# 减去某个孩子超过limit的情况（x >= limit+1），加上两个同时超过，减去三个都超过。
# 每个情况通过变量替换转化为无限制的非负整数解问题，使用组合公式 C(k, 2) = k*(k-1)/2。
#
# 时间复杂度: O(1)
# 空间复杂度: O(1)
#
# 关键点:
# - 容斥原理：总数 - 单项违规 + 双项违规 - 三项违规
# - 变量替换：x > limit 时设 x' = x - (limit+1)
# - C(k, 2) 定义k < 2 时为 0，处理负参数
