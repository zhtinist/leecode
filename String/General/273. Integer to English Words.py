"""
LeetCode #273 - Integer to English Words
中文题名：整数转换英文表示
https://leetcode.com/problems/integer-to-english-words/

Convert a non-negative integer to its english words representation. Given input is guaranteed
to be less than 2^31 - 1.

Example 1:

Input: 123
Output: "One Hundred Twenty Three"

Example 2:

Input: 12345
Output: "Twelve Thousand Three Hundred Forty Five"

Example 3:

Input: 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

Example 4:

Input: 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"

【中文翻译】
将非负整数转换为英文单词表示。给定输入保证小于 2^31 - 1。

示例 1：

输入：123
输出："One Hundred Twenty Three"

示例 2：

输入：12345
输出："Twelve Thousand Three Hundred Forty Five"

示例 3：

输入：1234567
输出："One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

示例 4：

输入：1234567891
输出："One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
"""

from typing import List, Optional


class Solution:
    def numberToWords(self, num: int) -> str:
        """Convert a non-negative integer to English words."""
        if num == 0:
            return "Zero"

        # Words for basic numbers
        ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
                "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen",
                "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        thousands = ["", "Thousand", "Million", "Billion"]

        def helper(n: int) -> str:
            """Convert number < 1000 to English words."""
            if n == 0:
                return ""
            if n < 20:
                return ones[n] + " "
            if n < 100:
                return tens[n // 10] + " " + helper(n % 10)
            # n >= 100
            return ones[n // 100] + " Hundred " + helper(n % 100)

        result = ""
        i = 0  # index for thousands array
        while num > 0:
            chunk = num % 1000
            if chunk != 0:
                result = helper(chunk) + thousands[i] + " " + result
            num //= 1000
            i += 1

        return result.strip()


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Hard
# Paid Only: No
#
# 解题思路:
# 将数字按三位一组（千位分隔）拆分处理。每一组（0-999）可以用一个辅助函数
# 转换为英文：先处理百位，再处理十位和个位（注意 1-19 有特殊词汇）。
# 然后在每组后面加上对应的量级词（Thousand, Million, Billion）。
# 从低位到高位逐组处理，结果从后往前拼接。
#
# 时间复杂度: O(1) - 数字范围固定（< 2^31），操作次数与数字位数有关，最多10位
# 空间复杂度: O(1) - 只使用固定大小的数组和递归栈（深度不超过3层）
#
# 关键点:
# - 按每三位一组拆分（西方数字的千位分隔习惯）
# - 1-19 有独立的英文单词需要特殊处理
# - 注意处理 chunk 为 0 的情况（跳过该组）
# - 注意去掉尾部空格（使用 strip）
