"""
LeetCode #2559 - Count Vowel Strings in Ranges
统计范围内的元音字符串数
https://leetcode.cn/problems/count-vowel-strings-in-ranges/

给你一个下标从 0 开始的字符串数组 `words` 以及一个二维整数数组 `queries` 。
每个查询 `queries[i] = [l_i, r_i]` 会要求我们统计在 `words` 中下标在 `l_i` 到 `r_i` 范围内（包含 这两个值）并且以元音开头和结尾的字符串的数目。
返回一个整数数组，其中数组的第 `i` 个元素对应第 `i` 个查询的答案。
注意：元音字母是 `'a'`、`'e'`、`'i'`、`'o'` 和 `'u'` 。

示例 1：
输入：words = ["aba","bcb","ece","aa","e"], queries = [[0,2],[1,4],[1,1]] 输出：[2,3,0] 解释：以元音开头和结尾的字符串是 "aba"、"ece"、"aa" 和 "e" 。 查询 [0,2] 结果为 2（字符串 "aba" 和 "ece"）。 查询 [1,4] 结果为 3（字符串 "ece"、"aa"、"e"）。 查询 [1,1] 结果为 0 。 返回结果 [2,3,0] 。
示例 2：
输入：words = ["a","e","i"], queries = [[0,2],[0,1],[2,2]] 输出：[3,2,1] 解释：每个字符串都满足这一条件，所以返回 [3,2,1] 。

提示：
`1 <= words.length <= 10^5`
`1 <= words[i].length <= 40`
`words[i]` 仅由小写英文字母组成
`sum(words[i].length) <= 3 * 10^5`
`1 <= queries.length <= 10^5`
`0 <= queries[j][0] <= queries[j][1] < words.length`
"""

from typing import List, Optional


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set('aeiou')
        n = len(words)
        prefix = [0] * (n + 1)
        for i, w in enumerate(words):
            prefix[i + 1] = prefix[i] + (1 if w[0] in vowels and w[-1] in vowels else 0)

        ans = []
        for l, r in queries:
            ans.append(prefix[r + 1] - prefix[l])
        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, String, Prefix Sum
#
# 解题思路:
# 构建前缀和数组。遍历words标记每个字符串是否以元音开头和结尾（1或0）。
# 前缀和prefix[i]表示前i个字符串中符合条件的数量。每个查询[l,r]的答案为prefix[r+1]-prefix[l]。
#
# 时间复杂度: O(N + Q)，N为words长度，Q为queries长度
# 空间复杂度: O(N)
#
# 关键点:
# - 前缀和将区间查询从O(N)降至O(1)
# - 判断条件：首字符和尾字符都在元音集合中
# - prefix数组长度为N+1，prefix[0]=0简化边界处理
