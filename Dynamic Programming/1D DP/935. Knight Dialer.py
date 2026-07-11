"""
LeetCode #935 - Knight Dialer
中文题名：骑士拨号器
https://leetcode.com/problems/knight-dialer/

A chess knight can move as indicated in the chess diagram below:

.

This time, we place our chess knight on any numbered key of a phone pad (indicated above),
and the knight makes `N-1` hops.  Each hop must be from one key to another
numbered key.

Each time it lands on a key (including the initial placement of the knight), it presses the
number of that key, pressing `N` digits total.

How many distinct numbers can you dial in this manner?

Since the answer may be large, output the answer modulo `10^9 +
7`.

Example 1:

Input: 1
Output: 10

Example 2:

Input: 2
Output: 20

Example 3:

Input: 3
Output: 46

Note:

`1 <= N <= 5000`

【中文翻译】
国际象棋中的骑士可以按照下图所示的方式移动：

.

这次，我们将骑士放在电话拨号盘的任意数字键上，骑士进行 N-1 次跳跃。
每次跳跃必须从一个数字键跳至另一个数字键。

每次它落在一个键上（包括骑士的初始位置），它就会按下该键的数字，
总共按下 N 位数字。

通过这种方式，你可以拨出多少个不同的号码？

由于答案可能很大，请输出答案对 10^9 + 7 取模的结果。

"""

from typing import List, Optional


class Solution:
    def knightDialer(self, n: int) -> int:
        MOD = 10**9 + 7

        # Moves from each digit
        moves = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4],
        }

        # dp[i] = number of ways to end at digit i
        dp = [1] * 10

        for _ in range(n - 1):
            next_dp = [0] * 10
            for digit in range(10):
                for next_digit in moves[digit]:
                    next_dp[next_digit] = (next_dp[next_digit] + dp[digit]) % MOD
            dp = next_dp

        return sum(dp) % MOD



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 1. 建立骑士移动映射表：定义每个数字键可以从哪些其他数字键一步跳过来。
#    骑士的合法移动：0<-{4,6}, 1<-{6,8}, 2<-{7,9}, 3<-{4,8}, 4<-{0,3,9},
#    5<-{}, 6<-{0,1,7}, 7<-{2,6}, 8<-{1,3}, 9<-{2,4}。
# 2. 动态规划：dp[digit] 表示以 digit 结尾的 N 位号码的数量。
#    初始状态（N=1）：所有数字的 dp 值均为 1（因为可以从任意数字开始）。
# 3. 状态转移：对于每一步（N-1 次），next_dp[next] = sum(dp[prev])，
#    其中 prev 是能跳到 next 的所有数字。
# 4. 最终答案：sum(dp[0..9]) % MOD。
#
# 时间复杂度: O(N) — 固定 10 个数字，每次迭代最多 2-3 条边，共 N-1 次迭代。
# 空间复杂度: O(1) — 仅需两个长度为 10 的数组。
#
# 关键点:
# - 骑士移动规则在电话键盘上只有特定映射（5 没有后继）
# - 动态规划只需 O(N) 时间，不需要建立 N x 10 的表格
# - 注意取模操作
