"""
LeetCode #1023 - Camelcase Matching
中文题名：驼峰式匹配
https://leetcode.com/problems/camelcase-matching/

A query word matches a given `pattern` if we can insert lowercase
letters to the pattern word so that it equals the `query`. (We may insert each
character at any position, and may insert 0 characters.)

Given a list of `queries`, and a `pattern`, return an
`answer` list of booleans, where `answer[i]` is true if and only if
`queries[i]` matches the `pattern`.

Example 1:

Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FB"
Output: [true,false,true,true,false]
Explanation:
"FooBar" can be generated like this "F" + "oo" + "B" + "ar".
"FootBall" can be generated like this "F" + "oot" + "B" + "all".
"FrameBuffer" can be generated like this "F" + "rame" + "B" + "uffer".

Example 2:

Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBa"
Output: [true,false,true,false,false]
Explanation:
"FooBar" can be generated like this "Fo" + "o" + "Ba" + "r".
"FootBall" can be generated like this "Fo" + "ot" + "Ba" + "ll".

Example 3:

Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBaT"
Output: [false,true,false,false,false]
Explanation:
"FooBarTest" can be generated like this "Fo" + "o" + "Ba" + "r" + "T" + "est".

Note:

`1 <= queries.length <= 100`

`1 <= queries[i].length <= 100`

`1 <= pattern.length <= 100`

All strings consists only of lower and upper case English letters.

【中文翻译】
如果我们可以向模式单词中插入小写字母，使其等于 `query`，则查询单词与给定的 `pattern` 匹配。（我们可以在任何位置插入每个字符，也可以插入 0 个字符。）

给定一个 `queries` 列表和一个 `pattern`，返回一个布尔值 `answer` 列表，其中 `answer[i]` 为 true 当且仅当 `queries[i]` 与 `pattern` 匹配。

示例 1：

输入：queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FB"
输出：[true,false,true,true,false]
解释：
"FooBar" 可以这样生成："F" + "oo" + "B" + "ar"。
"FootBall" 可以这样生成："F" + "oot" + "B" + "all"。
"FrameBuffer" 可以这样生成："F" + "rame" + "B" + "uffer"。

示例 2：

输入：queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBa"
输出：[true,false,true,false,false]
解释：
"FooBar" 可以这样生成："Fo" + "o" + "Ba" + "r"。
"FootBall" 可以这样生成："Fo" + "ot" + "Ba" + "ll"。

示例 3：

输入：queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBaT"
输出：[false,true,false,false,false]
解释：
"FooBarTest" 可以这样生成："Fo" + "o" + "Ba" + "r" + "T" + "est"。

注意：

`1 <= queries.length <= 100`

`1 <= queries[i].length <= 100`

`1 <= pattern.length <= 100`

所有字符串仅由小写和大写英文字母组成。

"""

from typing import List, Optional


class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        def match(query: str, pattern: str) -> bool:
            i = 0
            for ch in query:
                if i < len(pattern) and ch == pattern[i]:
                    i += 1
                elif ch.isupper():
                    return False
            return i == len(pattern)

        return [match(q, pattern) for q in queries]










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用双指针匹配。对于每个 query 字符串，用指针 i 追踪 pattern 的匹配位置。
# 遍历 query 的每个字符 ch：
# 1. 如果 i < len(pattern) 且 ch == pattern[i]，说明匹配成功，i 前进一位。
# 2. 否则，如果 ch 是大写字母，说明 query 中多了一个不该有的大写字母，
#    而 pattern 中没有对应的大写字母，返回 False。
# 3. 如果 ch 是小写字母且不匹配 pattern[i]，可以跳过（相当于插入的小写字母）。
# 遍历结束后，检查 i == len(pattern)，确保 pattern 的所有字符都已匹配。
#
# 时间复杂度: O(Q * L) - Q 个查询，每个查询遍历一次（L 为查询字符串长度）
# 空间复杂度: O(1) - 除输出数组外只使用常数额外空间
#
# 关键点:
# - pattern 中的大写字母必须按顺序出现在 query 中
# - query 中可以有额外的小写字母插入，但不能有额外的大写字母
# - 当 ch 不是匹配字符且是大写字母时，直接返回 False
# - 最后检查 pattern 是否完全匹配（i == len(pattern)）
