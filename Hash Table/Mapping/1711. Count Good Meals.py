"""
LeetCode #1711 - Count Good Meals
中文题名：大餐计数
https://leetcode.com/problems/count-good-meals/

A good meal is a meal that contains exactly two different
food items with a sum of deliciousness equal to a power of two.

You can pick any two different foods to make a good meal.

Given an array of integers `deliciousness` where
`deliciousness[i]` is the deliciousness of the `i​​​​​​th​​​​`​​​​
item of food, return the number of different good meals you can
make from this list modulo `109 + 7`.

Note that items with different indices are considered different even if they have the
same deliciousness value.

Example 1:

Input: deliciousness = [1,3,5,7,9]
Output: 4
Explanation: The good meals are (1,3), (1,7), (3,5) and, (7,9).
Their respective sums are 4, 8, 8, and 16, all of which are powers of 2.

Example 2:

Input: deliciousness = [1,1,1,3,3,3,7]
Output: 15
Explanation: The good meals are (1,1) with 3 ways, (1,3) with 9 ways, and (1,7) with 3 ways.

Constraints:

`1 <= deliciousness.length <= 105`

`0 <= deliciousness[i] <= 220`

【中文翻译】
一顿大餐是指包含恰好两种不同食品且美味程度之和等于 2 的幂的餐食。

你可以选择任意两种不同的食物来组成一顿大餐。

给定一个整数数组 `deliciousness`，其中 `deliciousness[i]` 是第 `i` 种食物的美味程度，
返回你可以用该列表组成的不同大餐的数量，结果对 `10^9 + 7` 取模。

注意，即使美味程度相同，不同下标的食物也被视为不同。

示例 1：

输入: deliciousness = [1,3,5,7,9]
输出: 4
解释: 大餐是 (1,3), (1,7), (3,5), (7,9)
它们的和分别为 4, 8, 8, 16，都是 2 的幂

示例 2：

输入: deliciousness = [1,1,1,3,3,3,7]
输出: 15
解释: 大餐是 (1,1) 有 3 种组合方式，(1,3) 有 9 种组合方式，(1,7) 有 3 种组合方式

约束条件：

`1 <= deliciousness.length <= 10^5`
`0 <= deliciousness[i] <= 2^20`
"""

from typing import List, Optional


class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        """
        两数之和变体：对于每个元素 val，枚举所有的 2 的幂 target，
        在哈希表中查找 target - val 的出现次数。

        由于 0 <= val <= 2^20，最大的两数之和 <= 2^21，
        所以需要检查的 2 的幂为 2^0, 2^1, ..., 2^21。
        """
        MOD = 10 ** 9 + 7
        count = {}
        result = 0

        for val in deliciousness:
            # 枚举 2^0 到 2^21
            for p in range(22):
                complement = (1 << p) - val
                if complement in count:
                    result = (result + count[complement]) % MOD
            # 将当前值加入哈希表
            count[val] = count.get(val, 0) + 1

        return result










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 两数之和 (Two Sum) 的变体。目标是从数组中选两个不同下标元素，使它们的和是 2 的幂。
#
# 由于 0 <= deliciousness[i] <= 2^20，两数之和最大为 2^21，
# 因此只有 22 个可能的 2 的幂：2^0, 2^1, ..., 2^21。
#
# 使用哈希表记录已遍历元素的频次。对于当前元素 val：
# - 枚举每个 2 的幂 target = 2^p (p=0..21)
# - complement = target - val
# - 如果 complement 在哈希表中，则存在 count[complement] 对有效组合
# - 将 val 加入哈希表（频次 + 1）
#
# 注意需要在查找之后再将 val 加入哈希表，避免 val 与自己配对。
#
# 时间复杂度: O(22 * n) = O(n)，遍历数组并枚举 22 个幂
# 空间复杂度: O(n)，哈希表存储
#
# 关键点:
# - 2 的幂只有 22 种可能（0 到 21 次方），而非无限
# - 先查找再插入，确保不同下标（即使值相同）
# - 使用 defaultdict 或 dict.get 记录频次
