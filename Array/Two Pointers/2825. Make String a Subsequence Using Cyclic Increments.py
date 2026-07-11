"""
LeetCode #2825 - Make String a Subsequence Using Cyclic Increments
循环增长使字符串子序列等于另一个字符串
https://leetcode.cn/problems/make-string-a-subsequence-using-cyclic-increments/

给你一个下标从 0 开始的字符串 `str1` 和 `str2` 。
一次操作中，你选择 `str1` 中的若干下标。对于选中的每一个下标 `i` ，你将 `str1[i]` 循环 递增，变成下一个字符。也就是说 `'a'` 变成 `'b'` ，`'b'` 变成 `'c'` ，以此类推，`'z'` 变成 `'a'` 。
如果执行以上操作 至多一次 ，可以让 `str2` 成为 `str1` 的子序列，请你返回 `true` ，否则返回 `false` 。
注意：一个字符串的子序列指的是从原字符串中删除一些（可以一个字符也不删）字符后，剩下字符按照原本先后顺序组成的新字符串。

示例 1：
输入：str1 = "abc", str2 = "ad" 输出：true 解释：选择 str1 中的下标 2 。 将 str1[2] 循环递增，得到 'd' 。 因此，str1 变成 "abd" 且 str2 现在是一个子序列。所以返回 true 。
示例 2：
输入：str1 = "zc", str2 = "ad" 输出：true 解释：选择 str1 中的下标 0 和 1 。 将 str1[0] 循环递增得到 'a' 。 将 str1[1] 循环递增得到 'd' 。 因此，str1 变成 "ad" 且 str2 现在是一个子序列。所以返回 true 。
示例 3：
输入：str1 = "ab", str2 = "d" 输出：false 解释：这个例子中，没法在执行一次操作的前提下，将 str2 变为 str1 的子序列。 所以返回 false 。

提示：
`1 <= str1.length <= 10^5`
`1 <= str2.length <= 10^5`
`str1` 和 `str2` 只包含小写英文字母。
"""

from typing import List, Optional


class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        j = 0
        for ch in str1:
            if j == len(str2):
                break
            target = str2[j]
            next_ch = chr((ord(ch) - ord('a') + 1) % 26 + ord('a'))
            if ch == target or next_ch == target:
                j += 1
        return j == len(str2)



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Two Pointers, String
#
# 解题思路:
# 贪心匹配。对于 str1 中的每个字符，可以保持不变或循环递增一次。
# 所以每个 str1[i] 最多能匹配两种 str2 字符：本身或循环递增后的字符（'z' 变成 'a'）。
# 使用双指针：j 指向 str2 待匹配位置。遍历 str1，如果当前字符可以匹配 str2[j]，则 j++。
# 当 j 到达 str2 末尾时匹配成功。
#
# 时间复杂度: O(n)
# 空间复杂度: O(1)
#
# 关键点:
# - 每个 str1 字符可以选择不变或循环递增（相当于可以匹配两个可能的字符）
# - 贪心匹配：尽可能早地匹配 str2 中的字符
# - 循环递增：'z' 的下一个字符是 'a'
