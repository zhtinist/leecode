"""
LeetCode #3076 - Shortest Uncommon Substring in an Array
数组中的最短非公共子字符串
https://leetcode.cn/problems/shortest-uncommon-substring-in-an-array/

给你一个数组 `arr` ，数组中有 `n` 个 非空 字符串。
请你求出一个长度为 `n` 的字符串数组 `answer` ，满足：
`answer[i]` 是 `arr[i]` 最短 的子字符串，且它不是 `arr` 中其他任何字符串的子字符串。如果有多个这样的子字符串存在，`answer[i]` 应该是它们中字典序最小的一个。如果不存在这样的子字符串，`answer[i]` 为空字符串。
请你返回数组 `answer` 。

示例 1：
输入：arr = ["cab","ad","bad","c"] 输出：["ab","","ba",""] 解释：求解过程如下： - 对于字符串 "cab" ，最短没有在其他字符串中出现过的子字符串是 "ca" 或者 "ab" ，我们选择字典序更小的子字符串，也就是 "ab" 。 - 对于字符串 "ad" ，不存在没有在其他字符串中出现过的子字符串。 - 对于字符串 "bad" ，最短没有在其他字符串中出现过的子字符串是 "ba" 。 - 对于字符串 "c" ，不存在没有在其他字符串中出现过的子字符串。
示例 2：
输入：arr = ["abc","bcd","abcd"] 输出：["","","abcd"] 解释：求解过程如下： - 对于字符串 "abc" ，不存在没有在其他字符串中出现过的子字符串。 - 对于字符串 "bcd" ，不存在没有在其他字符串中出现过的子字符串。 - 对于字符串 "abcd" ，最短没有在其他字符串中出现过的子字符串是 "abcd" 。

提示：
`n == arr.length`
`2 <= n <= 100`
`1 <= arr[i].length <= 20`
`arr[i]` 只包含小写英文字母。
"""

from typing import List, Optional


class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        """
        n <= 100, len <= 20. For each string, enumerate substrings by
        (length, lexicographic order). First one not found in any other
        string is the answer.
        """
        n = len(arr)
        # Precompute all substrings of all strings (grouped by index)
        all_subs = [set() for _ in range(n)]  # substrings of each string
        global_count = {}

        for idx, s in enumerate(arr):
            m = len(s)
            seen_in_this = set()
            for i in range(m):
                for j in range(i + 1, m + 1):
                    sub = s[i:j]
                    if sub not in seen_in_this:
                        seen_in_this.add(sub)
                        all_subs[idx].add(sub)
                        global_count[sub] = global_count.get(sub, 0) + 1

        ans = []
        for idx, s in enumerate(arr):
            m = len(s)
            candidates = []
            for i in range(m):
                for j in range(i + 1, m + 1):
                    sub = s[i:j]
                    # Check if sub appears only in this string
                    if global_count.get(sub, 0) == 1:
                        candidates.append(sub)

            if not candidates:
                ans.append("")
            else:
                # Pick shortest, then lexicographically smallest
                candidates.sort(key=lambda x: (len(x), x))
                ans.append(candidates[0])

        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Trie, Array, Hash Table, String
#
# 解题思路:
# n <= 100，每个字符串长度 <= 20。预处理所有字符串的所有子串，统计每个子串出现在多少个不同的字符串中。
# 对每个字符串，枚举其所有子串，找出全局出现次数为 1（即只在该字符串中出现）的子串，
# 按长度优先、字典序次优先排序，取第一个。若无则返回空字符串。
#
# 时间复杂度: O(n * L^2)，L <= 20，总计约 40000 个子串
# 空间复杂度: O(n * L^2)，存储所有子串和全局计数
#
# 关键点:
# - 子串在每个字符串中只需计数一次（同一字符串内重复出现的子串不影响"非公共"的判断）
# - 答案按"最短、字典序最小"排序，即 (len, str) 升序
# - 暴力枚举在小数据范围内完全可行
