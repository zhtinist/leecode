"""
LeetCode #1963 - Minimum Number of Swaps to Make the String Balanced
使字符串平衡的最小交换次数
https://leetcode.cn/problems/minimum-number-of-swaps-to-make-the-string-balanced/

给你一个字符串 `s` ，下标从 0 开始 ，且长度为偶数 `n` 。字符串 恰好 由 `n / 2` 个开括号 `'['` 和 `n / 2` 个闭括号 `']'` 组成。
只有能满足下述所有条件的字符串才能称为 平衡字符串 ：
字符串是一个空字符串，或者
字符串可以记作 `AB` ，其中 `A` 和 `B` 都是 平衡字符串 ，或者
字符串可以写成 `[C]` ，其中 `C` 是一个 平衡字符串 。
你可以交换 任意 两个下标所对应的括号 任意 次数。
返回使 `s` 变成 平衡字符串 所需要的 最小 交换次数。

示例 1：
输入：s = "][][" 输出：1 解释：交换下标 0 和下标 3 对应的括号，可以使字符串变成平衡字符串。 最终字符串变成 "[[]]" 。
示例 2：
输入：s = "]]][[[" 输出：2 解释：执行下述操作可以使字符串变成平衡字符串： - 交换下标 0 和下标 4 对应的括号，s = "[]][][" 。 - 交换下标 1 和下标 5 对应的括号，s = "[[][]]" 。 最终字符串变成 "[[][]]" 。
示例 3：
输入：s = "[]" 输出：0 解释：这个字符串已经是平衡字符串。

提示：
`n == s.length`
`2 <= n <= 10^6`
`n` 为偶数
`s[i]` 为`'['` 或 `']'`
开括号 `'['` 的数目为 `n / 2` ，闭括号 `']'` 的数目也是 `n / 2`
"""

from typing import List, Optional


class Solution:
    def minSwaps(self, s: str) -> int:
        """
        Track imbalance: count how many ']' are unmatched.
        Each swap fixes two unbalanced brackets.
        """
        imbalance = 0  # unmatched ']'
        balance = 0    # current balance of '[' minus ']'

        for ch in s:
            if ch == "[":
                balance += 1
            else:
                balance -= 1
            if balance < 0:
                imbalance += 1
                balance = 0  # reset after counting this mismatch

        # Each swap fixes two imbalances: (imbalance + 1) // 2
        return (imbalance + 1) // 2



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Stack, Greedy, Two Pointers, String
#
# 解题思路:
# 遍历字符串，维护当前的平衡值（balance = 左括号数 - 右括号数）。
# 当 balance 变为负数时，说明出现了一个无法匹配的右括号。
# 累计这些不匹配的次数 imbalance。
# 每次交换可以修复两个不匹配的括号（把一个不匹配的 ] 和一个不匹配的 [ 交换），
# 所以答案为 (imbalance + 1) // 2。
# 例如：]]][[[ ：遍历后 imbalance = 3，答案 = (3+1)//2 = 2。
#
# 时间复杂度: O(N)，一次遍历
# 空间复杂度: O(1)
#
# 关键点:
# - 只统计不匹配的右括号数量
# - 一次交换修复两个不匹配（一左一右）
# - 公式: (imbalance + 1) // 2
