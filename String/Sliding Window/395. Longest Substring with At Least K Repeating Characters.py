"""
LeetCode #395 - Longest Substring with At Least K Repeating Characters
中文题名：至少有K个重复字符的最长子串
https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/

Find the length of the longest substring T of a given string (consists of
lowercase letters only) such that every character in T appears no less than
k times.

Example 1:

Input:
s = "aaabb", k = 3

Output:
3

The longest substring is "aaa", as 'a' is repeated 3 times.

Example 2:

Input:
s = "ababbc", k = 2

Output:
5

The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.

【中文翻译】
给定一个字符串 s（仅由小写字母组成），找出 s 中的最长子串 T，要求 T 中的每个字符出现的次数都不少于 k。输出 T 的长度。

示例 1：

输入：
s = "aaabb", k = 3

输出：
3

最长的子串为 "aaa"，因为 'a' 重复了 3 次。

示例 2：

输入：
s = "ababbc", k = 2

输出：
5

最长的子串为 "ababb"，因为 'a' 重复了 2 次，'b' 重复了 3 次。
"""

from typing import List, Optional


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        def helper(left: int, right: int) -> int:
            if right - left < k:
                return 0
            count = {}
            for i in range(left, right):
                ch = s[i]
                count[ch] = count.get(ch, 0) + 1
            for i in range(left, right):
                if count[s[i]] < k:
                    j = i + 1
                    while j < right and count[s[j]] < k:
                        j += 1
                    return max(helper(left, i), helper(j, right))
            return right - left

        return helper(0, len(s))











# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用分治法。统计当前区间内每个字符的出现次数。
# 找到第一个出现次数 < k 的字符作为"分割点"：
# - 该字符不可能出现在任何有效子串中
# - 以此为界将问题一分为二，递归求解左右两边的最大长度
# - 如果所有字符出现次数都 >= k，整个区间即为有效子串
# 由于只有 26 个小写字母，递归深度和分支数都有限。
#
# 时间复杂度: O(n * 26) = O(n) - 每层递归扫描一次，最多 26 层（每次至少排除一个字符）
# 空间复杂度: O(26 * 26) = O(1) - 递归栈深度最多 26 层，不计递归则为 O(1)
#
# 关键点:
# - 分治的核心：出现次数不足 k 的字符必然不包含在任何有效子串中
# - 找到第一个不合格字符后，跳过连续的不合格字符以减少递归分支
# - 小写字母只有 26 个，保证了递归深度的上界
# - 另一种解法：枚举窗口中不同字符的数量（1~26），使用滑动窗口
