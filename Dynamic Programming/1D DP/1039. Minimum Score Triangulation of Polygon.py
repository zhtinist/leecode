"""
LeetCode #1039 - Minimum Score Triangulation of Polygon
中文题名：多边形三角剖分的最低得分
https://leetcode.com/problems/minimum-score-triangulation-of-polygon/

Given `N`, consider a convex `N`-sided polygon with vertices labelled
`A[0], A[i], ..., A[N-1]` in clockwise order.

Suppose you triangulate the polygon into `N-2` triangles.  For each triangle,
the value of that triangle is the product of the labels of the
vertices, and the total score of the triangulation is the sum of these values over
all `N-2` triangles in the triangulation.

Return the smallest possible total score that you can achieve with some triangulation of the
polygon.

Example 1:

Input: [1,2,3]
Output: 6
Explanation: The polygon is already triangulated, and the score of the only triangle is 6.

Example 2:

Input: [3,7,4,5]
Output: 144
Explanation: There are two triangulations, with possible scores: 3*7*5 + 4*5*7 = 245, or 3*4*5 + 3*4*7 = 144.  The minimum score is 144.

Example 3:

Input: [1,3,1,4,1,5]
Output: 13
Explanation: The minimum score triangulation has score 1*1*3 + 1*1*4 + 1*1*5 + 1*1*1 = 13.

Note:

`3 <= A.length <= 50`

`1 <= A[i] <= 100`

【中文翻译】
给定 N，考虑一个凸 N 边形，其顶点按顺时针顺序标记为 A[0], A[1], ..., A[N-1]。

假设你将多边形剖分成 N-2 个三角形。对于每个三角形，该三角形的值为三个顶点标签的乘积，三角剖分的总得分是剖分中所有 N-2 个三角形的这些值之和。

返回通过某种多边形三角剖分可以达到的最小可能总得分。

示例 1：

输入：[1,2,3]
输出：6
解释：多边形已经是一个三角形，唯一三角形的得分为 6。

示例 2：

输入：[3,7,4,5]
输出：144
解释：有两种三角剖分，可能的得分为：3*7*5 + 4*5*7 = 245，或 3*4*5 + 3*4*7 = 144。最小得分为 144。

示例 3：

输入：[1,3,1,4,1,5]
输出：13
解释：最小得分三角剖分的得分为 1*1*3 + 1*1*4 + 1*1*5 + 1*1*1 = 13。

注意：

3 <= A.length <= 50
1 <= A[i] <= 100
"""

from typing import List, Optional


class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        dp = [[0] * n for _ in range(n)]

        # length of the polygon side (j - i)
        for length in range(2, n):
            for i in range(n - length):
                j = i + length
                dp[i][j] = float('inf')
                for k in range(i + 1, j):
                    score = values[i] * values[k] * values[j] + dp[i][k] + dp[k][j]
                    dp[i][j] = min(dp[i][j], score)

        return dp[0][n - 1]










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用区间动态规划。定义 dp[i][j] 为将从顶点 i 到顶点 j（包含）的多边形进行三角剖分的最小得分。
# 对于多边形 i..j，选择中间顶点 k（i < k < j），形成三角形 (i, k, j)。
# 该三角形的得分为 values[i] * values[k] * values[j]。
# 剩下的两个子多边形分别为 i..k 和 k..j，它们的最小得分由 dp[i][k] 和 dp[k][j] 给出。
# 枚举所有可能的 k，取最小值。
# 按区间长度从小到大计算。
#
# 时间复杂度: O(N^3) - 三重循环：区间长度、起点、中间点
# 空间复杂度: O(N^2) - DP表格
#
# 关键点:
# - dp[i][j] 表示顶点 i 到 j 的子多边形的最小三角剖分得分
# - 边界条件：j - i < 2 时 dp[i][j] = 0（不足构成三角形）
# - 固定三角形的一条边 (i, j)，枚举第三个顶点 k
