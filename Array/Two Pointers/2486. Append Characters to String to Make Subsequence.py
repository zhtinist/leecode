"""
LeetCode #2486 - Append Characters to String to Make Subsequence
追加字符以获得子序列
https://leetcode.cn/problems/append-characters-to-string-to-make-subsequence/

给你两个仅由小写英文字母组成的字符串 `s` 和 `t` 。
现在需要通过向 `s` 末尾追加字符的方式使 `t` 变成 `s` 的一个 子序列 ，返回需要追加的最少字符数。
子序列是一个可以由其他字符串删除部分（或不删除）字符但不改变剩下字符顺序得到的字符串。

示例 1：
输入：s = "coaching", t = "coding" 输出：4 解释：向 s 末尾追加字符串 "ding" ，s = "coachingding" 。 现在，t 是 s ("coachingding") 的一个子序列。 可以证明向 s 末尾追加任何 3 个字符都无法使 t 成为 s 的一个子序列。
示例 2：
输入：s = "abcde", t = "a" 输出：0 解释：t 已经是 s ("abcde") 的一个子序列。
示例 3：
输入：s = "z", t = "abcde" 输出：5 解释：向 s 末尾追加字符串 "abcde" ，s = "zabcde" 。 现在，t 是 s ("zabcde") 的一个子序列。  可以证明向 s 末尾追加任何 4 个字符都无法使 t 成为 s 的一个子序列。

提示：
`1 <= s.length, t.length <= 10^5`
`s` 和 `t` 仅由小写英文字母组成
"""

from typing import List, Optional


class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        """
        双指针贪心匹配子序列：
        - i 在 s 上移动，j 在 t 上移动
        - 当 s[i] == t[j] 时，匹配成功，j 前进
        - i 始终前进
        - 遍历结束后，t 中已匹配的前 j 个字符不需要追加
        - 需要追加的字符数 = len(t) - j
        """
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                j += 1
            i += 1
        return len(t) - j



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Two Pointers, String
#
# 解题思路:
# 使用双指针技术。指针 i 遍历字符串 s，指针 j 遍历字符串 t。每当 s[i] == t[j]
# 时，将 j 向前移动一步（表示 t 中该字符已在 s 中匹配到），无论是否匹配 i 都前进。
# 最终 j 表示 t 中已被匹配为子序列的字符个数，剩余 len(t) - j 个字符就是需要追加
# 到 s 末尾的最少字符数。
#
# 时间复杂度: O(n) — 其中 n = len(s)，最多遍历 s 一次
# 空间复杂度: O(1) — 只使用两个指针变量
#
# 关键点:
# - 子序列不要求连续，只需保持原有的顺序
# - 贪心策略：每次匹配 t 的当前字符时尽早匹配（使用 s 中最早出现的匹配位置）
# - 已经匹配的部分不需要追加，只需追加 t 中未匹配的后缀
