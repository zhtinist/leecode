"""
LeetCode #3029 - Minimum Time to Revert Word to Initial State I
将单词恢复初始状态所需的最短时间 I
https://leetcode.cn/problems/minimum-time-to-revert-word-to-initial-state-i/

给你一个下标从 0 开始的字符串 `word` 和一个整数 `k` 。
在每一秒，你必须执行以下操作：
移除 `word` 的前 `k` 个字符。
在 `word` 的末尾添加 `k` 个任意字符。
注意 添加的字符不必和移除的字符相同。但是，必须在每一秒钟都执行 两种 操作。
返回将 `word` 恢复到其 初始 状态所需的 最短 时间（该时间必须大于零）。

示例 1：
输入：word = "abacaba", k = 3 输出：2 解释： 第 1 秒，移除 word 的前缀 "aba"，并在末尾添加 "bac" 。因此，word 变为 "cababac"。 第 2 秒，移除 word 的前缀 "cab"，并在末尾添加 "aba" 。因此，word 变为 "abacaba" 并恢复到始状态。 可以证明，2 秒是 word 恢复到其初始状态所需的最短时间。
示例 2：
输入：word = "abacaba", k = 4 输出：1 解释： 第 1 秒，移除 word 的前缀 "abac"，并在末尾添加 "caba" 。因此，word 变为 "abacaba" 并恢复到初始状态。 可以证明，1 秒是 word 恢复到其初始状态所需的最短时间。
示例 3：
输入：word = "abcbabcd", k = 2 输出：4 解释： 每一秒，我们都移除 word 的前 2 个字符，并在 word 末尾添加相同的字符。 4 秒后，word 变为 "abcbabcd" 并恢复到初始状态。 可以证明，4 秒是 word 恢复到其初始状态所需的最短时间。

提示：
`1 <= word.length <= 50`
`1 <= k <= word.length`
`word`仅由小写英文字母组成。
"""

from typing import List, Optional


class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        """
        After t seconds, first t*k characters are removed from the front
        and t*k arbitrary characters are appended. The word returns to
        initial state when word[t*k:] equals word[:n-t*k].
        Find the smallest t >= 1 satisfying this.
        """
        n = len(word)
        t = 1
        while t * k < n:
            # Check if suffix starting at t*k equals prefix of same length
            if word[t * k:] == word[:n - t * k]:
                return t
            t += 1
        # When t*k >= n, all original chars are removed, we can append anything
        # ceil(n/k) seconds needed
        return (n + k - 1) // k



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: String, String Matching, Hash Function, Rolling Hash
#
# 解题思路:
# 每秒操作：移除前 k 个字符，追加 k 个任意字符。经过 t 秒后，原字符串的前 t*k 个字符被移除。
# 要恢复初始状态，需要 word[t*k:] == word[:n-t*k]（后缀等于前缀），因为追加的字符可以任意选择来匹配后半部分。
# 枚举 t 从 1 到 ceil(n/k)，检查条件。如果所有原字符都被移除（t*k >= n），则一定可以恢复。
#
# 时间复杂度: O(n^2/k)，字符串切片比较，n <= 50 非常小
# 空间复杂度: O(n)，字符串切片
#
# 关键点:
# - 核心条件是 word[t*k:] == word[:n-t*k]，即剩余后缀等于原来前缀
# - 当 t*k >= n 时必然可以（因为追加字符可任意选）
# - 本题数据范围极小（n <= 50），暴力枚举即可
