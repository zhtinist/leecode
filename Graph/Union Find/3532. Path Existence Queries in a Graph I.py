"""
LeetCode #3532 - Path Existence Queries in a Graph I
针对图的路径存在性查询 I
https://leetcode.cn/problems/path-existence-queries-in-a-graph-i/

给你一个整数 `n`，表示图中的节点数量，这些节点按从 `0` 到 `n - 1` 编号。
同时给你一个长度为 `n` 的整数数组 `nums`，该数组按 非递减 顺序排序，以及一个整数 `maxDiff`。
如果满足 `|nums[i] - nums[j]| <= maxDiff`（即 `nums[i]` 和 `nums[j]` 的 绝对差 至多为 `maxDiff`），则节点 `i` 和节点 `j` 之间存在一条 无向边 。
此外，给你一个二维整数数组 `queries`。对于每个 `queries[i] = [u_i, v_i]`，需要判断节点 `u_i` 和 `v_i` 之间是否存在路径。
返回一个布尔数组 `answer`，其中 `answer[i]` 等于 `true` 表示在第 `i` 个查询中节点 `u_i` 和 `v_i` 之间存在路径，否则为 `false`。

示例 1：

输入: n = 2, nums = [1,3], maxDiff = 1, queries = [[0,0],[0,1]]
输出: [true,false]
解释:
查询 `[0,0]`：节点 0 有一条到自己的显然路径。
查询 `[0,1]`：节点 0 和节点 1 之间没有边，因为 `|nums[0] - nums[1]| = |1 - 3| = 2`，大于 `maxDiff`。
因此，在处理完所有查询后，最终答案为 `[true, false]`。
示例 2：

输入: n = 4, nums = [2,5,6,8], maxDiff = 2, queries = [[0,1],[0,2],[1,3],[2,3]]
输出: [false,false,true,true]
解释:
生成的图如下：

查询 `[0,1]`：节点 0 和节点 1 之间没有边，因为 `|nums[0] - nums[1]| = |2 - 5| = 3`，大于 `maxDiff`。
查询 `[0,2]`：节点 0 和节点 2 之间没有边，因为 `|nums[0] - nums[2]| = |2 - 6| = 4`，大于 `maxDiff`。
查询 `[1,3]`：节点 1 和节点 3 之间存在路径通过节点 2，因为 `|nums[1] - nums[2]| = |5 - 6| = 1` 和 `|nums[2] - nums[3]| = |6 - 8| = 2`，都小于等于 `maxDiff`。
查询 `[2,3]`：节点 2 和节点 3 之间有一条边，因为 `|nums[2] - nums[3]| = |6 - 8| = 2`，等于 `maxDiff`。
因此，在处理完所有查询后，最终答案为 `[false, false, true, true]`。

提示：
`1 <= n == nums.length <= 10^5`
`0 <= nums[i] <= 10^5`
`nums` 按 非递减 顺序排序。
`0 <= maxDiff <= 10^5`
`1 <= queries.length <= 10^5`
`queries[i] == [u_i, v_i]`
`0 <= u_i, v_i < n`
"""

from typing import List, Optional


class Solution:
    def areConnected(self, n: int, nums: List[int], maxDiff: int,
                     queries: List[List[int]]) -> List[bool]:
        # Assign component IDs based on adjacent differences
        comp = [0] * n
        comp_id = 0
        comp[0] = 0
        for i in range(1, n):
            if nums[i] - nums[i - 1] > maxDiff:
                comp_id += 1
            comp[i] = comp_id

        return [comp[u] == comp[v] for u, v in queries]



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Union Find, Graph, Array, Hash Table, Binary Search
#
# 解题思路:
# 1. nums 已按非递减排序，边存在当 |nums[i]-nums[j]| <= maxDiff
# 2. 关键性质：由于数组有序，若相邻差值 > maxDiff，则左右两侧不可能连通
#    - 因为对任意 i < k < j，若 nums[i] 和 nums[j] 相差 <= maxDiff，
#      则 nums[i] 和所有中间元素也都相差 <= maxDiff
#    - 反之，若某相邻对差值 > maxDiff，则形成分割点
# 3. 因此连通分量就是相邻差值 <= maxDiff 的连续段
# 4. 给每个节点分配连通分量 ID，查询时比较 ID 是否相同
#
# 时间复杂度: O(n + q)
# 空间复杂度: O(n)
#
# 关键点:
# - 排序数组 + 差值限制 → 连通分量必然是连续区间
# - 相邻差值 > maxDiff 是分量的边界
