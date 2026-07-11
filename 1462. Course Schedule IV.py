"""
LeetCode #1462 - Course Schedule IV
中文题名：课程表 IV
https://leetcode.com/problems/course-schedule-iv/

There are a total of `n` courses you have to take, labeled from
`0` to `n-1`.

Some courses may have direct prerequisites, for example, to take course 0 you have
first to take course 1, which is expressed as a pair: `[1,0]`

Given the total number of courses `n`, a list of direct `prerequisite`
pairs and a list of `queries` pairs.

You should answer for each `queries[i]` whether the course `queries[i][0]`
is a prerequisite of the course `queries[i][1]` or not.

Return a list of boolean, the answers to the given `queries`.

Please note that if course a is a prerequisite of course
b and course b is a prerequisite of course
c, then, course a is a prerequisite of course
c.

Example 1:

Input: n = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]]
Output: [false,true]
Explanation: course 0 is not a prerequisite of course 1 but the opposite is true.

Example 2:

Input: n = 2, prerequisites = [], queries = [[1,0],[0,1]]
Output: [false,false]
Explanation: There are no prerequisites and each course is independent.

Example 3:

Input: n = 3, prerequisites = [[1,2],[1,0],[2,0]], queries = [[1,0],[1,2]]
Output: [true,true]

Example 4:

Input: n = 3, prerequisites = [[1,0],[2,0]], queries = [[0,1],[2,0]]
Output: [false,true]

Example 5:

Input: n = 5, prerequisites = [[0,1],[1,2],[2,3],[3,4]], queries = [[0,4],[4,0],[1,3],[3,0]]
Output: [true,false,true,false]

Constraints:

`2 <= n <= 100`

`0 <= prerequisite.length <= (n * (n - 1) / 2)`

`0 <= prerequisite[i][0], prerequisite[i][1] < n`

`prerequisite[i][0] != prerequisite[i][1]`

The prerequisites graph has no cycles.

The prerequisites graph has no repeated edges.

`1 <= queries.length <= 10^4`

`queries[i][0] != queries[i][1]`

【中文翻译】
总共有 `n` 门课程你需要修读，编号从 `0` 到 `n-1`。

某些课程可能有直接先修要求，例如，要修读课程 0，你必须先修读课程 1，
这表示为一对：`[1,0]`

给定课程总数 `n`、直接 `prerequisite` 先修关系对列表和一个 `queries` 查询对列表。

你需要对每个 `queries[i]` 回答课程 `queries[i][0]` 是否是课程 `queries[i][1]` 的先修课程。

返回一个布尔值列表，作为给定 `queries` 的答案。

请注意，如果课程 a 是课程 b 的先修课程，课程 b 是课程 c 的先修课程，
那么课程 a 也是课程 c 的先修课程。

示例 1：

输入：n = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]]
输出：[false,true]
解释：课程 0 不是课程 1 的先修课程，但反过来是。

示例 2：

输入：n = 2, prerequisites = [], queries = [[1,0],[0,1]]
输出：[false,false]
解释：没有先修关系，每门课程都是独立的。

示例 3：

输入：n = 3, prerequisites = [[1,2],[1,0],[2,0]], queries = [[1,0],[1,2]]
输出：[true,true]

示例 4：

输入：n = 3, prerequisites = [[1,0],[2,0]], queries = [[0,1],[2,0]]
输出：[false,true]

示例 5：

输入：n = 5, prerequisites = [[0,1],[1,2],[2,3],[3,4]], queries = [[0,4],[4,0],[1,3],[3,0]]
输出：[true,false,true,false]

约束条件：

`2 <= n <= 100`

`0 <= prerequisite.length <= (n * (n - 1) / 2)`

`0 <= prerequisite[i][0], prerequisite[i][1] < n`

`prerequisite[i][0] != prerequisite[i][1]`

先修关系图没有环。

先修关系图没有重复边。

`1 <= queries.length <= 10^4`

`queries[i][0] != queries[i][1]`
"""

from typing import List, Optional


class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        reachable = [[False] * n for _ in range(n)]
        for u, v in prerequisites:
            reachable[u][v] = True

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if reachable[i][k] and reachable[k][j]:
                        reachable[i][j] = True

        return [reachable[u][v] for u, v in queries]



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用 Floyd-Warshall 算法计算传递闭包（transitive closure）。
# 创建 n×n 的布尔矩阵 reachable，其中 reachable[u][v] 表示课程 u 是否是课程 v 的先修课程。
# 初始化：对于每条直接先修关系 [u, v]，设置 reachable[u][v] = True。
# 然后进行三层循环：对于每个中间节点 k，如果 reachable[i][k] 且 reachable[k][j]，
# 则 reachable[i][j] = True（传递性）。
# 最后对每个查询直接返回 reachable[u][v] 的值。
#
# 时间复杂度: O(N^3)  -- Floyd-Warshall 三层循环
# 空间复杂度: O(N^2)  -- 布尔矩阵存储所有节点对的先修关系
#
# 关键点:
# - 先修关系具有传递性：a 是 b 的先修，b 是 c 的先修，则 a 是 c 的先修
# - Floyd-Warshall 可以一次性计算所有节点对的可达性
# - 也可用 BFS/DFS 从每个节点出发，复杂度 O(N * (N+E))，对于 N <= 100 两者都可行









