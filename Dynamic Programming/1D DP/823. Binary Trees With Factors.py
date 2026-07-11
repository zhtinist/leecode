"""
LeetCode #823 - Binary Trees With Factors
中文题名：带因子的二叉树
https://leetcode.com/problems/binary-trees-with-factors/

Given an array of unique integers, each integer is strictly greater than 1.

We make a binary tree using these integers and each number may be used for any number of
times.

Each non-leaf node's value should be equal to the product of the values of it's
children.

How many binary trees can we make?  Return the answer modulo 10 ** 9 +
7.

Example 1:

Input: `A = [2, 4]`
Output: 3
Explanation: We can make these trees: `[2], [4], [4, 2, 2]`

Example 2:

Input: `A = [2, 4, 5, 10]`
Output: `7`
Explanation: We can make these trees: `[2], [4], [5], [10], [4, 2, 2], [10, 2, 5], [10, 5, 2]`.

Note:

`1 <= A.length <= 1000`.

`2 <= A[i] <= 10 ^ 9`.

【中文翻译】
给定一个均严格大于 1 的唯一整数数组。

我们使用这些整数构建二叉树，每个数字可以使用任意多次。

每个非叶节点的值应该等于其子节点值的乘积。

我们可以构建多少棵二叉树？返回答案模 10^9 + 7。

示例 1：
输入：`A = [2, 4]`
输出：3
解释：可以构建这些树：`[2], [4], [4, 2, 2]`

示例 2：
输入：`A = [2, 4, 5, 10]`
输出：`7`
解释：可以构建这些树：`[2], [4], [5], [10], [4, 2, 2], [10, 2, 5], [10, 5, 2]`。

注意：
`1 <= A.length <= 1000`。
`2 <= A[i] <= 10^9`。
"""

from typing import List, Optional


class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        arr.sort()
        dp = {}

        for x in arr:
            dp[x] = 1  # The tree consisting of just x as a leaf
            for a in arr:
                if a >= x:
                    break
                if x % a == 0:
                    b = x // a
                    if b in dp:
                        dp[x] = (dp[x] + dp[a] * dp[b]) % MOD

        return sum(dp.values()) % MOD



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 动态规划。将数组排序后从小到大处理，确保处理 x 时，
# 所有可能作为其因子的较小数字已经计算完毕。
#
# dp[x] 表示以 x 为根的二叉树数量。
# 基础情况：每个数字自身可以组成单节点树，dp[x] = 1。
#
# 对于每个 x，遍历所有小于 x 的数字 a：
#   如果 a 能整除 x，则 b = x // a 也是一个因子。
#   如果 b 也在数组中，则 (a, b) 可以作为 x 的左右子树。
#   以 a 为根的树有 dp[a] 种，以 b 为根的树有 dp[b] 种，
#   组合数为 dp[a] * dp[b]。累加到 dp[x]。
#
# 注意：a 和 b 不同时，(a,b) 和 (b,a) 是两种不同的树
#   （左右子树交换），因为遍历所有 a < x 且 a * b == x，
#   自动包含了两种排列。
#
# 时间复杂度: O(N^2) - N <= 1000，约 10^6 次操作
# 空间复杂度: O(N) - 存储 dp 字典
#
# 关键点:
# - 先排序确保子问题先行计算
# - dp[a] * dp[b] 代表左右子树的所有组合
# - 模 10^9 + 7 防止溢出
# - a 和 b 可重复使用，但题目保证数组元素唯一
