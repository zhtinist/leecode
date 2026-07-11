"""
LeetCode #1541 - Minimum Insertions to Balance a Parentheses String
中文题名：平衡括号字符串的最少插入次数
https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/

Given a parentheses string `s` containing only the characters
`'('` and `')'`. A parentheses string is balanced
if:

Any left parenthesis `'('` must have a corresponding two
consecutive right parenthesis `'))'`.

Left parenthesis `'('` must go before the corresponding two consecutive
right parenthesis `'))'`.

For example, `"())"`, `"())(())))"` and
`"(())())))"` are balanced, `")()"`, `"()))"`
and `"(()))"` are not balanced.

You can insert the characters '(' and ')' at any position of the string to balance it
if needed.

Return the minimum number of insertions needed to make `s`
balanced.

Example 1:

Input: s = "(()))"
Output: 1
Explanation: The second '(' has two matching '))', but the first '(' has only ')' matching. We need to to add one more ')' at the end of the string to be "(())))" which is balanced.

Example 2:

Input: s = "())"
Output: 0
Explanation: The string is already balanced.

Example 3:

Input: s = "))())("
Output: 3
Explanation: Add '(' to match the first '))', Add '))' to match the last '('.

Example 4:

Input: s = "(((((("
Output: 12
Explanation: Add 12 ')' to balance the string.

Example 5:

Input: s = ")))))))"
Output: 5
Explanation: Add 4 '(' at the beginning of the string and one ')' at the end. The string becomes "(((())))))))".

Constraints:

`1 <= s.length <= 10^5`

`s` consists of `'('` and `')'` only.

【中文翻译】
给定一个只包含 '(' 和 ')' 的括号字符串 s。平衡定义：每个 '(' 必须对应两个连续的 '))'，
且 '(' 必须在对应的 '))' 之前。可以在任意位置插入 '(' 和 ')' 使字符串平衡。
返回使 s 平衡所需的最少插入次数。

示例 1：

输入：s = "(()))"
输出：1
解释：第二个 '(' 已匹配两个 ')'，第一个 '(' 只需一个 ')'，在末尾添加一个 ')' 即可。

示例 2：

输入：s = "())"
输出：0
解释：字符串已经平衡。

示例 3：

输入：s = "))())("
输出：3
解释：添加 '(' 匹配前面的 '))'，添加 '))' 匹配最后的 '('。

示例 4：

输入：s = "(((((("
输出：12
解释：添加 12 个 ')'。

示例 5：

输入：s = ")))))))"
输出：5
解释：开头添加 4 个 '('，末尾添加一个 ')'。
"""

from typing import List, Optional


class Solution:
    def minInsertions(self, s: str) -> int:
        insertions = 0
        need_right = 0  # number of ')' needed for pending '('
        i = 0
        n = len(s)
        while i < n:
            if s[i] == '(':
                need_right += 2
                i += 1
            else:
                # s[i] == ')'
                if i + 1 < n and s[i + 1] == ')':
                    # Found '))'
                    need_right -= 2
                    i += 2
                else:
                    # Single ')'
                    need_right -= 1
                    i += 1
                if need_right < 0:
                    # Need to insert '(' before this
                    insertions += 1
                    need_right += 2
        return insertions + need_right



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 每个 '(' 需要 2 个 ')' 来匹配。遍历字符串：
# 遇到 '('：需要 2 个 ')'，need_right += 2。
# 遇到 ')'：检查下一个是否也是 ')'（连续两个），如果是则消耗 2 个 need_right；
# 如果是单个 ')'，消耗 1 个。如果 need_right < 0，说明 ')' 多余，需要插入 '('，insertions++，need_right += 2。
# 最后，剩余的 need_right 需要插入相应数量的 ')'。
#
# 时间复杂度: O(N)
# 空间复杂度: O(1)
#
# 关键点:
# - 每个 '(' 匹配两个 ')'，而非标准括号的一个
# - 需要处理单个 ')' 的情况（中间插入 '('）
# - 处理连续的 '))' 作为一对
