"""
LeetCode #486 - Predict the Winner
中文题名：预测赢家
https://leetcode.com/problems/predict-the-winner/

Given an array of scores that are non-negative integers. Player 1 picks one of the numbers
from either end of the array followed by the player 2 and then player 1 and so on. Each time
a player picks a number, that number will not be available for the next player. This
continues until all the scores have been chosen. The player with the maximum score
wins.

Given an array of scores, predict whether player 1 is the winner. You can assume each player
plays to maximize his score.

Example 1:

Input: [1, 5, 2]
Output: False
Explanation: Initially, player 1 can choose between 1 and 2.
If he chooses 2 (or 1), then player 2 can choose from 1 (or 2) and 5. If player 2 chooses 5, then player 1 will be left with 1 (or 2).
So, final score of player 1 is 1 + 2 = 3, and player 2 is 5.
Hence, player 1 will never be the winner and you need to return False.

Example 2:

Input: [1, 5, 233, 7]
Output: True
Explanation: Player 1 first chooses 1. Then player 2 have to choose between 5 and 7. No matter which number player 2 choose, player 1 can choose 233.
Finally, player 1 has more score (234) than player 2 (12), so you need to return True representing player1 can win.

Note:

1

【中文翻译】
给定一个表示分数的非负整数数组。玩家 1 从数组的任意一端选择一个数字，然后玩家 2 选择，
依此类推。每次玩家选择一个数字后，该数字对下一个玩家不可用。这个过程一直持续到所有分数被选完。
得分最高的玩家获胜。

给定一个分数数组，预测玩家 1 是否能成为赢家。你可以假设每个玩家都会采取最大化自己分数的策略。

示例 1：
    输入：[1, 5, 2]
    输出：False
    解释：初始时，玩家 1 可以从 1 和 2 之间选择。
    如果他选择 2（或 1），那么玩家 2 可以从 1（或 2）和 5 中选择。如果玩家 2 选择了 5，
    那么玩家 1 只剩下 1（或 2）。
    所以，玩家 1 的最终分数是 1 + 2 = 3，玩家 2 是 5。
    因此，玩家 1 永远不会是赢家，需要返回 False。

示例 2：
    输入：[1, 5, 233, 7]
    输出：True
    解释：玩家 1 首先选择 1。然后玩家 2 必须在 5 和 7 之间选择。
    无论玩家 2 选择哪个数字，玩家 1 都可以选择 233。
    最终，玩家 1 的分数（234）超过玩家 2（12），所以返回 True，表示玩家 1 可以获胜。

注意：
    数组长度范围是 [1, 20]。
    数组元素为不超过 10^7 的非负整数。
"""

from typing import List, Optional


class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        # dp[i][j] = maximum score advantage the current player can achieve
        # over the opponent when playing on subarray nums[i..j]
        dp = [[0] * n for _ in range(n)]

        # Base case: single element subarrays
        for i in range(n):
            dp[i][i] = nums[i]

        # Fill DP for increasing subarray lengths
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                # Current player picks nums[i] or nums[j],
                # then opponent gets their best advantage from remaining
                dp[i][j] = max(
                    nums[i] - dp[i + 1][j],  # Pick left
                    nums[j] - dp[i][j - 1],  # Pick right
                )

        # Player 1 wins if their advantage over player 2 is >= 0
        return dp[0][n - 1] >= 0



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用动态规划计算当前玩家在一个子数组上能获得的最大净胜分（当前玩家分数减去对手分数）。
# dp[i][j] 表示在 nums[i..j] 子数组上，当前先手玩家能获得的最大优势。
# 当前玩家可以选择拿 nums[i] 或 nums[j]，拿到后对手将在剩余子数组上获得其最大优势，
# 因此 dp[i][j] = max(nums[i] - dp[i+1][j], nums[j] - dp[i][j-1])。
# 最终，dp[0][n-1] >= 0 意味着玩家 1 能够至少不输（净胜分非负即获胜）。
#
# 时间复杂度: O(N^2) — 填充 N*N 的 DP 表格，N 为数组长度（N <= 20）
# 空间复杂度: O(N^2) — 二维 DP 数组；可以优化到 O(N) 使用一维滚动数组
#
# 关键点:
# - dp[i][j] 定义为"先手净胜分"，巧妙地将两人博弈转化为单人最优化问题
# - 转移方程中的减号体现了极小化极大（minimax）思想：你的得分 = 当前选择 - 对手最优结果
# - 最终判断条件是 dp[0][n-1] >= 0，因为问题问的是玩家 1 是否能赢（打平也算赢？题目中平局玩家 1 获胜）
# - 也可以用递归 + 记忆化搜索实现，逻辑相同
