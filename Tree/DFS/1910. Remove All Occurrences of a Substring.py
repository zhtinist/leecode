"""
LeetCode #1910 - Remove All Occurrences of a Substring
删除一个字符串中所有出现的给定子字符串
https://leetcode.cn/problems/remove-all-occurrences-of-a-substring/

给你两个字符串 `s` 和 `part` ，请你对 `s` 反复执行以下操作直到 所有 子字符串 `part` 都被删除：
找到 `s` 中 最左边 的子字符串 `part` ，并将它从 `s` 中删除。
请你返回从 `s` 中删除所有 `part` 子字符串以后得到的剩余字符串。
一个 子字符串 是一个字符串中连续的字符序列。

示例 1：
输入：s = "daabcbaabcbc", part = "abc" 输出："dab" 解释：以下操作按顺序执行： - s = "daabcbaabcbc" ，删除下标从 2 开始的 "abc" ，得到 s = "dabaabcbc" 。 - s = "dabaabcbc" ，删除下标从 4 开始的 "abc" ，得到 s = "dababc" 。 - s = "dababc" ，删除下标从 3 开始的 "abc" ，得到 s = "dab" 。 此时 s 中不再含有子字符串 "abc" 。
示例 2：
输入：s = "axxxxyyyyb", part = "xy" 输出："ab" 解释：以下操作按顺序执行： - s = "axxxxyyyyb" ，删除下标从 4 开始的 "xy" ，得到 s = "axxxyyyb" 。 - s = "axxxyyyb" ，删除下标从 3 开始的 "xy" ，得到 s = "axxyyb" 。 - s = "axxyyb" ，删除下标从 2 开始的 "xy" ，得到 s = "axyb" 。 - s = "axyb" ，删除下标从 1 开始的 "xy" ，得到 s = "ab" 。 此时 s 中不再含有子字符串 "xy" 。

提示：
`1 <= s.length <= 1000`
`1 <= part.length <= 1000`
`s`​​​​​​ 和 `part` 只包小写英文字母。
"""

from typing import List, Optional


class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        m = len(part)

        for ch in s:
            stack.append(ch)
            # Check if the end of stack matches 'part'
            if len(stack) >= m and ''.join(stack[-m:]) == part:
                # Remove the matched part
                for _ in range(m):
                    stack.pop()

        return ''.join(stack)



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Stack, String, Simulation
#
# 解题思路:
# 使用栈模拟删除过程：
# 1. 遍历字符串 s 的每个字符，将其压入栈中。
# 2. 每次压入后，检查栈顶的 m 个字符是否等于 part。
# 3. 如果匹配，弹出这 m 个字符。
# 4. 由于是从左到右处理，自然满足"最左边"的要求，
#    且删除后可能产生新的匹配（栈顶变化）。
#
# 时间复杂度: O(n * m) — 每次检查需要比较 m 个字符
# 空间复杂度: O(n) — 栈空间
#
# 关键点:
# - 使用栈天然支持删除后重新检查（类似消消乐）
# - 每次检查栈顶 m 个字符是否等于 part
# - 也可以使用 str.replace 循环，但栈方法更高效
# - 只删除"最左边"出现的 part
