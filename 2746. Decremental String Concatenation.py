"""
LeetCode #2746 - Decremental String Concatenation
字符串连接删减字母
https://leetcode.cn/problems/decremental-string-concatenation/

给你一个下标从 0 开始的数组 `words` ，它包含 `n` 个字符串。
定义 连接 操作 `join(x, y)` 表示将字符串 `x` 和 `y` 连在一起，得到 `xy` 。如果 `x` 的最后一个字符与 `y` 的第一个字符相等，连接后两个字符中的一个会被 删除 。
比方说 `join("ab", "ba") = "aba"` ， `join("ab", "cde") = "abcde"` 。
你需要执行 `n - 1` 次 连接 操作。令 `str_0 = words[0]` ，从 `i = 1` 直到 `i = n - 1` ，对于第 `i` 个操作，你可以执行以下操作之一：
令 `str_i = join(str_i - 1, words[i])`
令 `str_i = join(words[i], str_i - 1)`
你的任务是使 `str_n - 1` 的长度 最小 。
请你返回一个整数，表示 `str_n - 1` 的最小长度。

示例 1：
输入：words = ["aa","ab","bc"] 输出：4 解释：这个例子中，我们按以下顺序执行连接操作，得到 `str_2` 的最小长度： `str_0 = "aa"` `str_1 = join(str_0, "ab") = "aab" ``str_2 = join(str_1, "bc") = "aabc"`  `str_2` 的最小长度为 4 。
示例 2：
输入：words = ["ab","b"] 输出：2 解释：这个例子中，str_0 = "ab"，可以得到两个不同的 str_1： join(str_0, "b") = "ab" 或者 join("b", str_0) = "bab" 。 第一个字符串 "ab" 的长度最短，所以答案为 2 。
示例 3：
输入：words = ["aaa","c","aba"] 输出：6 解释：这个例子中，我们按以下顺序执行连接操作，得到 `str_2 的最小长度：` `str_0 = "`aaa" `str_1 = join(str_0, "c") = "aaac"` `str_2 = join("aba", str_1) = "abaaac"` `str_2` 的最小长度为 6 。

提示：
`1 <= words.length <= 1000`
`1 <= words[i].length <= 50`
`words[i]` 中只包含小写英文字母。
"""

from typing import List, Optional


class Solution:
    def minimizeConcatenatedLength(self, words: List[str]) -> int:
        n = len(words)
        INF = 10 ** 9
        total_len = sum(len(w) for w in words)

        first_char = words[0][0]
        last_char = words[0][-1]

        dp = { (first_char, last_char): 0 }

        for i in range(1, n):
            w = words[i]
            a, b = w[0], w[-1]
            new_dp = {}
            for (head, tail), saved in dp.items():
                new_saved_1 = saved + (1 if tail == a else 0)
                key1 = (head, b)
                if key1 not in new_dp or new_saved_1 > new_dp[key1]:
                    new_dp[key1] = new_saved_1

                new_saved_2 = saved + (1 if b == head else 0)
                key2 = (a, tail)
                if key2 not in new_dp or new_saved_2 > new_dp[key2]:
                    new_dp[key2] = new_saved_2
            dp = new_dp

        max_saved = max(dp.values())
        return total_len - max_saved



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, String, Dynamic Programming
#
# 解题思路:
# 问题可以转化为：总字符数固定（所有单词长度之和），我们想最大化"节省"的字符数（相邻相同字符被删除的次数）。
# DP 状态为 (head, tail)：当前拼接后字符串的首字符和尾字符，值为已节省的字符数。
# 每次新单词 w 可以从左边拼接（w + str）或从右边拼接（str + w），更新首尾字符并累加可能的节省。
# 最终答案 = 总长度 - 最大节省数。
#
# 时间复杂度: O(n * 26^2) 实际上每个状态只存首尾字符（26种可能）
# 空间复杂度: O(26^2) = O(1)
#
# 关键点:
# - 只需关注拼接后字符串的首尾字符，中间内容不影响后续拼接
# - 每次拼接最多节省 1 个字符（当相邻字符相同时）
# - 从总长度中减去最大节省数得到最小长度
