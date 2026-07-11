"""
LeetCode #1535 - Find the Winner of an Array Game
中文题名：找出数组游戏的赢家
https://leetcode.com/problems/find-the-winner-of-an-array-game/

Given an integer array `arr` of distinct integers and an
integer `k`.

A game will be played between the first two elements of the array (i.e.
`arr[0]` and `arr[1]`). In each round of the game, we compare
`arr[0]` with `arr[1]`, the larger integer wins and
remains at position `0` and the smaller integer moves to the end of the
array. The game ends when an integer wins `k` consecutive rounds.

Return the integer which will win the game.

It is guaranteed that there will be a winner of the game.

Example 1:

Input: arr = [2,1,3,5,4,6,7], k = 2
Output: 5
Explanation: Let's see the rounds of the game:
Round |       arr       | winner | win_count
1   | [2,1,3,5,4,6,7] | 2      | 1
2   | [2,3,5,4,6,7,1] | 3      | 1
3   | [3,5,4,6,7,1,2] | 5      | 1
4   | [5,4,6,7,1,2,3] | 5      | 2
So we can see that 4 rounds will be played and 5 is the winner because it wins 2 consecutive games.

Example 2:

Input: arr = [3,2,1], k = 10
Output: 3
Explanation: 3 will win the first 10 rounds consecutively.

Example 3:

Input: arr = [1,9,8,2,3,7,6,4,5], k = 7
Output: 9

Example 4:

Input: arr = [1,11,22,33,44,55,66,77,88,99], k = 1000000000
Output: 99

Constraints:

`2 <= arr.length <= 10^5`

`1 <= arr[i] <= 10^6`

`arr` contains distinct integers.

`1 <= k <= 10^9`

【中文翻译】
给定一个由不同整数组成的数组 arr 和一个整数 k。
游戏在数组的前两个元素之间进行。每轮比较 arr[0] 和 arr[1]，较大的获胜并保持在位置 0，
较小的移到数组末尾。当某个整数连续赢得 k 轮时游戏结束。返回获胜的整数。

示例 1：

输入：arr = [2,1,3,5,4,6,7], k = 2
输出：5
解释：经过 4 轮后，5 连续获胜 2 次成为赢家。

示例 2：

输入：arr = [3,2,1], k = 10
输出：3
解释：3 将连续赢得前 10 轮。

示例 3：

输入：arr = [1,9,8,2,3,7,6,4,5], k = 7
输出：9

示例 4：

输入：arr = [1,11,22,33,44,55,66,77,88,99], k = 1000000000
输出：99
"""

from typing import List, Optional


class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        n = len(arr)
        if k >= n:
            return max(arr)
        winner = arr[0]
        wins = 0
        for i in range(1, n):
            if arr[i] > winner:
                winner = arr[i]
                wins = 1
            else:
                wins += 1
            if wins == k:
                return winner
        return winner



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 不需要模拟整个游戏过程。注意到：如果 k >= n，最大值一定会成为赢家。
# 对于 k < n，只需遍历一次数组。维护当前赢家 winner 和连胜次数 wins。
# 对于每个新元素 arr[i]，如果大于 winner 则更换赢家并重置 wins=1，否则 wins++。
# 如果 wins == k 则返回当前赢家。遍历完仍未达到 k，则返回当前赢家（即最大值）。
#
# 时间复杂度: O(N)
# 空间复杂度: O(1)
#
# 关键点:
# - 如果 k >= len(arr)，最大值必定获胜
# - 无需实际移动元素，只需追踪当前赢家和连胜次数
# - 一轮遍历即可确定结果
