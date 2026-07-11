"""
LeetCode #1190 - Reverse Substrings Between Each Pair of Parentheses
中文题名：反转每对括号间的子串
https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/

You are given a string `s` that consists of lower case English letters and
brackets.

Reverse the strings in each pair of matching parentheses, starting from the
innermost one.

Your result should not contain any brackets.

Example 1:

Input: s = "(abcd)"
Output: "dcba"

Example 2:

Input: s = "(u(love)i)"
Output: "iloveu"
Explanation: The substring "love" is reversed first, then the whole string is reversed.

Example 3:

Input: s = "(ed(et(oc))el)"
Output: "leetcode"
Explanation: First, we reverse the substring "oc", then "etco", and finally, the whole string.

Example 4:

Input: s = "a(bcdefghijkl(mno)p)q"
Output: "apmnolkjihgfedcbq"

Constraints:

`0 <= s.length <= 2000`

`s` only contains lower case English characters and parentheses.

It's guaranteed that all parentheses are balanced.

【中文翻译】
给出一个由小写英文字母和括号组成的字符串 s。

反转每对匹配括号之间的子串，从最内层开始。

你的结果不应包含任何括号。

示例 1：

输入：s = "(abcd)"
输出："dcba"

示例 2：

输入：s = "(u(love)i)"
输出："iloveu"
解释：先反转子串 "love"，然后反转整个字符串。

示例 3：

输入：s = "(ed(et(oc))el)"
输出："leetcode"
解释：先反转子串 "oc"，然后反转 "etco"，最后反转整个字符串。

示例 4：

输入：s = "a(bcdefghijkl(mno)p)q"
输出："apmnolkjihgfedcbq"

约束条件：

0 <= s.length <= 2000
s 只包含小写英文字母和括号。
保证所有括号都是平衡的。

"""

from typing import List, Optional


class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        res = []
        for ch in s:
            if ch == '(':
                stack.append(len(res))
            elif ch == ')':
                start = stack.pop()
                res[start:] = reversed(res[start:])
            else:
                res.append(ch)
        return ''.join(res)










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用栈来处理括号匹配和反转操作。
# 方法：遍历字符串，将字符逐个加入结果列表。
# - 遇到 '('：将当前结果列表的长度压入栈，标记反转的起始位置。
# - 遇到 ')'：弹出栈顶的起始位置，将从该位置到列表末尾的部分反转。
# - 普通字符：直接加入结果列表。
# 这种方式从最内层括号开始逐层反转，最终得到不含括号的结果。
#
# 另一种 O(n) 解法（虫洞法/Wormhole）：
# 预处理括号配对关系，然后使用方向变量在括号对之间"跳跃"遍历，
# 每次遇到括号就跳到对应的匹配括号并反转方向，避免多次反转操作。
#
# 时间复杂度: O(n^2) - 每次反转可能需要 O(n) 时间，最坏情况嵌套很深
# （使用虫洞法可优化至 O(n)）
# 空间复杂度: O(n) - 结果列表和栈的空间
#
# 关键点:
# - 用栈记录每个 '(' 对应的结果列表位置，遇到 ')' 时反转该段
# - 反转操作内置在列表中就地完成，无需额外字符串拼接
# - 括号匹配保证了正确性（题目保证括号平衡）
