"""
LeetCode #649 - Dota2 Senate
中文题名：Dota2 参议院
https://leetcode.com/problems/dota2-senate/

In the world of Dota2, there are two parties: the `Radiant` and the
`Dire`.

The Dota2 senate consists of senators coming from two parties. Now the senate wants to make a
decision about a change in the Dota2 game. The voting for this change is a round-based
procedure. In each round, each senator can exercise `one` of the two rights:

`Ban one senator's right`:

A senator can make another senator lose all his rights in this and all the
following rounds.

`Announce the victory`:

If this senator found the senators who still have rights to vote are all from the
same party, he can announce the victory and make the decision about the change
in the game.

Given a string representing each senator's party belonging. The character 'R' and
'D' represent the `Radiant` party and the `Dire` party
respectively. Then if there are `n` senators, the size of the given string will
be `n`.

The round-based procedure starts from the first senator to the last senator in the given
order. This procedure will last until the end of voting. All the senators who have lost
their rights will be skipped during the procedure.

Suppose every senator is smart enough and will play the best strategy for his own party, you
need to predict which party will finally announce the victory and make the change in the
Dota2 game. The output should be `Radiant` or `Dire`.

Example 1:

Input: "RD"
Output: "Radiant"
Explanation: The first senator comes from Radiant and he can just ban the next senator's right in the round 1.
And the second senator can't exercise any rights any more since his right has been banned.
And in the round 2, the first senator can just announce the victory since he is the only guy in the senate who can vote.

Example 2:

Input: "RDD"
Output: "Dire"
Explanation:
The first senator comes from Radiant and he can just ban the next senator's right in the round 1.
And the second senator can't exercise any rights anymore since his right has been banned.
And the third senator comes from Dire and he can ban the first senator's right in the round 1.
And in the round 2, the third senator can just announce the victory since he is the only guy in the senate who can vote.

Note:

The length of the given string will in the range [1, 10,000].

【中文翻译】
在 Dota2 的世界中，有两个派别：「天辉」(Radiant) 和「夜魇」(Dire)。

Dota2 参议院由来自两派的参议员组成。现在参议院希望对 Dota2 游戏中的一个更改做出决定。对此更改的投票是一个基于回合的过程。在每一轮中，每位参议员可以行使以下两项权利之一：

「禁止一位参议员的权利」：

一位参议员可以让另一位参议员在此轮及之后所有轮次中丧失所有权利。

「宣布胜利」：

如果这位参议员发现仍然拥有投票权的参议员全部来自同一阵营，他可以宣布胜利并决定游戏中的更改。

给定一个字符串表示每位参议员所属的阵营。字符 'R' 和 'D' 分别代表「天辉」阵营和「夜魇」阵营。如果有 n 位参议员，则给定字符串的长度为 n。

基于回合的过程从第一位参议员到最后一位参议员按给定顺序进行。此过程将持续到投票结束。在过程中，所有失去权利的参议员将被跳过。

假设每位参议员都足够聪明，会为自己的阵营采用最佳策略，你需要预测哪个阵营最终会宣布胜利并决定 Dota2 游戏的更改。输出应为 "Radiant" 或 "Dire"。

示例 1：

输入："RD"
输出："Radiant"
解释：第一位参议员来自 Radiant，他可以在第 1 轮中禁止下一位参议员的权利。而第二位参议员因为权利被禁止而无法再行使任何权利。在第 2 轮中，第一位参议员可以宣布胜利，因为他是参议院中唯一能投票的人。

示例 2：

输入："RDD"
输出："Dire"
解释：
第一位参议员来自 Radiant，他可以在第 1 轮中禁止下一位参议员的权利。第二位参议员因为权利被禁止而无法再行使任何权利。第三位参议员来自 Dire，他可以在第 1 轮中禁止第一位参议员的权利。在第 2 轮中，第三位参议员可以宣布胜利，因为他是参议院中唯一能投票的人。

注意：

给定字符串的长度在 [1, 10,000] 范围内。
"""

from collections import deque
from typing import List, Optional


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        radiant = deque()
        dire = deque()

        for i, ch in enumerate(senate):
            if ch == 'R':
                radiant.append(i)
            else:
                dire.append(i)

        while radiant and dire:
            r_idx = radiant.popleft()
            d_idx = dire.popleft()
            if r_idx < d_idx:
                radiant.append(r_idx + n)
            else:
                dire.append(d_idx + n)

        return "Radiant" if radiant else "Dire"











# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用两个队列分别存储 Radiant 和 Dire 阵营参议员的原始索引。
# 每一轮中，比较两个队列首部的索引：
# - 索引较小的参议员（先投票）可以禁止索引较大的参议员（后投票）的权利
# - 获胜的参议员重新加入队列尾部，其索引加上 n（偏移到下一轮）
# - 被禁言的参议员直接淘汰（不出队入队）
# 当某一队列为空时，另一队列所属阵营获胜。
# 这种贪心策略是最优的：每轮你应当禁止离你最近的下一个敌对参议员。
#
# 时间复杂度: O(n) - 每位参议员最多入队出队一次
# 空间复杂度: O(n) - 两个队列存储所有参议员索引
#
# 关键点:
# - 使用双队列模拟循环投票过程
# - 索引加 offset 表示进入下一轮
# - 贪心策略：每轮禁止下一个即将投票的敌对参议员
# - 这就是一个"最优回合制消除"问题，队列首部比较恰好模拟了回合顺序
