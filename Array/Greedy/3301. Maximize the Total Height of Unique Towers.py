"""
LeetCode #3301 - Maximize the Total Height of Unique Towers
高度互不相同的最大塔高和
https://leetcode.cn/problems/maximize-the-total-height-of-unique-towers/

给你一个数组 `maximumHeight` ，其中 `maximumHeight[i]` 表示第 `i` 座塔可以达到的 最大 高度。
你的任务是给每一座塔分别设置一个高度，使得：
第 `i` 座塔的高度是一个正整数，且不超过 `maximumHeight[i]` 。
所有塔的高度互不相同。
请你返回设置完所有塔的高度后，可以达到的 最大 总高度。如果没有合法的设置，返回 `-1` 。

示例 1：

输入：maximumHeight = [2,3,4,3]
输出：10
解释：
我们可以将塔的高度设置为：`[1, 2, 4, 3]` 。
示例 2：

输入：maximumHeight = [15,10]
输出：25
解释：
我们可以将塔的高度设置为：`[15, 10]` 。
示例 3：

输入：maximumHeight = [2,2,1]
输出：-1
解释：
无法设置塔的高度为正整数且高度互不相同。

提示：
`1 <= maximumHeight.length <= 10^5`
`1 <= maximumHeight[i] <= 10^9`
"""

from typing import List, Optional


class Solution:
    def maximumTotalSum(self, maximumHeight: List[int]) -> int:
        maximumHeight.sort(reverse=True)
        ans = 0
        prev = float('inf')
        for h in maximumHeight:
            # 当前塔的高度不能超过 h，且必须小于前一个塔的高度
            cur = min(h, prev - 1)
            if cur <= 0:
                return -1
            ans += cur
            prev = cur
        return ans










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Array, Sorting
#
# 解题思路:
# 所有塔高度互不相同且不超过各自的 maximumHeight，最大化总高度。
# 贪心：将 maximumHeight 降序排序，给每个塔分配尽可能高的高度。
# 对排序后的数组，第一座塔取 maximumHeight（可能需调整），
# 后续每座塔的高度不能超过其上限，且必须严格小于前一座塔的高度。
# 取 min(maximumHeight[i], prev_height - 1)。
# 如果某座塔分配的高度 <= 0，说明无法满足条件，返回 -1。
#
# 时间复杂度: O(n log n)
# 空间复杂度: O(1)
#
# 关键点:
# - 降序贪心分配，每次取 min(上限, 前一座高度 - 1)
# - 检测无解：高度降到 0 以下
