"""
LeetCode #1387 - Sort Integers by The Power Value
中文题名：将整数按权重排序
https://leetcode.com/problems/sort-integers-by-the-power-value/

The power of an integer `x` is defined as the number of steps needed to
transform `x` into `1` using the following steps:

if `x` is even then `x = x / 2`

if `x` is odd then `x = 3 * x + 1`

For example, the power of x = 3 is 7 because 3 needs 7 steps to become 1 (3 --> 10
--> 5 --> 16 --> 8 --> 4 --> 2 --> 1).

Given three integers `lo`, `hi` and `k`. The task is
to sort all integers in the interval `[lo, hi]` by the power value in
ascending order, if two or more integers have the
same power value sort them by ascending order.

Return the `k-th` integer in the range `[lo, hi]` sorted by the
power value.

Notice that for any integer `x` `(lo <= x <= hi)` it
is guaranteed that `x` will transform into
`1` using these steps and that the power of `x` is will
fit in 32 bit signed integer.

Example 1:

Input: lo = 12, hi = 15, k = 2
Output: 13
Explanation: The power of 12 is 9 (12 --> 6 --> 3 --> 10 --> 5 --> 16 --> 8 --> 4 --> 2 --> 1)
The power of 13 is 9
The power of 14 is 17
The power of 15 is 17
The interval sorted by the power value [12,13,14,15]. For k = 2 answer is the second element which is 13.
Notice that 12 and 13 have the same power value and we sorted them in ascending order. Same for 14 and 15.

Example 2:

Input: lo = 1, hi = 1, k = 1
Output: 1

Example 3:

Input: lo = 7, hi = 11, k = 4
Output: 7
Explanation: The power array corresponding to the interval [7, 8, 9, 10, 11] is [16, 3, 19, 6, 14].
The interval sorted by power is [8, 10, 11, 7, 9].
The fourth number in the sorted array is 7.

Example 4:

Input: lo = 10, hi = 20, k = 5
Output: 13

Example 5:

Input: lo = 1, hi = 1000, k = 777
Output: 570

Constraints:

`1 <= lo <= hi <= 1000`

`1 <= k <= hi - lo + 1`

【中文翻译】

整数 x 的"权重"定义为将其变为 1 所需的步数：
如果 x 是偶数：x = x / 2
如果 x 是奇数：x = 3 * x + 1

例如，x = 3 的权重为 7，因为 3 需要 7 步变为 1（3 --> 10 --> 5 --> 16 --> 8 --> 4 --> 2 --> 1）。

给定三个整数 lo、hi 和 k。将所有在 [lo, hi] 中的整数按权重升序排序，权重相同则按数值升序排序。返回排序后的第 k 个整数。

注意，对于任意整数 x (lo <= x <= hi)，保证能通过这些步变为 1，且权重在 32 位有符号整数范围内。

示例 1：
输入：lo = 12, hi = 15, k = 2
输出：13
解释：12 的权重为 9（12 --> 6 --> 3 --> 10 --> 5 --> 16 --> 8 --> 4 --> 2 --> 1）
13 的权重为 9
14 的权重为 17
15 的权重为 17
按权重排序的区间为 [12,13,14,15]。k = 2 返回第二个元素 13。
注意 12 和 13 权重相同，按数值升序排列。14 和 15 同理。

示例 2：
输入：lo = 1, hi = 1, k = 1
输出：1

示例 3：
输入：lo = 7, hi = 11, k = 4
输出：7
解释：[7, 8, 9, 10, 11] 对应权重 [16, 3, 19, 6, 14]。
按权重排序后为 [8, 10, 11, 7, 9]。第四个数是 7。

示例 4：
输入：lo = 10, hi = 20, k = 5
输出：13

示例 5：
输入：lo = 1, hi = 1000, k = 777
输出：570

约束条件：
1 <= lo <= hi <= 1000
1 <= k <= hi - lo + 1
"""

from typing import List, Optional


class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        memo = {}

        def power(x: int) -> int:
            if x == 1:
                return 0
            if x in memo:
                return memo[x]
            if x % 2 == 0:
                memo[x] = 1 + power(x // 2)
            else:
                memo[x] = 1 + power(3 * x + 1)
            return memo[x]

        # 生成区间内所有数字及其权重
        nums = [(power(i), i) for i in range(lo, hi + 1)]
        # 按 (权重, 数值) 升序排序
        nums.sort()
        return nums[k - 1][1]



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用记忆化递归计算每个数字的 Collatz（考拉兹）步数（权重）。
# 对于区间 [lo, hi] 中的每个数字，计算其权重并存储为 (权重, 数字) 元组。
# 按默认排序（先按权重，权重相同按数字）升序排列。
# 返回排序后第 k 个元素的数字部分。
#
# 时间复杂度: O(N log N)  N = hi - lo + 1，排序占主导
# 空间复杂度: O(N + M)  N 为区间大小，M 为记忆化缓存大小
#
# 关键点:
# - Collatz 猜想：每个正整数最终都会到达 1
# - 记忆化避免重复计算中间值的权重
# - Python 的 tuple 排序默认先按第一个元素，再按第二个元素，天然满足要求
# - 由于区间较小（<= 1000），也可以直接计算所有步数再排序










