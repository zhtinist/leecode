"""
LeetCode #3472 - Longest Palindromic Subsequence After at Most K Operations
至多 K 次操作后的最长回文子序列
https://leetcode.cn/problems/longest-palindromic-subsequence-after-at-most-k-operations/

给你一个字符串 `s` 和一个整数 `k`。
在一次操作中，你可以将任意位置的字符替换为字母表中相邻的字符（字母表是循环的，因此 `'z'` 的下一个字母是 `'a'`）。例如，将 `'a'` 替换为下一个字母结果是 `'b'`，将 `'a'` 替换为上一个字母结果是 `'z'`；同样，将 `'z'` 替换为下一个字母结果是 `'a'`，替换为上一个字母结果是 `'y'`。
返回在进行 最多 `k` 次操作后，`s` 的 最长回文子序列 的长度。
子序列 是一个 非空 字符串，可以通过删除原字符串中的某些字符（或不删除任何字符）并保持剩余字符的相对顺序得到。
回文 是正着读和反着读都相同的字符串。

示例 1：

输入: s = "abced", k = 2
输出: 3
解释:
将 `s[1]` 替换为下一个字母，得到 `"acced"`。
将 `s[4]` 替换为上一个字母，得到 `"accec"`。
子序列 `"ccc"` 形成一个长度为 3 的回文，这是最长的回文子序列。
示例 2：

输入: s = "aaazzz", k = 4
输出: 6
解释:
将 `s[0]` 替换为上一个字母，得到 `"zaazzz"`。
将 `s[4]` 替换为下一个字母，得到 `"zaazaz"`。
将 `s[3]` 替换为下一个字母，得到 `"zaaaaz"`。
整个字符串形成一个长度为 6 的回文。

提示:
`1 <= s.length <= 200`
`1 <= k <= 200`
`s` 仅由小写英文字母组成。
"""

from typing import List, Optional


class Solution:
    def longestPalindromicSubsequence(self, s: str, k: int) -> int:
        n = len(s)

        # dp_prev2[i][b]: best for substring of length L-2 starting at i, budget b
        # dp_prev1[i][b]: best for substring of length L-1 starting at i, budget b
        dp_prev2 = [[0] * (k + 1) for _ in range(n)]       # length 0
        dp_prev1 = [[1] * (k + 1) for _ in range(n)]       # length 1

        for length in range(2, n + 1):
            dp_cur = [[0] * (k + 1) for _ in range(n - length + 1)]
            for i in range(n - length + 1):
                j = i + length - 1
                for b in range(k + 1):
                    # Skip left or skip right
                    best = max(dp_prev1[i][b], dp_prev1[i + 1][b])

                    # Try to match s[i] and s[j]
                    d = abs(ord(s[i]) - ord(s[j]))
                    cost = min(d, 26 - d)
                    if cost == 0:  # same characters
                        best = max(best, dp_prev2[i + 1][b] + 2)
                    elif b >= cost:
                        best = max(best, dp_prev2[i + 1][b - cost] + 2)

                    dp_cur[i][b] = best
            dp_prev2 = dp_prev1
            dp_prev1 = dp_cur

        return max(dp_prev1[0])



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: String, Dynamic Programming
#
# 解题思路:
# 1. 经典最长回文子序列 DP + 操作次数限制
# 2. 定义 dp[i][j][b] = s[i..j] 在至多 b 次操作下的最长回文子序列
# 3. 空间优化：每次只保留前两个长度的 DP 表（长度 L-1 和 L-2）
# 4. 状态转移：
#    - 跳过左端 = dp(L-1, i)[b]（即不包含 s[i]）
#    - 跳过右端 = dp(L-1, i+1)[b]（即不包含 s[j]）
#    - 两端匹配：将字符变到相同的最小操作数为 min(|c1-c2|, 26-|c1-c2|)
#      若预算足够，best = max(best, dp(L-2, i+1)[b-cost] + 2)
# 5. 最终答案为 dp_prev1[0] 中的最大值（所有预算下的最优）
#
# 时间复杂度: O(n^2 * k)
# 空间复杂度: O(n * k)
#
# 关键点:
# - 字母表循环：cost = min(|a-b|, 26-|a-b|)
# - 空间优化到 O(nk) 通过滚动数组
# - 子序列可以跳过元素，所以有 skip 选项
