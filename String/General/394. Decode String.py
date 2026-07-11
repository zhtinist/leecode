"""
LeetCode #394 - Decode String
中文题名：字符串解码
https://leetcode.com/problems/decode-string/

Given an encoded string, return its decoded string.

The encoding rule is: `k[encoded_string]`, where the encoded_string inside
the square brackets is being repeated exactly k times. Note that k is
guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets
are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that
digits are only for those repeat numbers, k. For example, there won't be input
like `3a` or `2[4]`.

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".

【中文翻译】
给定一个经过编码的字符串，返回它解码后的字符串。

编码规则为：k[encoded_string]，表示方括号内的 encoded_string 恰好重复 k 次。注意，k 保证为正整数。

你可以假设输入字符串始终有效；没有额外的空白字符，方括号格式正确等。

此外，你可以假设原始数据不包含任何数字，数字仅用于重复次数 k。例如，不会有像 3a 或 2[4] 这样的输入。

示例：

s = "3[a]2[bc]"，返回 "aaabcbc"。
s = "3[a2[c]]"，返回 "accaccacc"。
s = "2[abc]3[cd]ef"，返回 "abcabccdcdcdef"。
"""

from typing import List, Optional


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        cur_num = 0
        cur_str = ""
        for ch in s:
            if ch.isdigit():
                cur_num = cur_num * 10 + int(ch)
            elif ch == '[':
                stack.append(cur_str)
                stack.append(cur_num)
                cur_str = ""
                cur_num = 0
            elif ch == ']':
                num = stack.pop()
                prev_str = stack.pop()
                cur_str = prev_str + cur_str * num
            else:
                cur_str += ch
        return cur_str











# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用栈来模拟解码过程。遍历字符串的每个字符：
# - 遇到数字：累加到 cur_num（处理多位数）
# - 遇到 '['：将当前字符串 cur_str 和数字 cur_num 压入栈中，重置 cur_str 和 cur_num
# - 遇到 ']'：从栈中弹出数字（重复次数）和之前的字符串，将当前字符串重复拼接
# - 遇到字母：追加到 cur_str
# 最后 cur_str 即为解码后的完整字符串。
#
# 时间复杂度: O(n) - 其中 n 为输出字符串长度，每个字符处理一次
# 空间复杂度: O(n) - 栈在最坏情况下（深度嵌套）存储所有中间字符串
#
# 关键点:
# - 栈内存储 "之前的字符串" 和 "当前重复次数" 两个元素
# - 遇到 '[' 时将当前状态保存，以便嵌套结束后恢复
# - cur_num 需要处理多位数情况（如 "12[a]"）
# - 内层解码完成后拼回外层，模拟递归展开过程
