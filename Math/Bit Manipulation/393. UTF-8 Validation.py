"""
LeetCode #393 - UTF-8 Validation
中文题名：UTF-8 编码验证
https://leetcode.com/problems/utf-8-validation/

A character in UTF8 can be from 1 to 4 bytes long, subjected to the following rules:

For 1-byte character, the first bit is a 0, followed by its unicode code.

For n-bytes character, the first n-bits are all one's, the n+1 bit is 0, followed by n-1
bytes with most significant 2 bits being 10.

This is how the UTF-8 encoding would work:

`   Char. number range  |        UTF-8 octet sequence
(hexadecimal)    |              (binary)
--------------------+---------------------------------------------
0000 0000-0000 007F | 0xxxxxxx
0000 0080-0000 07FF | 110xxxxx 10xxxxxx
0000 0800-0000 FFFF | 1110xxxx 10xxxxxx 10xxxxxx
0001 0000-0010 FFFF | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
`

Given an array of integers representing the data, return whether it is a valid utf-8
encoding.

Note:

The input is an array of integers. Only the least significant 8 bits of each integer
is used to store the data. This means each integer represents only 1 byte of data.

Example 1:

data = [197, 130, 1], which represents the octet sequence: 11000101 10000010 00000001.

Return true.
It is a valid utf-8 encoding for a 2-bytes character followed by a 1-byte character.

Example 2:

data = [235, 140, 4], which represented the octet sequence: 11101011 10001100 00000100.

Return false.
The first 3 bits are all one's and the 4th bit is 0 means it is a 3-bytes character.
The next byte is a continuation byte which starts with 10 and that's correct.
But the second continuation byte does not start with 10, so it is invalid.

【中文翻译】
UTF-8 中的一个字符的长度可以是 1 到 4 个字节，遵循以下规则：

对于 1 字节字符，第一个位为 0，后面跟着其 Unicode 码。

对于 n 字节字符，前 n 位都是 1，第 n+1 位是 0，后面跟着 n-1 个字节，每个字节的最高两位是 10。

UTF-8 编码的工作方式如下：

   字符编号范围      |        UTF-8 字节序列
   (十六进制)        |           (二进制)
--------------------+---------------------------------------------
0000 0000-0000 007F | 0xxxxxxx
0000 0080-0000 07FF | 110xxxxx 10xxxxxx
0000 0800-0000 FFFF | 1110xxxx 10xxxxxx 10xxxxxx
0001 0000-0010 FFFF | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx

给定一个表示数据的整数数组，返回它是否是有效的 UTF-8 编码。

注意：

输入是一个整数数组。每个整数只使用最低有效 8 位来存储数据。这意味着每个整数只代表 1 个字节的数据。

示例 1：

data = [197, 130, 1]，表示字节序列：11000101 10000010 00000001。

返回 true。
这是一个有效的 UTF-8 编码，包含一个 2 字节字符后跟一个 1 字节字符。

示例 2：

data = [235, 140, 4]，表示字节序列：11101011 10001100 00000100。

返回 false。
前 3 位都是 1 且第 4 位是 0，意味着它是一个 3 字节字符。
下一个字节是以 10 开头的延续字节，这是正确的。
但是第二个延续字节不是以 10 开头，所以是无效的。
"""

from typing import List, Optional


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        # 需要跟进的延续字节数
        remaining = 0

        for byte in data:
            # 只取低 8 位
            byte &= 0xFF

            if remaining == 0:
                # 判断当前字节是几字节字符的开头
                if byte >> 7 == 0:        # 0xxxxxxx: 1 字节
                    continue
                elif byte >> 5 == 0b110:  # 110xxxxx: 2 字节
                    remaining = 1
                elif byte >> 4 == 0b1110: # 1110xxxx: 3 字节
                    remaining = 2
                elif byte >> 3 == 0b11110:# 11110xxx: 4 字节
                    remaining = 3
                else:
                    return False
            else:
                # 延续字节必须为 10xxxxxx
                if byte >> 6 != 0b10:
                    return False
                remaining -= 1

        return remaining == 0











# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 逐个字节扫描验证 UTF-8 编码规则。
# 1. 维护一个计数器 remaining，表示当前字符还需要多少个后续的延续字节（10xxxxxx）。
# 2. 遍历每个字节（只取低 8 位）：
#    - 如果 remaining == 0，说明需要判断当前字节是一个新字符的开头：
#      * 0xxxxxxx → 1 字节字符，直接跳过（remaining 保持 0）
#      * 110xxxxx → 2 字节字符，设置 remaining = 1
#      * 1110xxxx → 3 字节字符，设置 remaining = 2
#      * 11110xxx → 4 字节字符，设置 remaining = 3
#      * 其他情况 → 无效，返回 False
#    - 如果 remaining > 0，说明当前字节应该是延续字节：
#      * 必须以 10 开头（byte >> 6 == 0b10），否则返回 False
#      * remaining -= 1
# 3. 遍历结束后，remaining 必须为 0（没有未闭合的多字节字符）。
#
# 时间复杂度: O(n) - 遍历数组一次，n 为字节数
# 空间复杂度: O(1) - 只使用常数个变量
#
# 关键点:
# - 只取每个整数的低 8 位（byte & 0xFF）
# - 使用位移操作判断字节类型（>> 7, >> 5, >> 4, >> 3）
# - 延续字节统一检查（>> 6 == 0b10）
# - 注意 0b10 是二进制字面量，表示十进制的 2
# - 最后检查 remaining == 0 确保没有不完整的多字节字符
