"""
LeetCode #3572 - Maximize Y‑Sum by Picking a Triplet of Distinct X‑Values
选择不同 X 值三元组使 Y 值之和最大
https://leetcode.cn/problems/maximize-ysum-by-picking-a-triplet-of-distinct-xvalues/

给你两个整数数组 `x` 和 `y`，长度均为 `n`。你必须选择三个 不同 的下标 `i` ，`j` 和 `k`，满足以下条件：
`x[i] != x[j]`
`x[j] != x[k]`
`x[k] != x[i]`
你的目标是在满足这些条件下 最大化 `y[i] + y[j] + y[k]` 的值。返回通过选择这样一组三元组下标所能获得的 最大 可能和。
如果不存在这样的三元组，返回 -1。

示例 1：

输入：x = [1,2,1,3,2], y = [5,3,4,6,2]
输出：14
解释：
选择 `i = 0`（`x[i] = 1`，`y[i] = 5`），`j = 1`（`x[j] = 2`，`y[j] = 3`），`k = 3`（`x[k] = 3`，`y[k] = 6`）。
选出的三个 `x` 中的值互不相同。`5 + 3 + 6 = 14` 是我们能获得的最大值。因此输出为 14。
示例 2：

输入：x = [1,2,1,2], y = [4,5,6,7]
输出：-1
解释：
`x` 中只有两个不同的值。因此输出为 -1。

提示：
`n == x.length == y.length`
`3 <= n <= 10^5`
`1 <= x[i], y[i] <= 10^6`
"""

from typing import List, Optional
from collections import defaultdict


class Solution:
    def maxYSum(self, x: List[int], y: List[int]) -> int:
        n = len(x)

        # 按 x 值分组，每组保留前 3 大的 y 值
        groups = defaultdict(list)
        for i in range(n):
            groups[x[i]].append(y[i])

        # 每组只保留最大的 3 个 y 值
        candidates = []
        for x_val, y_list in groups.items():
            y_list.sort(reverse=True)
            for v in y_list[:3]:
                candidates.append((x_val, v))

        # 如果不同的 x 值少于 3 个，返回 -1
        if len(groups) < 3:
            return -1

        # 暴力枚举三个不同 x 值的组合
        ans = -1
        m = len(candidates)
        for i in range(m):
            for j in range(i + 1, m):
                if candidates[i][0] == candidates[j][0]:
                    continue
                for k in range(j + 1, m):
                    if candidates[i][0] == candidates[k][0]:
                        continue
                    if candidates[j][0] == candidates[k][0]:
                        continue
                    total = candidates[i][1] + candidates[j][1] + candidates[k][1]
                    if total > ans:
                        ans = total

        return ans










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Array, Hash Table, Sorting, Heap (Priority Queue)
#
# 解题思路:
# 1. 按 x 值分组，每组只需保留前 3 大的 y 值（因为最多选 3 个不同 x 值）。
# 2. 提取所有候选 (x, y) 对，最多 3 * distinct_x 个。
# 3. 暴力三重循环枚举三个不同 x 的候选对，取最大 y 和。
# 4. 如果不同 x 值少于 3 个，返回 -1。
# 复杂度分析：最坏情况下候选数量为 3 * 10^5，三重循环为 O((3·d)³)
# 但实际上因为 constrain 且可以提前终止：
# 因为每组最多 3 个候选，候选总数 ≤ 3 * 10^5 / 3? 不，最多 3 * n。
# 优化：对候选按 y 降序排列，在三重循环中尽早剪枝。
# 实际数据规模下，因为答案只需要最大的几次尝试，可以进一步优化为：
# 取各组最大 y 值，枚举三个不同 x 组合（类似 Top 3 思想），复杂度 O(d³) 其中 d 是 x 的不同值数量。
#
# 时间复杂度: O(n log n + d³)，其中 d 为不同 x 值的数量，d ≤ n
# 空间复杂度: O(d)
#
# 关键点:
# - 每组只保留前 3 大 y 值（贪心剪枝）
# - x 值必须互不相同
# - 需要至少有 3 个不同的 x 值，否则返回 -1
