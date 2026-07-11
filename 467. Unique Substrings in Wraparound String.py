"""
LeetCode #467 - Unique Substrings in Wraparound String
中文题名：环绕字符串中唯一的子字符串
https://leetcode.com/problems/unique-substrings-in-wraparound-string/

Consider the string `s` to be the infinite wraparound string of
"abcdefghijklmnopqrstuvwxyz", so `s` will look like this:
"...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd....".

Now we have another string `p`. Your job is to find out how many unique non-empty
substrings of `p` are present in `s`. In particular, your input is the
string `p` and you need to output the number of different non-empty substrings of
`p` in the string `s`.

Note: `p` consists of only lowercase English letters and the size of p
might be over 10000.

Example 1:

Input: "a"
Output: 1

Explanation: Only the substring "a" of string "a" is in the string s.

Example 2:

Input: "cac"
Output: 2
Explanation: There are two substrings "a", "c" of string "cac" in the string s.

Example 3:

Input: "zab"
Output: 6
Explanation: There are six substrings "z", "a", "b", "za", "ab", "zab" of string "zab" in the string s.

【中文翻译】
考虑字符串 `s` 是 "abcdefghijklmnopqrstuvwxyz" 的无限环绕字符串，即：
"...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd...."。

给定另一个字符串 `p`，找出 `p` 中有多少个不同的非空子串也出现在 `s` 中。
注意：`p` 只包含小写英文字母，且长度可能超过 10000。

示例 1：
    输入："a"
    输出：1
    解释：只有子串 "a" 在 s 中。

示例 2：
    输入："cac"
    输出：2
    解释：有两个子串 "a"、"c" 在 s 中。

示例 3：
    输入："zab"
    输出：6
    解释：六个子串 "z"、"a"、"b"、"za"、"ab"、"zab" 均在 s 中。
"""

from typing import List, Optional


class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        """
        For each character, track the max length of a consecutive
        (wraparound) substring ending at that character. The sum
        of these max lengths across all 26 letters gives the answer.
        """
        if not p:
            return 0

        # max_len[char] = longest valid substring length ending with char
        max_len = [0] * 26
        curr_len = 0

        for i, ch in enumerate(p):
            idx = ord(ch) - ord('a')
            if i > 0 and (ord(p[i]) - ord(p[i - 1]) == 1 or
                          (p[i - 1] == 'z' and p[i] == 'a')):
                curr_len += 1
            else:
                curr_len = 1
            max_len[idx] = max(max_len[idx], curr_len)

        return sum(max_len)



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 核心洞察：对于每个字符 ch，以 ch 结尾且在 s（环绕字符串）中的不同子串数量，等于
# 以 ch 结尾的最长连续子串的长度。遍历 p，维护当前连续长度 curr_len（前后字符相差 1
# 或构成 'z'→'a' 环绕则累加，否则重置为 1）。对每个位置更新 max_len[ch]。
# 最终答案 = Σ max_len[ch]（共 26 个字母）。这种方法巧妙的去重基于：若以某字符结尾
# 的最长有效子串长度为 L，则所有更短的以该字符结尾的子串一定也被包含。
#
# 时间复杂度: O(N) — 一次遍历，N 为 p 的长度
# 空间复杂度: O(1) — max_len 固定 26 个元素
#
# 关键点:
# - "环绕"条件：相邻字符 ASCII 差 1 或 'z' 后跟 'a'
# - 以字符 ch 结尾的最长连续长度决定了以 ch 结尾的合法子串数量
# - 去重原理：所有较短子串已自动包含在最长子串中
