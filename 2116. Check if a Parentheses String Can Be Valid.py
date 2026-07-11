"""
LeetCode #2116 - Check if a Parentheses String Can Be Valid
判断一个括号字符串是否有效
https://leetcode.cn/problems/check-if-a-parentheses-string-can-be-valid/

一个括号字符串是只由 `'('` 和 `')'` 组成的 非空 字符串。如果一个字符串满足下面 任意 一个条件，那么它就是有效的：
字符串为 `()`.
它可以表示为 `AB`（`A` 与 `B` 连接），其中`A` 和 `B` 都是有效括号字符串。
它可以表示为 `(A)` ，其中 `A` 是一个有效括号字符串。
给你一个括号字符串 `s` 和一个字符串 `locked` ，两者长度都为 `n` 。`locked` 是一个二进制字符串，只包含 `'0'` 和 `'1'` 。对于 `locked` 中 每一个 下标 `i` ：
如果 `locked[i]` 是 `'1'` ，你 不能 改变 `s[i]` 。
如果 `locked[i]` 是 `'0'` ，你 可以 将 `s[i]` 变为 `'('` 或者 `')'` 。
如果你可以将 `s` 变为有效括号字符串，请你返回 `true` ，否则返回 `false` 。

示例 1：

输入：s = "))()))", locked = "010100" 输出：true 解释：locked[1] == '1' 和 locked[3] == '1' ，所以我们无法改变 s[1] 或者 s[3] 。 我们可以将 s[0] 和 s[4] 变为 '(' ，不改变 s[2] 和 s[5] ，使 s 变为有效字符串。
示例 2：
输入：s = "()()", locked = "0000" 输出：true 解释：我们不需要做任何改变，因为 s 已经是有效字符串了。
示例 3：
输入：s = ")", locked = "0" 输出：false 解释：locked 允许改变 s[0] 。 但无论将 s[0] 变为 '(' 或者 ')' 都无法使 s 变为有效字符串。
示例 4：
输入：s = "(((())(((())", locked = "111111010111" 输出：true 解释：locked 允许我们改变 s[6] 和 s[8]。 我们将 s[6] 和 s[8] 改为 ')' 使 s 变为有效字符串。

提示：
`n == s.length == locked.length`
`1 <= n <= 10^5`
`s[i]` 要么是 `'('` 要么是 `')'` 。
`locked[i]` 要么是 `'0'` 要么是 `'1'` 。
"""

from typing import List, Optional


class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if n % 2 != 0:
            return False

        # Left to right: ensure we never have too many ')'
        balance = 0
        flexible = 0
        for i in range(n):
            if locked[i] == '1':
                balance += 1 if s[i] == '(' else -1
            else:
                flexible += 1
            if balance + flexible < 0:
                return False

        # Right to left: ensure we never have too many '('
        balance = 0
        flexible = 0
        for i in range(n - 1, -1, -1):
            if locked[i] == '1':
                balance += 1 if s[i] == ')' else -1
            else:
                flexible += 1
            if balance + flexible < 0:
                return False

        return True



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Stack, Greedy, String
#
# 解题思路:
# 首先，字符串长度必须是偶数，否则括号无法配对。
# 使用两次遍历（贪心策略）：
# 1. 从左到右：将可变位置视为 '('，检查是否会出现过多的 ')'。
#    维护固定括号的平衡值 balance 和可变位置数 flexible。
#    如果 balance + flexible < 0，说明即使把所有可变位置都变成 '(' 也无法挽救，返回 False。
# 2. 从右到左：将可变位置视为 ')'，检查是否会出现过多的 '('。
#    同理，如果 balance + flexible < 0，返回 False。
# 两次遍历都通过，则字符串可以变为有效括号。
#
# 时间复杂度: O(n)
# 空间复杂度: O(1)
#
# 关键点:
# - 长度奇数直接返回 False
# - 左扫验证 ')' 不会过多，右扫验证 '(' 不会过多
# - 可变位置灵活分配，两次扫描扮演不同角色
