"""
LeetCode #2457 - Minimum Addition to Make Integer Beautiful
美丽整数的最小增量
https://leetcode.cn/problems/minimum-addition-to-make-integer-beautiful/

给你两个正整数 `n` 和 `target` 。
如果某个整数每一位上的数字相加小于或等于 `target` ，则认为这个整数是一个 美丽整数 。
找出并返回满足 `n + x` 是 美丽整数 的最小非负整数 `x` 。生成的输入保证总可以使 `n` 变成一个美丽整数。

示例 1：
输入：n = 16, target = 6 输出：4 解释：最初，n 是 16 ，且其每一位数字的和是 1 + 6 = 7 。在加 4 之后，n 变为 20 且每一位数字的和变成 2 + 0 = 2 。可以证明无法加上一个小于 4 的非负整数使 n 变成一个美丽整数。
示例 2：
输入：n = 467, target = 6 输出：33 解释：最初，n 是 467 ，且其每一位数字的和是 4 + 6 + 7 = 17 。在加 33 之后，n 变为 500 且每一位数字的和变成 5 + 0 + 0 = 5 。可以证明无法加上一个小于 33 的非负整数使 n 变成一个美丽整数。
示例 3：
输入：n = 1, target = 1 输出：0 解释：最初，n 是 1 ，且其每一位数字的和是 1 ，已经小于等于 target 。

提示：
`1 <= n <= 10^12`
`1 <= target <= 150`
生成的输入保证总可以使 `n` 变成一个美丽整数。
"""

from typing import List, Optional


class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        def digit_sum(num: int) -> int:
            """计算 num 的各位数字之和"""
            s = 0
            while num > 0:
                s += num % 10
                num //= 10
            return s

        if digit_sum(n) <= target:
            return 0

        # 从最低位开始，尝试将某些低位变为0并进位
        # n' = ((n // (10**i)) + 1) * (10**i)，即把末 i 位全部置0并向高位进1
        ans = float('inf')
        for i in range(14):  # n 最大 10^12，13位数字足够
            power = 10 ** i
            # 将末 i 位清零并进位
            rounded = ((n // power) + 1) * power
            if digit_sum(rounded) <= target:
                ans = min(ans, rounded - n)

        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Math
#
# 解题思路:
# 贪心法：如果 n 的各位数字之和已经 <= target，直接返回 0。
# 否则，要让数字和变小，最有效的方式是将低位数字变为 0 并进位。
# 具体做法：枚举 i 从 0 到 13（因为 n <= 10^12），对于每个 i：
#   1. 计算 power = 10^i
#   2. 计算 rounded = ((n // power) + 1) * power，即把末 i 位清零并向第 i+1 位进 1
#   3. 检查 rounded 的数字和是否 <= target，若是则候选答案为 rounded - n
# 取所有候选答案的最小值。这种贪心策略的正确性在于，任何能使数字和 <= target 的增量
# 必然对应着将某几位清零并进位的操作。
#
# 时间复杂度: O((log n)^2)，外层循环 O(log n)，每次 digit_sum 也是 O(log n)
# 空间复杂度: O(1)
#
# 关键点:
# - 数字和只能通过进位+清零来减小
# - 枚举所有可能的进位位置，取最小增量
# - n 最大为 10^12，所以枚举 0 到 13 位即可
