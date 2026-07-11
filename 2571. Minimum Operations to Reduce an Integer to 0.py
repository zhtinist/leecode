"""
LeetCode #2571 - Minimum Operations to Reduce an Integer to 0
将整数减少到零需要的最少操作数
https://leetcode.cn/problems/minimum-operations-to-reduce-an-integer-to-0/

给你一个正整数 `n` ，你可以执行下述操作 任意 次：
`n` 加上或减去 `2` 的某个 幂
返回使 `n` 等于 `0` 需要执行的 最少 操作数。
如果 `x == 2^i` 且其中 `i >= 0` ，则数字 `x` 是 `2` 的幂。

示例 1：
输入：n = 39 输出：3 解释：我们可以执行下述操作： - n 加上 2^0 = 1 ，得到 n = 40 。 - n 减去 2^3 = 8 ，得到 n = 32 。 - n 减去 2^5 = 32 ，得到 n = 0 。 可以证明使 n 等于 0 需要执行的最少操作数是 3 。
示例 2：
输入：n = 54 输出：3 解释：我们可以执行下述操作： - n 加上 2^1 = 2 ，得到 n = 56 。 - n 加上 2^3 = 8 ，得到 n = 64 。 - n 减去 2^6 = 64 ，得到 n = 0 。 使 n 等于 0 需要执行的最少操作数是 3 。

提示：
`1 <= n <= 10^5`
"""

from typing import List, Optional


class Solution:
    def minOperations(self, n: int) -> int:
        ans = 0
        while n > 0:
            if n & 1:
                if n & 2:
                    n += 1  # carry: replace run of 1s with one operation
                else:
                    n -= 1  # subtract isolated 1
                ans += 1
            n >>= 1
        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Bit Manipulation, Dynamic Programming
#
# 解题思路:
# 贪心扫描二进制位。当前位为1时：若下一位也为1（连续1游程），则加2^k产生进位
# （将多个1合并为一次操作）；若下一位为0（孤立1），则减2^k抵消此位。
# 每次操作后右移继续处理。此贪心等价于计算最优的有符号2的幂展开。
#
# 时间复杂度: O(log N)
# 空间复杂度: O(1)
#
# 关键点:
# - 连续1游程(11...1)可以用一次进位(+2^k)合并处理，比逐个消去更优
# - 孤立1只需一次减法
# - n+=1产生进位可能传播，但算法通过位右移逐步处理
