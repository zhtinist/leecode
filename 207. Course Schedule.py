"""
LeetCode #207 - Course Schedule
https://leetcode.com/problems/course-schedule/

There are a total of *n* courses you have to take, labeled from `0` to `n-1`.

Some courses may have prerequisites, for example to take course 0 you have to first take
course 1, which is expressed as a pair: `[0,1]`

Given the total number of courses and a list of prerequisite pairs, is it possible for
you to finish all courses?

Example 1:

Input: 2, [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0. So it is possible.

Example 2:

Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0, and to take course 0 you should
also have finished course 1. So it is impossible.

Note:

The input prerequisites is a graph represented by a list of edges, not adjacency
matrices. Read more about how a graph is represented.

You may assume that there are no duplicate edges in the input prerequisites.
"""

from typing import List, Optional


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import deque

        # Build adjacency list and indegree array
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1

        # BFS: start with courses that have no prerequisites
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        taken = 0

        while queue:
            curr = queue.popleft()
            taken += 1
            for neighbor in graph[curr]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return taken == numCourses


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 拓扑排序（Kahn's Algorithm / BFS）。问题等价于判断有向图是否存在环。
# 如果存在拓扑排序（所有课程都能被完成），说明无环。
#
# 步骤：
# 1. 构建邻接表和入度数组：prereq -> course（先修课指向后修课）
# 2. 将所有入度为 0 的节点（无先修课要求）加入 BFS 队列
# 3. BFS 取出节点时"完成"该课程（taken++），并将其所有后继节点的入度减 1
# 4. 如果后继节点入度变为 0，加入队列
# 5. 最后检查 taken == numCourses，相等说明无环（能完成所有课程）
#
# 时间复杂度: O(V + E) — 构建图 + BFS
# 空间复杂度: O(V + E) — 邻接表和入度数组
#
# 关键点:
# - 拓扑排序是判断 DAG（有向无环图）的标准方法
# - [course, prereq] 表示 course 依赖 prereq，所以边是 prereq -> course
# - 也可用 DFS 三色法检测环
