"""
LeetCode #231 - Power of Two
中文题名：2 的幂
https://leetcode.com/problems/power-of-two/

Given an integer, write a function to determine if it is a power of two.

Example 1:

Input: 1
Output: true
Explanation: 2^0 = 1

Example 2:

Input: 16
Output: true
Explanation: 2^4 = 16

Example 3:

Input: 218
Output: false

【中文翻译】
给定一个整数，编写一个函数来判断它是否是 2 的幂次方。

示例 1：

输入：1
输出：true
解释：2^0 = 1

示例 2：

输入：16
输出：true
解释：2^4 = 16

示例 3：

输入：218
输出：false
"""

from typing import List, Optional


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Easy
# Paid Only: No
#
# 解题思路:
# 使用位运算判断一个数是否为 2 的幂。
# 2 的幂的二进制形式只包含一个 1，例如: 1(1), 2(10), 4(100), 8(1000)。
# 对于 n > 0，n & (n - 1) 会消除 n 最低位的 1。
# 如果 n 是 2 的幂，消除后结果为 0；如果 n 不是 2 的幂，消除后结果非 0。
# 例如: n = 8 (1000), n - 1 = 7 (0111), 8 & 7 = 0。
#
# 时间复杂度: O(1) - 单次位运算
# 空间复杂度: O(1) - 不使用额外空间
#
# 关键点:
# - 必须确保 n > 0，因为 0 和负数不是 2 的幂
# - n & (n - 1) == 0 是判断 2 的幂的标准位运算技巧
# - 也可用循环除以 2，但位运算 O(1) 更高效
