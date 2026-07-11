"""
LeetCode #2140 - Solving Questions With Brainpower
解决智力问题
https://leetcode.cn/problems/solving-questions-with-brainpower/

给你一个下标从 0 开始的二维整数数组 `questions` ，其中 `questions[i] = [points_i, brainpower_i]` 。
这个数组表示一场考试里的一系列题目，你需要 按顺序 （也就是从问题 `0` 开始依次解决），针对每个问题选择 解决 或者 跳过 操作。解决问题 `i` 将让你 获得  `points_i` 的分数，但是你将 无法 解决接下来的 `brainpower_i` 个问题（即只能跳过接下来的 `brainpower_i`_ 个问题）。如果你跳过问题 `i` ，你可以对下一个问题决定使用哪种操作。
比方说，给你 `questions = [[3, 2], [4, 3], [4, 4], [2, 5]]` ：
如果问题 `0` 被解决了， 那么你可以获得 `3` 分，但你不能解决问题 `1` 和 `2` 。
如果你跳过问题 `0` ，且解决问题 `1` ，你将获得 `4` 分但是不能解决问题 `2` 和 `3` 。
请你返回这场考试里你能获得的 最高 分数。

示例 1：
输入：questions = [[3,2],[4,3],[4,4],[2,5]] 输出：5 解释：解决问题 0 和 3 得到最高分。 - 解决问题 0 ：获得 3 分，但接下来 2 个问题都不能解决。 - 不能解决问题 1 和 2 - 解决问题 3 ：获得 2 分 总得分为：3 + 2 = 5 。没有别的办法获得 5 分或者多于 5 分。
示例 2：
输入：questions = [[1,1],[2,2],[3,3],[4,4],[5,5]] 输出：7 解释：解决问题 1 和 4 得到最高分。 - 跳过问题 0 - 解决问题 1 ：获得 2 分，但接下来 2 个问题都不能解决。 - 不能解决问题 2 和 3 - 解决问题 4 ：获得 5 分 总得分为：2 + 5 = 7 。没有别的办法获得 7 分或者多于 7 分。

提示：
`1 <= questions.length <= 10^5`
`questions[i].length == 2`
`1 <= points_i, brainpower_i <= 10^5`
"""

from typing import List, Optional


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            points, brainpower = questions[i]
            next_idx = i + brainpower + 1
            take = points + (dp[next_idx] if next_idx < n else 0)
            skip = dp[i + 1]
            dp[i] = max(take, skip)

        return dp[0]



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Dynamic Programming
#
# 解题思路:
# 动态规划，从后往前遍历。定义 dp[i] 表示从第 i 题开始到末尾能获得的最高分数。
# 对于第 i 题，有两种选择：
#   1. 解决：获得 points_i 分，然后必须跳过 brainpower_i 个问题，
#      下一个可选的问题是 i + brainpower_i + 1，即 dp[i+brainpower_i+1]
#   2. 跳过：不得分，考虑下一题 dp[i+1]
# 取两者最大值。从后往前计算可以保证在计算 dp[i] 时 dp[i+1] 和 dp[i+brainpower_i+1] 都已知。
#
# 时间复杂度: O(N)，每个问题只处理一次。
# 空间复杂度: O(N)，需要长度为 N+1 的 dp 数组。
#
# 关键点:
# - 从后往前的 DP 方向，确保子问题已经求解
# - 跳过 brainpower_i 个问题的处理：直接跳转到 i + brainpower_i + 1
