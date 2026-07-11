"""
LeetCode #2672 - Number of Adjacent Elements With the Same Color
有相同颜色的相邻元素数目
https://leetcode.cn/problems/number-of-adjacent-elements-with-the-same-color/

给定一个整数 `n` 表示一个长度为 `n` 的数组  `colors`，初始所有元素均为 0 ，表示是 未染色 的。同时给定一个二维整数数组 `queries`，其中 `queries[i] = [index_i, color_i]`。对于第 `i` 个 查询：
将 `colors[index_i]` 染色为 `color_i`。
统计 `colors` 中颜色相同的相邻对的数量（无论 `color_i`）。
请你返回一个长度与 `queries` 相等的数组 `answer` ，其中 `answer[i]`是前 `i` 个操作的答案。

示例 1：

输入：n = 4, queries = [[0,2],[1,2],[3,1],[1,1],[2,1]]
输出：[0,1,1,0,2]
解释：
一开始 colors = [0,0,0,0]，其中 0 表示数组中未染色的元素。
在第 1 次查询后 colors = [2,0,0,0]。颜色相同的相邻对的数量是 0。
在第 2 次查询后 colors = [2,2,0,0]。颜色相同的相邻对的数量是 1。
在第 3 次查询后 colors = [2,2,0,1]。颜色相同的相邻对的数量是 1。
在第 4 次查询后 colors = [2,1,0,1]。颜色相同的相邻对的数量是 0。
在第 5 次查询后 colors = [2,1,1,1]。颜色相同的相邻对的数量是 2。
示例 2：

输入：n = 1, queries = [[0,100000]]
输出：[0]
解释：
在第一次查询后 colors = [100000]。颜色相同的相邻对的数量是 0。

提示：
`1 <= n <= 10^5`
`1 <= queries.length <= 10^5`
`queries[i].length == 2`
`0 <= index_i <= n - 1`
`1 <=  color_i <= 10^5`
"""

from typing import List, Optional


class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        colors = [0] * n
        ans = []
        cur = 0  # current number of adjacent same-color pairs

        for idx, color in queries:
            # remove old adjacent pairs involving idx
            if colors[idx] != 0:
                if idx > 0 and colors[idx - 1] == colors[idx]:
                    cur -= 1
                if idx < n - 1 and colors[idx + 1] == colors[idx]:
                    cur -= 1

            # set new color
            colors[idx] = color

            # add new adjacent pairs involving idx
            if idx > 0 and colors[idx - 1] == color:
                cur += 1
            if idx < n - 1 and colors[idx + 1] == color:
                cur += 1

            ans.append(cur)

        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array
#
# 解题思路:
# 维护当前数组中相同颜色相邻对的总数cur。每次查询只修改一个位置：
# 先移除该位置与左右邻居旧的配对贡献（如果之前有色），再设置新颜色，
# 然后添加新的配对贡献。这样可以O(1)处理每个查询，避免每次重新扫描数组。
#
# 时间复杂度: O(q) 其中q是查询数量
# 空间复杂度: O(n)
#
# 关键点:
# - 增量更新：只更新受影响的相邻对，不重新计算全局
# - 初始0表示未染色，不计入配对
# - 先减后加，确保同一位置重复染色时正确
