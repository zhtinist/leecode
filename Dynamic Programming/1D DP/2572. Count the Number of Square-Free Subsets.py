"""
LeetCode #2572 - Count the Number of Square-Free Subsets
无平方子集计数
https://leetcode.cn/problems/count-the-number-of-square-free-subsets/

给你一个正整数数组 `nums` 。
如果数组 `nums` 的子集中的元素乘积是一个 无平方因子数 ，则认为该子集是一个 无平方 子集。
无平方因子数 是无法被除 `1` 之外任何平方数整除的数字。
返回数组 `nums` 中 无平方 且 非空 的子集数目。因为答案可能很大，返回对 `10^9 + 7` 取余的结果。
`nums` 的 非空子集 是可以由删除 `nums` 中一些元素（可以不删除，但不能全部删除）得到的一个数组。如果构成两个子集时选择删除的下标不同，则认为这两个子集不同。

示例 1：
输入：nums = [3,4,4,5] 输出：3 解释：示例中有 3 个无平方子集： - 由第 0 个元素 [3] 组成的子集。其元素的乘积是 3 ，这是一个无平方因子数。 - 由第 3 个元素 [5] 组成的子集。其元素的乘积是 5 ，这是一个无平方因子数。 - 由第 0 个和第 3 个元素 [3,5] 组成的子集。其元素的乘积是 15 ，这是一个无平方因子数。 可以证明给定数组中不存在超过 3 个无平方子集。
示例 2：
输入：nums = [1] 输出：1 解释：示例中有 1 个无平方子集： - 由第 0 个元素 [1] 组成的子集。其元素的乘积是 1 ，这是一个无平方因子数。 可以证明给定数组中不存在超过 1 个无平方子集。

提示：
`1 <= nums.length <= 1000`
`1 <= nums[i] <= 30`
"""

from typing import List, Optional


class Solution:
    def squareFreeSubsets(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        pidx = {p: i for i, p in enumerate(primes)}
        # compute prime mask for numbers 1..30
        mask = [0] * 31
        for x in range(1, 31):
            m = 0
            valid = True
            t = x
            for p in primes:
                if t % p == 0:
                    t //= p
                    if t % p == 0:  # square factor
                        valid = False
                        break
                    m |= 1 << pidx[p]
            if valid and t == 1:
                mask[x] = m
            # else mask stays 0 (invalid)

        cnt = [0] * 31
        for x in nums:
            cnt[x] += 1

        dp = [0] * (1 << 10)
        dp[0] = 1

        for x in range(2, 31):
            if cnt[x] == 0 or mask[x] == 0:
                continue
            m = mask[x]
            for s in range((1 << 10) - 1, -1, -1):
                if dp[s] and (s & m) == 0:
                    dp[s | m] = (dp[s | m] + dp[s] * cnt[x]) % MOD

        total = sum(dp) % MOD
        total = (total * pow(2, cnt[1], MOD) - 1) % MOD
        return total



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Bit Manipulation, Array, Math, Dynamic Programming, Bitmask, Number Theory
#
# 解题思路:
# nums[i]<=30且平方因子数为不可被任何大于1的平方数整除。预先为1-30每个数计算质因数位掩码，
# 若含平方因子则标记为无效。使用DP在1024个位掩码状态上统计合法子集数：每个>=2的数（含质因数）
# 最多选一次（因为选两次会产生平方因子）。数字1可以选任意次，最后乘以2^count(1)。
# 遍历每个有效数字，反向更新DP避免重复计数。
#
# 时间复杂度: O(N + 30 * 2^10)，N为数组长度
# 空间复杂度: O(2^10)
#
# 关键点:
# - 10个质数对应10位掩码（2^10=1024）
# - DP反向遍历避免同一数字被多次选择
# - 1可以任意次选择，贡献2^cnt[1]倍乘子
# - 空子集不算，最终结果-1
