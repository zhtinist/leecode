"""
LeetCode #1170 - Compare Strings by Frequency of the Smallest Character
中文题名：比较字符串最小字母出现频次
https://leetcode.com/problems/compare-strings-by-frequency-of-the-smallest-character/

Let's define a function `f(s)` over a non-empty string `s`, which
calculates the frequency of the smallest character in `s`. For example, if
`s = "dcce"` then `f(s) = 2` because the smallest character
is `"c"` and its frequency is 2.

Now, given string arrays `queries` and `words`, return an integer
array `answer`, where each `answer[i]` is the number of words
such that `f(queries[i])` < `f(W)`, where `W` is
a word in `words`.

Example 1:

Input: queries = ["cbd"], words = ["zaaaz"]
Output: [1]
Explanation: On the first query we have f("cbd") = 1, f("zaaaz") = 3 so f("cbd") < f("zaaaz").

Example 2:

Input: queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"]
Output: [1,2]
Explanation: On the first query only f("bbb") < f("aaaa"). On the second query both f("aaa") and f("aaaa") are both > f("cc").

Constraints:

`1 <= queries.length <= 2000`

`1 <= words.length <= 2000`

`1 <= queries[i].length, words[i].length <= 10`

`queries[i][j]`, `words[i][j]` are English lowercase letters.

【中文翻译】
定义一个非空字符串 s 的函数 f(s)，它计算字符串 s 中最小字符的出现频率。例如，如果 s = "dcce"，则 f(s) = 2，因为最小字符是 "c"，其频率为 2。

现在，给定字符串数组 queries 和 words，返回一个整数数组 answer，其中每个 answer[i] 是满足 f(queries[i]) < f(W) 的单词 W 的数量（W 是 words 中的单词）。

示例 1：

输入：queries = ["cbd"], words = ["zaaaz"]
输出：[1]
解释：对于第一个查询，f("cbd") = 1，f("zaaaz") = 3，所以 f("cbd") < f("zaaaz")。

示例 2：

输入：queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"]
输出：[1,2]
解释：对于第一个查询，只有 f("bbb") < f("aaaa")。对于第二个查询，f("aaa") 和 f("aaaa") 都大于 f("cc")。

约束条件：

`1 <= queries.length <= 2000`

`1 <= words.length <= 2000`

`1 <= queries[i].length, words[i].length <= 10`

`queries[i][j]`、`words[i][j]` 均为小写英文字母。
"""

from typing import List, Optional
import bisect


class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def f(s: str) -> int:
            """Returns frequency of the smallest character in s."""
            min_char = min(s)
            return s.count(min_char)

        # Compute f(w) for all words and sort
        word_freqs = sorted(f(w) for w in words)

        answer = []
        for q in queries:
            qf = f(q)
            # Count words with f(W) > f(query)
            # bisect_right gives index of first element > qf
            idx = bisect.bisect_right(word_freqs, qf)
            answer.append(len(word_freqs) - idx)

        return answer










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 1. 定义辅助函数 f(s)：找出字符串 s 中的最小字符，并统计其出现次数。
#    由于只含小写字母，可用 min(s) 找最小字符，s.count() 统计频率。
# 2. 计算 words 中所有单词的 f(W)，并将结果排序。
# 3. 对于每个查询 query，计算 f(query)，然后在排序后的 word_freqs 中
#    使用二分查找统计有多少个 f(W) > f(query)。
#    即：总数 - bisect_right(word_freqs, f(query))。
#    bisect_right 返回第一个大于 f(query) 的位置。
#
# 时间复杂度: O((M+N) * L + M log M)，其中 M = len(words), N = len(queries), L 为字符串最大长度
#   - 计算所有 f 值：O((M+N) * L)
#   - 排序 word_freqs：O(M log M)
#   - N 次二分查找：O(N log M)
# 空间复杂度: O(M) - 存储 word_freqs 数组
#
# 关键点:
# - f(s) 的计算：最小字符 + 它的频率
# - 排序 + 二分查找是将 O(N*M) 优化为 O((M+N)log M) 的关键
# - bisect_right 用于处理严格大于（>）的情况
# - 字符串长度不超过 10，f(s) 计算是 O(L) 的
