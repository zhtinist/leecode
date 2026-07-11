"""
LeetCode #1828 - Queries on Number of Points Inside a Circle
中文题名：圆内点的数量查询
https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle/

You are given an array `points` where `points[i] = [xi, yi]` is the coordinates of the `ith` point on a 2D plane. Multiple points can have the same coordinates.

You are also given an array `queries` where `queries[j] = [xj, yj, rj]` describes a circle centered at `(xj, yj)` with a radius of `rj`.

For each query `queries[j]`, compute the number of points inside the `jth` circle. Points on the border of the circle are considered inside.

Return an array `answer`, where `answer[j]` is the answer to the `jth` query.

Example 1:

Input: points = [[1,3],[3,3],[5,3],[2,2]], queries = [[2,3,1],[4,3,1],[1,1,2]]
Output: [3,2,2]
Explanation: The points and circles are shown above.
queries[0] is the green circle, queries[1] is the red circle, and queries[2] is the blue circle.

Example 2:

Input: points = [[1,1],[2,2],[3,3],[4,4],[5,5]], queries = [[1,2,2],[2,2,2],[4,3,2],[4,3,3]]
Output: [2,3,2,4]
Explanation: The points and circles are shown above.
queries[0] is green, queries[1] is red, queries[2] is blue, and queries[3] is purple.

Constraints:

`1 <= points.length <= 500`

`points[i].length == 2`

`0 <= x​​​​​​i, y​​​​​​i <= 500`

`1 <= queries.length <= 500`

`queries[j].length == 3`

`0 <= xj, yj <= 500`

`1 <= rj <= 500`

All coordinates are integers.

Follow up: Could you find the answer for each query in better complexity than `O(n)`?

【中文翻译】

给定一个点数组 `points`，其中 `points[i] = [xi, yi]` 是第i个点在二维平面上的坐标。多个点可能具有相同的坐标。

同时给定一个查询数组 `queries`，其中 `queries[j] = [xj, yj, rj]` 描述了一个以 `(xj, yj)` 为圆心、`rj` 为半径的圆。

对于每个查询 `queries[j]`，计算圆内点的数量。在圆边界上的点也视为在圆内。

返回答案数组 `answer`，其中 `answer[j]` 是第j个查询的答案。

示例：
输入：points = [[1,3],[3,3],[5,3],[2,2]], queries = [[2,3,1],[4,3,1],[1,1,2]]
输出：[3,2,2]

"""

from typing import List, Optional


class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        answer = []
        for x, y, r in queries:
            r2 = r * r
            count = 0
            for px, py in points:
                if (px - x) ** 2 + (py - y) ** 2 <= r2:
                    count += 1
            answer.append(count)
        return answer










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 暴力解法。对于每个查询圆，遍历所有点，检查点是否在圆内。
# 判断条件：(px - x)^2 + (py - y)^2 <= r^2（边界上的点也算在内）。
# 由于数据范围较小（点和查询各最多500个），O(N*M)可以通过。
#
# 时间复杂度: O(N * M)，N为查询数，M为点数
# 空间复杂度: O(1)，除了输出数组外使用常数空间
#
# 关键点:
# - 使用距离平方比较避免浮点数开方
# - 圆边界上的点视为在圆内（使用<=）
