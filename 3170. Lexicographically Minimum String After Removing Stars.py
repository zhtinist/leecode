"""
LeetCode #3170 - Lexicographically Minimum String After Removing Stars
删除星号以后字典序最小的字符串
https://leetcode.cn/problems/lexicographically-minimum-string-after-removing-stars/

给你一个字符串 `s` 。它可能包含任意数量的 `'*'` 字符。你的任务是删除所有的 `'*'` 字符。
当字符串还存在至少一个 `'*'` 字符时，你可以执行以下操作：
删除最左边的 `'*'` 字符，同时删除该星号字符左边一个字典序 最小 的字符。如果有多个字典序最小的字符，你可以删除它们中的任意一个。
请你返回删除所有 `'*'` 字符以后，剩余字符连接而成的 字典序最小 的字符串。

示例 1：

输入：s = "aaba*"
输出："aab"
解释：
删除 `'*'` 号和它左边的其中一个 `'a'` 字符。如果我们选择删除 `s[3]` ，`s` 字典序最小。
示例 2：

输入：s = "abc"
输出："abc"
解释：
字符串中没有 `'*'` 字符。

提示：
`1 <= s.length <= 10^5`
`s` 只含有小写英文字母和 `'*'` 字符。
输入保证操作可以删除所有的 `'*'` 字符。
"""

from typing import List, Optional


class Solution:
    def clearStars(self, s: str) -> str:
        n = len(s)
        stacks = [[] for _ in range(26)]  # 每个字母的位置栈
        deleted = [False] * n

        for i, ch in enumerate(s):
            if ch == '*':
                deleted[i] = True
                # 找最小字母并删除其最右侧出现
                for c in range(26):
                    if stacks[c]:
                        pos = stacks[c].pop()
                        deleted[pos] = True
                        break
            else:
                stacks[ord(ch) - 97].append(i)

        return ''.join(s[i] for i in range(n) if not deleted[i])



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Stack, Greedy, Hash Table, String, Heap (Priority Queue)
#
# 解题思路:
# 每个星号必须删除其左边一个字典序最小的字符。为使最终字符串字典序最小，
# 应优先删除较小的字符。使用26个栈分别记录每个字母的出现位置。
# 遇到星号时，从'a'到'z'找到第一个非空栈，弹出栈顶（最右侧位置）标记删除。
# 最后收集所有未被删除的字符。
#
# 时间复杂度: O(n * 26) = O(n)
# 空间复杂度: O(n)
#
# 关键点:
# - 每个星号删除左边最小字母，贪心正确
# - 同字母选最右侧删除（保留左侧更早出现的）
# - 用26个栈实现O(1)查找最小字母
