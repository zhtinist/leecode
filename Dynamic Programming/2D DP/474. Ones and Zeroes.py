"""
LeetCode #474 - Ones and Zeroes
中文题名：一和零
https://leetcode.com/problems/ones-and-zeroes/

In the computer world, use restricted resource you have to generate maximum benefit is what
we always want to pursue.

For now, suppose you are a dominator of m `0s` and n `1s`
respectively. On the other hand, there is an array with strings consisting of only
`0s` and `1s`.

Now your task is to find the maximum number of strings that you can form with given m
`0s` and n `1s`. Each `0` and `1` can be
used at most once.

Note:

The given numbers of `0s` and `1s` will both not exceed
`100`

The size of given string array won't exceed `600`.

Example 1:

Input: Array = {"10", "0001", "111001", "1", "0"}, m = 5, n = 3
Output: 4

Explanation: This are totally 4 strings can be formed by the using of 5 0s and 3 1s, which are &ldquo;10,&rdquo;0001&rdquo;,&rdquo;1&rdquo;,&rdquo;0&rdquo;

Example 2:

Input: Array = {"10", "0", "1"}, m = 1, n = 1
Output: 2

Explanation: You could form "10", but then you'd have nothing left. Better form "0" and "1".

【中文翻译】
在计算机世界中，我们总是希望用有限的资源获得最大的收益。

现在假设你分别控制着 m 个 '0' 和 n 个 '1'。另外，有一个仅由 '0' 和 '1' 组成的字符串数组。

你的任务是找出用给定的 m 个 '0' 和 n 个 '1' 最多能组成数组中的多少个字符串。每个 '0' 和 '1' 最多只能使用一次。

注意：
    给定的 '0' 和 '1' 的数量均不超过 100。
    给定字符串数组的大小不超过 600。

示例 1：
    输入：Array = {"10", "0001", "111001", "1", "0"}, m = 5, n = 3
    输出：4
    解释：使用 5 个 0 和 3 个 1 总共可以组成 4 个字符串，即 "10"、"0001"、"1"、"0"。

示例 2：
    输入：Array = {"10", "0", "1"}, m = 1, n = 1
    输出：2
    解释：你可以组成 "10"，但之后就什么都没有了。更好的方案是组成 "0" 和 "1"。
"""

from typing import List, Optional


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # dp[i][j] = max strings we can form with i zeros and j ones
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for s in strs:
            zeros = s.count("0")
            ones = len(s) - zeros

            # Traverse backwards to avoid reusing the same string
            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)

        return dp[m][n]



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 这是一个二维背包问题。每个字符串相当于一件物品，消耗的"重量"是其中的 0 的个数和 1 的个数。
# 使用二维 DP 数组 dp[i][j] 表示用 i 个 0 和 j 个 1 最多能组成的字符串数量。
# 对每个字符串，统计其 0 和 1 的个数，然后从后向前更新 dp 数组（避免重复使用同一字符串）。
# 状态转移方程：dp[i][j] = max(dp[i][j], dp[i-zeros][j-ones] + 1)。最终答案为 dp[m][n]。
#
# 时间复杂度: O(L * m * n)，其中 L 是字符串数组长度，m 和 n 分别是 0 和 1 的配额
# 空间复杂度: O(m * n) — 二维 DP 数组
#
# 关键点:
# - 二维 0/1 背包的变种，重量维度从一维扩展到二维
# - 内层循环必须从大到小遍历，否则会重复使用同一字符串
# - 每个字符串的 zeros 和 ones 计数是其"成本"，价值恒为 1（因为求的是最多字符串数）
