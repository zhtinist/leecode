"""
LeetCode #3030 - Find the Grid of Region Average
找出网格的区域平均强度
https://leetcode.cn/problems/find-the-grid-of-region-average/

给你一个下标从 0 开始、大小为 `m x n` 的网格 `image` ，表示一个灰度图像，其中 `image[i][j]` 表示在范围 `[0..255]` 内的某个像素强度。另给你一个 非负 整数 `threshold` 。
如果 `image[a][b]` 和 `image[c][d]` 满足 `|a - c| + |b - d| == 1` ，则称这两个像素是 相邻像素 。
区域 是一个 `3 x 3` 的子网格，且满足区域中任意两个 相邻 像素之间，像素强度的 绝对差  小于或等于 `threshold` 。
区域 内的所有像素都认为属于该区域，而一个像素 可以 属于 多个 区域。
你需要计算一个下标从 0 开始、大小为 `m x n` 的网格 `result` ，其中 `result[i][j]` 是 `image[i][j]` 所属区域的 平均 强度，向下取整 到最接近的整数。如果 `image[i][j]` 属于多个区域，`result[i][j]` 是这些区域的 “取整后的平均强度” 的 平均值，也 向下取整 到最接近的整数。如果 `image[i][j]` 不属于任何区域，则 `result[i][j]` 等于 `image[i][j]` 。
返回网格 `result` 。

示例 1：
输入：image = [[5,6,7,10],[8,9,10,10],[11,12,13,10]], threshold = 3 输出：[[9,9,9,9],[9,9,9,9],[9,9,9,9]] 解释：图像中存在两个区域，如图片中的阴影区域所示。第一个区域的平均强度为 9 ，而第二个区域的平均强度为 9.67 ，向下取整为 9 。两个区域的平均强度为 (9 + 9) / 2 = 9 。由于所有像素都属于区域 1 、区域 2 或两者，因此 result 中每个像素的强度都为 9 。 注意，在计算多个区域的平均值时使用了向下取整的值，因此使用区域 2 的平均强度 9 来进行计算，而不是 9.67 。
示例 2：
输入：image = [[10,20,30],[15,25,35],[20,30,40],[25,35,45]], threshold = 12 输出：[[25,25,25],[27,27,27],[27,27,27],[30,30,30]] 解释：图像中存在两个区域，如图片中的阴影区域所示。第一个区域的平均强度为 25 ，而第二个区域的平均强度为 30 。两个区域的平均强度为 (25 + 30) / 2 = 27.5 ，向下取整为 27 。图像中第 0 行的所有像素属于区域 1 ，因此 result 中第 0 行的所有像素为 25 。同理，result 中第 3 行的所有像素为 30 。图像中第 1 行和第 2 行的像素属于区域 1 和区域 2 ，因此它们在 result 中的值为 27 。
示例 3：
输入：image = [[5,6,7],[8,9,10],[11,12,13]], threshold = 1 输出：[[5,6,7],[8,9,10],[11,12,13]] 解释：图像中不存在任何区域，因此对于所有像素，result[i][j] == image[i][j] 。

提示：
`3 <= n, m <= 500`
`0 <= image[i][j] <= 255`
`0 <= threshold <= 255`
"""

from typing import List, Optional


class Solution:
    def resultGrid(
        self, image: List[List[int]], threshold: int
    ) -> List[List[int]]:
        """
        Check every 3x3 region. If all adjacent pairs within the region
        satisfy the threshold condition, compute the region's average.
        For each pixel, track sum of region averages and count of regions.
        """
        m, n = len(image), len(image[0])
        # For each pixel: sum of region averages, count of regions
        region_sum = [[0] * n for _ in range(m)]
        region_cnt = [[0] * n for _ in range(m)]

        # Adjacent offsets within a 3x3: horizontal and vertical edges
        # All 12 adjacent pairs
        adj_pairs = [
            ((0,0),(0,1)), ((0,1),(0,2)),
            ((1,0),(1,1)), ((1,1),(1,2)),
            ((2,0),(2,1)), ((2,1),(2,2)),
            ((0,0),(1,0)), ((1,0),(2,0)),
            ((0,1),(1,1)), ((1,1),(2,1)),
            ((0,2),(1,2)), ((1,2),(2,2)),
        ]

        for i in range(m - 2):
            for j in range(n - 2):
                # Check all adjacent pairs
                valid = True
                for (dx1, dy1), (dx2, dy2) in adj_pairs:
                    v1 = image[i + dx1][j + dy1]
                    v2 = image[i + dx2][j + dy2]
                    if abs(v1 - v2) > threshold:
                        valid = False
                        break

                if valid:
                    # Compute average of this 3x3 region
                    total = 0
                    for dx in range(3):
                        for dy in range(3):
                            total += image[i + dx][j + dy]
                    avg = total // 9

                    # Record for each pixel in this region
                    for dx in range(3):
                        for dy in range(3):
                            region_sum[i + dx][j + dy] += avg
                            region_cnt[i + dx][j + dy] += 1

        # Build result
        result = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if region_cnt[i][j] == 0:
                    result[i][j] = image[i][j]
                else:
                    result[i][j] = region_sum[i][j] // region_cnt[i][j]

        return result



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Matrix
#
# 解题思路:
# 枚举所有可能的 3x3 区域（每个以 (i,j) 为左上角）。对于每个区域，检查所有 12 对相邻像素
# （6 条水平边 + 6 条垂直边）的差值是否都不超过 threshold。若是有效区域，计算其 9 个像素的平均值（向下取整），
# 并为区域内每个像素累加该平均值和计数。最后对于每个像素，求其所属区域平均值的平均值（向下取整）。
#
# 时间复杂度: O(m * n)，每个 3x3 区域常数时间检查（12 对 + 9 个像素求和）
# 空间复杂度: O(m * n)，存储每个像素的区域和与计数
#
# 关键点:
# - 区域有效性检查：只需验证 3x3 内的 12 对相邻像素
# - 像素可属于多个区域，最终值取其所属区域平均值的平均值
# - 不属于任何区域的像素保持原值
