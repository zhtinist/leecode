"""
LeetCode #263 - Ugly Number
中文题名：丑数
https://leetcode.com/problems/ugly-number/

Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include `2,
3, 5`.

Example 1:

Input: 6
Output: true
Explanation: 6 = 2 &times; 3

Example 2:

Input: 8
Output: true
Explanation: 8 = 2 &times; 2 &times; 2

Example 3:

Input: 14
Output: false
Explanation: `14` is not ugly since it includes another prime factor `7`.

Note:

`1` is typically treated as an ugly number.

Input is within the 32-bit signed integer range: [&minus;2^31,
2^31 &minus; 1].

【中文翻译】
编写一个程序判断给定的数是否为丑数。

丑数就是只包含质因数 `2, 3, 5` 的正整数。

示例 1：

输入：6
输出：true
解释：6 = 2 × 3

示例 2：

输入：8
输出：true
解释：8 = 2 × 2 × 2

示例 3：

输入：14
输出：false
解释：`14` 不是丑数，因为它包含另一个质因数 `7`。

注意：

`1` 通常被视为丑数。

输入在 32 位有符号整数范围内：[−2^31, 2^31 − 1]。
"""

from typing import List, Optional


class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False

        # 反复除以 2、3、5
        for factor in [2, 3, 5]:
            while n % factor == 0:
                n //= factor

        return n == 1


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Easy
# Paid Only: No
#
# 解题思路：
# 负数和非正数不是 ugly number（因为 ugly number 是正整数）。
# 对于正数，不断除以 2、3、5（只要能被整除就一直除）。
# 最后如果剩下 1，说明所有质因子都是 2、3、5；否则含有其他质因子。
#
# 时间复杂度: O(log n)
# 空间复杂度: O(1)
#
# 关键点：
# - n <= 0 返回 False
# - 循环除以 2、3、5 直到不能整除
# - 最终判断 n 是否等于 1
