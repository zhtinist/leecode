"""
LeetCode #554 - Brick Wall
中文题名：砖墙
https://leetcode.com/problems/brick-wall/

There is a brick wall in front of you. The wall is rectangular and has several rows of
bricks. The bricks have the same height but different width. You want to draw a vertical
line from the top to the bottom and cross the least bricks.

The brick wall is represented by a list of rows. Each row is a list of integers representing
the width of each brick in this row from left to right.

If your line go through the edge of a brick, then the brick is not considered as crossed. You
need to find out how to draw the line to cross the least bricks and return the number of
crossed bricks.

You cannot draw a line just along one of the two vertical edges of the wall, in which case
the line will obviously cross no bricks.

Example:

Input: [[1,2,2,1],
[3,1,2],
[1,3,2],
[2,4],
[3,1,2],
[1,3,1,1]]

Output: 2

Explanation:

Note:

The width sum of bricks in different rows are the same and won't exceed INT_MAX.

The number of bricks in each row is in range [1,10,000]. The height of wall is in range
[1,10,000]. Total number of bricks of the wall won't exceed 20,000.

【中文翻译】
你面前有一堵矩形的砖墙，由多行砖块组成。每行砖块高度相同但宽度不同。你想画一条从上到下的垂直
线，使得穿过的砖块数量最少。

砖墙由一个行列表表示，每行是从左到右表示该行每块砖的宽度。

如果画的线穿过砖块的边缘（缝隙），则该砖块不被视为被穿过。你需要找出一条画线的方式使得穿过的
砖块数量最少，并返回该最少数量。

不能沿着墙的左右两条垂直边缘画线（那样的话显然不会穿过任何砖块）。

示例：
    输入：[[1,2,2,1],
          [3,1,2],
          [1,3,2],
          [2,4],
          [3,1,2],
          [1,3,1,1]]
    输出：2

注意：
    不同行砖块的宽度总和相同且不超过 INT_MAX。
    每行砖块数量范围 [1, 10,000]。墙的高度范围 [1, 10,000]。砖块总数不超过 20,000。
"""

from typing import List, Optional
from collections import defaultdict


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        edge_count = defaultdict(int)
        for row in wall:
            pos = 0
            # 不包括最后一块砖的右边缘（即墙的右边缘），因为不能在那里画线
            for width in row[:-1]:
                pos += width
                edge_count[pos] += 1

        max_edges = max(edge_count.values()) if edge_count else 0
        return len(wall) - max_edges



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 将问题转化为找砖块缝隙最多的位置。对于每行砖，计算从左到右的累计宽度（前缀和），
# 记录每个缝隙位置出现的次数。穿过砖块最少的线 = 总行数 - 缝隙出现次数最多的位置。
# 注意不能计算每行最右端（墙的右边缘），因为不能沿墙边缘画线。
#
# 时间复杂度: O(B) — 其中 B 是砖块总数（不超过 20,000）
# 空间复杂度: O(M) — 其中 M 是不同缝隙位置的数量，最坏情况等于砖块总数
#
# 关键点:
# - 每行砖块不包含最后一块的右边缘（墙的右边界不能画线）
# - 用哈希表统计每个水平位置（累计宽度）出现的次数
# - 答案是 总行数 - 最大缝隙频数
