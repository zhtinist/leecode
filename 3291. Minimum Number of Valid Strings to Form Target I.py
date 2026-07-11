"""
LeetCode #3291 - Minimum Number of Valid Strings to Form Target I
形成目标字符串需要的最少字符串数 I
https://leetcode.cn/problems/minimum-number-of-valid-strings-to-form-target-i/

给你一个字符串数组 `words` 和一个字符串 `target`。
如果字符串 `x` 是 `words` 中 任意 字符串的 前缀，则认为 `x` 是一个 有效 字符串。
现计划通过 连接 有效字符串形成 `target` ，请你计算并返回需要连接的 最少 字符串数量。如果无法通过这种方式形成 `target`，则返回 `-1`。

示例 1：

输入： words = ["abc","aaaaa","bcdef"], target = "aabcdabc"
输出： 3
解释：
target 字符串可以通过连接以下有效字符串形成：
`words[1]` 的长度为 2 的前缀，即 `"aa"`。
`words[2]` 的长度为 3 的前缀，即 `"bcd"`。
`words[0]` 的长度为 3 的前缀，即 `"abc"`。
示例 2：

输入： words = ["abababab","ab"], target = "ababaababa"
输出： 2
解释：
target 字符串可以通过连接以下有效字符串形成：
`words[0]` 的长度为 5 的前缀，即 `"ababa"`。
`words[0]` 的长度为 5 的前缀，即 `"ababa"`。
示例 3：

输入： words = ["abcdef"], target = "xyz"
输出： -1

提示：
`1 <= words.length <= 100`
`1 <= words[i].length <= 5 * 10^3`
输入确保 `sum(words[i].length) <= 10^5`。
`words[i]` 只包含小写英文字母。
`1 <= target.length <= 5 * 10^3`
`target` 只包含小写英文字母。
"""

from typing import List, Optional


class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        # 构建 Trie
        trie = {}
        for w in words:
            node = trie
            for ch in w:
                if ch not in node:
                    node[ch] = {}
                node = node[ch]

        n = len(target)
        # dp[i] = 形成 target[0..i-1] 所需的最少字符串数
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(n):
            if dp[i] == float('inf'):
                continue
            # 从 target[i] 开始在 Trie 中匹配最长的前缀
            node = trie
            j = i
            while j < n and target[j] in node:
                node = node[target[j]]
                j += 1
                dp[j] = min(dp[j], dp[i] + 1)

        return dp[n] if dp[n] != float('inf') else -1










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Trie, Segment Tree, Array, String, Binary Search, Dynamic Programming, String Matching, Hash Function, Rolling Hash
#
# 解题思路:
# 有效字符串是 words 中任意单词的前缀。
# 将 words 中所有字符串插入 Trie。
# DP：dp[i] = 形成 target 前 i 个字符所需的最少有效字符串数。
# 对于每个位置 i，从 target[i] 开始在 Trie 中匹配最长的有效前缀，
# 对于每个匹配到的位置 j > i，更新 dp[j] = min(dp[j], dp[i] + 1)。
#
# 时间复杂度: O(L + n * T) 其中 L = sum(words[i].length), n = len(target), T 为平均匹配长度
# 空间复杂度: O(L + n)
#
# 关键点:
# - 用 Trie 快速查找从任意位置开始的最长有效前缀
# - DP 状态转移：每次匹配一个有效前缀
