"""
LeetCode #1423 - Maximum Points You Can Obtain from Cards
中文题名：可获得的最大点数
https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

There are several cards arranged in a row, and each card has
an associated number of points The points are given in the integer
array `cardPoints`.

In one step, you can take one card from the beginning or from the end of the row. You
have to take exactly `k` cards.

Your score is the sum of the points of the cards you have taken.

Given the integer array `cardPoints` and the integer `k`,
return the maximum score you can obtain.

Example 1:

Input: cardPoints = [1,2,3,4,5,6,1], k = 3
Output: 12
Explanation: After the first step, your score will always be 1. However, choosing the rightmost card first will maximize your total score. The optimal strategy is to take the three cards on the right, giving a final score of 1 + 6 + 5 = 12.

Example 2:

Input: cardPoints = [2,2,2], k = 2
Output: 4
Explanation: Regardless of which two cards you take, your score will always be 4.

Example 3:

Input: cardPoints = [9,7,7,9,7,7,9], k = 7
Output: 55
Explanation: You have to take all the cards. Your score is the sum of points of all cards.

Example 4:

Input: cardPoints = [1,1000,1], k = 1
Output: 1
Explanation: You cannot take the card in the middle. Your best score is 1.

Example 5:

Input: cardPoints = [1,79,80,1,1,1,200,1], k = 3
Output: 202

Constraints:

`1 <= cardPoints.length <= 10^5`

`1 <= cardPoints[i] <= 10^4`

`1 <= k <= cardPoints.length`

【中文翻译】

有几张卡片排成一行，每张卡片都有一个对应的点数。点数在整数数组 `cardPoints` 中给出。

每一步，你可以从行首或行尾取一张卡片。你必须恰好取 `k` 张卡片。

你的得分是你取到的卡片的点数之和。

给定整数数组 `cardPoints` 和整数 `k`，返回你能获得的最大得分。

示例 1：
输入：cardPoints = [1,2,3,4,5,6,1], k = 3
输出：12
解释：第一步后，你的得分始终为 1。然而，先拿最右边的卡片可以最大化你的总得分。最佳策略是取最右边的三张卡片，最终得分为 1 + 6 + 5 = 12。

示例 2：
输入：cardPoints = [2,2,2], k = 2
输出：4
解释：无论你取哪两张卡片，你的得分始终为 4。

示例 3：
输入：cardPoints = [9,7,7,9,7,7,9], k = 7
输出：55
解释：你必须取走所有卡片。你的得分是所有卡片点数之和。

示例 4：
输入：cardPoints = [1,1000,1], k = 1
输出：1
解释：你不能取中间的卡片。你最好的得分是 1。

示例 5：
输入：cardPoints = [1,79,80,1,1,1,200,1], k = 3
输出：202

约束条件：
`1 <= cardPoints.length <= 10^5`
`1 <= cardPoints[i] <= 10^4`
`1 <= k <= cardPoints.length`

"""

from typing import List, Optional


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        total = sum(cardPoints)

        # 如果取所有卡片，直接返回总和
        if k == n:
            return total

        # 滑动窗口找长度为 n - k 的最小子数组和
        window_size = n - k
        # 初始窗口
        window_sum = sum(cardPoints[:window_size])
        min_window_sum = window_sum

        for i in range(window_size, n):
            # 窗口右移一格
            window_sum += cardPoints[i] - cardPoints[i - window_size]
            min_window_sum = min(min_window_sum, window_sum)

        # 最大得分 = 总和 - 中间未取的最小子数组和
        return total - min_window_sum



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 滑动窗口法（等价转换）：
# 1. 取 k 张卡片，可以从左端取，从右端取，或两端混合取。
#    等价于：留下中间连续的 n-k 张卡片不取，取走两端共 k 张。
# 2. 因此，最大得分 = 数组总和 - 中间长度为 n-k 的最小连续子数组和。
#    问题转换为：找长度为 (n-k) 的最小子数组和。
# 3. 使用固定大小的滑动窗口：
#    a. 计算初始窗口（前 n-k 个元素）的和。
#    b. 滑动窗口每次右移一位，更新窗口和：
#       window_sum = window_sum + cardPoints[i] - cardPoints[i - window_size]
#    c. 跟踪最小的窗口和。
# 4. 返回 total - min_window_sum。
#
# 时间复杂度: O(N)，只遍历一次数组。
# 空间复杂度: O(1)，只使用常数级额外空间。
#
# 关键点:
# - 等价转换：取 k 张 = 总和 - 保留 n-k 张（中间连续子数组）
# - 固定窗口滑动找最小子数组和
# - 边界情况：k == n 时直接返回总和










