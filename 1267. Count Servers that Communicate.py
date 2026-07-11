"""
LeetCode #1267 - Count Servers that Communicate
中文题名：统计参与通信的服务器
https://leetcode.com/problems/count-servers-that-communicate/

You are given a map of a server center, represented as a `m * n` integer
matrix `grid`, where 1 means that on that cell there is a server and 0
means that it is no server. Two servers are said to communicate if they are on the same
row or on the same column.

Return the number of servers that communicate with any other server.

Example 1:

Input: grid = [[1,0],[0,1]]
Output: 0
Explanation: No servers can communicate with others.

Example 2:

Input: grid = [[1,0],[1,1]]
Output: 3
Explanation: All three servers can communicate with at least one other server.

Example 3:

Input: grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
Output: 4
Explanation: The two servers in the first row can communicate with each other. The two servers in the third column can communicate with each other. The server at right bottom corner can't communicate with any other server.

Constraints:

`m == grid.length`

`n == grid[i].length`

`1 <= m <= 250`

`1 <= n <= 250`

`grid[i][j] == 0 or 1`

【中文翻译】
给你一个服务器中心的分布图，表示为一个 `m * n` 的整数矩阵 `grid`，其中 1 表示该单元格有一台服务器，0 表示没有。如果两台服务器位于同一行或同一列，则认为它们可以互相通信。

请统计并返回能够与至少一台其他服务器通信的服务器的数量。

示例 1：

输入：grid = [[1,0],[0,1]]
输出：0
解释：没有服务器可以与其他服务器通信。

示例 2：

输入：grid = [[1,0],[1,1]]
输出：3
解释：所有三台服务器都可以与至少一台其他服务器通信。

示例 3：

输入：grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
输出：4
解释：第一行的两台服务器可以互相通信。第三列的两台服务器可以互相通信。右下角的服务器无法与其他任何服务器通信。

约束条件：

`m == grid.length`

`n == grid[i].length`

`1 <= m <= 250`

`1 <= n <= 250`

`grid[i][j] == 0 或 1`
"""

from typing import List, Optional


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        row_count = [0] * m
        col_count = [0] * n

        # First pass: count servers in each row and column
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    row_count[i] += 1
                    col_count[j] += 1

        # Second pass: count servers that can communicate
        result = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (row_count[i] > 1 or col_count[j] > 1):
                    result += 1

        return result










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 两次遍历法。
# 1. 第一次遍历：统计每行和每列的服务器总数。
#    - row_count[i] 表示第 i 行有多少台服务器。
#    - col_count[j] 表示第 j 列有多少台服务器。
# 2. 第二次遍历：对于每台服务器 (grid[i][j] == 1)：
#    - 如果 row_count[i] > 1（该行至少有 2 台服务器）或 col_count[j] > 1（该列至少有 2 台服务器），
#      说明这台服务器至少能与同一行或同一列的某台服务器通信，计数 +1。
# 3. 返回最终计数。
# 这种方法的正确性：一台服务器能通信当且仅当它所在行或所在列还有其他服务器。
# 因此只需检查行计数或列计数是否大于 1。
#
# 时间复杂度: O(M * N)，两次遍历
# 空间复杂度: O(M + N)，行计数和列计数数组
#
# 关键点:
# - 不需要显式连接服务器，只需判断该行/列是否有 >1 台服务器
# - 两次遍历：第一次统计，第二次判断
# - 条件 row_count[i] > 1 or col_count[j] > 1 精确刻画了"能通信"
# - 时间复杂度 O(M*N) 对于 M,N <= 250 完全可行（最多 62500 个单元格）
