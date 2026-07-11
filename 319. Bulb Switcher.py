"""
LeetCode #319 - Bulb Switcher
中文题名：灯泡开关
https://leetcode.com/problems/bulb-switcher/

There are n bulbs that are initially off. You first turn on all the bulbs. Then, you
turn off every second bulb. On the third round, you toggle every third bulb (turning on if
it's off or turning off if it's on). For the i-th round, you toggle every i
bulb. For the n-th round, you only toggle the last bulb. Find how many bulbs are on
after n rounds.

Example:

Input: 3
Output: 1
Explanation:
At first, the three bulbs are [off, off, off].
After first round, the three bulbs are [on, on, on].
After second round, the three bulbs are [on, off, on].
After third round, the three bulbs are [on, off, off].

So you should return 1, because there is only one bulb is on.

【中文翻译】
初始时有 n 个灯泡处于关闭状态。第一轮，你打开所有的灯泡。第二轮，你每两个灯泡关闭一个（即关闭第 2、4、6… 个灯泡）。
第三轮，你每三个灯泡切换一次开关（即打开关闭的灯泡，关闭打开的灯泡）。
第 i 轮，你每 i 个灯泡切换一次开关。第 n 轮，你只切换最后一个灯泡的开关。
找出 n 轮之后有多少个亮着的灯泡。

示例：

输入：3
输出：1
解释：
初始时，三个灯泡状态为 [关, 关, 关]。
第一轮后，三个灯泡状态为 [开, 开, 开]。
第二轮后，三个灯泡状态为 [开, 关, 开]。
第三轮后，三个灯泡状态为 [开, 关, 关]。

所以你应该返回 1，因为只有一个灯泡亮着。
"""

from typing import List, Optional
import math


class Solution:
    def bulbSwitch(self, n: int) -> int:
        return math.isqrt(n)











# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 一个灯泡最终亮着当且仅当它在 n 轮中被切换了奇数次。
# 第 k 个灯泡在第 i 轮被切换，当且仅当 i 能整除 k（即 i 是 k 的因数）。
# 因此，第 k 个灯泡被切换的次数等于 k 的因数个数。
# 只有完全平方数有奇数个因数（因子成对出现，只有平方根与自己配对）。
# 所以最终亮着的灯泡数就是 1 到 n 中完全平方数的个数，即 floor(sqrt(n))。
#
# 时间复杂度: O(1)
# 空间复杂度: O(1)
#
# 关键点:
# - 只有完全平方数有奇数个因数
# - 问题转化为求 sqrt(n) 的整数部分
# - math.isqrt(n) 返回 n 的整数平方根（Python 3.8+）
