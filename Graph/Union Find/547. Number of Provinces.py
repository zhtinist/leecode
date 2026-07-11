"""
LeetCode #547 - Number of Provinces
中文题名：省份数量
https://leetcode.com/problems/number-of-provinces/

There are N students in a class. Some of them are friends, while some are not. Their
friendship is transitive in nature. For example, if A is a direct friend of B, and B
is a direct friend of C, then A is an indirect friend of C. And we defined a
friend circle is a group of students who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in
the class. If M[i][j] = 1, then the ith and jth students are
direct friends with each other, otherwise not. And you have to output the total
number of friend circles among all the students.

Example 1:

Input:
[[1,1,0],
[1,1,0],
[0,0,1]]
Output: 2
Explanation:The 0th and 1st students are direct friends, so they are in a friend circle.
The 2nd student himself is in a friend circle. So return 2.

Example 2:

Input:
[[1,1,0],
[1,1,1],
[0,1,1]]
Output: 1
Explanation:The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends,
so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.

Note:

N is in range [1,200].

M[i][i] = 1 for all students.

If M[i][j] = 1, then M[j][i] = 1.

【中文翻译】
班上有 N 名学生。其中有些人是朋友，有些则不是。他们的友谊具有传递性。例如，如果 A 是 B 的直
接朋友，且 B 是 C 的直接朋友，那么 A 是 C 的间接朋友。我们定义朋友圈是一群直接或间接朋友的
集合。

给定一个 N×N 的矩阵 M 表示班级中学生之间的朋友关系。如果 M[i][j] = 1，表示第 i 个和第 j 个
学生互为直接朋友，否则不是。你需要输出所有学生中的朋友圈总数。

示例 1：
    输入：
    [[1,1,0],
     [1,1,0],
     [0,0,1]]
    输出：2
    解释：第 0 个和第 1 个学生是直接朋友，所以他们在一个朋友圈中。
    第 2 个学生自己在另一个朋友圈中。所以返回 2。

示例 2：
    输入：
    [[1,1,0],
     [1,1,1],
     [0,1,1]]
    输出：1
    解释：第 0 个和第 1 个学生是直接朋友，第 1 个和第 2 个学生是直接朋友，
    所以第 0 个和第 2 个学生是间接朋友。所有人都在同一个朋友圈中，所以返回 1。

注意：
    N 的范围是 [1, 200]。
    M[i][i] = 1 对所有学生成立。
    如果 M[i][j] = 1，则 M[j][i] = 1。
"""

from typing import List, Optional


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n
        count = 0

        def dfs(i: int) -> None:
            for j in range(n):
                if isConnected[i][j] == 1 and not visited[j]:
                    visited[j] = True
                    dfs(j)

        for i in range(n):
            if not visited[i]:
                count += 1
                visited[i] = True
                dfs(i)

        return count



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用 DFS 遍历朋友圈（连通分量）。用一个 visited 数组标记已访问的学生。
# 遍历每个学生，若未访问则计数 +1，然后 DFS 标记其所有直接和间接朋友为已访问。
# 本质上是在邻接矩阵上统计连通分量数，与岛屿数量问题思路一致。
#
# 时间复杂度: O(N^2) — 邻接矩阵中的每个元素最多被访问一次
# 空间复杂度: O(N) — visited 数组和递归栈深度
#
# 关键点:
# - 将问题转化为在无向图的邻接矩阵上统计连通分量数
# - 可使用 DFS / BFS / 并查集三种方法
# - visited 数组确保每人只被处理一次，避免重复计数
