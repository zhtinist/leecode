"""
LeetCode #1690 - Stone Game VII
中文题名：石子游戏 VII
https://leetcode.com/problems/stone-game-vii/

Alice and Bob take turns playing a game, with Alice starting first.

There are `n` stones arranged in a row. On each player's turn, they can
remove either the leftmost stone or the rightmost stone from the
row and receive points equal to the sum of the remaining stones'
values in the row. The winner is the one with the higher score when there are no
stones left to remove.

Bob found that he will always lose this game (poor Bob, he always loses), so he
decided to minimize the score's difference. Alice's goal is to
maximize the difference in the score.

Given an array of integers `stones` where `stones[i]`
represents the value of the `ith` stone from the
left, return the difference in Alice and Bob's
score if they both play optimally.

Example 1:

Input: stones = [5,3,1,4,2]
Output: 6
Explanation:
- Alice removes 2 and gets 5 + 3 + 1 + 4 = 13 points. Alice = 13, Bob = 0, stones = [5,3,1,4].
- Bob removes 5 and gets 3 + 1 + 4 = 8 points. Alice = 13, Bob = 8, stones = [3,1,4].
- Alice removes 3 and gets 1 + 4 = 5 points. Alice = 18, Bob = 8, stones = [1,4].
- Bob removes 1 and gets 4 points. Alice = 18, Bob = 12, stones = [4].
- Alice removes 4 and gets 0 points. Alice = 18, Bob = 12, stones = [].
The score difference is 18 - 12 = 6.

Example 2:

Input: stones = [7,90,5,1,100,10,10,2]
Output: 122

Constraints:

`n == stones.length`

`2 <= n <= 1000`

`1 <= stones[i] <= 1000`

【中文翻译】
爱丽丝和鲍勃轮流玩游戏，爱丽丝先手。

有 `n` 块石头排成一行。每回合玩家可以移除最左边或最右边的石头，
获得等于剩下的石头值之和的分数。当没有石头可移除时，得分高者胜出。

鲍勃发现他总是输掉这个游戏（可怜的鲍勃），所以他决定最小化分数差。
爱丽丝的目标是最大化分数差。

给定一个整数数组 `stones`，其中 `stones[i]` 表示第 `i` 块石头的值，
如果双方都采取最优策略，返回爱丽丝和鲍勃的分数差。

示例 1：

输入: stones = [5,3,1,4,2]
输出: 6
解释:
- 爱丽丝移除 2，得到 5+3+1+4 = 13 分。爱丽丝=13，鲍勃=0，stones=[5,3,1,4]
- 鲍勃移除 5，得到 3+1+4 = 8 分。爱丽丝=13，鲍勃=8，stones=[3,1,4]
- 爱丽丝移除 3，得到 1+4 = 5 分。爱丽丝=18，鲍勃=8，stones=[1,4]
- 鲍勃移除 1，得到 4 分。爱丽丝=18，鲍勃=12，stones=[4]
- 爱丽丝移除 4，得到 0 分。爱丽丝=18，鲍勃=12，stones=[]
分数差为 18 - 12 = 6

示例 2：

输入: stones = [7,90,5,1,100,10,10,2]
输出: 122

约束条件：

`n == stones.length`
`2 <= n <= 1000`
`1 <= stones[i] <= 1000`
"""

from typing import List, Optional


class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        """
        DP: dp[i][j] = 当前玩家在子数组 stones[i..j] 中能获得的最大分数差
        (当前玩家得分 - 对手得分)

        选择移除左端：得分 = sum[i+1..j] - dp[i+1][j]
        选择移除右端：得分 = sum[i..j-1] - dp[i][j-1]
        取最大值

        使用前缀和快速计算区间和。
        """
        n = len(stones)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stones[i]

        # dp[i][j] = max difference for subarray stones[i..j]
        dp = [[0] * n for _ in range(n)]

        # 区间长度从 2 到 n
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                # 移除左端: 获得 sum(i+1..j)，对手在 [i+1..j] 上的最优差为 dp[i+1][j]
                left_score = (prefix[j + 1] - prefix[i + 1]) - dp[i + 1][j]
                # 移除右端: 获得 sum(i..j-1)，对手在 [i..j-1] 上的最优差为 dp[i][j-1]
                right_score = (prefix[j] - prefix[i]) - dp[i][j - 1]
                dp[i][j] = max(left_score, right_score)

        return dp[0][n - 1]










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 博弈类 DP。定义 dp[i][j] 表示在子数组 stones[i..j] 上，当前玩家与对手的
# 最大分数差（当前玩家得分 - 对手得分）。
#
# 当前玩家可以选择移除最左端或最右端：
# - 移除左端 i：获得 sum(i+1..j)，然后对手在 [i+1..j] 上获得 dp[i+1][j] 的净优势
#   所以当前玩家的净收益 = sum(i+1..j) - dp[i+1][j]
# - 移除右端 j：获得 sum(i..j-1)，对手在 [i..j-1] 上获得 dp[i][j-1] 的净优势
#   所以当前玩家的净收益 = sum(i..j-1) - dp[i][j-1]
#
# 取两者最大值。使用前缀和 O(1) 计算区间和。
# 从小区间向大区间递推，最终答案 = dp[0][n-1]。
#
# 时间复杂度: O(n^2)
# 空间复杂度: O(n^2)
#
# 关键点:
# - DP 状态定义为"当前玩家与对手的分数差"，而非两人的绝对分数
# - 前缀和快速计算区间和，避免 O(n) 查询
# - 移除石头后，对手成为"当前玩家"，所以用 sum - opponent_advantage
# - 区间 DP 的循环顺序：从长度为 2 到 n 逐步扩大
