"""
LeetCode #2201 - Count Artifacts That Can Be Extracted
统计可以提取的工件
https://leetcode.cn/problems/count-artifacts-that-can-be-extracted/

存在一个 `n x n` 大小、下标从 0 开始的网格，网格中埋着一些工件。给你一个整数 `n` 和一个下标从 0 开始的二维整数数组 `artifacts` ，`artifacts` 描述了矩形工件的位置，其中 `artifacts[i] = [r1_i, c1_i, r2_i, c2_i]` 表示第 `i` 个工件在子网格中的填埋情况：
`(r1_i, c1_i)` 是第 `i` 个工件 左上 单元格的坐标，且
`(r2_i, c2_i)` 是第 `i` 个工件 右下 单元格的坐标。
你将会挖掘网格中的一些单元格，并清除其中的填埋物。如果单元格中埋着工件的一部分，那么该工件这一部分将会裸露出来。如果一个工件的所有部分都都裸露出来，你就可以提取该工件。
给你一个下标从 0 开始的二维整数数组 `dig` ，其中 `dig[i] = [r_i, c_i]` 表示你将会挖掘单元格 `(r_i, c_i)` ，返回你可以提取的工件数目。
生成的测试用例满足：
不存在重叠的两个工件。
每个工件最多只覆盖 `4` 个单元格。
`dig` 中的元素互不相同。

示例 1：
输入：n = 2, artifacts = [[0,0,0,0],[0,1,1,1]], dig = [[0,0],[0,1]] 输出：1 解释：  不同颜色表示不同的工件。挖掘的单元格用 'D' 在网格中进行标记。 有 1 个工件可以提取，即红色工件。 蓝色工件在单元格 (1,1) 的部分尚未裸露出来，所以无法提取该工件。 因此，返回 1 。
示例 2：
输入：n = 2, artifacts = [[0,0,0,0],[0,1,1,1]], dig = [[0,0],[0,1],[1,1]] 输出：2 解释：红色工件和蓝色工件的所有部分都裸露出来（用 'D' 标记），都可以提取。因此，返回 2 。

提示：
`1 <= n <= 1000`
`1 <= artifacts.length, dig.length <= min(n^2, 10^5)`
`artifacts[i].length == 4`
`dig[i].length == 2`
`0 <= r1_i, c1_i, r2_i, c2_i, r_i, c_i <= n - 1`
`r1_i <= r2_i`
`c1_i <= c2_i`
不存在重叠的两个工件
每个工件 最多 只覆盖 `4` 个单元格
`dig` 中的元素互不相同
"""

from typing import List, Optional


class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        # Store all dug cells in a set for O(1) lookup
        dug_set: set[tuple[int, int]] = set()
        for r, c in dig:
            dug_set.add((r, c))

        extractable = 0

        for r1, c1, r2, c2 in artifacts:
            all_dug = True
            for r in range(r1, r2 + 1):
                for c in range(c1, c2 + 1):
                    if (r, c) not in dug_set:
                        all_dug = False
                        break
                if not all_dug:
                    break
            if all_dug:
                extractable += 1

        return extractable


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Hash Table, Simulation
#
# 解题思路:
# 1. 将所有挖掘过的单元格坐标存储在一个哈希集合中，以便 O(1) 时间查询某个单元格是否被挖掘。
# 2. 遍历每一个工件，检查该工件覆盖的所有单元格是否都在已挖掘集合中。
# 3. 如果某个工件的所有单元格都被挖掘，则该工件可提取，计数加 1。
# 4. 关键优化：由于题目限定每个工件最多只覆盖 4 个单元格，内层双重循环最多执行 4 次，
#    因此总体效率很高。
#
# 时间复杂度: O(D + A * C)，其中 D 为 dig 长度，A 为 artifacts 长度，
#              C 为每个工件覆盖的单元格数（题目限定 <= 4）。
#              即 O(D + A)，线性时间复杂度。
# 空间复杂度: O(D)，存储已挖掘单元格的哈希集合。
#
# 关键点:
# - 利用"每个工件最多覆盖 4 个单元格"的条件，可以放心地枚举每个工件的所有单元格。
# - 利用"不存在重叠工件"和"工件最多覆盖 4 格"的保证，避免了对整个 n*n 网格的存储。
# - 使用 set of tuple 进行 O(1) 查找，而非构建 n*n 的二维数组（n 最大 1000，n^2 可达 10^6）。
