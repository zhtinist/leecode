"""
LeetCode #3517 - Smallest Palindromic Rearrangement I
最小回文排列 I
https://leetcode.cn/problems/smallest-palindromic-rearrangement-i/

给你一个 回文 字符串 `s`。
返回 `s` 的按字典序排列的 最小 回文排列。
如果一个字符串从前往后和从后往前读都相同，那么这个字符串是一个 回文 字符串。
排列 是字符串中所有字符的重排。 如果字符串 `a` 按字典序小于字符串 `b`，则表示在第一个不同的位置，`a` 中的字符比 `b` 中的对应字符在字母表中更靠前。
如果在前 `min(a.length, b.length)` 个字符中没有区别，则较短的字符串按字典序更小。

示例 1：

输入： s = "z"
输出： "z"
解释：
仅由一个字符组成的字符串已经是按字典序最小的回文。
示例 2：

输入： s = "babab"
输出： "abbba"
解释：
通过重排 `"babab"` → `"abbba"`，可以得到按字典序最小的回文。
示例 3：

输入： s = "daccad"
输出： "acddca"
解释：
通过重排 `"daccad"` → `"acddca"`，可以得到按字典序最小的回文。

提示：
`1 <= s.length <= 10^5`
`s` 由小写英文字母组成。
保证 `s` 是回文字符串。
"""

from typing import List, Optional


class Solution:
    def smallestPalindrome(self, s: str) -> str:
        from collections import Counter
        cnt = Counter(s)
        half = []
        middle = ""
        for ch in sorted(cnt.keys()):
            c = cnt[ch]
            half.append(ch * (c // 2))
            if c % 2 == 1 and middle == "":
                middle = ch
        first_half = ''.join(half)
        return first_half + middle + first_half[::-1]



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: String, Counting Sort, Sorting
#
# 解题思路:
# 1. 统计每个字符的频率
# 2. 按字母顺序构建回文的前半部分：
#    - 每个字符取 freq[ch] // 2 个放入前半
# 3. 中间字符：若有奇数频率的字符，取字母序最小的作为中心
# 4. 后半部分是前半的逆序
# 5. 拼接：前半 + 中间 + 逆序(前半)
#
# 时间复杂度: O(n)
# 空间复杂度: O(n)
#
# 关键点:
# - 输入保证是回文，所以奇数频率的字符最多只有一个
# - 字典序最小 = 前半部分字母尽可能小
# - 中间字符选择字母序最小的奇数频率字符
