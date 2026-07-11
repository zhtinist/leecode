"""
LeetCode #1366 - Rank Teams by Votes
中文题名：通过投票对团队排名
https://leetcode.com/problems/rank-teams-by-votes/

In a special ranking system, each voter gives a rank from highest to lowest to
all teams participated in the competition.

The ordering of teams is decided by who received the most position-one votes. If two
or more teams tie in the first position, we consider the second position to resolve
the conflict, if they tie again, we continue this process until the ties are
resolved. If two or more teams are still tied after considering all positions, we
rank them alphabetically based on their team letter.

Given an array of strings `votes` which is the votes of all voters in the
ranking systems. Sort all teams according to the ranking system described above.

Return a string of all teams sorted by the ranking system.

Example 1:

Input: votes = ["ABC","ACB","ABC","ACB","ACB"]
Output: "ACB"
Explanation: Team A was ranked first place by 5 voters. No other team was voted as first place so team A is the first team.
Team B was ranked second by 2 voters and was ranked third by 3 voters.
Team C was ranked second by 3 voters and was ranked third by 2 voters.
As most of the voters ranked C second, team C is the second team and team B is the third.

Example 2:

Input: votes = ["WXYZ","XYZW"]
Output: "XWYZ"
Explanation: X is the winner due to tie-breaking rule. X has same votes as W for the first position but X has one vote as second position while W doesn't have any votes as second position.

Example 3:

Input: votes = ["ZMNAGUEDSJYLBOPHRQICWFXTVK"]
Output: "ZMNAGUEDSJYLBOPHRQICWFXTVK"
Explanation: Only one voter so his votes are used for the ranking.

Example 4:

Input: votes = ["BCA","CAB","CBA","ABC","ACB","BAC"]
Output: "ABC"
Explanation:
Team A was ranked first by 2 voters, second by 2 voters and third by 2 voters.
Team B was ranked first by 2 voters, second by 2 voters and third by 2 voters.
Team C was ranked first by 2 voters, second by 2 voters and third by 2 voters.
There is a tie and we rank teams ascending by their IDs.

Example 5:

Input: votes = ["M","M","M","M"]
Output: "M"
Explanation: Only team M in the competition so it has the first rank.

Constraints:

`1 <= votes.length <= 1000`

`1 <= votes[i].length <= 26`

`votes[i].length == votes[j].length` for `0 <= i, j
< votes.length`.

`votes[i][j]` is an English upper-case letter.

All characters of `votes[i]` are unique.

All the characters that occur in `votes[0]` also occur in
`votes[j]` where `1 <= j < votes.length`.

【中文翻译】
在一个特殊的排名系统中，每位投票者对所有参赛团队从高到低进行排名。

团队的排名顺序由获得最多第一名投票的团队决定。如果有两个或多个团队在第一位置并列，则考虑第二位置来解决平局；如果再次并列，则继续此过程直到平局解决。如果在考虑所有位置后仍有平局，则按团队字母顺序升序排列。

给定一个字符串数组 `votes`，表示所有投票者的投票情况。按上述排名系统对所有团队进行排序。

返回按排名系统排序后的所有团队组成的字符串。

示例 1：
输入：votes = ["ABC","ACB","ABC","ACB","ACB"]
输出："ACB"
解释：A 队获得 5 票第一名，没有其他队伍获得第一名，所以 A 队排名第一。
B 队获得 2 票第二名和 3 票第三名。
C 队获得 3 票第二名和 2 票第三名。
由于 C 队在第二名上获得更多票数，所以 C 队排名第二，B 队排名第三。

示例 2：
输入：votes = ["WXYZ","XYZW"]
输出："XWYZ"
解释：X 在并列情况下获胜。X 和 W 在第一名票数相同，但 X 在第二名有 1 票，而 W 在第二名没有票。

示例 3：
输入：votes = ["ZMNAGUEDSJYLBOPHRQICWFXTVK"]
输出："ZMNAGUEDSJYLBOPHRQICWFXTVK"
解释：只有一位投票者，所以他的投票直接决定排名。

示例 4：
输入：votes = ["BCA","CAB","CBA","ABC","ACB","BAC"]
输出："ABC"
解释：
A 队获得 2 票第一、2 票第二、2 票第三。
B 队获得 2 票第一、2 票第二、2 票第三。
C 队获得 2 票第一、2 票第二、2 票第三。
完全平局，按字母顺序排名。

示例 5：
输入：votes = ["M","M","M","M"]
输出："M"
解释：只有 M 队参赛，所以排名第一。
"""

from typing import List
from collections import defaultdict


class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        if not votes:
            return ""

        num_teams = len(votes[0])
        # count[team] = 长度为 num_teams 的列表，表示该团队在每个排名位置的得票数
        teams = votes[0]
        count = {team: [0] * num_teams for team in teams}

        for vote in votes:
            for pos, team in enumerate(vote):
                count[team][pos] += 1

        # 排序：按每个位置的票数降序（票多优先），最后按字母升序
        sorted_teams = sorted(teams, key=lambda team: (
            [-count[team][i] for i in range(num_teams)] + [team]
        ))

        return "".join(sorted_teams)



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 统计每支队伍在每个排名位置上获得的票数。
# 1. 用字典 count[team] = [pos0_票数, pos1_票数, ..., posN_票数] 记录每支队伍在各位置的得票。
# 2. 遍历所有投票，累加每个位置上的票数。
# 3. 排序规则：依次比较每个位置的得票数（降序，即票多排前），如果所有位置都平局，按团队字母升序排列。
#    使用元组 ([-pos0票数, -pos1票数, ..., team字母]) 作为排序键。
#
# 时间复杂度: O(N * M log M)，N 为投票人数，M 为队伍数（排序 O(M log M)，每次比较 O(M)）
# 空间复杂度: O(M^2)，存储每支队伍在各位置的得票数
#
# 关键点:
# - 多级排序键：先按每个位置票数降序，再按字母升序
# - 使用负号将降序转换为升序（Python sorted 默认升序）
# - votes[0] 包含所有参赛队伍，可直接获取队伍列表













