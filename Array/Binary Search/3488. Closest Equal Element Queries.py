"""
LeetCode #3488 - Closest Equal Element Queries
距离最小相等元素查询
https://leetcode.cn/problems/closest-equal-element-queries/

给你一个 环形 数组 `nums` 和一个数组 `queries` 。
对于每个查询 `i` ，你需要找到以下内容：
数组 `nums` 中下标 `queries[i]` 处的元素与 任意 其他下标 `j`（满足 `nums[j] == nums[queries[i]]`）之间的 最小 距离。如果不存在这样的下标 `j`，则该查询的结果为 `-1` 。
返回一个数组 `answer`，其大小与 `queries` 相同，其中 `answer[i]` 表示查询`i`的结果。

示例 1：

输入： nums = [1,3,1,4,1,3,2], queries = [0,3,5]
输出： [2,-1,3]
解释：
查询 0：下标 `queries[0] = 0` 处的元素为 `nums[0] = 1` 。最近的相同值下标为 2，距离为 2。
查询 1：下标 `queries[1] = 3` 处的元素为 `nums[3] = 4` 。不存在其他包含值 4 的下标，因此结果为 -1。
查询 2：下标 `queries[2] = 5` 处的元素为 `nums[5] = 3` 。最近的相同值下标为 1，距离为 3（沿着循环路径：`5 -> 6 -> 0 -> 1`）。
示例 2：

输入： nums = [1,2,3,4], queries = [0,1,2,3]
输出： [-1,-1,-1,-1]
解释：
数组 `nums` 中的每个值都是唯一的，因此没有下标与查询的元素值相同。所有查询的结果均为 -1。

提示：
`1 <= queries.length <= nums.length <= 10^5`
`1 <= nums[i] <= 10^6`
`0 <= queries[i] < nums.length`
"""

from typing import List, Optional


class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        from collections import defaultdict
        from bisect import bisect_left

        n = len(nums)
        val_to_indices = defaultdict(list)
        for i, v in enumerate(nums):
            val_to_indices[v].append(i)

        ans = []
        for q in queries:
            v = nums[q]
            indices = val_to_indices[v]
            m = len(indices)
            if m == 1:
                ans.append(-1)
                continue

            pos = bisect_left(indices, q)
            # Predecessor
            if pos == 0:
                pred = indices[-1]
                d1 = min(q + n - pred, pred - q)  # wrap around
            else:
                pred = indices[pos - 1]
                d1 = q - pred  # direct distance
            # Successor
            if pos == m - 1:
                succ = indices[0]
                d2 = min(succ + n - q, q - succ)
            else:
                succ = indices[pos + 1]
                d2 = succ - q

            ans.append(min(d1, d2))

        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Hash Table, Binary Search
#
# 解题思路:
# 1. 用哈希表将相同值的下标分组
# 2. 对于每个查询 q，在对应值的下标列表中用二分查找定位
# 3. 检查前驱（列表中前一个下标）和后继（列表中后一个下标）
#    - 若 q 是列表第一个，前驱为列表最后一个（循环数组）
#    - 若 q 是列表最后一个，后继为列表第一个（循环数组）
# 4. 距离计算：直线距离 |i-j|，循环距离 = min(|i-j|, n - |i-j|)
#    对于非 wrap 情况，前驱距离 = q - pred，后继距离 = succ - q（均为正数）
#    对于 wrap 情况，需计算循环距离
#
# 时间复杂度: O(n + Q log m) — 分组 O(n)，每个查询二分 O(log m)
# 空间复杂度: O(n)
#
# 关键点:
# - 循环数组的前驱/后继需要考虑 "wrap around"
# - 距离用 min(直线距离, 循环距离)
