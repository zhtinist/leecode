"""
LeetCode #2121 - Intervals Between Identical Elements
相同元素的间隔之和
https://leetcode.cn/problems/intervals-between-identical-elements/

给你一个下标从 0 开始、由 `n` 个整数组成的数组 `arr` 。
`arr` 中两个元素的 间隔 定义为它们下标之间的 绝对差 。更正式地，`arr[i]` 和 `arr[j]` 之间的间隔是 `|i - j|` 。
返回一个长度为 `n` 的数组 `intervals` ，其中 `intervals[i]` 是 `arr[i]` 和 `arr` 中每个相同元素（与 `arr[i]` 的值相同）的 间隔之和 。
注意：`|x|` 是 `x` 的绝对值。

示例 1：
输入：arr = [2,1,3,1,2,3,3] 输出：[4,2,7,2,4,4,5] 解释： - 下标 0 ：另一个 2 在下标 4 ，|0 - 4| = 4 - 下标 1 ：另一个 1 在下标 3 ，|1 - 3| = 2 - 下标 2 ：另两个 3 在下标 5 和 6 ，|2 - 5| + |2 - 6| = 7 - 下标 3 ：另一个 1 在下标 1 ，|3 - 1| = 2 - 下标 4 ：另一个 2 在下标 0 ，|4 - 0| = 4 - 下标 5 ：另两个 3 在下标 2 和 6 ，|5 - 2| + |5 - 6| = 4 - 下标 6 ：另两个 3 在下标 2 和 5 ，|6 - 2| + |6 - 5| = 5
示例 2：
输入：arr = [10,5,10,10] 输出：[5,0,3,4] 解释： - 下标 0 ：另两个 10 在下标 2 和 3 ，|0 - 2| + |0 - 3| = 5 - 下标 1 ：只有这一个 5 在数组中，所以到相同元素的间隔之和是 0 - 下标 2 ：另两个 10 在下标 0 和 3 ，|2 - 0| + |2 - 3| = 3 - 下标 3 ：另两个 10 在下标 0 和 2 ，|3 - 0| + |3 - 2| = 4

提示：
`n == arr.length`
`1 <= n <= 10^5`
`1 <= arr[i] <= 10^5`

注意：本题与 2615. 等值距离和 相同。
"""

from typing import List, Optional


class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        n = len(arr)
        indices = {}
        for i, val in enumerate(arr):
            if val not in indices:
                indices[val] = []
            indices[val].append(i)

        result = [0] * n

        for val, pos in indices.items():
            if len(pos) == 1:
                continue
            m = len(pos)
            prefix = [0] * (m + 1)
            for i in range(m):
                prefix[i + 1] = prefix[i] + pos[i]

            for i in range(m):
                idx = pos[i]
                left_count = i
                right_count = m - 1 - i
                left_sum = pos[i] * left_count - (prefix[i] - prefix[0])
                right_sum = (prefix[m] - prefix[i + 1]) - pos[i] * right_count
                result[idx] = left_sum + right_sum

        return result



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Hash Table, Prefix Sum
#
# 解题思路:
# 首先按元素值分组，记录相同值出现的所有下标位置。
# 对于每个值对应的下标列表 pos，使用前缀和优化计算间隔距离：
# - 对于位于 pos[i] 的元素，其左侧有 i 个相同元素，右侧有 m-1-i 个。
# - 左侧间隔和 = pos[i] * i - (前缀和中前 i 个元素的和)
# - 右侧间隔和 = (前缀和中后 m-1-i 个元素的和) - pos[i] * (m-1-i)
# - 该元素的总间隔和 = 左侧 + 右侧
# 只有单个元素的组直接跳过（间隔和为 0）。
#
# 时间复杂度: O(n)
# 空间复杂度: O(n)
#
# 关键点:
# - 按值分组下标，使用哈希表
# - 前缀和避免 O(k^2) 的两两计算
# - 公式拆分：左半部分和右半部分分别计算
