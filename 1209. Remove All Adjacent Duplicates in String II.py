"""
LeetCode #1209 - Remove All Adjacent Duplicates in String II
中文题名：删除字符串中的所有相邻重复项 II
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/

Given a string `s`, a k duplicate removal consists
of choosing `k` adjacent and equal letters from `s` and
removing them causing the left and the right side of the deleted substring to
concatenate together.

We repeatedly make `k` duplicate removals on `s` until we no longer
can.

Return the final string after all such duplicate removals have been made.

It is guaranteed that the answer is unique.

Example 1:

Input: s = "abcd", k = 2
Output: "abcd"
Explanation: There's nothing to delete.

Example 2:

Input: s = "deeedbbcccbdaa", k = 3
Output: "aa"
Explanation:
First delete "eee" and "ccc", get "ddbbbdaa"
Then delete "bbb", get "dddaa"
Finally delete "ddd", get "aa"

Example 3:

Input: s = "pbbcggttciiippooaais", k = 2
Output: "ps"

Constraints:

`1 <= s.length <= 10^5`

`2 <= k <= 10^4`

`s` only contains lower case English letters.

【中文翻译】
给你一个字符串 s，「k 倍重复项删除操作」将会从 s 中选择 k 个相邻且相等的字母，并删除它们，使被删去的字符串的左侧和右侧连在一起。

你需要对 s 重复进行无限次这样的删除操作，直到无法继续为止。

在执行完所有删除操作后，返回最终得到的字符串。

本题答案保证唯一。

示例 1：

输入：s = "abcd", k = 2
输出："abcd"
解释：没有要删除的内容。

示例 2：

输入：s = "deeedbbcccbdaa", k = 3
输出："aa"
解释：
先删除 "eee" 和 "ccc"，得到 "ddbbbdaa"
再删除 "bbb"，得到 "dddaa"
最后删除 "ddd"，得到 "aa"

示例 3：

输入：s = "pbbcggttciiippooaais", k = 2
输出："ps"

约束条件：

1 <= s.length <= 10^5
2 <= k <= 10^4
s 只包含小写英文字母。

"""

from typing import List, Optional


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []  # (char, count)

        for ch in s:
            if stack and stack[-1][0] == ch:
                stack[-1] = (ch, stack[-1][1] + 1)
            else:
                stack.append((ch, 1))

            if stack[-1][1] == k:
                stack.pop()

        return ''.join(ch * cnt for ch, cnt in stack)










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用栈存储 (字符, 连续出现次数) 的元组。
# 遍历字符串中的每个字符：
# 1. 如果栈非空且栈顶字符与当前字符相同，则增加计数。
# 2. 否则，将 (当前字符, 1) 压入栈。
# 3. 如果栈顶的计数达到 k，则弹出栈顶（删除这 k 个连续相同字符）。
#
# 遍历结束后，栈中剩余的元素即为最终结果，按顺序展开即可。
# 这种方法的妙处在于：删除操作后可能产生新的相邻重复（如示例 2），
# 而栈自然地处理了这种情况，因为被删除段两端的字符在栈中成为相邻元素。
#
# 时间复杂度: O(n) - 每个字符入栈一次、出栈一次
# 空间复杂度: O(n) - 最坏情况下栈存储所有字符
#
# 关键点:
# - 栈不只存储字符，还存储连续出现次数，避免重复计数
# - 当计数达到 k 时立即弹出，自然实现级联删除
# - 栈的性质天然处理了删除后新产生的相邻重复（原本不相邻、删除中间段后相邻）
# - 最终还原时使用 ch * cnt 展开，性能优于逐个字符追加
