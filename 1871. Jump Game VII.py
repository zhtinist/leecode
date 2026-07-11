"""
LeetCode #1871 - Jump Game VII
跳跃游戏 VII
https://leetcode.cn/problems/jump-game-vii/

给你一个下标从 0 开始的二进制字符串 `s` 和两个整数 `minJump` 和 `maxJump` 。一开始，你在下标 `0` 处，且该位置的值一定为 `'0'` 。当同时满足如下条件时，你可以从下标 `i` 移动到下标 `j` 处：
`i + minJump <= j <= min(i + maxJump, s.length - 1)` 且
`s[j] == '0'`.
如果你可以到达 `s` 的下标 `s.length - 1` 处，请你返回 `true` ，否则返回 `false` 。

示例 1：
输入：s = "011010", minJump = 2, maxJump = 3 输出：true 解释： 第一步，从下标 0 移动到下标 3 。 第二步，从下标 3 移动到下标 5 。
示例 2：
输入：s = "01101110", minJump = 2, maxJump = 3 输出：false

提示：
`2 <= s.length <= 10^5`
`s[i]` 要么是 `'0'` ，要么是 `'1'`
`s[0] == '0'`
`1 <= minJump <= maxJump < s.length`
"""

from typing import List, Optional


class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        if s[-1] == '1':
            return False

        # dp[i] = whether position i is reachable
        dp = [False] * n
        dp[0] = True

        # prefix sum of dp to quickly check if any position in range is reachable
        # pre[i] = number of reachable positions in dp[0..i]
        pre = [0] * n
        pre[0] = 1  # dp[0] is True

        for i in range(1, n):
            if s[i] == '0':
                # Check if any position in [i-maxJump, i-minJump] is reachable
                left = max(0, i - maxJump)
                right = i - minJump
                if right >= 0:
                    # Count reachable positions in [left, right]
                    reachable_count = pre[right] - (pre[left - 1] if left > 0 else 0)
                    if reachable_count > 0:
                        dp[i] = True

            pre[i] = pre[i - 1] + (1 if dp[i] else 0)

        return dp[-1]



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: String, Dynamic Programming, Prefix Sum, Sliding Window
#
# 解题思路:
# 动态规划 + 前缀和优化。
# 1. dp[i] 表示位置 i 是否可达。
# 2. 对于位置 i (s[i]=='0')，检查区间 [i-maxJump, i-minJump] 内
#    是否存在可达位置。
# 3. 使用前缀和数组 pre 快速判断区间内是否有可达位置：
#    如果区间内可达位置计数 > 0，则 dp[i] = True。
# 4. 最终返回 dp[n-1]。
#
# 时间复杂度: O(n) — 单次遍历
# 空间复杂度: O(n) — dp 和前缀和数组
#
# 关键点:
# - s[0] 一定为 '0' 且是起点
# - 使用前缀和避免对每个位置 O(maxJump-minJump) 的区间检查
# - 跳跃范围是 [i+minJump, i+maxJump]
# - 目标位置 s[n-1] 必须为 '0'
