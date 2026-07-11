"""
LeetCode #1686 - Stone Game VI
中文题名：石子游戏 VI
https://leetcode.com/problems/stone-game-vi/

Alice and Bob take turns playing a game, with Alice starting first.

There are `n` stones in a pile. On each player's turn, they can remove
a stone from the pile and receive points based on the stone's value. Alice and Bob
may value the stones differently.

You are given two integer arrays of length `n`, `aliceValues`
and `bobValues`. Each `aliceValues[i]` and
`bobValues[i]` represents how Alice and Bob, respectively, value the
`ith` stone.

The winner is the person with the most points after all the stones are chosen. If
both players have the same amount of points, the game results in a draw. Both
players will play optimally.

Determine the result of the game, and:

If Alice wins, return `1`.

If Bob wins, return `-1`.

If the game results in a draw, return `0`.

Example 1:

Input: aliceValues = [1,3], bobValues = [2,1]
Output: 1
Explanation:
If Alice takes stone 1 (0-indexed) first, Alice will receive 3 points.
Bob can only choose stone 0, and will only receive 2 points.
Alice wins.

Example 2:

Input: aliceValues = [1,2], bobValues = [3,1]
Output: 0
Explanation:
If Alice takes stone 0, and Bob takes stone 1, they will both have 1 point.
Draw.

Example 3:

Input: aliceValues = [2,4,3], bobValues = [1,6,7]
Output: -1
Explanation:
Regardless of how Alice plays, Bob will be able to have more points than Alice.
For example, if Alice takes stone 1, Bob can take stone 2, and Alice takes stone 0, Alice will have 6 points to Bob's 7.
Bob wins.

Constraints:

`n == aliceValues.length == bobValues.length`

`1 <= n <= 105`

`1 <= aliceValues[i], bobValues[i] <= 100`

【中文翻译】
Alice和Bob轮流玩一个游戏，Alice先手。

有n颗石子。在每个玩家的回合中，他们可以从堆中取出一颗石子并获得基于该石子价值的分数。Alice和Bob对石子的估值可能不同。

给定两个长度为n的整数数组aliceValues和bobValues。aliceValues[i]和bobValues[i]分别代表Alice和Bob对第i颗石子的估值。

在所有石子都被选完后，获得更多分数的玩家获胜。如果双方分数相同，则游戏平局。双方都会以最优策略进行游戏。

判断游戏结果：
- 如果Alice获胜，返回1。
- 如果Bob获胜，返回-1。
- 如果平局，返回0。

示例1：

输入：aliceValues = [1,3], bobValues = [2,1]
输出：1
解释：如果Alice先取石子1（0索引），Alice将获得3分。
Bob只能选石子0，只能获得2分。
Alice获胜。

示例2：

输入：aliceValues = [1,2], bobValues = [3,1]
输出：0
解释：如果Alice取石子0，Bob取石子1，他们都将获得1分。
平局。

示例3：

输入：aliceValues = [2,4,3], bobValues = [1,6,7]
输出：-1
解释：无论Alice怎么选，Bob都能获得比Alice更多的分数。
例如，如果Alice取石子1，Bob可以取石子2，Alice再取石子0，Alice得6分，Bob得7分。
Bob获胜。

约束条件：

n == aliceValues.length == bobValues.length
1 <= n <= 10^5
1 <= aliceValues[i], bobValues[i] <= 100

"""

from typing import List, Optional


class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        n = len(aliceValues)
        # 按a[i] + b[i]降序排列的索引
        indices = list(range(n))
        indices.sort(key=lambda i: aliceValues[i] + bobValues[i], reverse=True)

        alice_score = 0
        bob_score = 0

        for turn, i in enumerate(indices):
            if turn % 2 == 0:
                # Alice的回合
                alice_score += aliceValues[i]
            else:
                # Bob的回合
                bob_score += bobValues[i]

        if alice_score > bob_score:
            return 1
        elif alice_score < bob_score:
            return -1
        else:
            return 0










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 贪心博弈论。关键洞察：当Alice拿走石子i时，她不仅获得了aliceValues[i]分，
# 还阻止了Bob获得bobValues[i]分。因此每颗石子的"总价值"可以看作是aliceValues[i]+bobValues[i]。
# 最优策略：双方都按aliceValues[i]+bobValues[i]从大到小的顺序选取石子。
# Alice先手取第1、3、5...（索引0开始）大的石子，Bob取第2、4、6...大的石子。
# 最后比较双方总分。
#
# 时间复杂度: O(n log n)，排序
# 空间复杂度: O(n)
#
# 关键点:
# - 将石子按a[i]+b[i]降序排列
# - 取石子不仅有收益，还有"阻止对手获益"的隐性价值
# - a[i]+b[i]代表了该石子的总博弈价值
# - 按此值从大到小轮流分配
