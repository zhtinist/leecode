"""
LeetCode #2768 - Number of Black Blocks
黑格子的数目
https://leetcode.cn/problems/number-of-black-blocks/

给你两个整数 `m` 和 `n` ，表示一个下标从 0 开始的 `m x n` 的网格图。
给你一个下标从 0 开始的二维整数矩阵 `coordinates` ，其中 `coordinates[i] = [x, y]` 表示坐标为 `[x, y]` 的格子是 黑色的 ，所有没出现在 `coordinates` 中的格子都是 白色的。
一个块定义为网格图中 `2 x 2` 的一个子矩阵。更正式的，对于左上角格子为 `[x, y]` 的块，其中 `0 <= x < m - 1` 且 `0 <= y < n - 1` ，包含坐标为 `[x, y]` ，`[x + 1, y]` ，`[x, y + 1]` 和 `[x + 1, y + 1]` 的格子。
请你返回一个下标从 0 开始长度为 `5` 的整数数组 `arr` ，`arr[i]` 表示恰好包含 `i` 个 黑色 格子的块的数目。

示例 1：
输入：m = 3, n = 3, coordinates = [[0,0]] 输出：[3,1,0,0,0] 解释：网格图如下：  只有 1 个块有一个黑色格子，这个块是左上角为 [0,0] 的块。 其他 3 个左上角分别为 [0,1] ，[1,0] 和 [1,1] 的块都有 0 个黑格子。 所以我们返回 [3,1,0,0,0] 。
示例 2：
输入：m = 3, n = 3, coordinates = [[0,0],[1,1],[0,2]] 输出：[0,2,2,0,0] 解释：网格图如下：  有 2 个块有 2 个黑色格子（左上角格子分别为 [0,0] 和 [0,1]）。 左上角为 [1,0] 和 [1,1] 的两个块，都有 1 个黑格子。 所以我们返回 [0,2,2,0,0] 。

提示：
`2 <= m <= 10^5`
`2 <= n <= 10^5`
`0 <= coordinates.length <= 10^4`
`coordinates[i].length == 2`
`0 <= coordinates[i][0] < m`
`0 <= coordinates[i][1] < n`
`coordinates` 中的坐标对两两互不相同。
"""

from typing import List, Optional


class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        from collections import Counter
        cnt = Counter()
        total_blocks = (m - 1) * (n - 1)

        for x, y in coordinates:
            for dx in range(-1, 1):
                for dy in range(-1, 1):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m - 1 and 0 <= ny < n - 1:
                        cnt[(nx, ny)] += 1

        ans = [0] * 5
        for b in cnt.values():
            ans[b] += 1
        ans[0] = total_blocks - sum(ans[1:])
        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Hash Table, Enumeration
#
# 解题思路:
# 每个黑格子会影响以其为右下角、右上角、左下角、左上角的 4 个 2x2 块。
# 遍历所有黑格子，对每个 2x2 块（以左上角坐标标识）计数包含的黑格数。
# 使用 Counter 统计每个块的黑格数量，然后汇总到 ans[0]~ans[4]。
# 注意总块数 = (m-1)*(n-1)，未出现在 Counter 中的块黑格数为 0。
#
# 时间复杂度: O(k) 其中 k = len(coordinates)，每个黑格子只影响 4 个块
# 空间复杂度: O(k) Counter 最多存储 4k 个块的键
#
# 关键点:
# - 逆向思维：从黑格子出发找受影响的 2x2 块，而不是遍历所有可能的块
# - 每个黑格子 (x,y) 可以是 (x-1,y-1), (x-1,y), (x,y-1), (x,y) 这 4 个块的成员
# - 总块数减去有黑格的块数得到 0 黑格的块数
