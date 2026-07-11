"""
LeetCode #1247 - Minimum Swaps to Make Strings Equal
中文题名：交换字符使得字符串相同
https://leetcode.com/problems/minimum-swaps-to-make-strings-equal/

You are given two strings `s1` and `s2` of equal
length consisting of letters `"x"` and `"y"`
only. Your task is to make these two strings equal to each other. You
can swap any two characters that belong to different strings, which
means: swap `s1[i]` and `s2[j]`.

Return the minimum number of swaps required to make `s1` and
`s2` equal, or return `-1` if it is impossible to do
so.

Example 1:

Input: s1 = "xx", s2 = "yy"
Output: 1
Explanation:
Swap s1[0] and s2[1], s1 = "yx", s2 = "yx".

Example 2:

Input: s1 = "xy", s2 = "yx"
Output: 2
Explanation:
Swap s1[0] and s2[0], s1 = "yy", s2 = "xx".
Swap s1[0] and s2[1], s1 = "xy", s2 = "xy".
Note that you can't swap s1[0] and s1[1] to make s1 equal to "yx", cause we can only swap chars in different strings.

Example 3:

Input: s1 = "xx", s2 = "xy"
Output: -1

Example 4:

Input: s1 = "xxyyxyxyxx", s2 = "xyyxyxxxyx"
Output: 4

Constraints:

`1 <= s1.length, s2.length <= 1000`

`s1, s2` only contain `'x'` or
`'y'`.

【中文翻译】
给你两个长度相同的字符串 `s1` 和 `s2`，它们只包含字母 `"x"` 和 `"y"`。你需要让这两个字符串变得相同。你可以交换任意两个属于不同字符串的字符，即：交换 `s1[i]` 和 `s2[j]`。

请返回让 `s1` 和 `s2` 相同所需的最小交换次数。如果不可能做到，返回 `-1`。

示例 1：

输入：s1 = "xx", s2 = "yy"
输出：1
解释：
交换 s1[0] 和 s2[1]，s1 = "yx"，s2 = "yx"。

示例 2：

输入：s1 = "xy", s2 = "yx"
输出：2
解释：
交换 s1[0] 和 s2[0]，s1 = "yy"，s2 = "xx"。
交换 s1[0] 和 s2[1]，s1 = "xy"，s2 = "xy"。
注意你不能交换 s1[0] 和 s1[1] 使 s1 等于 "yx"，因为我们只能交换不同字符串中的字符。

示例 3：

输入：s1 = "xx", s2 = "xy"
输出：-1

示例 4：

输入：s1 = "xxyyxyxyxx", s2 = "xyyxyxxxyx"
输出：4

约束条件：

`1 <= s1.length, s2.length <= 1000`

`s1, s2` 仅包含 `'x'` 或 `'y'`。
"""

from typing import List, Optional


class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        # Count mismatches: xy means s1[i]='x', s2[i]='y'
        #                 yx means s1[i]='y', s2[i]='x'
        xy = yx = 0
        for c1, c2 in zip(s1, s2):
            if c1 != c2:
                if c1 == 'x':
                    xy += 1
                else:
                    yx += 1

        # Total mismatches must be even
        if (xy + yx) % 2 != 0:
            return -1

        # Two xy pairs can be fixed with 1 swap: (xy, xy) -> swap s1[0] with s2[1]
        # Two yx pairs can be fixed with 1 swap: (yx, yx) -> swap s1[0] with s2[1]
        # One xy + one yx pair needs 2 swaps

        # Pair up same types first (cheaper): each pair needs 1 swap
        swaps = xy // 2 + yx // 2

        # Remaining unmatched pairs (if any) need 2 swaps each
        # After pairing, either 0 xy and 0 yx remain, or 1 xy and 1 yx remain
        if xy % 2 == 1:  # yx % 2 is also 1
            swaps += 2

        return swaps










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 贪心 + 数学分析。只关注 s1[i] != s2[i] 的位置。
# 1. 扫描两个字符串，统计两种不匹配情况：
#    - xy：s1[i] = 'x', s2[i] = 'y'
#    - yx：s1[i] = 'y', s2[i] = 'x'
# 2. 如果 (xy + yx) 是奇数，不可能做到相同，返回 -1。
# 3. 两个 xy（或两个 yx）可以通过 1 次交换解决：
#    例如 s1="xx", s2="yy" → swap(s1[0], s2[1]) → s1="yx", s2="yx"，两对同时解决。
# 4. 一个 xy 和一个 yx 需要 2 次交换解决。
# 5. 贪心策略：优先配对同类型的（xy 内部配对，yx 内部配对），
#    每对用 1 次交换，剩余一个 xy 和一个 yx 需要额外 2 次交换。
# 6. 总交换次数 = xy//2 + yx//2 + (2 if xy%2 == 1 else 0)。
#
# 时间复杂度: O(N)，一次遍历统计
# 空间复杂度: O(1)
#
# 关键点:
# - 只关心不匹配的位置，匹配的位置不需要任何操作
# - 将同类型的不匹配两两配对是最优的（1 次交换解决 2 对）
# - 剩余的一对 xy 和一对 yx 需要 2 次交换
# - 不匹配总数必须为偶数，否则无解
