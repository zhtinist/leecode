"""
LeetCode #3186 - Maximum Total Damage With Spell Casting
施咒的最大总伤害
https://leetcode.cn/problems/maximum-total-damage-with-spell-casting/

一个魔法师有许多不同的咒语。
给你一个数组 `power` ，其中每个元素表示一个咒语的伤害值，可能会有多个咒语有相同的伤害值。
已知魔法师使用伤害值为 `power[i]` 的咒语时，他们就 不能 使用伤害为 `power[i] - 2` ，`power[i] - 1` ，`power[i] + 1` 或者 `power[i] + 2` 的咒语。
每个咒语最多只能被使用 一次 。
请你返回这个魔法师可以达到的伤害值之和的 最大值 。

示例 1：

输入：power = [1,1,3,4]
输出：6
解释：
可以使用咒语 0，1，3，伤害值分别为 1，1，4，总伤害值为 6 。
示例 2：

输入：power = [7,1,6,6]
输出：13
解释：
可以使用咒语 1，2，3，伤害值分别为 1，6，6，总伤害值为 13 。

提示：
`1 <= power.length <= 10^5`
`1 <= power[i] <= 10^9`
"""

from typing import List, Optional


class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        from collections import Counter
        from bisect import bisect_left

        cnt = Counter(power)
        values = sorted(cnt.keys())
        n = len(values)

        dp = [0] * (n + 1)
        for i in range(n):
            v = values[i]
            d = v * cnt[v]
            # 找到最后一个与v差值>2的元素（即值<v-2的最大索引）
            j = bisect_left(values, v - 2)  # 第一个>=v-2的位置
            dp[i + 1] = max(dp[i], dp[j] + d)

        return dp[n]



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Hash Table, Two Pointers, Binary Search, Dynamic Programming, Counting, Sorting
#
# 解题思路:
# 使用咒语后不能使用伤害值相差<=2的咒语。统计每个伤害值的总伤害（值*频率），
# 按值排序。DP：dp[i+1]表示前i个不同伤害值的最大总伤害。
# 对于第i个值v，找到最后一个与v差>2的值的位置j，
# dp[i+1] = max(不选v: dp[i], 选v: dp[j] + v*cnt[v])。
#
# 时间复杂度: O(n log n)
# 空间复杂度: O(n)
#
# 关键点:
# - 相同伤害值可全部使用（无额外冲突）
# - 冲突范围是相邻±2，类似打家劫舍
# - 用二分查找找到不冲突的前驱位置
