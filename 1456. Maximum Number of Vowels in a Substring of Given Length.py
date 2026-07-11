"""
LeetCode #1456 - Maximum Number of Vowels in a Substring of Given Length
中文题名：定长子串中元音的最大数目
https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/

Given a string `s` and an integer `k`.

Return the maximum number of vowel letters in any substring of
`s` with length `k`.

Vowel letters in English are (a, e, i, o, u).

Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.

Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.

Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.

Example 4:

Input: s = "rhythms", k = 4
Output: 0
Explanation: We can see that s doesn't have any vowel letters.

Example 5:

Input: s = "tryhard", k = 4
Output: 1

Constraints:

`1 <= s.length <= 10^5`

`s` consists of lowercase English letters.

`1 <= k <= s.length`

【中文翻译】
给定一个字符串 `s` 和一个整数 `k`。

返回 `s` 中长度为 `k` 的任意子串中元音字母的最大数量。

英语中的元音字母为 (a, e, i, o, u)。

示例 1：

输入：s = "abciiidef", k = 3
输出：3
解释：子串 "iii" 包含 3 个元音字母。

示例 2：

输入：s = "aeiou", k = 2
输出：2
解释：任何长度为 2 的子串都包含 2 个元音。

示例 3：

输入：s = "leetcode", k = 3
输出：2
解释："lee"、"eet" 和 "ode" 包含 2 个元音。

示例 4：

输入：s = "rhythms", k = 4
输出：0
解释：字符串 s 中没有任何元音字母。

示例 5：

输入：s = "tryhard", k = 4
输出：1

约束条件：

`1 <= s.length <= 10^5`

`s` 由小写英文字母组成。

`1 <= k <= s.length`
"""

from typing import List, Optional


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        cur = 0
        for i in range(k):
            if s[i] in vowels:
                cur += 1
        ans = cur
        for i in range(k, len(s)):
            if s[i - k] in vowels:
                cur -= 1
            if s[i] in vowels:
                cur += 1
            ans = max(ans, cur)
        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用固定大小的滑动窗口。定义元音集合 vowels = {'a','e','i','o','u'}。
# 先计算前 k 个字符中的元音数量作为初始值。
# 然后滑动窗口：每次右移一位，从当前计数中减去离开窗口的字符（如果是元音），
# 加上进入窗口的字符（如果是元音）。
# 在每一步更新最大元音数量。
#
# 时间复杂度: O(N)  -- 遍历字符串一次
# 空间复杂度: O(1)  -- 元音集合大小固定为 5
#
# 关键点:
# - 固定窗口大小 k，不需要双指针收缩
# - 每次只更新首尾两个字符的贡献，O(1) 完成窗口滑动
# - 用 set 的 O(1) 查找判断字符是否为元音









