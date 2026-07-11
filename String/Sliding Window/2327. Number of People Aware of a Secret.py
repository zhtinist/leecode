"""
LeetCode #2327 - Number of People Aware of a Secret
知道秘密的人数
https://leetcode.cn/problems/number-of-people-aware-of-a-secret/

在第 `1` 天，有一个人发现了一个秘密。
给你一个整数 `delay` ，表示每个人会在发现秘密后的 `delay` 天之后，每天 给一个新的人 分享 秘密。同时给你一个整数 `forget` ，表示每个人在发现秘密 `forget` 天之后会 忘记 这个秘密。一个人 不能 在忘记秘密那一天及之后的日子里分享秘密。
给你一个整数 `n` ，请你返回在第 `n` 天结束时，知道秘密的人数。由于答案可能会很大，请你将结果对 `10^9 + 7` 取余 后返回。

示例 1：
输入：n = 6, delay = 2, forget = 4 输出：5 解释： 第 1 天：假设第一个人叫 A 。（一个人知道秘密） 第 2 天：A 是唯一一个知道秘密的人。（一个人知道秘密） 第 3 天：A 把秘密分享给 B 。（两个人知道秘密） 第 4 天：A 把秘密分享给一个新的人 C 。（三个人知道秘密） 第 5 天：A 忘记了秘密，B 把秘密分享给一个新的人 D 。（三个人知道秘密） 第 6 天：B 把秘密分享给 E，C 把秘密分享给 F 。（五个人知道秘密）
示例 2：
输入：n = 4, delay = 1, forget = 3 输出：6 解释： 第 1 天：第一个知道秘密的人为 A 。（一个人知道秘密） 第 2 天：A 把秘密分享给 B 。（两个人知道秘密） 第 3 天：A 和 B 把秘密分享给 2 个新的人 C 和 D 。（四个人知道秘密） 第 4 天：A 忘记了秘密，B、C、D 分别分享给 3 个新的人。（六个人知道秘密）

提示：
`2 <= n <= 1000`
`1 <= delay < forget <= n`
"""

from typing import List, Optional


class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        """
        dp[i] = number of people who learn the secret on day i.

        A person who learns on day j can share on days [j+delay, j+forget-1].
        Each day they share with exactly 1 new person.

        So dp[i] = sum(dp[j]) for j in [i-forget+1, i-delay]
        i.e., all people who learned between day i-forget+1 and i-delay
        are actively sharing on day i.
        """
        MOD = 10**9 + 7
        dp = [0] * (n + 1)  # 1-indexed: dp[i] = people who learn on day i
        dp[1] = 1

        window_sum = 0  # sum of dp[j] for j in current sharing window

        for i in range(2, n + 1):
            # People who learned on day i-delay enter the sharing window
            if i - delay >= 1:
                window_sum = (window_sum + dp[i - delay]) % MOD
            # People who learned on day i-forget exit the sharing window (they forgot)
            if i - forget >= 1:
                window_sum = (window_sum - dp[i - forget]) % MOD
            dp[i] = window_sum

        # People who still know the secret on day n:
        # those who learned from day n-forget+1 to n (haven't forgotten yet)
        ans = 0
        for i in range(max(1, n - forget + 1), n + 1):
            ans = (ans + dp[i]) % MOD
        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Queue, Dynamic Programming, Simulation
#
# 解题思路:
# 定义 dp[i] 表示在第 i 天新知道秘密的人数。
# 第 1 天有 1 个人知道秘密，即 dp[1] = 1。
# 在第 j 天知道秘密的人，会在 [j+delay, j+forget-1] 这段时间内每天分享给
# 一个新人。因此第 i 天新知道秘密的人数等于所有在 [i-forget+1, i-delay]
# 天内知道秘密的人数之和。使用滑动窗口维护这个区间和：
#   - 当 i-delay >= 1 时，dp[i-delay] 加入窗口
#   - 当 i-forget >= 1 时，dp[i-forget] 移出窗口
# 最后，第 n 天结束时仍知道秘密的人是那些在 [n-forget+1, n] 天内知道秘密
# 且尚未忘记的人。
#
# 时间复杂度: O(n) — 单次遍历 n 天，每次 O(1) 更新滑动窗口
# 空间复杂度: O(n) — dp 数组存储每天新知道秘密的人数
#
# 关键点:
# - 滑动窗口维护"当前正在分享秘密"的人数区间和
# - 忘记秘密的人不再分享，需及时从窗口移出
# - 最终答案不是 dp[n]，而是过去 forget 天内知道秘密的人数之和
# - 负数取模需加 MOD 保证非负
