"""
LeetCode #837 - New 21 Game
中文题名：新21点
https://leetcode.com/problems/new-21-game/

Alice plays the following game, loosely based on the card game "21".

Alice starts with `0` points, and draws numbers while she has less than
`K` points.  During each draw, she gains an integer number of points
randomly from the range `[1, W]`, where `W` is an integer.  Each
draw is independent and the outcomes have equal probabilities.

Alice stops drawing numbers when she gets `K` or more points.  What is the
probability that she has `N` or less points?

Example 1:

Input: N = 10, K = 1, W = 10
Output: 1.00000
Explanation:  Alice gets a single card, then stops.

Example 2:

Input: N = 6, K = 1, W = 10
Output: 0.60000
Explanation:  Alice gets a single card, then stops.
In 6 out of W = 10 possibilities, she is at or below N = 6 points.

Example 3:

Input: N = 21, K = 17, W = 10
Output: 0.73278

Note:

`0 <= K <= N <= 10000`

`1 <= W <= 10000`

Answers will be accepted as correct if they are within `10^-5` of the correct
answer.

The judging time limit has been reduced for this question.

【中文翻译】
爱丽丝参加一个大致基于纸牌游戏"21点"的规则的游戏，描述如下：

爱丽丝以 0 分开始，并在她的分数少于 `K` 分时抽取数字。每次抽取时，她从 `[1, W]` 的范围中随机获得一个整数分数，其中 `W` 是整数。每次抽取是独立的，且每个结果的概率相等。

当爱丽丝获得 `K` 或更多分时，她就停止抽取数字。她的分数不超过 `N` 的概率是多少？

示例 1：

输入：N = 10, K = 1, W = 10
输出：1.00000
解释：爱丽丝得到一张牌，然后停止。

示例 2：

输入：N = 6, K = 1, W = 10
输出：0.60000
解释：爱丽丝得到一张牌，然后停止。在 W = 10 的可能性中，有 6 种情况她的分数 <= N = 6。

示例 3：

输入：N = 21, K = 17, W = 10
输出：0.73278

注意：

`0 <= K <= N <= 10000`

`1 <= W <= 10000`

答案与正确答案误差在 `10^-5` 以内即视为正确。

此题的时间限制已降低。

"""

from typing import List, Optional


class Solution:
    def new21Game(self, n: int, k: int, w: int) -> float:
        if k == 0 or n >= k + w:
            return 1.0

        # dp[i] = probability of ending with exactly i points
        # We need dp up to K+W (max reachable points)
        dp = [0.0] * (k + w)
        dp[0] = 1.0

        # Sliding window sum of last W dp values
        window_sum = 1.0
        for i in range(1, k + w):
            dp[i] = window_sum / w
            if i < k:
                window_sum += dp[i]
            if i >= w:
                window_sum -= dp[i - w]

        # Sum probabilities for points <= N, but starting from K (where Alice stops)
        result = 0.0
        for i in range(k, min(n + 1, k + w)):
            result += dp[i]

        return result



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 动态规划 + 滑动窗口。
# 定义 dp[i] = 恰好得到 i 分的概率（无论是否停止）。
# 初始 dp[0] = 1（从 0 分开始）。
# 对于 i > 0：dp[i] = (dp[i-1] + dp[i-2] + ... + dp[i-W]) / W
# 即从最近 W 个状态转移而来，每个转移概率为 1/W。
#
# 关键细节：
# - 只有当分数 < K 时才能继续抽牌，因此只有状态 0 到 K-1 能转移到后续状态
# - 使用滑动窗口维护最近 W 个 dp 值的和（只包含那些 < K 的状态）
# - 最终答案为 sum(dp[K] + dp[K+1] + ... + dp[N])
#   （因为停止条件是 >= K，我们关心 <= N 的概率）
#
# 时间复杂度: O(K + W) — 遍历 dp 数组
# 空间复杂度: O(K + W) — dp 数组大小
#
# 关键点:
# - dp[i] 表示到达恰好 i 分的概率（到达途径无关）
# - 滑动窗口技巧将每次转移从 O(W) 降为 O(1)
# - 只有当 i < K 时 dp[i] 才进入窗口（因为这些状态还能继续抽牌）
# - 特殊情况：K = 0 或 N >= K + W - 1 时概率为 1（前者不抽牌，后者一定能到 <=N）
