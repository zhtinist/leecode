"""
LeetCode #3081 - Replace Question Marks in String to Minimize Its Value
替换字符串中的问号使分数最小
https://leetcode.cn/problems/replace-question-marks-in-string-to-minimize-its-value/

给你一个字符串 `s` 。`s[i]` 要么是小写英文字母，要么是问号 `'?'` 。
对于长度为 `m` 且 只 含有小写英文字母的字符串 `t` ，我们定义函数 `cost(i)` 为下标 `i` 之前（也就是范围 `[0, i - 1]` 中）出现过与 `t[i]` 相同 字符出现的次数。
字符串 `t` 的 分数 为所有下标 `i` 的 `cost(i)` 之 和 。
比方说，字符串 `t = "aab"` ：
`cost(0) = 0`
`cost(1) = 1`
`cost(2) = 0`
所以，字符串 `"aab"` 的分数为 `0 + 1 + 0 = 1` 。
你的任务是用小写英文字母 替换 `s` 中 所有 问号，使 `s` 的 分数最小 。
请你返回替换所有问号 `'?'` 之后且分数最小的字符串。如果有多个字符串的 分数最小 ，那么返回字典序最小的一个。

示例 1：

输入：s = "???"
输出： "abc"
解释：这个例子中，我们将 `s` 中的问号 `'?'` 替换得到 `"abc"` 。
对于字符串 `"abc"` ，`cost(0) = 0` ，`cost(1) = 0` 和 `cost(2) = 0` 。
`"abc"` 的分数为 `0` 。
其他修改 `s` 得到分数 `0` 的字符串为 `"cba"` ，`"abz"` 和 `"hey"` 。
这些字符串中，我们返回字典序最小的。
示例 2：

输入： s = "a?a?"
输出： "abac"
解释：这个例子中，我们将 `s` 中的问号 `'?'` 替换得到 `"abac"` 。
对于字符串 `"abac"` ，`cost(0) = 0` ，`cost(1) = 0` ，`cost(2) = 1` 和 `cost(3) = 0` 。
`"abac"` 的分数为 `1` 。

提示：
`1 <= s.length <= 10^5`
`s[i]` 要么是小写英文字母，要么是 `'?'` 。
"""

from typing import List, Optional


class Solution:
    def minimizeStringValue(self, s: str) -> str:
        """
        Score depends only on character frequencies: sum C(cnt, 2).
        To minimize: distribute '?' among letters with smallest current count.
        For lexicographically smallest output: sort replacement chars and fill
        left-to-right.
        """
        import heapq

        # Count existing characters
        cnt = [0] * 26
        for c in s:
            if c != '?':
                cnt[ord(c) - ord('a')] += 1

        # Min-heap for distributing replacements
        heap = [(cnt[i], i) for i in range(26)]
        heapq.heapify(heap)

        replacements = []
        for c in s:
            if c == '?':
                count, idx = heapq.heappop(heap)
                replacements.append(chr(ord('a') + idx))
                heapq.heappush(heap, (count + 1, idx))

        # Sort replacements and fill into '?' positions
        replacements.sort()
        rep_idx = 0
        result = list(s)
        for i in range(len(result)):
            if result[i] == '?':
                result[i] = replacements[rep_idx]
                rep_idx += 1

        return ''.join(result)



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Hash Table, String, Counting, Sorting, Heap (Priority Queue)
#
# 解题思路:
# 分数 = sum(C(count[c], 2))，仅取决于各字母的最终频率，与位置无关。
# 要使分数最小化，需将 '?' 均匀分配到频率最小的字母上（边际成本递增）。
# 使用最小堆维护各字母当前频率，每次取最小频率的字母分配一个 '?'。
# 为使最终字符串字典序最小，将分配得到的替换字母排序后，从左到右填入原字符串的 '?' 位置。
#
# 时间复杂度: O(n log 26)，n 为字符串长度，堆操作 O(log 26)
# 空间复杂度: O(n)，存储替换字母列表
#
# 关键点:
# - 分数只与最终频率有关（C(cnt,2) 形式），与字符位置无关
# - 贪心向最小频率字母添加 '?' 是边际成本最优的
# - 字典序最小化：将确定的替换字母排序后左到右填入
