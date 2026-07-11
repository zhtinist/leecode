"""
LeetCode #1943 - Describe the Painting
描述绘画结果
https://leetcode.cn/problems/describe-the-painting/

给你一个细长的画，用数轴表示。这幅画由若干有重叠的线段表示，每个线段有 独一无二 的颜色。给你二维整数数组 `segments` ，其中 `segments[i] = [start_i, end_i, color_i]` 表示线段为 半开区间 `[start_i, end_i)` 且颜色为 `color_i` 。
线段间重叠部分的颜色会被 混合 。如果有两种或者更多颜色混合时，它们会形成一种新的颜色，用一个 集合 表示这个混合颜色。
比方说，如果颜色 `2` ，`4` 和 `6` 被混合，那么结果颜色为 `{2,4,6}` 。
为了简化题目，你不需要输出整个集合，只需要用集合中所有元素的 和 来表示颜色集合。
你想要用 最少数目 不重叠 半开区间 来 表示 这幅混合颜色的画。这些线段可以用二维数组 `painting` 表示，其中 `painting[j] = [left_j, right_j, mix_j]` 表示一个 半开区间`[left_j, right_j)` 的颜色 和 为 `mix_j` 。
比方说，这幅画由 `segments = [[1,4,5],[1,7,7]]` 组成，那么它可以表示为 `painting = [[1,4,12],[4,7,7]]` ，因为：
`[1,4)` 由颜色 `{5,7}` 组成（和为 `12`），分别来自第一个线段和第二个线段。
`[4,7)` 由颜色 `{7}` 组成，来自第二个线段。
请你返回二维数组 `painting` ，它表示最终绘画的结果（没有 被涂色的部分不出现在结果中）。你可以按 任意顺序 返回最终数组的结果。
半开区间 `[a, b)` 是数轴上点 `a` 和点 `b` 之间的部分，包含 点 `a` 且 不包含 点 `b` 。

示例 1：
输入：segments = [[1,4,5],[4,7,7],[1,7,9]] 输出：[[1,4,14],[4,7,16]] 解释：绘画结果可以表示为： - [1,4) 颜色为 {5,9} （和为 14），分别来自第一和第二个线段。 - [4,7) 颜色为 {7,9} （和为 16），分别来自第二和第三个线段。
示例 2：
输入：segments = [[1,7,9],[6,8,15],[8,10,7]] 输出：[[1,6,9],[6,7,24],[7,8,15],[8,10,7]] 解释：绘画结果可以以表示为： - [1,6) 颜色为 9 ，来自第一个线段。 - [6,7) 颜色为 {9,15} （和为 24），来自第一和第二个线段。 - [7,8) 颜色为 15 ，来自第二个线段。 - [8,10) 颜色为 7 ，来自第三个线段。
示例 3：
输入：segments = [[1,4,5],[1,4,7],[4,7,1],[4,7,11]] 输出：[[1,4,12],[4,7,12]] 解释：绘画结果可以表示为： - [1,4) 颜色为 {5,7} （和为 12），分别来自第一和第二个线段。 - [4,7) 颜色为 {1,11} （和为 12），分别来自第三和第四个线段。 注意，只返回一个单独的线段 [1,7) 是不正确的，因为混合颜色的集合不相同。

提示：
`1 <= segments.length <= 2 * 10^4`
`segments[i].length == 3`
`1 <= start_i < end_i <= 10^5`
`1 <= color_i <= 10^9`
每种颜色 `color_i` 互不相同。
"""

from typing import List, Optional


class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        """
        Use difference array (sweep line) to compute color sum at each coordinate,
        then merge contiguous intervals with the same color sum.
        """
        diff = {}
        for start, end, color in segments:
            diff[start] = diff.get(start, 0) + color
            diff[end] = diff.get(end, 0) - color

        points = sorted(diff.keys())
        result = []
        cur_sum = 0
        prev = points[0]

        for p in points:
            if cur_sum > 0:
                result.append([prev, p, cur_sum])
            cur_sum += diff[p]
            prev = p

        return result



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Hash Table, Prefix Sum, Sorting
#
# 解题思路:
# 使用差分数组（扫描线）技巧。把每个线段 [start, end, color] 转化为：
# - 在 start 处增加 color
# - 在 end 处减少 color
# 然后按坐标排序所有关键点，扫描累加当前颜色和。
# 每当当前颜色和 > 0 时，从上一个关键点到当前关键点形成一个区间，
# 颜色和为当前累加值。
# 只有当颜色和 > 0 时才输出（没有被涂色的部分不出现）。
#
# 时间复杂度: O(N log N)，排序关键点，N 为线段数
# 空间复杂度: O(N)，存储差分字典和关键点
#
# 关键点:
# - 差分数组: start 处 +color, end 处 -color
# - 排序后扫描累加，区间 [prev, cur) 颜色和为累加值
# - 颜色和为 0 的区间不输出
