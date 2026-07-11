"""
LeetCode #3144 - Minimum Substring Partition of Equal Character Frequency
分割字符频率相等的最少子字符串
https://leetcode.cn/problems/minimum-substring-partition-of-equal-character-frequency/

给你一个字符串 `s` ，你需要将它分割成一个或者更多的 平衡 子字符串。比方说，`s == "ababcc"` 那么 `("abab", "c", "c")` ，`("ab", "abc", "c")` 和 `("ababcc")` 都是合法分割，但是 `("a", "bab", "cc")` ，`("aba", "bc", "c")` 和 `("ab", "abcc")` 不是，不平衡的子字符串用粗体表示。
请你返回 `s` 最少 能分割成多少个平衡子字符串。
注意：一个 平衡 字符串指的是字符串中所有字符出现的次数都相同。

示例 1：

输入：s = "fabccddg"
输出：3
解释：
我们可以将 `s` 分割成 3 个子字符串：`("fab, "ccdd", "g")` 或者 `("fabc", "cd", "dg")` 。
示例 2：

输入：s = "abababaccddb"
输出：2
解释：
我们可以将 `s` 分割成 2 个子字符串：`("abab", "abaccddb")` 。

提示：
`1 <= s.length <= 1000`
`s` 只包含小写英文字母。
"""

from typing import List, Optional


class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        n = len(s)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            cnt = [0] * 26
            for j in range(i - 1, -1, -1):
                cnt[ord(s[j]) - 97] += 1
                # 检查子串s[j:i]是否平衡：所有非零计数相等
                target = 0
                balanced = True
                for c in cnt:
                    if c > 0:
                        if target == 0:
                            target = c
                        elif c != target:
                            balanced = False
                            break
                if balanced:
                    dp[i] = min(dp[i], dp[j] + 1)

        return dp[n]



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Hash Table, String, Dynamic Programming, Counting
#
# 解题思路:
# 动态规划：dp[i]表示前i个字符的最少分割数。对于每个i，从后向前枚举子串起点j，
# 维护字符计数数组，检查s[j:i]是否平衡（所有出现字符的频次相等）。
# 若平衡则dp[i] = min(dp[i], dp[j] + 1)。n<=1000，O(n^2*26)可接受。
#
# 时间复杂度: O(n^2 * 26)，n<=1000
# 空间复杂度: O(n)
#
# 关键点:
# - 平衡定义：子串中所有字符出现次数相同
# - 后向枚举j同时维护计数，避免重复计算
# - dp从dp[j]转移，表示在j处新增一个分割
