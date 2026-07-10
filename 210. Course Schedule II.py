"""
LeetCode #210 - Course Schedule II
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
