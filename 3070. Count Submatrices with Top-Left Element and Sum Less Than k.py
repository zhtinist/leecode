"""
LeetCode #3070 - Count Submatrices with Top-Left Element and Sum Less Than k
元素和小于等于 k 的子矩阵的数目
https://leetcode.cn/problems/count-submatrices-with-top-left-element-and-sum-less-than-k/

给你一个下标从 0 开始的整数矩阵 `grid` 和一个整数 `k`。
返回包含 `grid` 左上角元素、元素和小于或等于 `k` 的 子矩阵的数目。

示例 1：
输入：grid = [[7,6,3],[6,6,1]], k = 18 输出：4 解释：如上图所示，只有 4 个子矩阵满足：包含 grid 的左上角元素，并且元素和小于或等于 18 。
示例 2：
输入：grid = [[7,2,9],[1,5,0],[2,6,6]], k = 20 输出：6 解释：如上图所示，只有 6 个子矩阵满足：包含 grid 的左上角元素，并且元素和小于或等于 20 。

提示：
`m == grid.length `
`n == grid[i].length`
`1 <= n, m <= 1000 `
`0 <= grid[i][j] <= 1000`
`1 <= k <= 10^9`
"""

from typing import List, Optional


class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        """
        Submatrices must include top-left element (0,0).
        For each (i,j) as bottom-right corner, check prefix sum <= k.
        """
        m, n = len(grid), len(grid[0])
        # 2D prefix sum
        prefix = [[0] * (n + 1) for _ in range(m + 1)]
        ans = 0

        for i in range(m):
            for j in range(n):
                prefix[i + 1][j + 1] = (
                    grid[i][j]
                    + prefix[i][j + 1]
                    + prefix[i + 1][j]
                    - prefix[i][j]
                )
                if prefix[i + 1][j + 1] <= k:
                    ans += 1

        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Matrix, Prefix Sum
#
# 解题思路:
# 子矩阵必须包含左上角元素 (0,0)，因此每个可能的右下角 (i,j) 唯一确定一个子矩阵。
# 使用二维前缀和快速计算子矩阵和。在构建前缀和的同时判断是否 <= k，若满足则计数加一。
#
# 时间复杂度: O(m * n)，构建前缀和并统计
# 空间复杂度: O(m * n)，前缀和数组
#
# 关键点:
# - 包含左上角的子矩阵由右下角坐标唯一确定
# - 二维前缀和公式：prefix[i+1][j+1] = grid[i][j] + prefix[i][j+1] + prefix[i+1][j] - prefix[i][j]
# - 一边计算一边统计，无需二次遍历
