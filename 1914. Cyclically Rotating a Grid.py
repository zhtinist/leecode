"""
LeetCode #1914 - Cyclically Rotating a Grid
循环轮转矩阵
https://leetcode.cn/problems/cyclically-rotating-a-grid/

给你一个大小为 `m x n` 的整数矩阵 `grid`​​​ ，其中 `m` 和 `n` 都是 偶数 ；另给你一个整数 `k` 。
矩阵由若干层组成，如下图所示，每种颜色代表一层：

矩阵的循环轮转是通过分别循环轮转矩阵中的每一层完成的。在对某一层进行一次循环旋转操作时，层中的每一个元素将会取代其 逆时针 方向的相邻元素。轮转示例如下：
返回执行 `k` 次循环轮转操作后的矩阵。

示例 1：
输入：grid = [[40,10],[30,20]], k = 1 输出：[[10,20],[40,30]] 解释：上图展示了矩阵在执行循环轮转操作时每一步的状态。
示例 2：
输入：grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], k = 2 输出：[[3,4,8,12],[2,11,10,16],[1,7,6,15],[5,9,13,14]] 解释：上图展示了矩阵在执行循环轮转操作时每一步的状态。

提示：
`m == grid.length`
`n == grid[i].length`
`2 <= m, n <= 50`
`m` 和 `n` 都是 偶数
`1 <= grid[i][j] <=^ 5000`
`1 <= k <= 10^9`
"""

from typing import List, Optional


class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        layers = min(m, n) // 2

        for layer in range(layers):
            # Extract layer elements in clockwise order
            elements = []
            # Top row (left to right)
            for col in range(layer, n - layer):
                elements.append(grid[layer][col])
            # Right column (top to bottom, excluding top)
            for row in range(layer + 1, m - layer):
                elements.append(grid[row][n - 1 - layer])
            # Bottom row (right to left, excluding right)
            if m - 1 - layer > layer:
                for col in range(n - 2 - layer, layer - 1, -1):
                    elements.append(grid[m - 1 - layer][col])
            # Left column (bottom to top, excluding bottom and top)
            if n - 1 - layer > layer:
                for row in range(m - 2 - layer, layer, -1):
                    elements.append(grid[row][layer])

            # Rotate the layer
            length = len(elements)
            if length > 0:
                rot = k % length
                elements = elements[rot:] + elements[:rot]

                # Write back rotated elements
                idx = 0
                # Top row
                for col in range(layer, n - layer):
                    grid[layer][col] = elements[idx]
                    idx += 1
                # Right column
                for row in range(layer + 1, m - layer):
                    grid[row][n - 1 - layer] = elements[idx]
                    idx += 1
                # Bottom row
                if m - 1 - layer > layer:
                    for col in range(n - 2 - layer, layer - 1, -1):
                        grid[m - 1 - layer][col] = elements[idx]
                        idx += 1
                # Left column
                if n - 1 - layer > layer:
                    for row in range(m - 2 - layer, layer, -1):
                        grid[row][layer] = elements[idx]
                        idx += 1

        return grid



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Matrix, Simulation
#
# 解题思路:
# 逐层处理矩阵的每一圈（洋葱圈）。
# 1. 对于每一层，按顺时针方向提取所有元素到一个列表中。
# 2. 对列表进行循环旋转：k % len(layer) 次。
# 3. 将旋转后的元素按原顺序写回矩阵对应位置。
# 4. 内层和外层独立旋转，互不影响。
#
# 时间复杂度: O(m * n) — 每个元素处理一次
# 空间复杂度: O(m + n) — 存储一层的元素（最外层）
#
# 关键点:
# - 逆时针旋转等价于顺时针提取后向左循环移位
# - 每层元素数量 = 2*(m+n-4*layer-2)（最外层）
# - 旋转次数取模避免重复操作
# - 处理每层时注意边界避免重复提取角落元素
