"""
LeetCode #2546 - Apply Bitwise Operations to Make Strings Equal
执行逐位运算使字符串相等
https://leetcode.cn/problems/apply-bitwise-operations-to-make-strings-equal/

给你两个下标从 0 开始的 二元 字符串 `s` 和 `target` ，两个字符串的长度均为 `n` 。你可以对 `s` 执行下述操作 任意 次：
选择两个 不同 的下标 `i` 和 `j` ，其中 `0 <= i, j < n` 。
同时，将 `s[i]` 替换为 (`s[i]` OR `s[j]`) ，`s[j]` 替换为 (`s[i]` XOR `s[j]`) 。
例如，如果 `s = "0110"` ，你可以选择 `i = 0` 和 `j = 2`，然后同时将 `s[0]` 替换为 (`s[0]` OR `s[2]` = `0` OR `1` = `1`)，并将 `s[2]` 替换为 (`s[0]` XOR `s[2]` = `0` XOR `1` = `1`)，最终得到 `s = "1110"` 。
如果可以使 `s` 等于 `target` ，返回 `true` ，否则，返回 `false` 。

示例 1：
输入：s = "1010", target = "0110" 输出：true 解释：可以执行下述操作： - 选择 i = 2 和 j = 0 ，得到 s = "0010". - 选择 i = 2 和 j = 1 ，得到 s = "0110". 可以使 s 等于 target ，返回 true 。
示例 2：
输入：s = "11", target = "00" 输出：false 解释：执行任意次操作都无法使 s 等于 target 。

提示：
`n == s.length == target.length`
`2 <= n <= 10^5`
`s` 和 `target` 仅由数字 `0` 和 `1` 组成
"""

from typing import List, Optional


class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        has_one_s = '1' in s
        has_one_t = '1' in target
        if not has_one_s:
            return not has_one_t
        return has_one_t



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Bit Manipulation, String
#
# 解题思路:
# 操作规律：当s中至少有一个'1'时，可以通过操作生成任意包含至少一个'1'的字符串；
# 当s全为'0'时，永远是全'0'无法改变。因此只需比较两个字符串是否都有'1'或都没有'1'。
# 核心：只要s中有'1'，target也有'1'就可行；否则需要两者都是全'0'。
#
# 时间复杂度: O(N)
# 空间复杂度: O(1)
#
# 关键点:
# - 操作(0,1)→(1,1)可以传播1；(1,1)→(1,0)可以消灭1（但不能消灭最后一个）
# - 当s全0时无法产生1，因此target也必须全0
# - 当s有1时，target有1就可以，因为能生成任意非全0模式
