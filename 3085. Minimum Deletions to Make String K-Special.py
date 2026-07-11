"""
LeetCode #3085 - Minimum Deletions to Make String K-Special
成为 K 特殊字符串需要删除的最少字符数
https://leetcode.cn/problems/minimum-deletions-to-make-string-k-special/

给你一个字符串 `word` 和一个整数 `k`。
如果 `|freq(word[i]) - freq(word[j])| <= k` 对于字符串中所有下标 `i` 和 `j`  都成立，则认为 `word` 是 k 特殊字符串。
此处，`freq(x)` 表示字符 `x` 在 `word` 中的出现频率，而 `|y|` 表示 `y` 的绝对值。
返回使 `word` 成为 k 特殊字符串 需要删除的字符的最小数量。

示例 1：

输入：word = "aabcaba", k = 0
输出：3
解释：可以删除 `2` 个 `"a"` 和 `1` 个 `"c"` 使 `word` 成为 `0` 特殊字符串。`word` 变为 `"baba"`，此时 `freq('a') == freq('b') == 2`。
示例 2：

输入：word = "dabdcbdcdcd", k = 2
输出：2
解释：可以删除 `1` 个 `"a"` 和 `1` 个 `"d"` 使 `word` 成为 `2` 特殊字符串。`word` 变为 `"bdcbdcdcd"`，此时 `freq('b') == 2`，`freq('c') == 3`，`freq('d') == 4`。
示例 3：

输入：word = "aaabaaa", k = 2
输出：1
解释：可以删除 1 个 `"b"` 使 `word` 成为 `2`特殊字符串。因此，`word` 变为 `"aaaaaa"`，此时每个字母的频率都是 `6`。

提示：
`1 <= word.length <= 10^5`
`0 <= k <= 10^5`
`word` 仅由小写英文字母组成。
"""

from typing import List, Optional


class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        """
        For each possible minimum frequency min_f (from 0 to max freq),
        compute deletions needed to bring all character frequencies into
        [min_f, min_f + k]. Take the minimum.
        """
        from collections import Counter

        freq = list(Counter(word).values())
        max_f = max(freq)
        ans = len(word)  # worst case: delete everything

        for min_f in range(max_f + 1):
            deletions = 0
            for f in freq:
                if f < min_f:
                    deletions += f  # delete all occurrences
                elif f > min_f + k:
                    deletions += f - (min_f + k)  # reduce to upper bound
                # else: f is in [min_f, min_f+k], keep all
            ans = min(ans, deletions)

        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Hash Table, String, Counting, Sorting
#
# 解题思路:
# 要使所有字符频率之差不超过 k，需要选择一个频率区间 [min_f, min_f+k]。
# 枚举可能的 min_f（从 0 到最大频率），对于每个字符频率 f：
# - 若 f < min_f：删除所有该字符（f 次）
# - 若 f > min_f + k：删除多余部分（f - (min_f + k) 次）
# - 若 min_f <= f <= min_f + k：完全保留
# 取所有 min_f 中的最小删除次数。
#
# 时间复杂度: O(26 * max_freq)，max_freq <= 10^5，26 个字母
# 空间复杂度: O(26) = O(1)
#
# 关键点:
# - 只需考虑 26 个字母的频率，枚举 min_f 到 max_freq
# - 频率区间的下界 min_f 决定了哪些字符需要完全删除（低于下界的）
# - 上界 min_f+k 决定了哪些字符需要削减（高于上界的）
