"""
LeetCode #2438 - Range Product Queries of Powers
二的幂数组中查询范围内的乘积
https://leetcode.cn/problems/range-product-queries-of-powers/

给你一个正整数 `n` ，你需要找到一个下标从 0 开始的数组 `powers` ，它包含 最少 数目的 `2` 的幂，且它们的和为 `n` 。`powers` 数组是 非递减 顺序的。根据前面描述，构造 `powers` 数组的方法是唯一的。
同时给你一个下标从 0 开始的二维整数数组 `queries` ，其中 `queries[i] = [left_i, right_i]` ，其中 `queries[i]` 表示请你求出满足 `left_i <= j <= right_i` 的所有 `powers[j]` 的乘积。
请你返回一个数组 `answers` ，长度与 `queries` 的长度相同，其中 `answers[i]`是第 `i` 个查询的答案。由于查询的结果可能非常大，请你将每个 `answers[i]` 都对 `10^9 + 7` 取余 。

示例 1：
输入：n = 15, queries = [[0,1],[2,2],[0,3]] 输出：[2,4,64] 解释： 对于 n = 15 ，得到 powers = [1,2,4,8] 。没法得到元素数目更少的数组。 第 1 个查询的答案：powers[0] * powers[1] = 1 * 2 = 2 。 第 2 个查询的答案：powers[2] = 4 。 第 3 个查询的答案：powers[0] * powers[1] * powers[2] * powers[3] = 1 * 2 * 4 * 8 = 64 。 每个答案对 10^9 + 7 取余得到的结果都相同，所以返回 [2,4,64] 。
示例 2：
输入：n = 2, queries = [[0,0]] 输出：[2] 解释： 对于 n = 2, powers = [2] 。 唯一一个查询的答案是 powers[0] = 2 。答案对 10^9 + 7 取余后结果相同，所以返回 [2] 。

提示：
`1 <= n <= 10^9`
`1 <= queries.length <= 10^5`
`0 <= start_i <= end_i < powers.length`
"""

from typing import List, Optional


class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = 10 ** 9 + 7

        # 将 n 分解为 2 的幂次数组
        powers = []
        bit = 0
        while n:
            if n & 1:
                powers.append(1 << bit)
            n >>= 1
            bit += 1

        # 构建前缀积数组
        m = len(powers)
        pref = [1] * (m + 1)
        for i in range(m):
            pref[i + 1] = (pref[i] * powers[i]) % MOD

        # 回答查询：区间积 = pref[r+1] * inv(pref[l]) % MOD
        result = []
        for l, r in queries:
            ans = pref[r + 1] * pow(pref[l], MOD - 2, MOD) % MOD
            result.append(ans)

        return result


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Bit Manipulation, Array, Prefix Sum
#
# 解题思路:
# 首先将 n 用二进制表示分解为 2 的幂次数组 powers：
# n 的二进制中每一个为 1 的位对应一个 2^i，这些 2^i 构成 powers 数组。
# 然后构建前缀积数组 pref，其中 pref[i] = powers[0] * ... * powers[i-1] % MOD。
# 对于查询 [l, r]，区间积 = powers[l] * ... * powers[r]
# = pref[r+1] * pow(pref[l], MOD-2, MOD) % MOD（利用费马小定理求模逆元）。
#
# 时间复杂度: O(log n + q)，q 为查询数量
# 空间复杂度: O(log n + q)
#
# 关键点:
# - 二进制分解 n 得到 powers 数组
# - 前缀积配合费马小定理求模逆元：a^(MOD-2) ≡ a^(-1) (mod MOD)
# - MOD = 10^9 + 7 是质数，满足费马小定理条件
