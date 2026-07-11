"""
LeetCode #3128 - Right Triangles
直角三角形
https://leetcode.cn/problems/right-triangles/

给你一个二维 boolean 矩阵 `grid` 。
如果 `grid` 的 3 个元素的集合中，一个元素与另一个元素在 同一行，并且与第三个元素在 同一列，则该集合是一个 直角三角形。3 个元素 不必 彼此相邻。
请你返回使用 `grid` 中的 3 个元素可以构建的 直角三角形 数目，且满足 3 个元素值 都 为 1 。

示例 1：
0 			1 			0 		 		 			0 			1 			1 		 		 			0 			1 			0 		 	    	 		 			0 			1 			0 		 		 			0 			1 			1 		 		 			0 			1 			0

输入：grid = [[0,1,0],[0,1,1],[0,1,0]]
输出：2
解释：
有 2 个值为 1 的直角三角形。注意蓝色的那个 没有 组成直角三角形，因为 3 个元素在同一列。
示例 2：
1 			0 			0 			0 		 		 			0 			1 			0 			1 		 		 			1 			0 			0 			0

输入：grid = [[1,0,0,0],[0,1,0,1],[1,0,0,0]]
输出：0
解释：
没有值为 1 的直角三角形。注意蓝色的那个 没有 组成直角三角形。
示例 3：
1 			0 			1 		 		 			1 			0 			0 		 		 			1 			0 			0 		 	    	 		 			1 			0 			1 		 		 			1 			0 			0 		 		 			1 			0 			0

输入：grid = [[1,0,1],[1,0,0],[1,0,0]]
输出：2
解释：
有两个值为 1 的直角三角形。

提示：
`1 <= grid.length <= 1000`
`1 <= grid[i].length <= 1000`
`0 <= grid[i][j] <= 1`
"""

from typing import List, Optional


class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        row_cnt = [sum(row) for row in grid]
        col_cnt = [sum(grid[i][j] for i in range(m)) for j in range(n)]

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ans += (row_cnt[i] - 1) * (col_cnt[j] - 1)
        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Hash Table, Math, Combinatorics, Counting
#
# 解题思路:
# 直角三角形的三个1构成"直角"，即有一个角点与其他两个点分别同行和同列。
# 对于每个值为1的格子(i,j)，以它为角的直角三角形数量 = (该行其余1的个数) * (该列其余1的个数)。
# 预处理每行和每列的1的个数，然后遍历每个1格子累加贡献。
#
# 时间复杂度: O(m*n)
# 空间复杂度: O(m+n)
#
# 关键点:
# - 理解直角三角形的几何意义：角点是同行同列的交叉点
# - 组合计数：(row_cnt-1)*(col_cnt-1)
# - 不和角点在同行列的点不构成三角形
