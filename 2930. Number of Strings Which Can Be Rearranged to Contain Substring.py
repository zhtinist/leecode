"""
LeetCode #2930 - Number of Strings Which Can Be Rearranged to Contain Substring
重新排列后包含指定子字符串的字符串数目
https://leetcode.cn/problems/number-of-strings-which-can-be-rearranged-to-contain-substring/

给你一个整数 `n` 。
如果一个字符串 `s` 只包含小写英文字母，且 将 `s` 的字符重新排列后，新字符串包含 子字符串 `"leet"` ，那么我们称字符串 `s` 是一个 好 字符串。
比方说：
字符串 `"lteer"` 是好字符串，因为重新排列后可以得到 `"leetr"` 。
`"letl"` 不是好字符串，因为无法重新排列并得到子字符串 `"leet"` 。
请你返回长度为 `n` 的好字符串 总 数目。
由于答案可能很大，将答案对 `10^9 + 7` 取余 后返回。
子字符串 是一个字符串中一段连续的字符序列。

示例 1：
输入：n = 4 输出：12 解释：总共有 12 个字符串重新排列后包含子字符串 "leet" ："eelt" ，"eetl" ，"elet" ，"elte" ，"etel" ，"etle" ，"leet" ，"lete" ，"ltee" ，"teel" ，"tele" 和 "tlee" 。
示例 2：
输入：n = 10 输出：83943898 解释：长度为 10 的字符串重新排列后包含子字符串 "leet" 的方案数为 526083947580 。所以答案为 526083947580 % (10^9 + 7) = 83943898 。

提示：
`1 <= n <= 10^5`
"""

from typing import List, Optional


class Solution:
    def stringCount(self, n: int) -> int:
        MOD = 10**9 + 7
        # dp[l][e][t]: l in {0,1}, e in {0,1,2}, t in {0,1}
        dp = [[[0, 0], [0, 0], [0, 0]] for _ in range(2)]
        dp[0][0][0] = 1

        for _ in range(n):
            ndp = [[[0, 0], [0, 0], [0, 0]] for _ in range(2)]
            for l in range(2):
                for e in range(3):
                    for t in range(2):
                        cur = dp[l][e][t]
                        if cur == 0:
                            continue
                        # Add 'l'
                        ndp[min(1, l + 1)][e][t] = (ndp[min(1, l + 1)][e][t] + cur) % MOD
                        # Add 'e'
                        ndp[l][min(2, e + 1)][t] = (ndp[l][min(2, e + 1)][t] + cur) % MOD
                        # Add 't'
                        ndp[l][e][min(1, t + 1)] = (ndp[l][e][min(1, t + 1)] + cur) % MOD
                        # Add other 23 letters
                        ndp[l][e][t] = (ndp[l][e][t] + cur * 23) % MOD
            dp = ndp

        return dp[1][2][1]



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Math, Dynamic Programming, Combinatorics
#
# 解题思路:
# 字符串重新排列后能包含"leet"等价于同时满足：至少1个'l'、至少2个'e'、至少1个't'。
# 使用DP：dp[l][e][t] 其中 l 取0/1，e 取0/1/2，t 取0/1（均表示达到需求的最小计数）。
# 每次迭代添加一个字符，分别处理添加'l'、'e'、't'或其他23个字母的情况。
# 最终答案为 dp[1][2][1]（三项都满足）。
#
# 时间复杂度: O(n)
# 空间复杂度: O(1)
#
# 关键点:
# - 转换为字符计数条件：l>=1, e>=2, t>=1
# - 状态压缩DP：每个维度只需追踪是否达到阈值
# - 四种转移：加l、加e、加t、加其他23个字母
