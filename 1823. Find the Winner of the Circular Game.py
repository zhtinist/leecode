"""
LeetCode #1823 - Find the Winner of the Circular Game
中文题名：找出游戏的获胜者
https://leetcode.com/problems/find-the-winner-of-the-circular-game/

There are `n` friends that are playing a game. The friends are sitting in a circle and are numbered from `1` to `n` in clockwise order. More formally, moving clockwise from the `ith` friend brings you to the `(i+1)th` friend for `1 <= i < n`, and moving clockwise from the `nth` friend brings you to the `1st` friend.

The rules of the game are as follows:

Start at the `1st` friend.

Count the next `k` friends in the clockwise direction including the friend you started at. The counting wraps around the circle and may count some friends more than once.

The last friend you counted leaves the circle and loses the game.

If there is still more than one friend in the circle, go back to step `2` starting from the friend immediately clockwise of the friend who just lost and repeat.

Else, the last friend in the circle wins the game.

Given the number of friends, `n`, and an integer `k`, return the winner of the game.

Example 1:

Input: n = 5, k = 2
Output: 3
Explanation: Here are the steps of the game:
1) Start at friend 1.
2) Count 2 friends clockwise, which are friends 1 and 2.
3) Friend 2 leaves the circle. Next start is friend 3.
4) Count 2 friends clockwise, which are friends 3 and 4.
5) Friend 4 leaves the circle. Next start is friend 5.
6) Count 2 friends clockwise, which are friends 5 and 1.
7) Friend 1 leaves the circle. Next start is friend 3.
8) Count 2 friends clockwise, which are friends 3 and 5.
9) Friend 5 leaves the circle. Only friend 3 is left, so they are the winner.

Example 2:

Input: n = 6, k = 5
Output: 1
Explanation: The friends leave in this order: 5, 4, 6, 2, 3. The winner is friend 1.

Constraints:

`1 <= k <= n <= 500`

【中文翻译】

有n个朋友围成一圈，按顺时针顺序从1到n编号。游戏规则如下：
1. 从第1个朋友开始。
2. 顺时针数k个朋友（包括起始的那个朋友），数到的最后一位朋友出局。
3. 从出局者顺时针方向的下一个朋友开始，重复步骤2。
4. 最后剩下的一位朋友获胜。

给定朋友数量n和整数k，返回获胜者的编号。

示例：
输入：n = 5, k = 2
输出：3
解释：出局顺序为2、4、1、5，最后剩下3获胜。

"""

from typing import List, Optional


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # Josephus递推: f(n,k) = (f(n-1,k) + k) % n, 0-indexed
        winner = 0  # f(1, k) = 0
        for i in range(2, n + 1):
            winner = (winner + k) % i
        return winner + 1  # 转换为1索引










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 经典的约瑟夫环问题。递推公式：f(n,k) = (f(n-1,k) + k) % n，
# 其中f(1,k) = 0（0索引）。最终答案需要转换为1索引：f(n,k) + 1。
# 也可以使用队列模拟，但数学解法更高效。
#
# 时间复杂度: O(N)，迭代从2到n
# 空间复杂度: O(1)，只使用常数空间
#
# 关键点:
# - f(n,k) = (f(n-1,k) + k) % n 是0索引的递推公式
# - 初始化winner=0即f(1,k)=0
# - 返回winner+1转换为1索引
