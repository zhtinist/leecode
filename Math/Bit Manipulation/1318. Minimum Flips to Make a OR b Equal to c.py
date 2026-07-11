"""
LeetCode #1318 - Minimum Flips to Make a OR b Equal to c
中文题名：或运算的最小翻转次数
https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/

Given 3 positives numbers `a`, `b` and `c`. Return
the minimum flips required in some bits of `a` and `b` to make ( `a`
OR `b` == `c` ). (bitwise OR operation).

Flip operation consists of change any single bit 1 to 0
or change the bit 0 to 1 in their binary representation.

Example 1:

Input: a = 2, b = 6, c = 5
Output: 3
Explanation: After flips a = 1 , b = 4 , c = 5 such that (`a` OR `b` == `c`)

Example 2:

Input: a = 4, b = 2, c = 7
Output: 1

Example 3:

Input: a = 1, b = 2, c = 3
Output: 0

Constraints:

`1 <= a <= 10^9`

`1 <= b <= 10^9`

`1 <= c <= 10^9`

【中文翻译】
给定三个正整数 a、b 和 c。返回使得 (a OR b == c) 成立所需的最少翻转次数。
（翻转操作指将某个二进制位从 1 变为 0 或从 0 变为 1。）

示例 1：
输入：a = 2, b = 6, c = 5
输出：3
解释：翻转后 a = 1，b = 4，c = 5，满足 (a OR b == c)

示例 2：
输入：a = 4, b = 2, c = 7
输出：1

示例 3：
输入：a = 1, b = 2, c = 3
输出：0

约束条件：
1 <= a <= 10^9
1 <= b <= 10^9
1 <= c <= 10^9
"""

from typing import List


class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0
        while a > 0 or b > 0 or c > 0:
            bit_a = a & 1
            bit_b = b & 1
            bit_c = c & 1

            if bit_c == 1:
                # c 的当前位为 1，需要 a|b 的该位为 1
                # 如果 a 和 b 都是 0，只需翻转 1 次（将 a 或 b 翻转为 1）
                if bit_a == 0 and bit_b == 0:
                    flips += 1
            else:
                # c 的当前位为 0，需要 a|b 的该位为 0
                # 如果 a 或 b 是 1，都需要翻转为 0
                flips += bit_a + bit_b  # 每个 1 需要 1 次翻转

            a >>= 1
            b >>= 1
            c >>= 1

        return flips



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 逐位分析，对 a、b、c 的每一位进行判断。
# 对于每一位，取出 a、b、c 在该位的值（通过 & 1 和右移操作）。
# 分两种情况讨论：
# 情况 1：c 的当前位为 1
#   - 目标是让 a|b 的该位为 1。
#   - 如果 a 或 b 至少有一个 1，不需要翻转（0 次）。
#   - 如果 a 和 b 都是 0，只需翻转其中一个（1 次）。
# 情况 2：c 的当前位为 0
#   - 目标是让 a|b 的该位为 0。
#   - 需要将 a 和 b 中所有为 1 的位翻转为 0。
#   - 翻转次数 = bit_a + bit_b（每个 1 需要 1 次翻转）。
# 循环处理所有位，直到三个数都变成 0。
#
# 时间复杂度: O(1)，最多处理 30-32 位（a,b,c <= 10^9 < 2^30）
# 空间复杂度: O(1)，只使用常数个变量
#
# 关键点:
# - 位运算题核心：逐位独立分析
# - a & 1 获取最低位，>>= 1 右移继续处理下一位
# - c 位为 1 但 a、b 都是 0：翻 1 次（任意一个是 0->1）
# - c 位为 0 但 a 或 b 是 1：每个 1 翻 1 次（1->0）
# - 翻转次数 = 针对 a 和 b 的修改，不涉及 c 的修改
# - 循环条件 a>0 or b>0 or c>0 而非固定 32 次，更高效










