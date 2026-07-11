"""
LeetCode #1540 - Can Convert String in K Moves
中文题名：K 次操作转变字符串
https://leetcode.com/problems/can-convert-string-in-k-moves/

Given two strings `s` and `t`, your goal is to
convert `s` into `t` in `k` moves
or less.

During the `ith` (`1 <=
i <= k`) move you can:

Choose any index `j` (1-indexed) from `s`,
such that `1 <= j <= s.length` and `j` has
not been chosen in any previous move, and shift the character at that index `i` times.

Do nothing.

Shifting a character means replacing it by the next letter in the alphabet (wrapping
around so that `'z'` becomes `'a'`). Shifting a
character by `i` means applying the shift
operations `i` times.

Remember that any index `j` can be picked at most once.

Return `true` if it's possible to convert `s` into `t` in
no more than `k` moves, otherwise
return `false`.

Example 1:

Input: s = "input", t = "ouput", k = 9
Output: true
Explanation: In the 6th move, we shift 'i' 6 times to get 'o'. And in the 7th move we shift 'n' to get 'u'.

Example 2:

Input: s = "abc", t = "bcd", k = 10
Output: false
Explanation: We need to shift each character in s one time to convert it into t. We can shift 'a' to 'b' during the 1st move. However, there is no way to shift the other characters in the remaining moves to obtain t from s.

Example 3:

Input: s = "aab", t = "bbb", k = 27
Output: true
Explanation: In the 1st move, we shift the first 'a' 1 time to get 'b'. In the 27th move, we shift the second 'a' 27 times to get 'b'.

Constraints:

`1 <= s.length, t.length <= 10^5`

`0 <= k <= 10^9`

`s`, `t` contain only lowercase English letters.

【中文翻译】
给定两个字符串 s 和 t，目标是在 k 次或更少操作内将 s 转换为 t。
在第 i 次（1<=i<=k）操作中，你可以选择一个未被选过的索引 j，将该位置的字符移动 i 次，
或者什么都不做。移动字符意味着用字母表中的下一个字母替换（循环，'z' 变为 'a'）。
如果可以在 k 次操作内完成转换，返回 true，否则返回 false。

示例 1：

输入：s = "input", t = "ouput", k = 9
输出：true
解释：第 6 次操作将 'i' 移动 6 次得 'o'，第 7 次操作将 'n' 移动得 'u'。

示例 2：

输入：s = "abc", t = "bcd", k = 10
输出：false
解释：每个字符需要移动 1 次。可以将 'a' 在第 1 次操作移为 'b'，但无法在剩余操作中移动其他字符。

示例 3：

输入：s = "aab", t = "bbb", k = 27
输出：true
解释：第 1 次操作移动第一个 'a' 1 次得 'b'，第 27 次操作移动第二个 'a' 27 次得 'b'。
"""

from typing import List, Optional


class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False
        # Track how many times each shift amount (1-25) has been used
        shift_count = [0] * 26
        for i in range(len(s)):
            if s[i] != t[i]:
                shift = (ord(t[i]) - ord(s[i]) + 26) % 26
                shift_count[shift] += 1
        # For shift amount x used c times, need: x + 26*(c-1) <= k
        for shift in range(1, 26):
            if shift_count[shift] > 0:
                max_move = shift + 26 * (shift_count[shift] - 1)
                if max_move > k:
                    return False
        return True



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 首先长度必须相等。对于每个位置，计算需要的位移量 shift = (t[i]-s[i]+26)%26。
# 相同位移量的字符不能在同一次操作中完成（因为每个索引只能用一次），
# 所以如果一个位移量 shift 被用了 c 次，需要的最晚操作号 = shift + 26*(c-1)。
# 检查所有位移量，如果最晚需要的操作号 <= k 即可完成。
#
# 时间复杂度: O(N) — 遍历字符串
# 空间复杂度: O(1) — 26 个位移量的计数数组
#
# 关键点:
# - 位移量 0 的字符无需操作
# - 相同位移量需要在不同轮次完成（间隔 26）
# - 第 c 次使用位移量 shift 的操作编号 = shift + 26*(c-1)
