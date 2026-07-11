"""
LeetCode #1358 - Number of Substrings Containing All Three Characters
中文题名：包含所有三种字符的子字符串数目
https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/

Given a string `s` consisting only of characters a,
b and c.

Return the number of substrings containing at least one occurrence of all
these characters a, b and c.

Example 1:

Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again).

Example 2:

Input: s = "aaacb"
Output: 3
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb".

Example 3:

Input: s = "abc"
Output: 1

Constraints:

`3 <= s.length <= 5 x 10^4`

`s` only consists of a, b or
c characters.

【中文翻译】
给定一个只包含字符 'a'、'b' 和 'c' 的字符串 `s`。

返回包含至少一个 'a'、'b' 和 'c' 的所有子字符串的数目。

示例 1：
输入：s = "abcabc"
输出：10
解释：包含字符 a、b 和 c 至少一次的子字符串有 "abc"、"abca"、"abcab"、"abcabc"、"bca"、"bcab"、"bcabc"、"cab"、"cabc" 和 "abc"（再次出现）。

示例 2：
输入：s = "aaacb"
输出：3
解释：包含字符 a、b 和 c 至少一次的子字符串有 "aaacb"、"aacb" 和 "acb"。

示例 3：
输入：s = "abc"
输出：1
"""


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        count = {"a": 0, "b": 0, "c": 0}
        result = 0
        left = 0

        for right in range(n):
            count[s[right]] += 1

            # 当窗口包含所有三个字符时，统计子串数量
            while count["a"] > 0 and count["b"] > 0 and count["c"] > 0:
                # 以 left 开头、right 到结尾的所有子串都满足条件
                result += n - right
                count[s[left]] -= 1
                left += 1

        return result



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 滑动窗口 + 计数。维护窗口内 'a'、'b'、'c' 的计数。
# 右指针 right 遍历字符串，将 s[right] 加入窗口。
# 当窗口内三个字符的计数都大于 0 时，说明从 left 到 right 的子串已包含全部三种字符。
# 此时，对于当前 left，以 right 到 n-1 为结尾的所有子串（共 n - right 个）都满足条件，
# 将这些计入结果。然后收缩左边界 left，继续检查。
#
# 时间复杂度: O(N)，每个字符最多被访问两次（right 遍历一次，left 收缩一次）
# 空间复杂度: O(1)，固定大小的计数字典
#
# 关键点:
# - 滑动窗口中三个字符计数均 > 0 时触发统计
# - 一次统计算入 n - right 个有效子串，而非逐个子串枚举
# - 收缩窗口时从 left 的计数减 1，left 右移













