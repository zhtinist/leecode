"""
LeetCode #1954 - Minimum Garden Perimeter to Collect Enough Apples
收集足够苹果的最小花园周长
https://leetcode.cn/problems/minimum-garden-perimeter-to-collect-enough-apples/

给你一个用无限二维网格表示的花园，每一个 整数坐标处都有一棵苹果树。整数坐标 `(i, j)` 处的苹果树有 `|i| + |j|` 个苹果。
你将会买下正中心坐标是 `(0, 0)` 的一块 正方形土地 ，且每条边都与两条坐标轴之一平行。
给你一个整数 `neededApples` ，请你返回土地的 最小周长 ，使得 至少 有 `neededApples` 个苹果在土地 里面或者边缘上。
`|x|` 的值定义为：
如果 `x >= 0` ，那么值为 `x`
如果 `x < 0` ，那么值为 `-x`

示例 1：
输入：neededApples = 1 输出：8 解释：边长长度为 1 的正方形不包含任何苹果。 但是边长为 2 的正方形包含 12 个苹果（如上图所示）。 周长为 2 * 4 = 8 。
示例 2：
输入：neededApples = 13 输出：16
示例 3：
输入：neededApples = 1000000000 输出：5040

提示：
`1 <= neededApples <= 10^15`
"""

from typing import List, Optional


class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        """
        A square of half-side length x has apples:
        sum over the square = 2 * x * (x + 1) * (2 * x + 1)
        Binary search for the smallest x satisfying neededApples.
        Perimeter = 8 * x.
        """
        # Total apples in a square with half-side x (corners at (±x, ±x))
        def total_apples(x: int) -> int:
            return 2 * x * (x + 1) * (2 * x + 1)

        lo, hi = 1, 1
        # Expand upper bound until enough apples
        while total_apples(hi) < neededApples:
            hi *= 2

        while lo < hi:
            mid = (lo + hi) // 2
            if total_apples(mid) >= neededApples:
                hi = mid
            else:
                lo = mid + 1

        return 8 * lo



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Math, Binary Search
#
# 解题思路:
# 设正方形半边长为 x（即正方形角坐标为 (±x, ±x)），周长为 8x。
# 苹果总数公式推导：正方形内每个点 (i, j) 的苹果数为 |i| + |j|。
# 总苹果数 = 2 * x * (x + 1) * (2 * x + 1)
# 使用二分查找找到最小的 x 使得 total_apples(x) >= neededApples。
# 由于 neededApples 可达 10^15，先用倍增确定上界。
#
# 时间复杂度: O(log(neededApples))，二分查找
# 空间复杂度: O(1)
#
# 关键点:
# - 苹果总数公式: 2*x*(x+1)*(2*x+1)
# - 半边长的含义：正方形从 -x 到 x
# - 周长 = 8 * x
