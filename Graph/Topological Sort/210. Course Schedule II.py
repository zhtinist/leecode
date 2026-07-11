"""
LeetCode #210 - Course Schedule II
中文题名：课程表 II
https://leetcode.com/problems/course-schedule-ii/

There are a total of *n* courses you have to take, labeled from `0` to
`n-1`.

Some courses may have prerequisites, for example to take course 0 you have to first take
course 1, which is expressed as a pair: `[0,1]`

Given the total number of courses and a list of prerequisite pairs, return
the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is
impossible to finish all courses, return an empty array.

Example 1:

Input: 2, [[1,0]]
Output: `[0,1]`
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished
course 0. So the correct course order is `[0,1] .`

Example 2:

Input: 4, [[1,0],[2,0],[3,1],[3,2]]
Output: `[0,1,2,3] or [0,2,1,3]`
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both
courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is `[0,1,2,3]`. Another correct ordering is `[0,2,1,3] .`

Note:

The input prerequisites is a graph represented by a list of edges, not
adjacency matrices. Read more about how a graph is represented.

You may assume that there are no duplicate edges in the input prerequisites.

【中文翻译】
现在你总共有 *n* 门课需要选，记为 `0` 到 `n-1`。

在选修某些课程之前需要一些先修课程。例如，想要学习课程 0，你需要先完成课程 1，我们用一个匹配来表示：[0,1]

给定课程总量以及它们之间的先修关系，返回你为了完成所有课程所安排的学习顺序。

可能会有多个正确的顺序，你只需要返回其中一种即可。如果不可能完成所有课程，返回一个空数组。

示例 1：

输入：2, [[1,0]]
输出：`[0,1]`
解释：共有 2 门课程。学习课程 1 之前，你需要完成课程 0。所以正确的课程顺序为 `[0,1]`。

示例 2：

输入：4, [[1,0],[2,0],[3,1],[3,2]]
输出：`[0,1,2,3]` 或 `[0,2,1,3]`
解释：共有 4 门课程。学习课程 3 之前，你需要完成课程 1 和课程 2。课程 1 和课程 2 都应该在完成课程 0 之后学习。所以一个正确的课程顺序是 `[0,1,2,3]`。另一个正确的排序是 `[0,2,1,3]`。

注意：

输入的先修关系是用边列表表示的图，而不是邻接矩阵。请阅读更多关于图如何表示的内容。

你可以假设输入的先修关系中没有重复的边。
"""

from typing import List, Optional


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Build adjacency list and indegree array
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for dst, src in prerequisites:
            graph[src].append(dst)
            indegree[dst] += 1

        # Start with courses that have no prerequisites
        queue = [i for i in range(numCourses) if indegree[i] == 0]
        order = []
        idx = 0

        while idx < len(queue):
            course = queue[idx]
            idx += 1
            order.append(course)
            for neighbor in graph[course]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return order if len(order) == numCourses else []


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用拓扑排序（Kahn 算法 / BFS）来解决课程安排问题。
# 1. 构建邻接表 graph 和入度数组 indegree。
# 2. 将所有入度为 0 的课程加入队列（没有先修课程的课可以直接上）。
# 3. 每次从队列中取出一个课程加入结果顺序，将其所有后续课程的入度减 1。
# 4. 如果某后续课程入度变为 0，加入队列。
# 5. 最后检查结果长度是否等于总课程数：如果相等则返回顺序，否则说明存在环，返回空数组。
#
# 时间复杂度: O(V + E)，V 为课程数，E 为先修关系数
# 空间复杂度: O(V + E)，用于存储邻接表和入度数组
#
# 关键点:
# - 入度为 0 表示该课程没有未完成的先修课，可以立即学习
# - 若最终结果长度不等于 numCourses，说明图中存在环，无法完成所有课程
# - 使用列表 + 索引指针代替 deque，避免额外 import
