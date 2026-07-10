"""
LeetCode #159 - Longest Substring with At Most Two Distinct Characters
https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/

Given a string s, return the length of the longest substring that contains at
most two distinct characters.

Example 1:
    Input: s = "eceba"
    Output: 3
    Explanation: The substring is "ece" which its length is 3.

Example 2:
    Input: s = "ccaabbb"
    Output: 5
    Explanation: The substring is "aabbb" which its length is 5.

Constraints:
    1 <= s.length <= 10^5
    s consists of English letters.
"""


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        count = {}
        left = 0
        result = 0

        for right, char in enumerate(s):
            count[char] = count.get(char, 0) + 1

            while len(count) > 2:
                count[s[left]] -= 1
                if count[s[left]] == 0:
                    del count[s[left]]
                left += 1

            result = max(result, right - left + 1)

        return result
