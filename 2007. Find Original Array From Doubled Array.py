"""
LeetCode #2007 - Find Original Array From Doubled Array
从双倍数组中还原原数组
https://leetcode.cn/problems/find-original-array-from-doubled-array/

一个整数数组 `original` 可以转变成一个 双倍 数组 `changed` ，转变方式为将 `original` 中每个元素 值乘以 2 加入数组中，然后将所有元素 随机打乱 。
给你一个数组 `changed` ，如果 `change` 是 双倍 数组，那么请你返回 `original`数组，否则请返回空数组。`original` 的元素可以以 任意 顺序返回。

示例 1：
输入：changed = [1,3,4,2,6,8] 输出：[1,3,4] 解释：一个可能的 original 数组为 [1,3,4] : - 将 1 乘以 2 ，得到 1 * 2 = 2 。 - 将 3 乘以 2 ，得到 3 * 2 = 6 。 - 将 4 乘以 2 ，得到 4 * 2 = 8 。 其他可能的原数组方案为 [4,3,1] 或者 [3,1,4] 。
示例 2：
输入：changed = [6,3,0,1] 输出：[] 解释：changed 不是一个双倍数组。
示例 3：
输入：changed = [1] 输出：[] 解释：changed 不是一个双倍数组。

提示：
`1 <= changed.length <= 10^5`
`0 <= changed[i] <= 10^5`
"""

from typing import List, Optional


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        """
        Sort changed. For each value, if it has been consumed, skip.
        Otherwise, it must be an original value; its double must also exist.
        Track counts with a frequency map.
        """
        from collections import Counter

        n = len(changed)
        if n % 2 != 0:
            return []

        freq = Counter(changed)
        result = []

        for x in sorted(freq.keys()):
            if freq[x] == 0:
                continue
            # Special case: x == 0, need pairs of 0s
            if x == 0:
                if freq[0] % 2 != 0:
                    return []
                result.extend([0] * (freq[0] // 2))
                freq[0] = 0
                continue

            double_x = x * 2
            if freq[x] > freq.get(double_x, 0):
                return []

            result.extend([x] * freq[x])
            freq[double_x] -= freq[x]
            freq[x] = 0

        return result



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Array, Hash Table, Sorting
#
# 解题思路:
# 首先，changed 的长度必须是偶数，否则不可能。
# 使用 Counter 统计每个数的频次。从小到大排序后遍历：
# 对于每个数 x，如果频次为 0 则跳过。
# 如果 x == 0，必须成对出现，每两个 0 对应一个 original 中的 0。
# 如果 x > 0，x 必须是 original 中的数，它的双倍 2*x 也必须在 changed 中，
# 且频次不低于 x。减去对应的频次后继续。
# 如果中途发现 2*x 的频次不足，返回空数组。
#
# 时间复杂度: O(N log N)，排序主导
# 空间复杂度: O(N)，Counter 和结果
#
# 关键点:
# - x == 0 的特殊处理
# - 贪心从小到大匹配，先匹配小的不会影响后面的选择
# - Counter 记录剩余频次
