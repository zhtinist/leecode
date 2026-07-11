"""
LeetCode #1234 - Replace the Substring for Balanced String
中文题名：替换子串得到平衡字符串
https://leetcode.com/problems/replace-the-substring-for-balanced-string/

You are given a string containing only 4 kinds of characters `'Q',`
`'W', 'E'` and `'R'`.

A string is said to be balanced if each of its characters
appears `n/4` times where `n` is the length of the string.

Return the minimum length of the substring that can be replaced with any
other string of the same length to make the original string `s` balanced.

Return 0 if the string is already balanced.

Example 1:

Input: s = "QWER"
Output: 0
Explanation: s is already balanced.

Example 2:

Input: s = "QQWE"
Output: 1
Explanation: We need to replace a 'Q' to 'R', so that "RQWE" (or "QRWE") is balanced.

Example 3:

Input: s = "QQQW"
Output: 2
Explanation: We can replace the first "QQ" to "ER".

Example 4:

Input: s = "QQQQ"
Output: 3
Explanation: We can replace the last 3 'Q' to make s = "QWER".

Constraints:

`1 <= s.length <= 10^5`

`s.length` is a multiple of `4`

`s `contains only `'Q'`, `'W'`,
`'E'` and `'R'`.

【中文翻译】
你有一个仅包含四种字符 `'Q', 'W', 'E', 'R'` 的字符串。

如果字符串中每种字符都恰好出现 `n/4` 次（其中 `n` 是字符串的长度），我们就称它是平衡的。

请返回将 `s` 变平衡所需替换的最小子串长度。替换意味着可以将子串中的字符改为任意你想要的字符（长度不变）。

如果字符串已经是平衡的，返回 0。

示例 1：

输入：s = "QWER"
输出：0
解释：s 已经是平衡的。

示例 2：

输入：s = "QQWE"
输出：1
解释：我们需要将一个 'Q' 替换为 'R'，使得 "RQWE" (或 "QRWE") 是平衡的。

示例 3：

输入：s = "QQQW"
输出：2
解释：我们可以将前两个 "QQ" 替换为 "ER"。

示例 4：

输入：s = "QQQQ"
输出：3
解释：我们可以将最后 3 个 'Q' 替换为 "WER"，使得 s = "QWER"。

约束条件：

`1 <= s.length <= 10^5`

`s.length` 是 `4` 的倍数

`s` 仅包含 `'Q'`、`'W'`、`'E'` 和 `'R'`。
"""

from typing import List, Optional


class Solution:
    def balancedString(self, s: str) -> int:
        from collections import Counter

        n = len(s)
        target = n // 4
        count = Counter(s)

        # If already balanced
        if all(v <= target for v in count.values()):
            return 0

        left = 0
        res = n

        for right in range(n):
            count[s[right]] -= 1

            while left <= right and all(v <= target for v in count.values()):
                res = min(res, right - left + 1)
                count[s[left]] += 1
                left += 1

        return res










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 滑动窗口。问题等价于：找到最短的连续子串，使得将其替换后，字符串中每种字符的出现次数都不超过 n/4。
# 1. 首先统计整个字符串中每种字符的出现次数。
# 2. 如果所有字符的次数都已 <= n/4，直接返回 0。
# 3. 使用滑动窗口 [left, right] 表示"待替换的子串"。
#    将窗口内的字符从全局计数中减去，如果剩余字符（窗口外的字符）每种都不超过 n/4，
#    说明当前窗口是一个可行解——我们可以替换窗口内的字符来补齐不足的部分。
# 4. 找到可行解后，收缩左边界（left++）以寻找更短的窗口。
# 5. 记录最小的窗口长度。
# 另一种思路：同向双指针，找到需要替换的多余字符，滑动窗口恰好覆盖这些多余字符。
#
# 时间复杂度: O(N)，每个字符最多被左右指针各访问一次
# 空间复杂度: O(1)，计数数组大小固定为 4
#
# 关键点:
# - 问题转化：不是"替换后凑成平衡"，而是"窗外每种字符都不超过 n/4"
# - 滑动窗口维护窗外字符的计数，当窗外满足条件时收缩窗口
# - 字符种类只有 4 种，`all(v <= target for v in count.values())` 是 O(1) 的
# - 窗口内的字符可以是任意数量（通过替换调整），所以不需要对窗口内做任何限制
