"""
LeetCode #1414 - Find the Minimum Number of Fibonacci Numbers Whose Sum Is K
中文题名：和为 K 的最少斐波那契数字数目
https://leetcode.com/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k/

Given the number `k`, return the minimum number of Fibonacci numbers
whose sum is equal to `k`, whether a Fibonacci number could be used
multiple times.

The Fibonacci numbers are defined as:

F1 = 1

F2 = 1

Fn = Fn-1 + Fn-2 , for n > 2.

It is guaranteed that for the given constraints we can always find such fibonacci
numbers that sum `k`.

Example 1:

Input: k = 7
Output: 2
Explanation: The Fibonacci numbers are: 1, 1, 2, 3, 5, 8, 13, ...
For k = 7 we can use 2 + 5 = 7.

Example 2:

Input: k = 10
Output: 2
Explanation: For k = 10 we can use 2 + 8 = 10.

Example 3:

Input: k = 19
Output: 3
Explanation: For k = 19 we can use 1 + 5 + 13 = 19.

Constraints:

`1 <= k <= 10^9`

【中文翻译】

给定一个整数 `k`，返回和为 `k` 的最少斐波那契数字数目，其中每个斐波那契数字可以被多次使用。

斐波那契数字定义为：

F1 = 1
F2 = 1
Fn = Fn-1 + Fn-2，其中 n > 2。

题目保证对于给定的约束条件，我们总能找到和为 `k` 的斐波那契数字。

示例 1：
输入：k = 7
输出：2
解释：斐波那契数字为：1, 1, 2, 3, 5, 8, 13, ...
对于 k = 7，我们可以使用 2 + 5 = 7。

示例 2：
输入：k = 10
输出：2
解释：对于 k = 10，我们可以使用 2 + 8 = 10。

示例 3：
输入：k = 19
输出：3
解释：对于 k = 19，我们可以使用 1 + 5 + 13 = 19。

约束条件：
`1 <= k <= 10^9`

"""

from typing import List, Optional


class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        # 生成不超过 k 的所有斐波那契数
        fib = [1, 1]
        while fib[-1] < k:
            fib.append(fib[-1] + fib[-2])
        # 如果最后的数超过 k，去除它
        if fib[-1] > k:
            fib.pop()

        count = 0
        # 从大到小贪心地减去最大的斐波那契数
        for i in range(len(fib) - 1, -1, -1):
            if k >= fib[i]:
                k -= fib[i]
                count += 1
            if k == 0:
                break

        return count



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 贪心法（类似于找零钱问题，但斐波那契数具有特殊的性质）：
# 1. 生成所有不超过 k 的斐波那契数，存入数组 fib。
# 2. 从大到小遍历 fib 数组，对于每个斐波那契数 fib[i]：
#    a. 如果 k >= fib[i]，则从 k 中减去 fib[i]，计数加 1。
#    b. 如果 k == 0，跳出循环。
# 3. 返回计数。
#
# 贪心正确性：斐波那契数满足 Zeckendorf 定理——每个正整数都可以唯一地表示为
# 不连续的斐波那契数之和。贪心选择可以保证选出最少数量的斐波那契数。
# 通俗地说，对于斐波那契数列，每次选择不大于当前剩余值的最大的那个，
# 一定能够得到最优解。这本质上是因为相邻斐波那契数之间满足 2*F(n-1) > F(n) 的性质。
#
# 时间复杂度: O(log K)，斐波那契数以指数级增长，生成的斐波那契数个数约为 O(log K)。
# 空间复杂度: O(log K)，用于存储生成的斐波那契数列。
#
# 关键点:
# - 斐波那契数增长极快（指数级），数量很少
# - 贪心策略有效：每次选不大于 k 的最大斐波那契数
# - 可以使用 while 循环从大到小选择，无需预先存储整个数组










