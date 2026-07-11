"""
LeetCode #1680 - Concatenation of Consecutive Binary Numbers
中文题名：连接连续二进制数字
https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/

Given an integer `n`, return the decimal value of
the binary string formed by concatenating the binary representations of
`1` to `n` in order,
modulo `109 + 7`.

Example 1:

Input: n = 1
Output: 1
Explanation: "1" in binary corresponds to the decimal value 1.

Example 2:

Input: n = 3
Output: 27
Explanation: In binary, 1, 2, and 3 corresponds to "1", "10", and "11".
After concatenating them, we have "11011", which corresponds to the decimal value 27.

Example 3:

Input: n = 12
Output: 505379714
Explanation: The concatenation results in "1101110010111011110001001101010111100".
The decimal value of that is 118505380540.
After modulo 109 + 7, the result is 505379714.

Constraints:

`1 <= n <= 105`

【中文翻译】
给定一个整数n，返回将1到n的二进制表示按顺序连接而成的二进制字符串所对应的十进制值，结果对10^9+7取模。

示例1：

输入：n = 1
输出：1
解释：二进制中的"1"对应的十进制值是1。

示例2：

输入：n = 3
输出：27
解释：二进制中，1、2、3分别对应"1"、"10"、"11"。
连接后得到"11011"，对应的十进制值是27。

示例3：

输入：n = 12
输出：505379714
解释：连接结果为"1101110010111011110001001101010111100"。
该值的十进制是118505380540。
对10^9+7取模后结果为505379714。

约束条件：

1 <= n <= 10^5

"""

from typing import List, Optional


class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        result = 0
        for i in range(1, n + 1):
            # 计算 i 的二进制表示的长度
            length = i.bit_length()
            # 将 result 左移 length 位（相当于在二进制末尾追加length个0），然后加上 i
            result = ((result << length) | i) % MOD
        return result










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 位运算。对于每个数i从1到n：
# 1. 获取i的二进制位数（i.bit_length()）
# 2. 将当前结果result左移length位，相当于在二进制末尾追加length个0
# 3. 通过按位或操作将i追加到result的二进制末尾
# 4. 对10^9+7取模防止溢出
# 这样就模拟了字符串连接过程，但使用整数位运算，效率更高。
#
# 时间复杂度: O(n)
# 空间复杂度: O(1)
#
# 关键点:
# - 位运算模拟二进制连接：result = (result << length) | i
# - i.bit_length()获取二进制位数
# - 每次操作后取模，防止溢出
