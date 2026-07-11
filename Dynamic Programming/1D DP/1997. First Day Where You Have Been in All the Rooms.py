"""
LeetCode #1997 - First Day Where You Have Been in All the Rooms
访问完所有房间的第一天
https://leetcode.cn/problems/first-day-where-you-have-been-in-all-the-rooms/

你需要访问 `n` 个房间，房间从 `0` 到 `n - 1` 编号。同时，每一天都有一个日期编号，从 `0` 开始，依天数递增。你每天都会访问一个房间。
最开始的第 `0` 天，你访问 `0` 号房间。给你一个长度为 `n` 且 下标从 0 开始 的数组 `nextVisit` 。在接下来的几天中，你访问房间的 次序 将根据下面的 规则 决定：
假设某一天，你访问 `i` 号房间。
如果算上本次访问，访问 `i` 号房间的次数为 奇数 ，那么 第二天 需要访问 `nextVisit[i]` 所指定的房间，其中 `0 <= nextVisit[i] <= i` 。
如果算上本次访问，访问 `i` 号房间的次数为 偶数 ，那么 第二天 需要访问 `(i + 1) mod n` 号房间。
请返回你访问完所有房间的第一天的日期编号。题目数据保证总是存在这样的一天。由于答案可能很大，返回对 `10^9 + 7` 取余后的结果。

示例 1：
输入：nextVisit = [0,0] 输出：2 解释： - 第 0 天，你访问房间 0 。访问 0 号房间的总次数为 1 ，次数为奇数。   下一天你需要访问房间的编号是 nextVisit[0] = 0 - 第 1 天，你访问房间 0 。访问 0 号房间的总次数为 2 ，次数为偶数。   下一天你需要访问房间的编号是 (0 + 1) mod 2 = 1 - 第 2 天，你访问房间 1 。这是你第一次完成访问所有房间的那天。
示例 2：
输入：nextVisit = [0,0,2] 输出：6 解释： 你每天访问房间的次序是 [0,0,1,0,0,1,2,...] 。 第 6 天是你访问完所有房间的第一天。
示例 3：
输入：nextVisit = [0,1,2,0] 输出：6 解释： 你每天访问房间的次序是 [0,0,1,1,2,2,3,...] 。 第 6 天是你访问完所有房间的第一天。

提示：
`n == nextVisit.length`
`2 <= n <= 10^5`
`0 <= nextVisit[i] <= i`
"""

from typing import List, Optional


class Solution:
    def firstDayBeenInAllRooms(self, nextVisit: List[int]) -> int:
        """
        DP: dp[i] = days needed to visit room i for the first time.
        When we first reach room i (odd visit count), we go back to nextVisit[i],
        then need to come back to i again before we can move to i+1.
        """
        MOD = 10**9 + 7
        n = len(nextVisit)
        dp = [0] * n  # dp[i] = days to reach room i for the first time

        for i in range(1, n):
            # To reach room i the first time:
            # 1. Reach room i-1 first time: dp[i-1] days
            # 2. After visiting i-1 (odd count), go back to nextVisit[i-1]
            # 3. From nextVisit[i-1], come back to i-1 again (this takes
            #    dp[i-1] - dp[nextVisit[i-1]] days, plus 1 day for the
            #    second visit to i-1 itself)
            # 4. Then go to i (+1 day)
            dp[i] = (2 * dp[i - 1] - dp[nextVisit[i - 1]] + 2) % MOD

        return dp[n - 1] % MOD



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Dynamic Programming
#
# 解题思路:
# 定义 dp[i] = 第一次到达房间 i 所需的天数。
# 递推关系：
# 要首次到达房间 i，需要先首次到达房间 i-1（花费 dp[i-1] 天）。
# 到达 i-1 后，这是奇数次访问，所以下一天会跳到 nextVisit[i-1]。
# 从 nextVisit[i-1] 再回到 i-1 需要：dp[i-1] - dp[nextVisit[i-1]] + 1 天。
# 然后从 i-1 到 i 再花 1 天。
# 总天数：dp[i] = 2*dp[i-1] - dp[nextVisit[i-1]] + 2
# 最终答案是 dp[n-1]（第一次到达最后一个房间的天数）。
#
# 时间复杂度: O(N)
# 空间复杂度: O(N)
#
# 关键点:
# - 奇数次访问跳回 nextVisit[i]，偶数次前进到 i+1
# - 相邻两次到达同一房间之间的时间差
# - dp 递推关系需要取模
