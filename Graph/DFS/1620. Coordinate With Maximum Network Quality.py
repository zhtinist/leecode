"""
LeetCode #1620 - Coordinate With Maximum Network Quality
中文题名：网络信号最好的坐标
https://leetcode.com/problems/coordinate-with-maximum-network-quality/

You are given an array of network towers `towers` and an integer `radius`,
where `towers[i] = [xi, yi, qi]` denotes the
`ith` network tower with location `(xi,
yi)` and quality factor `qi`. All the
coordinates are integral coordinates on the X-Y plane, and the distance
between two coordinates is the Euclidean distance.

The integer `radius` denotes the maximum distance in
which the tower is reachable. The tower is
reachable if the distance is less than or equal to
`radius`. Outside that distance, the signal becomes garbled, and the
tower is not reachable.

The signal quality of the `ith` tower at a coordinate `(x,
y)` is calculated with the formula `⌊qi / (1 + d)⌋`,
where `d` is the distance between the tower and the coordinate. The
network quality at a coordinate is the sum of the signal qualities
from all the reachable towers.

Return the integral coordinate where the network quality is
maximum. If there are multiple coordinates with the same network
quality, return the lexicographically minimum coordinate.

Note:

A coordinate `(x1, y1)` is lexicographically smaller than `(x2,
y2)` if either `x1 < x2` or `x1 == x2` and `y1
< y2`.

`⌊val⌋` is the greatest integer less than or equal to
`val` (the floor function).

Example 1:

Input: towers = [[1,2,5],[2,1,7],[3,1,9]], radius = 2
Output: [2,1]
Explanation:
At coordinate (2, 1) the total quality is 13
- Quality of 7 from (2, 1) results in ⌊7 / (1 + sqrt(0)⌋ = ⌊7⌋ = 7
- Quality of 5 from (1, 2) results in ⌊5 / (1 + sqrt(2)⌋ = ⌊2.07⌋ = 2
- Quality of 9 from (3, 1) results in ⌊9 / (1 + sqrt(1)⌋ = ⌊4.5⌋ = 4
No other coordinate has higher quality.

Example 2:

Input: towers = [[23,11,21]], radius = 9
Output: [23,11]

Example 3:

Input: towers = [[1,2,13],[2,1,7],[0,1,9]], radius = 2
Output: [1,2]

Example 4:

Input: towers = [[2,1,9],[0,1,9]], radius = 2
Output: [0,1]
Explanation: Both (0, 1) and (2, 1) are optimal in terms of quality but (0, 1) is lexicograpically minimal.

Constraints:

`1 <= towers.length <= 50`

`towers[i].length == 3`

`0 <= xi, yi, qi <= 50`

`1 <= radius <= 50`

【中文翻译】
给定一个信号塔数组 towers[i] = [x, y, q]，表示塔位于坐标 (x, y) 且信号质量为 q。
给定半径 radius，对于任意坐标 (X, Y)，其网络信号质量为所有信号塔的信号强度之和。
塔 i 对 (X, Y) 的信号强度为 ⌊q / (1 + d)⌋，其中 d 是塔到坐标的距离（d = sqrt((x-X)^2 + (y-Y)^2)），
如果 d > radius 则信号为 0。返回网络信号质量最大的整数坐标，如有多个返回字典序最小（x 最小，x 相同时 y 最小）。

示例 1：
输入: towers = [[1,2,5],[2,1,7],[3,1,9]], radius = 2
输出: [2,1]
解释: 坐标 (2,1) 的总信号质量最高。
"""

from typing import List, Optional
import math


class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        # 确定搜索范围
        if not towers:
            return [0, 0]
        max_x = max(t[0] for t in towers)
        max_y = max(t[1] for t in towers)

        best = [0, 0]
        max_quality = 0

        for x in range(max_x + 1):
            for y in range(max_y + 1):
                quality = 0
                for tx, ty, q in towers:
                    d_sq = (x - tx) ** 2 + (y - ty) ** 2
                    if d_sq <= radius ** 2:
                        quality += int(q / (1 + math.sqrt(d_sq)))
                if quality > max_quality:
                    max_quality = quality
                    best = [x, y]

        return best
# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 由于信号塔坐标范围有限（0到50），可以暴力枚举所有可能的整数坐标 (x, y)。
# 对每个坐标，计算所有信号塔的信号强度之和（距离超过 radius 的忽略），取最大值。
# 坐标遍历顺序天然满足字典序最小要求。
#
# 时间复杂度: O(X * Y * T) — X, Y 为坐标范围，T 为信号塔数量
# 空间复杂度: O(1) — 仅使用常数额外空间
#
# 关键点:
# - 坐标范围由信号塔位置决定（0 到 max_x, max_y）
# - 距离判断用平方比较避免浮点误差：d_sq <= radius^2
# - 信号强度公式 floor(q / (1 + d))，d 为欧氏距离
