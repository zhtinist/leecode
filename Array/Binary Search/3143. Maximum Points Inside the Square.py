"""
LeetCode #3143 - Maximum Points Inside the Square
正方形中的最多点数
https://leetcode.cn/problems/maximum-points-inside-the-square/

给你一个二维数组 `points` 和一个字符串 `s` ，其中 `points[i]` 表示第 `i` 个点的坐标，`s[i]` 表示第 `i` 个点的 标签 。
如果一个正方形的中心在 `(0, 0)` ，所有边都平行于坐标轴，且正方形内 不 存在标签相同的两个点，那么我们称这个正方形是 合法 的。
请你返回 合法 正方形中可以包含的 最多 点数。
注意：
如果一个点位于正方形的边上或者在边以内，则认为该点位于正方形内。
正方形的边长可以为零。

示例 1：

输入：points = [[2,2],[-1,-2],[-4,4],[-3,1],[3,-3]], s = "abdca"
输出：2
解释：
边长为 4 的正方形包含两个点 `points[0]` 和 `points[1]` 。
示例 2：

输入：points = [[1,1],[-2,-2],[-2,2]], s = "abb"
输出：1
解释：
边长为 2 的正方形包含 1 个点 `points[0]` 。
示例 3：

输入：points = [[1,1],[-1,-1],[2,-2]], s = "ccd"
输出：0
解释：
任何正方形都无法只包含 `points[0]` 和 `points[1]` 中的一个点，所以合法正方形中都不包含任何点。

提示：
`1 <= s.length, points.length <= 10^5`
`points[i].length == 2`
`-10^9 <= points[i][0], points[i][1] <= 10^9`
`s.length == points.length`
`points` 中的点坐标互不相同。
`s` 只包含小写英文字母。
"""

from typing import List, Optional


class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        # 计算每个点到原点的切比雪夫距离，按距离排序
        arr = [(max(abs(x), abs(y)), s[i]) for i, (x, y) in enumerate(points)]
        arr.sort()

        seen = set()  # 已经包含的标签
        i = 0
        n = len(arr)

        while i < n:
            d = arr[i][0]
            # 处理同一距离内的所有点
            j = i
            level_labels = set()
            while j < n and arr[j][0] == d:
                label = arr[j][1]
                if label in seen or label in level_labels:
                    return i  # 只能包含当前距离之前的点
                level_labels.add(label)
                j += 1
            seen.update(level_labels)
            i = j

        return n



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Hash Table, String, Binary Search, Sorting
#
# 解题思路:
# 正方形中心在原点、边平行坐标轴，点到边界的距离由max(|x|,|y|)决定（切比雪夫距离）。
# 按此距离升序排列所有点。逐层扩展正方形，每层处理相同距离的所有点。
# 如果某层出现重复标签，或标签已在之前的层出现过，则只能包含该层之前的点。
# 返回最大可包含点数。
#
# 时间复杂度: O(n log n)
# 空间复杂度: O(n)
#
# 关键点:
# - 用切比雪夫距离max(|x|,|y|)表示点到正方形边界的距离
# - 同一距离的点必须同时包含或同时排除
# - 一旦某个标签重复出现，无法继续扩展
