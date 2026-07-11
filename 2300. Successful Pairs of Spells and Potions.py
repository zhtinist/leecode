"""
LeetCode #2300 - Successful Pairs of Spells and Potions
咒语和药水的成功对数
https://leetcode.cn/problems/successful-pairs-of-spells-and-potions/

给你两个正整数数组 `spells` 和 `potions` ，长度分别为 `n` 和 `m` ，其中 `spells[i]` 表示第 `i` 个咒语的能量强度，`potions[j]` 表示第 `j` 瓶药水的能量强度。
同时给你一个整数 `success` 。一个咒语和药水的能量强度 相乘 如果 大于等于 `success` ，那么它们视为一对 成功 的组合。
请你返回一个长度为 `n` 的整数数组 `pairs`，其中 `pairs[i]` 是能跟第 `i` 个咒语成功组合的 药水 数目。

示例 1：
输入：spells = [5,1,3], potions = [1,2,3,4,5], success = 7 输出：[4,0,3] 解释： - 第 0 个咒语：5 * [1,2,3,4,5] = [5,10,15,20,25] 。总共 4 个成功组合。 - 第 1 个咒语：1 * [1,2,3,4,5] = [1,2,3,4,5] 。总共 0 个成功组合。 - 第 2 个咒语：3 * [1,2,3,4,5] = [3,6,9,12,15] 。总共 3 个成功组合。 所以返回 [4,0,3] 。
示例 2：
输入：spells = [3,1,2], potions = [8,5,8], success = 16 输出：[2,0,2] 解释： - 第 0 个咒语：3 * [8,5,8] = [24,15,24] 。总共 2 个成功组合。 - 第 1 个咒语：1 * [8,5,8] = [8,5,8] 。总共 0 个成功组合。 - 第 2 个咒语：2 * [8,5,8] = [16,10,16] 。总共 2 个成功组合。 所以返回 [2,0,2] 。

提示：
`n == spells.length`
`m == potions.length`
`1 <= n, m <= 10^5`
`1 <= spells[i], potions[i] <= 10^5`
`1 <= success <= 10^10`
"""

from typing import List, Optional
import bisect


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # 将 potions 升序排序，以便二分查找
        potions.sort()
        m = len(potions)
        result = []

        for spell in spells:
            # 需要满足 spell * potion >= success
            # 即 potion >= ceil(success / spell)
            # 等价于 potion >= (success + spell - 1) // spell
            threshold = (success + spell - 1) // spell
            # 二分查找第一个 >= threshold 的位置
            idx = bisect.bisect_left(potions, threshold)
            # 从 idx 到末尾的药水都满足条件
            result.append(m - idx)

        return result


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Two Pointers, Binary Search, Sorting
#
# 解题思路:
# 1. 将 potions 数组升序排序，这样我们可以通过二分查找快速统计符合条件的药水数量。
# 2. 对于每个咒语 spell，我们需要找到满足 spell * potion >= success 的最小的 potion，
#    即 potion >= ceil(success / spell)。使用整除技巧计算阈值 threshold。
# 3. 用二分查找在排序后的 potions 中找到第一个 >= threshold 的位置 idx，
#    那么从 idx 到数组末尾的所有药水都满足条件，数量为 m - idx。
# 4. 如果 spell * max(potion) < success，则 idx == m，结果为 0（自然处理）。
# 5. 本题也可以使用双指针法（对 spells 也排序），但二分查找更为直观。
#
# 时间复杂度: O((m + n) * log m)
# - 排序 potions: O(m log m)
# - 对每个 spell 二分查找: O(n log m)
#
# 空间复杂度: O(1) 额外空间（不计返回值）
# - 排序可能使用 O(log m) 栈空间，或 O(m) 取决于排序算法实现
#
# 关键点:
# - 向上取整的计算: threshold = (success + spell - 1) // spell
# - bisect_left 找到第一个 >= threshold 的位置
# - 利用排序 + 二分搜索避免 O(n*m) 的暴力枚举
