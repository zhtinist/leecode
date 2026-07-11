"""
LeetCode #3160 - Find the Number of Distinct Colors Among the Balls
所有球里面不同颜色的数目
https://leetcode.cn/problems/find-the-number-of-distinct-colors-among-the-balls/

给你一个整数 `limit` 和一个大小为 `n x 2` 的二维数组 `queries` 。
总共有 `limit + 1` 个球，每个球的编号为 `[0, limit]` 中一个 互不相同 的数字。一开始，所有球都没有颜色。`queries` 中每次操作的格式为 `[x, y]` ，你需要将球 `x` 染上颜色 `y` 。每次操作之后，你需要求出所有球颜色的数目。
请你返回一个长度为 `n` 的数组 `result` ，其中 `result[i]` 是第 `i` 次操作以后颜色的数目。
注意 ，没有染色的球不算作一种颜色。

示例 1：

输入：limit = 4, queries = [[1,4],[2,5],[1,3],[3,4]]
输出：[1,2,2,3]
解释：

操作 0 后，球 1 颜色为 4 。
操作 1 后，球 1 颜色为 4 ，球 2 颜色为 5 。
操作 2 后，球 1 颜色为 3 ，球 2 颜色为 5 。
操作 3 后，球 1 颜色为 3 ，球 2 颜色为 5 ，球 3 颜色为 4 。
示例 2：

输入：limit = 4, queries = [[0,1],[1,2],[2,2],[3,4],[4,5]]
输出：[1,2,2,3,4]
解释：

操作 0 后，球 0 颜色为 1 。
操作 1 后，球 0 颜色为 1 ，球 1 颜色为 2 。
操作 2 后，球 0 颜色为 1 ，球 1 和 2 颜色为 2 。
操作 3 后，球 0 颜色为 1 ，球 1 和 2 颜色为 2 ，球 3 颜色为 4 。
操作 4 后，球 0 颜色为 1 ，球 1 和 2 颜色为 2 ，球 3 颜色为 4 ，球 4 颜色为 5 。

提示：
`1 <= limit <= 10^9`
`1 <= n == queries.length <= 10^5`
`queries[i].length == 2`
`0 <= queries[i][0] <= limit`
`1 <= queries[i][1] <= 10^9`
"""

from typing import List, Optional


class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ball_color = {}    # 球 -> 颜色
        color_cnt = {}     # 颜色 -> 出现次数
        ans = []

        for x, y in queries:
            if x in ball_color:
                old = ball_color[x]
                color_cnt[old] -= 1
                if color_cnt[old] == 0:
                    del color_cnt[old]

            ball_color[x] = y
            color_cnt[y] = color_cnt.get(y, 0) + 1
            ans.append(len(color_cnt))

        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Hash Table, Simulation
#
# 解题思路:
# 使用两个哈希表：ball_color记录每个球的当前颜色，color_cnt记录每种颜色的球的数量。
# 每次操作：若该球之前有颜色，将旧颜色的计数减1（归零则删除）；
# 赋予新颜色并更新计数。不同颜色数量即为color_cnt的大小。
# limit可能很大（10^9），但只有O(n)个球会被染色，所以用哈希表。
#
# 时间复杂度: O(n)
# 空间复杂度: O(n)
#
# 关键点:
# - 只记录被染色的球，不需要为所有球分配空间
# - 颜色计数归零时删除，len(color_cnt)即为颜色种数
# - 球换颜色时先删除旧颜色的记录再添加新颜色
