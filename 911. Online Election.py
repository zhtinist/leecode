"""
LeetCode #911 - Online Election
中文题名：在线选举
https://leetcode.com/problems/online-election/

In an election, the `i`-th vote was cast for `persons[i]` at time
`times[i]`.

Now, we would like to implement the following query function: `TopVotedCandidate.q(int
t)` will return the number of the person that was leading the election at time
`t`.

Votes cast at time `t` will count towards our query.  In the case of a tie,
the most recent vote (among tied candidates) wins.

Example 1:

Input: ["TopVotedCandidate","q","q","q","q","q","q"], [[[0,1,1,0,0,1,0],[0,5,10,15,20,25,30]],[3],[12],[25],[15],[24],[8]]
Output: [null,0,1,1,0,0,1]
Explanation:
At time 3, the votes are [0], and 0 is leading.
At time 12, the votes are [0,1,1], and 1 is leading.
At time 25, the votes are [0,1,1,0,0,1], and 1 is leading (as ties go to the most recent vote.)
This continues for 3 more queries at time 15, 24, and 8.

Note:

`1 <= persons.length = times.length <= 5000`

`0 <= persons[i] <= persons.length`

`times` is a strictly increasing array with all elements in `[0,
10^9]`.

`TopVotedCandidate.q` is called at most `10000` times per test
case.

`TopVotedCandidate.q(int t)` is always called with `t >=
times[0]`.

【中文翻译】

在选举中，第 i 张票是在时间 times[i] 投给候选人 persons[i] 的。
现在，我们希望实现以下查询函数：TopVotedCandidate.q(int t) 将返回在时间 t
领先的候选人编号。在时间 t 投出的票将计入我们的查询。如果出现平局，则最近
获得投票的候选人（在平局候选人中）获胜。

"""

from typing import List, Optional


class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        """
        Initialize the data structure.
        Precompute the leader at each unique time point.
        """
        self.times = times
        self.leaders = []
        count = {}
        leader = -1
        max_votes = 0

        for p in persons:
            count[p] = count.get(p, 0) + 1
            if count[p] >= max_votes:
                max_votes = count[p]
                leader = p
            self.leaders.append(leader)

    def q(self, t: int) -> int:
        """
        Return the leader at time t using binary search.
        """
        import bisect
        idx = bisect.bisect_right(self.times, t) - 1
        return self.leaders[idx]


class Solution:
    """
    This problem is a design problem. The actual LeetCode submission expects
    a class named TopVotedCandidate (defined above). The Solution class here
    serves as a wrapper/testing entry point.
    """

    def topVotedCandidate(self, persons: List[int], times: List[int]) -> TopVotedCandidate:
        return TopVotedCandidate(persons, times)



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 1. 在初始化时，遍历所有投票，维护一个计数字典和当前领先者。
#    由于平局时取最近获得投票的候选人，当当前候选人的票数 >= 最大票数时即更新领先者。
#    将每个时刻的领先者记录在 self.leaders 数组中（与 self.times 同步）。
# 2. 查询 q(t) 时，使用二分查找 (bisect_right) 找到最后一个 <= t 的时间点，
#    返回该时刻的领先者。
#
# 时间复杂度: 初始化 O(N)，每次查询 O(log N)
# 空间复杂度: O(N)
#
# 关键点:
# - 平局时选择最近获得投票的候选人，因此使用 >= 而不是 >
# - times 严格递增，可以直接二分查找
# - 可以使用 bisect 模块简化二分查找
