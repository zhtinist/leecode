"""
LeetCode #1626 - Best Team With No Conflicts
中文题名：无矛盾的最佳球队
https://leetcode.com/problems/best-team-with-no-conflicts/

You are the manager of a basketball team. For the upcoming tournament, you want to
choose the team with the highest overall score. The score of the team is the
sum of scores of all the players in the team.

However, the basketball team is not allowed to have conflicts. A
conflict exists if a younger player has a strictly
higher score than an older player. A conflict does not
occur between players of the same age.

Given two lists, `scores` and `ages`, where each `scores[i]`
and `ages[i]` represents the score and age of the
`ith` player, respectively, return the highest overall
score of all possible basketball teams.

Example 1:

Input: scores = [1,3,5,10,15], ages = [1,2,3,4,5]
Output: 34
Explanation: You can choose all the players.

Example 2:

Input: scores = [4,5,6,5], ages = [2,1,2,1]
Output: 16
Explanation: It is best to choose the last 3 players. Notice that you are allowed to choose multiple people of the same age.

Example 3:

Input: scores = [1,2,3,5], ages = [8,9,10,1]
Output: 6
Explanation: It is best to choose the first 3 players.

Constraints:

`1 <= scores.length, ages.length <= 1000`

`scores.length == ages.length`

`1 <= scores[i] <= 106`

`1 <= ages[i] <= 1000`

【中文翻译】
给定两个列表 scores 和 ages，表示每个球员的得分和年龄。
选择若干球员组成球队，要求没有矛盾。矛盾定义：年龄小的球员得分严格高于年龄大的球员。
求所有可能的无矛盾球队中最高总得分。

示例 1：
输入: scores = [1,3,5,10,15], ages = [1,2,3,4,5]
输出: 34
解释: 可以选择所有球员，因为没有矛盾。

示例 2：
输入: scores = [4,5,6,5], ages = [2,1,2,1]
输出: 16
解释: 最佳选择是后三个球员。注意你可以选择同龄球员。
"""

from typing import List, Optional


class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = len(scores)
        players = sorted(zip(ages, scores))  # 按年龄排序，年龄相同按分数排序
        dp = [0] * n
        ans = 0

        for i in range(n):
            dp[i] = players[i][1]  # 只有自己
            for j in range(i):
                # 如果 j 的分数不超过 i，可以加入
                if players[j][1] <= players[i][1]:
                    dp[i] = max(dp[i], dp[j] + players[i][1])
            ans = max(ans, dp[i])

        return ans
# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 排序 + 动态规划（类似最长递增子序列 LIS）。
# 1. 按年龄升序排序（年龄相同时按分数升序），保证前面的球员年龄 <= 后面的
# 2. 对排序后的序列，求分数非递减的最大子序列和（因为年龄已经非递减，只需保证分数也非递减即可避免矛盾）
# 3. DP: dp[i] = 以第 i 个球员结尾的最大总得分 = max(dp[j] + score[i])（其中 score[j] <= score[i]）
#
# 时间复杂度: O(N^2) — 双重循环
# 空间复杂度: O(N) — DP 数组
#
# 关键点:
# - 先年龄后分数的排序是关键转化步骤
# - 分数可以相等（同龄人分数相等不算矛盾）
# - 问题转化为求分数非递减的最大子序列和（类似 LIS 但要求和最大）
