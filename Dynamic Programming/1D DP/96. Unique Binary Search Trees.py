"""
LeetCode #96 - Unique Binary Search Trees
https://leetcode.com/problems/unique-binary-search-trees/

Given an integer n, return the number of structurally unique BST's (binary search
trees) which has exactly n nodes of unique values from 1 to n.

Example 1:
    Input: n = 3
    Output: 5

Example 2:
    Input: n = 1
    Output: 1

Constraints:
    1 <= n <= 19
"""


class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1

        for nodes in range(1, n + 1):
            for root in range(1, nodes + 1):
                dp[nodes] += dp[root - 1] * dp[nodes - root]

        return dp[n]
