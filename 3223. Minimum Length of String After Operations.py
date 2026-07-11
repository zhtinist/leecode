"""
LeetCode #3223 - Minimum Length of String After Operations
操作后字符串的最短长度
https://leetcode.cn/problems/minimum-length-of-string-after-operations/

给你一个字符串 `s` 。
你需要对 `s` 执行以下操作 任意 次：
选择一个下标 `i` ，满足 `s[i]` 左边和右边都 至少 有一个字符与它相同。
删除 `i` 左边 离它 最近 的 `s[i]` 字符。
删除 `i` 右边 离它 最近 的 `s[i]` 字符。
请你返回执行完所有操作后， `s` 的 最短 长度。

示例 1：

输入：s = "abaacbcbb"
输出：5
解释：
我们执行以下操作：
选择下标 2 ，然后删除下标 0 和 3 处的字符，得到 `s = "bacbcbb"` 。
选择下标 3 ，然后删除下标 0 和 5 处的字符，得到 `s = "acbcb"` 。
示例 2：

输入：s = "aa"
输出：2
解释：
无法对字符串进行任何操作，所以返回初始字符串的长度。

提示：
`1 <= s.length <= 2 * 10^5`
`s` 只包含小写英文字母。
"""

from typing import List, Optional


class Solution:
    def minimumLength(self, s: str) -> int:
        from collections import Counter
        cnt = Counter(s)
        ans = 0
        for c in cnt.values():
            if c % 2 == 0:
                ans += 2
            else:
                ans += 1
        return ans










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Hash Table, String, Counting
#
# 解题思路:
# 对每个字符单独分析。操作规则：选取一个位置 i，其左右两侧至少各有一个相同字符，
# 删除左侧最近和右侧最近的相同字符（共删除 2 个，保留中间那个）。
# 对于频数为 c 的字符：
# - 每次操作减少 2 个该字符（删除左右各一个）
# - 无法操作时：当该字符不超过 2 个时（无法找到两侧都有相同字符的位置）
# - 若 c 为偶数：最终剩下 2 个
# - 若 c 为奇数：最终剩下 1 个
# 因此答案 = sum(2 if c % 2 == 0 else 1 for c in counts)
#
# 时间复杂度: O(n)
# 空间复杂度: O(1)（只有 26 个小写字母）
#
# 关键点:
# - 每种字符独立处理，操作不影响其他字符
# - 规律：奇数频数剩 1 个，偶数频数剩 2 个
