"""
LeetCode #1035 - Uncrossed Lines
中文题名：不相交的线
https://leetcode.com/problems/uncrossed-lines/

We write the integers of `A` and `B` (in the order they are given)
on two separate horizontal lines.

Now, we may draw connecting lines: a straight line connecting two numbers
`A[i]` and `B[j]` such that:

`A[i] == B[j]`;

The line we draw does not intersect any other connecting (non-horizontal) line.

Note that a connecting lines cannot intersect even at the endpoints: each number can
only belong to one connecting line.

Return the maximum number of connecting lines we can draw in this way.

Example 1:

Input: A = [1,4,2], B = [1,2,4]
Output: 2
Explanation: We can draw 2 uncrossed lines as in the diagram.
We cannot draw 3 uncrossed lines, because the line from A[1]=4 to B[2]=4 will intersect the line from A[2]=2 to B[1]=2.

Example 2:

Input: A = [2,5,1,2,5], B = [10,5,2,1,5,2]
Output: 3

Example 3:

Input: A = [1,3,7,1,7,5], B = [1,9,2,5,1]
Output: 2

【中文翻译】
我们在两条独立的水平线上按给定的顺序写下整数数组 A 和 B。

现在，我们可以绘制一些连接线：一条直线连接两个数字 A[i] 和 B[j]，满足：

A[i] == B[j]；
我们绘制的线不会与任何其他连接（非水平）线相交。

请注意，连接线即使在端点处也不能相交：每个数字只能属于一条连接线。

返回以这种方式可以绘制的最大连接线数。

示例 1：

输入：A = [1,4,2], B = [1,2,4]
输出：2
解释：我们可以按照图示绘制 2 条不相交的线。
无法绘制 3 条不相交的线，因为从 A[1]=4 到 B[2]=4 的线将与从 A[2]=2 到 B[1]=2 的线相交。

示例 2：

输入：A = [2,5,1,2,5], B = [10,5,2,1,5,2]
输出：3

示例 3：

输入：A = [1,3,7,1,7,5], B = [1,9,2,5,1]
输出：2
"""

from typing import List, Optional


class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[m][n]










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 这道题本质上是最长公共子序列(LCS)问题。要绘制不相交的连线，连接的数字对必须
# 在A和B中保持相同的相对顺序。即如果连接了 A[i]-B[j] 和 A[p]-B[q]，且 i < p，
# 则必须有 j < q，否则连线会相交。这正好就是LCS的定义。
# 使用二维DP：dp[i][j] 表示 A[0..i-1] 和 B[0..j-1] 的最长公共子序列长度。
# 如果 A[i-1] == B[j-1]，则 dp[i][j] = dp[i-1][j-1] + 1
# 否则 dp[i][j] = max(dp[i-1][j], dp[i][j-1])
#
# 时间复杂度: O(M * N) - M和N分别为两个数组的长度
# 空间复杂度: O(M * N) - DP表格，可以优化到O(min(M,N))
#
# 关键点:
# - 识别出问题本质是LCS
# - 不相交的条件 => 连线对应的索引必须同时递增
# - 标准LCS DP递推公式
