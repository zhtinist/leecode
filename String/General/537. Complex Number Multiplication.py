"""
LeetCode #537 - Complex Number Multiplication
中文题名：复数乘法
https://leetcode.com/problems/complex-number-multiplication/

Given two strings representing two complex
numbers.

You need to return a string representing their multiplication. Note i2 = -1
according to the definition.

Example 1:

Input: "1+1i", "1+1i"
Output: "0+2i"
Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.

Example 2:

Input: "1+-1i", "1+-1i"
Output: "0+-2i"
Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.

Note:

The input strings will not have extra blank.

The input strings will be given in the form of a+bi, where the integer a
and b will both belong to the range of [-100, 100]. And the output should be
also in this form.

【中文翻译】
给定两个以 "a+bi" 格式表示的复数字符串，返回它们相乘的结果字符串。
根据定义 i² = -1，复数乘法公式为：(a+bi) × (c+di) = (ac-bd) + (ad+bc)i。
输入字符串不会有多余空格，a 和 b 的范围均为 [-100, 100]，输出也需保持 "a+bi" 格式。

示例 1：
    输入："1+1i", "1+1i"
    输出："0+2i"
    解释：(1+i) × (1+i) = 1 + i² + 2i = 2i，转换为 0+2i 格式

示例 2：
    输入："1+-1i", "1+-1i"
    输出："0+-2i"
    解释：(1-i) × (1-i) = 1 + i² - 2i = -2i，转换为 0+-2i 格式
"""

from typing import List, Optional


class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        a1, b1 = self._parse(num1)
        a2, b2 = self._parse(num2)
        real = a1 * a2 - b1 * b2
        imag = a1 * b2 + a2 * b1
        return f"{real}+{imag}i"

    def _parse(self, s: str) -> tuple:
        """Parse 'a+bi' into (a, b) integers."""
        s = s.rstrip("i")
        parts = s.split("+")
        return int(parts[0]), int(parts[1])



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 将两个复数字符串分别解析为实部和虚部的整数，然后直接套用复数乘法公式：
# (a+bi)(c+di) = (ac-bd) + (ad+bc)i。解析时将字符串末尾的 'i' 去掉，
# 按 '+' 分割得到实部和虚部字符串，转为整数即可。最后用 f-string 拼接结果。
#
# 时间复杂度: O(1) — 字符串长度固定，解析和计算均为常数操作
# 空间复杂度: O(1) — 仅使用常数个变量
#
# 关键点:
# - 复数乘法公式：(a+bi)(c+di) = (ac-bd) + (ad+bc)i，牢记 i² = -1
# - 字符串解析注意去掉末尾的 'i'，并按 '+' 分割
# - 输入可能为 "1+-1i" 这样虚部含正负号的形式，split("+") 可以正确处理
# - 注意：输入 "a+-bi" 形式中 split("+") 得到 ["a", "-b"]，int("-b") 自动转负
