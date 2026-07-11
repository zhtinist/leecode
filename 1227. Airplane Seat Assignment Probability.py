"""
LeetCode #1227 - Airplane Seat Assignment Probability
中文题名：飞机座位分配概率
https://leetcode.com/problems/airplane-seat-assignment-probability/

`n` passengers board an airplane with exactly `n` seats. The first passenger has lost the ticket
and picks a seat randomly. But after that, the rest of passengers will:

Take their own seat if it is still available,

Pick other seats randomly when they find their seat occupied

What is the probability that the n-th person can get his own seat?

Example 1:

Input: n = 1
Output: 1.00000
Explanation: The first person can only get the first seat.

Example 2:

Input: n = 2
Output: 0.50000
Explanation: The second person has a probability of 0.5 to get the second seat (when first person gets the first seat).

Constraints:

`1 <= n <= 10^5`

【中文翻译】
有 n 位乘客即将登机，飞机正好有 n 个座位。第一位乘客的票丢了，他随便挑了一个座位坐下。剩下的乘客将会：

- 如果他们的座位还空着，就坐自己的座位；
- 当他们发现自己的座位被占了，就会随机挑一个别的座位坐下。

请问第 n 位乘客坐到自己的座位上的概率是多少？

示例 1：

输入：n = 1
输出：1.00000
解释：第一个人只会坐在第一个座位上。

示例 2：

输入：n = 2
输出：0.50000
解释：第二个人有 0.5 的概率坐在第二个座位上（当第一个人坐在第一个座位上时）。

约束条件：

`1 <= n <= 10^5`
"""

from typing import List, Optional


class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        return 1.0 if n == 1 else 0.5










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 数学归纳法。设 f(n) 为第 n 位乘客坐到第 n 个座位的概率。
# 第一位乘客随机选座，有三种情况：
# 1. 选了第 1 个座位(自己的)——概率 1/n，此时后面所有人都能坐自己的座位，第 n 位乘客一定能坐到自己的座位。
# 2. 选了第 n 个座位——概率 1/n，此时第 n 位乘客一定坐不到自己的座位。
# 3. 选了第 k 个座位(1 < k < n)——概率 (n-2)/n，此时第 2 到第 k-1 位乘客都能坐自己的座位，
#    第 k 位乘客登机时发现座位被占，问题退化为规模为 n-k+1 的子问题 f(n-k+1)。
# 通过数学归纳法可证：f(1) = 1, f(2) = f(3) = ... = f(n) = 0.5 (n >= 2)。
#
# 时间复杂度: O(1)
# 空间复杂度: O(1)
#
# 关键点:
# - 核心是数学结论而非模拟：n=1 时概率为 1.0，n>=2 时概率恒为 0.5
# - 可通过递推公式 f(n) = 1/n + (n-2)/n * f(n-1) 用数学归纳法证明
# - 当 n >= 2 时答案恒为 0.5，与 n 的大小无关
