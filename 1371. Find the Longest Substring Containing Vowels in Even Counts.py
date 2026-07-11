"""
LeetCode #1371 - Find the Longest Substring Containing Vowels in Even Counts
中文题名：每个元音包含偶数次的最长子字符串
https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/

Given the string `s`, return the size of the longest substring containing
each vowel an even number of times. That is, 'a', 'e', 'i', 'o', and 'u' must appear an
even number of times.

Example 1:

Input: s = "eleetminicoworoep"
Output: 13
Explanation: The longest substring is "leetminicowor" which contains two each of the vowels: e, i and o and zero of the vowels: a and u.

Example 2:

Input: s = "leetcodeisgreat"
Output: 5
Explanation: The longest substring is "leetc" which contains two e's.

Example 3:

Input: s = "bcbcbc"
Output: 6
Explanation: In this case, the given string "bcbcbc" is the longest because all vowels: a, e, i, o and u appear zero times.

Constraints:

`1 <= s.length <= 5 x 10^5`

`s` contains only lowercase English letters.

【中文翻译】
给定字符串 `s`，返回每个元音字母（'a'、'e'、'i'、'o'、'u'）均出现偶数次的最长子字符串的长度。

示例 1：
输入：s = "eleetminicoworoep"
输出：13
解释：最长的子字符串是 "leetminicowor"，其中 e、i、o 各出现 2 次，a 和 u 出现 0 次。

示例 2：
输入：s = "leetcodeisgreat"
输出：5
解释：最长子字符串是 "leetc"，其中包含 2 个 e。

示例 3：
输入：s = "bcbcbc"
输出：6
解释：该示例中，字符串 "bcbcbc" 本身是最长的，因为所有元音 a、e、i、o、u 都出现了 0 次。
"""


class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowel_to_bit = {"a": 1, "e": 2, "i": 4, "o": 8, "u": 16}
        first_occurrence = {0: -1}  # mask 0 首次出现在索引 -1
        mask = 0
        max_len = 0

        for i, ch in enumerate(s):
            if ch in vowel_to_bit:
                mask ^= vowel_to_bit[ch]  # 翻转对应元音的奇偶状态

            if mask in first_occurrence:
                max_len = max(max_len, i - first_occurrence[mask])
            else:
                first_occurrence[mask] = i

        return max_len



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用 5 位二进制掩码表示 5 个元音字母的奇偶状态（0=偶数次，1=奇数次）。
# a->bit0(1), e->bit1(2), i->bit2(4), o->bit3(8), u->bit4(16)。
# 遍历字符串，遇到元音字母时翻转对应位（XOR）。
# 如果某个 mask 状态在之前出现过，说明两次出现之间的子串中所有元音出现了偶数次
# （因为 mask 相同意味着两者的奇偶状态相同，差值子串种每种元音的变动次数为偶数）。
# 记录每个 mask 第一次出现的位置，用当前索引减去第一次出现位置得到子串长度。
#
# 时间复杂度: O(N)，单次遍历
# 空间复杂度: O(1)，最多 32 种 mask 状态
#
# 关键点:
# - 位掩码压缩 5 个元音的奇偶状态
# - 相同 mask 出现两次 = 中间子串满足条件
# - mask=0 初始化为索引 -1（空子串）
# - XOR 翻转奇偶：偶数个 1 翻转为 0，奇数个翻转为 1













