"""
LeetCode #3208 - Alternating Groups II
交替组 II
https://leetcode.cn/problems/alternating-groups-ii/

给你一个整数数组 `colors` 和一个整数 `k` ，`colors`表示一个由红色和蓝色瓷砖组成的环，第 `i` 块瓷砖的颜色为 `colors[i]` ：
`colors[i] == 0` 表示第 `i` 块瓷砖的颜色是 红色 。
`colors[i] == 1` 表示第 `i` 块瓷砖的颜色是 蓝色 。
环中连续 `k` 块瓷砖的颜色如果是 交替 颜色（也就是说除了第一块和最后一块瓷砖以外，中间瓷砖的颜色与它 左边 和 右边 的颜色都不同），那么它被称为一个 交替 组。
请你返回 交替 组的数目。
注意 ，由于 `colors` 表示一个 环 ，第一块 瓷砖和 最后一块 瓷砖是相邻的。

示例 1：

输入：colors = [0,1,0,1,0], k = 3
输出：3
解释：

交替组包括：

示例 2：

输入：colors = [0,1,0,0,1,0,1], k = 6
输出：2
解释：

交替组包括：

示例 3：
输入：colors = [1,1,0,1], k = 4
输出：0
解释：

提示：
`3 <= colors.length <= 10^5`
`0 <= colors[i] <= 1`
`3 <= k <= colors.length`
"""

from typing import List, Optional


class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        ans = 0
        cnt = 1  # 当前交替连续长度
        for i in range(1, n + k - 1):
            if colors[i % n] != colors[(i - 1) % n]:
                cnt += 1
            else:
                cnt = 1
            if cnt >= k:
                ans += 1
        return ans










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Sliding Window
#
# 解题思路:
# 环形数组的交替组问题。将数组视为首尾相接（通过取模实现）。
# 维护当前交替连续长度 cnt：若相邻元素不同则 cnt+1，否则重置为 1。
# 当 cnt >= k 时，当前结尾的窗口是一个交替组。
# 遍历 n + k - 1 个位置（覆盖所有可能的环形窗口）。
#
# 时间复杂度: O(n + k)
# 空间复杂度: O(1)
#
# 关键点:
# - 环形数组通过 % n 处理越界
# - 交替条件只需要相邻元素不同即可，不需要严格递增
