"""
LeetCode #316 - Remove Duplicate Letters
中文题名：去除重复字母
https://leetcode.com/problems/remove-duplicate-letters/

Given a string which contains only lowercase letters, remove duplicate letters so that every
letter appears once and only once. You must make sure your result is the smallest in
lexicographical order among all possible results.

Example 1:

Input: `"bcabc"`
Output: `"abc"`

Example 2:

Input: `"cbacdcbc"`
Output: `"acdb"`

【中文翻译】
给你一个仅包含小写字母的字符串，请你去除字符串中重复的字母，使得每个字母只出现一次。
需保证返回结果的字典序最小（要求不能打乱其他字符的相对位置）。

示例 1：

输入："bcabc"
输出："abc"

示例 2：

输入："cbacdcbc"
输出："acdb"
"""

from typing import List, Optional


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # 记录每个字符最后出现的索引
        last = {c: i for i, c in enumerate(s)}
        seen = set()      # 当前栈中已有的字符
        stack = []        # 单调栈，维护递增顺序
        for i, c in enumerate(s):
            if c in seen:
                continue
            # 如果栈顶字符 > 当前字符，且栈顶字符在后面还会出现，则可以弹出
            while stack and c < stack[-1] and i < last[stack[-1]]:
                seen.remove(stack.pop())
            stack.append(c)
            seen.add(c)
        return ''.join(stack)










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 单调栈 + 贪心。目标是去重后字典序最小。
# 遍历字符串，对每个字符 c：
# - 如果 c 已经在栈中（seen 集合），直接跳过（保证每个字符只出现一次）。
# - 当栈非空且栈顶字符大于当前字符（即当前字符字典序更小），且栈顶字符在后面的位置还会再出现时，
#   弹出栈顶（放弃当前位置的栈顶字符，等后面再加入可以获得更小的字典序）。
# - 将当前字符入栈并标记为已见。
# last 字典记录每个字符在字符串中最后出现的位置，用于判断是否可以安全弹出栈顶字符。
#
# 时间复杂度: O(n) - 每个字符最多入栈出栈各一次
# 空间复杂度: O(1) - 栈、seen、last 最多存储 26 个小写字母
#
# 关键点:
# - 贪心策略：尽量让字典序小的字符靠前，同时确保每种字符都保留至少一个
# - 单调栈维护结果字符的递增顺序
# - 需要 last[c] 判断栈顶字符是否还有机会在后面被添加
# - 与 LeetCode #1081（不同编号的同一题目）解法完全相同
