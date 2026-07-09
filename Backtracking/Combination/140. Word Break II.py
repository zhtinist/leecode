"""
LeetCode #140 - Word Break II
https://leetcode.com/problems/word-break-ii/

Given a string s and a dictionary of strings wordDict, add spaces in s to
construct a sentence where each word is a valid dictionary word. Return a list
of all possible sentences.

Example 1:
    Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
    Output: ["cats and dog","cat sand dog"]

Example 2:
    Input: s = "pineapplepenapple",
           wordDict = ["apple","pen","applepen","pine","pineapple"]
    Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]

Example 3:
    Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
    Output: []

Constraints:
    1 <= s.length <= 20
    1 <= wordDict.length <= 1000
    1 <= wordDict[i].length <= 10
    s and wordDict[i] consist of only lowercase English letters.
    All strings in wordDict are unique.
    Input is generated in a way that the number of different sentences does not
    exceed 10^4.
"""

from typing import Dict, List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        memo: Dict[int, List[str]] = {}

        def backtrack(start: int) -> List[str]:
            if start in memo:
                return memo[start]
            if start == len(s):
                return [""]

            sentences = []
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word not in word_set:
                    continue
                for rest in backtrack(end):
                    sentences.append(word if not rest else f"{word} {rest}")

            memo[start] = sentences
            return sentences

        return backtrack(0)
