"""
LeetCode #916 - Word Subsets
中文题名：单词子集
https://leetcode.com/problems/word-subsets/

We are given two arrays `A` and `B` of words.  Each word is a
string of lowercase letters.

Now, say that word `b` is a subset of word
`a` if every letter in `b` occurs in
`a`, including multiplicity.  For example, `"wrr"`
is a subset of `"warrior"`, but is not a subset of `"world"`.

Now say a word `a` from `A` is universal if for every
`b` in `B`, `b` is a subset of `a`.

Return a list of all universal words in `A`.  You can return the words in any
order.

Example 1:

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["e","o"]
Output: ["facebook","google","leetcode"]

Example 2:

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["l","e"]
Output: ["apple","google","leetcode"]

Example 3:

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["e","oo"]
Output: ["facebook","google"]

Example 4:

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["lo","eo"]
Output: ["google","leetcode"]

Example 5:

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["ec","oc","ceo"]
Output: ["facebook","leetcode"]

Note:

`1 <= A.length, B.length <= 10000`

`1 <= A[i].length, B[i].length <= 10`

`A[i]` and `B[i]` consist only of lowercase
letters.

All words in `A[i]` are unique: there isn't `i
!= j` with
`A[i] == A[j]`.

【中文翻译】

给定两个单词数组 A 和 B，每个单词都由小写字母组成。
如果单词 b 中的每个字母都在单词 a 中出现（包括重复次数），则称 b 是 a 的子集。
如果对于 B 中的每个 b，b 都是 a 的子集，则称 A 中的单词 a 是"通用单词"。
返回 A 中所有通用单词的列表，可以按任意顺序返回。

"""

from typing import List, Optional


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        """
        1. Combine all words in words2 into a single max-frequency requirement.
        2. For each word in words1, check if it meets the combined requirement.
        """
        # Step 1: Combine words2 requirements
        max_freq = [0] * 26
        for word in words2:
            freq = [0] * 26
            for ch in word:
                freq[ord(ch) - ord('a')] += 1
            for i in range(26):
                max_freq[i] = max(max_freq[i], freq[i])

        # Step 2: Check each word in words1
        result = []
        for word in words1:
            freq = [0] * 26
            for ch in word:
                freq[ord(ch) - ord('a')] += 1
            if all(freq[i] >= max_freq[i] for i in range(26)):
                result.append(word)

        return result



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 关键优化：将 words2 (B) 中的所有单词合并为一个"最大需求"。
# 对于每个字母，取所有 B 中单词对该字母需求的最大值。
# 例如 B = ["e","oo"] → 需要至少 1 个 'e' 和 2 个 'o'。
# 然后只需对 words1 (A) 中每个单词检查是否满足这个合并后的需求即可。
#
# 时间复杂度: O(A总长度 + B总长度)
# 空间复杂度: O(1)（固定 26 个字母的数组）
#
# 关键点:
# - 将 B 合并成一个频率需求表，避免对每个 A 都遍历 B
# - 只包含小写字母，可以用长度为 26 的数组代替哈希表
