"""
LeetCode #3531 - Count Covered Buildings
统计被覆盖的建筑
https://leetcode.cn/problems/count-covered-buildings/

给你一个正整数 `n`，表示一个 `n x n` 的城市，同时给定一个二维数组 `buildings`，其中 `buildings[i] = [x, y]` 表示位于坐标 `[x, y]` 的一个 唯一 建筑。
如果一个建筑在四个方向（左、右、上、下）中每个方向上都至少存在一个建筑，则称该建筑 被覆盖 。
返回 被覆盖 的建筑数量。

示例 1：

输入: n = 3, buildings = [[1,2],[2,2],[3,2],[2,1],[2,3]]
输出: 1
解释:
只有建筑 `[2,2]` 被覆盖，因为它在每个方向上都至少存在一个建筑：
上方 (`[1,2]`)
下方 (`[3,2]`)
左方 (`[2,1]`)
右方 (`[2,3]`)
因此，被覆盖的建筑数量是 1。
示例 2：

输入: n = 3, buildings = [[1,1],[1,2],[2,1],[2,2]]
输出: 0
解释:
没有任何一个建筑在每个方向上都有至少一个建筑。
示例 3：

输入: n = 5, buildings = [[1,3],[3,2],[3,3],[3,5],[5,3]]
输出: 1
解释:
只有建筑 `[3,3]` 被覆盖，因为它在每个方向上至少存在一个建筑：
上方 (`[1,3]`)
下方 (`[5,3]`)
左方 (`[3,2]`)
右方 (`[3,5]`)
因此，被覆盖的建筑数量是 1。

提示：
`2 <= n <= 10^5`
`1 <= buildings.length <= 10^5`
`buildings[i] = [x, y]`
`1 <= x, y <= n`
`buildings` 中所有坐标均 唯一 。
"""

from typing import List, Optional


class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        from collections import defaultdict

        # Group by x: min_y, max_y for each x
        x_group = defaultdict(list)
        for x, y in buildings:
            x_group[x].append(y)

        y_covered = {}  # (x, y) -> bool
        for x, ys in x_group.items():
            min_y = min(ys)
            max_y = max(ys)
            for y in ys:
                if min_y < y < max_y:
                    y_covered[(x, y)] = True

        # Group by y: min_x, max_x for each y
        y_group = defaultdict(list)
        for x, y in buildings:
            if (x, y) in y_covered:  # only check those already covered in y-dir
                y_group[y].append(x)

        ans = 0
        for y, xs in y_group.items():
            min_x = min(xs)
            max_x = max(xs)
            for x in xs:
                if min_x < x < max_x:
                    ans += 1

        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Hash Table, Sorting
#
# 解题思路:
# 1. 一个建筑被覆盖 = 四个方向都有其他建筑
#    - 上下：同列 x 有其他建筑在它上面和下面 → min_y < y < max_y
#    - 左右：同行 y 有其他建筑在它左边和右边 → min_x < x < max_x
# 2. 按 x 坐标分组，对每组找 y 的 min/max，标记满足 y 方向覆盖的建筑
# 3. 对 y 方向覆盖的建筑按 y 坐标分组，找 x 的 min/max
# 4. 同时满足两个条件的计入答案
#
# 时间复杂度: O(N)
# 空间复杂度: O(N)
#
# 关键点:
# - 建筑坐标唯一，直接分组统计极值即可
# - 先过滤 y 方向再检查 x 方向可减少计算量
