"""
LeetCode #2434 - Using a Robot to Print the Lexicographically Smallest String
使用机器人打印字典序最小的字符串
https://leetcode.cn/problems/using-a-robot-to-print-the-lexicographically-smallest-string/

给你一个字符串 `s` 和一个机器人，机器人当前有一个空字符串 `t` 。执行以下操作之一，直到 `s` 和 `t` 都变成空字符串：
删除字符串 `s` 的 第一个 字符，并将该字符给机器人。机器人把这个字符添加到 `t` 的尾部。
删除字符串 `t` 的 最后一个 字符，并将该字符给机器人。机器人将该字符写到纸上。
请你返回纸上能写出的字典序最小的字符串。

示例 1：
输入：s = "zza" 输出："azz" 解释：用 p 表示写出来的字符串。 一开始，p="" ，s="zza" ，t="" 。 执行第一个操作三次，得到 p="" ，s="" ，t="zza" 。 执行第二个操作三次，得到 p="azz" ，s="" ，t="" 。
示例 2：
输入：s = "bac" 输出："abc" 解释：用 p 表示写出来的字符串。 执行第一个操作两次，得到 p="" ，s="c" ，t="ba" 。 执行第二个操作两次，得到 p="ab" ，s="c" ，t="" 。 执行第一个操作，得到 p="ab" ，s="" ，t="c" 。 执行第二个操作，得到 p="abc" ，s="" ，t="" 。
示例 3：
输入：s = "bdda" 输出："addb" 解释：用 p 表示写出来的字符串。 一开始，p="" ，s="bdda" ，t="" 。 执行第一个操作四次，得到 p="" ，s="" ，t="bdda" 。 执行第二个操作四次，得到 p="addb" ，s="" ，t="" 。

提示：
`1 <= s.length <= 10^5`
`s` 只包含小写英文字母。
"""

from typing import List, Optional


class Solution:
    def robotWithString(self, s: str) -> str:
        n = len(s)
        # 后缀最小字符数组：suffix_min[i] 表示 s[i:] 中的最小字符
        suffix_min = [''] * n
        suffix_min[-1] = s[-1]
        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(s[i], suffix_min[i + 1])

        t = []       # 模拟栈
        result = []
        i = 0
        while i < n:
            # 如果栈顶字符不大于后续所有字符中的最小字符，则弹出到结果
            if t and t[-1] <= suffix_min[i]:
                result.append(t.pop())
            else:
                t.append(s[i])
                i += 1
        # 弹出栈中剩余字符
        while t:
            result.append(t.pop())

        return ''.join(result)


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Stack, Greedy, Hash Table, String
#
# 解题思路:
# 贪心 + 栈。要使最终字符串字典序最小，应该在每一步都尽量把较小的字符写到纸上。
# 操作规则：只能从 s 的开头取字符压入栈 t，或从栈 t 的顶部弹出字符写到纸上。
# 关键决策：当前栈顶字符是否可以弹出？如果栈顶字符小于或等于 s 剩余部分的最小字符，
# 说明即使把 s 剩余字符全部压栈后再弹出，也不会得到更小的结果，此时应该弹出栈顶。
# 预处理后缀最小字符数组 suffix_min[i] = min(s[i:]),
# 然后模拟操作过程，最后将栈中剩余字符全部弹出。
#
# 时间复杂度: O(n)
# 空间复杂度: O(n)
#
# 关键点:
# - 预处理后缀最小字符数组是实现贪心决策的前提
# - 判断条件 t[-1] <= suffix_min[i] 是核心贪心策略
# - 最后将栈中剩余字符全部弹出
