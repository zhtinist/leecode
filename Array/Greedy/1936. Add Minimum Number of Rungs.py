"""
LeetCode #1936 - Add Minimum Number of Rungs
新增的最少台阶数
https://leetcode.cn/problems/add-minimum-number-of-rungs/

给你一个 严格递增 的整数数组 `rungs` ，用于表示梯子上每一台阶的 高度 。当前你正站在高度为 `0` 的地板上，并打算爬到最后一个台阶。
另给你一个整数 `dist` 。每次移动中，你可以到达下一个距离你当前位置（地板或台阶）不超过 `dist` 高度的台阶。当然，你也可以在任何正 整数 高度处插入尚不存在的新台阶。
返回爬到最后一阶时必须添加到梯子上的 最少 台阶数。

示例 1：
输入：rungs = [1,3,5,10], dist = 2 输出：2 解释： 现在无法到达最后一阶。 在高度为 7 和 8 的位置增设新的台阶，以爬上梯子。  梯子在高度为 [1,3,5,7,8,10] 的位置上有台阶。
示例 2：
输入：rungs = [3,6,8,10], dist = 3 输出：0 解释： 这个梯子无需增设新台阶也可以爬上去。
示例 3：
输入：rungs = [3,4,6,7], dist = 2 输出：1 解释： 现在无法从地板到达梯子的第一阶。  在高度为 1 的位置增设新的台阶，以爬上梯子。  梯子在高度为 [1,3,4,6,7] 的位置上有台阶。
示例 4：
输入：rungs = [5], dist = 10 输出：0 解释：这个梯子无需增设新台阶也可以爬上去。

提示：
`1 <= rungs.length <= 10^5`
`1 <= rungs[i] <= 10^9`
`1 <= dist <= 10^9`
`rungs` 严格递增
"""

from typing import List, Optional


class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        """
        Calculate minimum number of additional rungs needed.
        Starting from height 0, you can climb at most `dist` at a time.
        """
        ans = 0
        prev = 0  # current position (start at floor = 0)

        for h in rungs:
            gap = h - prev
            if gap > dist:
                # Need (gap - 1) // dist additional rungs
                ans += (gap - 1) // dist
            prev = h

        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Array
#
# 解题思路:
# 贪心策略：从位置 0 开始，依次检查能否到达下一个台阶。
# 对于当前位置 prev 和下一个台阶高度 h，如果间距 gap = h - prev 超过 dist，
# 则需要插入额外的台阶。插入的最少数量为 (gap - 1) // dist（因为每次最多跳 dist）。
# 例如 gap=5, dist=2：需要 (5-1)//2 = 2 个台阶（在高度 2 和 4 处）。
# 遍历所有台阶，累计需要的额外台阶数。
#
# 时间复杂度: O(N)，其中 N 为 rungs 数组长度
# 空间复杂度: O(1)，只使用常数额外空间
#
# 关键点:
# - 额外台阶数公式: (gap - 1) // dist
# - 初始位置是 0（地板），不是第一个台阶
# - 贪心正确性：在必须插入的地方插入尽可能少的台阶
