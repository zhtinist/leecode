"""
LeetCode #3447 - Assign Elements to Groups with Constraints
将元素分配给有约束条件的组
https://leetcode.cn/problems/assign-elements-to-groups-with-constraints/

给你一个整数数组 `groups`，其中 `groups[i]` 表示第 `i` 组的大小。另给你一个整数数组 `elements`。
请你根据以下规则为每个组分配 一个 元素：
如果 `groups[i]` 能被 `elements[j]` 整除，则下标为 `j` 的元素可以分配给组 `i`。
如果有多个元素满足条件，则分配 最小的下标 `j` 的元素。
如果没有元素满足条件，则分配 -1 。
返回一个整数数组 `assigned`，其中 `assigned[i]` 是分配给组 `i` 的元素的索引，若无合适的元素，则为 -1。
注意：一个元素可以分配给多个组。

示例 1：

输入： groups = [8,4,3,2,4], elements = [4,2]
输出： [0,0,-1,1,0]
解释：
`elements[0] = 4` 被分配给组 0、1 和 4。
`elements[1] = 2` 被分配给组 3。
无法为组 2 分配任何元素，分配 -1 。
示例 2：

输入： groups = [2,3,5,7], elements = [5,3,3]
输出： [-1,1,0,-1]
解释：
`elements[1] = 3` 被分配给组 1。
`elements[0] = 5` 被分配给组 2。
无法为组 0 和组 3 分配任何元素，分配 -1 。
示例 3：

输入： groups = [10,21,30,41], elements = [2,1]
输出： [0,1,0,1]
解释：
`elements[0] = 2` 被分配给所有偶数值的组，而 `elements[1] = 1` 被分配给所有奇数值的组。

提示：
`1 <= groups.length <= 10^5`
`1 <= elements.length <= 10^5`
`1 <= groups[i] <= 10^5`
`1 <= elements[i] <= 10^5`
"""

from typing import List, Optional


class Solution:
    def assignElements(self, groups: List[int], elements: List[int]) -> List[int]:
        max_val = max(groups)
        # best_divisor[v] = smallest index of element equal to v (or INF)
        INF = 10 ** 9
        best = [INF] * (max_val + 1)
        for idx, val in enumerate(elements):
            if val <= max_val and best[val] == INF:
                best[val] = idx

        ans = []
        for g in groups:
            res = INF
            # Enumerate all divisors of g
            d = 1
            while d * d <= g:
                if g % d == 0:
                    if best[d] < res:
                        res = best[d]
                    d2 = g // d
                    if best[d2] < res:
                        res = best[d2]
                d += 1
            ans.append(res if res != INF else -1)
        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Hash Table
#
# 解题思路:
# 1. groups[i] 能被 elements[j] 整除 ⇔ elements[j] 是 groups[i] 的因子
# 2. 对于每个值 v，记录 elements 中值为 v 的最小下标
# 3. 对每个 groups[i] = g，枚举 g 的所有因子（O(√g)）
#    - 检查每个因子是否在 elements 中出现（通过 best 数组）
#    - 取最小下标
# 4. 若所有因子都不在 elements 中，返回 -1
#
# 时间复杂度: O(E + G * √maxVal) 其中 E = len(elements), G = len(groups)
# 空间复杂度: O(maxVal)
#
# 关键点:
# - 只需记录每个值的首次出现下标（最小下标）
# - 枚举因子只需 O(√g)，利用 d 和 g//d 同时检查
# - elements 中的值可能大于 max(groups)，此时可以直接忽略
