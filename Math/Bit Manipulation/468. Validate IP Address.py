"""
LeetCode #468 - Validate IP Address
中文题名：验证IP地址
https://leetcode.com/problems/validate-ip-address/

Write a function to check whether an input string is a valid IPv4 address or IPv6 address or
neither.

IPv4 addresses are canonically represented in dot-decimal notation, which consists of
four decimal numbers, each ranging from 0 to 255, separated by dots ("."), e.g.,`172.16.254.1`;

Besides, leading zeros in the IPv4 is invalid. For example, the address
`172.16.254.01` is invalid.

IPv6 addresses are represented as eight groups of four hexadecimal digits, each group
representing 16 bits. The groups are separated by colons (":"). For example, the address
`2001:0db8:85a3:0000:0000:8a2e:0370:7334` is a valid one. Also, we could omit
some leading zeros among four hexadecimal digits and some low-case characters in the address
to upper-case ones, so `2001:db8:85a3:0:0:8A2E:0370:7334` is also a valid IPv6
address(Omit leading zeros and using upper cases).

However, we don't replace a consecutive group of zero value with a single empty group using
two consecutive colons (::) to pursue simplicity. For example, `2001:0db8:85a3::8A2E:0370:7334`
is an invalid IPv6 address.

Besides, extra leading zeros in the IPv6 is also invalid. For example, the address `02001:0db8:85a3:0000:0000:8a2e:0370:7334`
is invalid.

Note:
You may assume there is no extra space or special characters in the input string.

Example 1:

Input: "172.16.254.1"

Output: "IPv4"

Explanation: This is a valid IPv4 address, return "IPv4".

Example 2:

Input: "2001:0db8:85a3:0:0:8A2E:0370:7334"

Output: "IPv6"

Explanation: This is a valid IPv6 address, return "IPv6".

Example 3:

Input: "256.256.256.256"

Output: "Neither"

Explanation: This is neither a IPv4 address nor a IPv6 address.

【中文翻译】
编写一个函数来检查输入字符串是有效的 IPv4 地址、IPv6 地址还是两者都不是。

IPv4 地址以点分十进制表示，由四个十进制数组成（0 到 255），以点 (".") 分隔，如 `172.16.254.1`。
IPv4 不允许前导零，如 `172.16.254.01` 无效。

IPv6 地址由八组四位十六进制数字组成，每组 16 位，以冒号 (":") 分隔，如
`2001:0db8:85a3:0000:0000:8a2e:0370:7334`。允许省略前导零、使用大写字母，故
`2001:db8:85a3:0:0:8A2E:0370:7334` 也有效。但不允许用双冒号 (::) 压缩连续零组，
`2001:0db8:85a3::8A2E:0370:7334` 无效。IPv6 不允许多余前导零，如 `02001:0db8:...` 无效。

示例 1：
    输入："172.16.254.1"
    输出："IPv4"

示例 2：
    输入："2001:0db8:85a3:0:0:8A2E:0370:7334"
    输出："IPv6"

示例 3：
    输入："256.256.256.256"
    输出："Neither"
"""

from typing import List, Optional


class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        """
        Validate whether the input string is IPv4, IPv6, or neither
        by checking the separator and applying IPv4/IPv6 rules.
        """

        def is_ipv4(s: str) -> bool:
            parts = s.split(".")
            if len(parts) != 4:
                return False
            for part in parts:
                if not part or not part.isdigit():
                    return False
                if len(part) > 1 and part[0] == "0":
                    return False  # leading zero
                if int(part) > 255:
                    return False
            return True

        def is_ipv6(s: str) -> bool:
            parts = s.split(":")
            if len(parts) != 8:
                return False
            hex_digits = set("0123456789abcdefABCDEF")
            for part in parts:
                if not part or len(part) > 4:
                    return False
                if any(ch not in hex_digits for ch in part):
                    return False
            return True

        if queryIP.count(".") == 3 and is_ipv4(queryIP):
            return "IPv4"
        if queryIP.count(":") == 7 and is_ipv6(queryIP):
            return "IPv6"
        return "Neither"



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 分别实现 IPv4 和 IPv6 的验证函数，然后根据输入字符串的分隔符特征判断调用哪个。
# IPv4：按 "." 拆分，必须恰好 4 段，每段必须是纯数字、值在 0-255 之间，且不能有
# 前导零（"0" 本身除外）。IPv6：按 ":" 拆分，必须恰好 8 段，每段长度 1-4 位，
# 每位必须是合法的十六进制字符（0-9, a-f, A-F）。先通过 count(".") == 3 或
# count(":") == 7 快速筛选，再调用相应的验证逻辑。
#
# 时间复杂度: O(N) — 遍历输入字符串一次（split 和验证均线性）
# 空间复杂度: O(N) — split 产生的列表存储所有分段
#
# 关键点:
# - 前导零判断：长度 > 1 且首字符为 '0' 即非法
# - IPv6 每位必须是合法 hex 字符
# - 用 count() 快速区分 IPv4 和 IPv6 场景
# - ""（空字符串）的边界处理
