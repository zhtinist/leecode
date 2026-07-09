"""
LeetCode #149 - Max Points on a Line
https://leetcode.com/problems/max-points-on-a-line/

Given an array of points where points[i] = [xi, yi] represents a point on the
X-Y plane, return the maximum number of points that lie on the same straight
line.

Example 1:
    Input: points = [[1,1],[2,2],[3,3]]
    Output: 3

Example 2:
    Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
    Output: 4

Constraints:
    1 <= points.length <= 300
    points[i].length == 2
    -10^4 <= xi, yi <= 10^4
    All the points are unique.
"""

from collections import defaultdict
from math import gcd
from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return len(points)

        max_count = 0

        for i, (x1, y1) in enumerate(points):
            slopes = defaultdict(int)
            same = 1

            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                if x1 == x2 and y1 == y2:
                    same += 1
                    continue

                dx = x2 - x1
                dy = y2 - y1
                sign = -1 if dx < 0 else 1
                if dx == 0:
                    key = (0, 1)
                else:
                    g = gcd(dx, dy)
                    key = (sign * dx // g, sign * dy // g)
                slopes[key] += 1

            current_max = same
            for count in slopes.values():
                current_max = max(current_max, count + same)
            max_count = max(max_count, current_max)

        return max_count
