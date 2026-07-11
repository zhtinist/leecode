"""
LeetCode #3428 - Maximum and Minimum Sums of at Most Size K Subsequences
最多 K 个元素的子序列的最值之和
https://leetcode.cn/problems/maximum-and-minimum-sums-of-at-most-size-k-subsequences/

给你一个整数数组 `nums` 和一个正整数 `k`，返回所有长度最多为 `k` 的 子序列 中 最大值 与 最小值 之和的总和。
非空子序列 是指从另一个数组中删除一些或不删除任何元素（且不改变剩余元素的顺序）得到的数组。
由于答案可能非常大，请返回对 `10^9 + 7` 取余数的结果。

示例 1：

输入： nums = [1,2,3], k = 2
输出： 24
解释：
数组 `nums` 中所有长度最多为 2 的子序列如下：   	 		 			子序列 			最小值 			最大值 			和 		 	 	 		 			`[1]` 			1 			1 			2 		 		 			`[2]` 			2 			2 			4 		 		 			`[3]` 			3 			3 			6 		 		 			`[1, 2]` 			1 			2 			3 		 		 			`[1, 3]` 			1 			3 			4 		 		 			`[2, 3]` 			2 			3 			5 		 		 			总和 			  			  			24
因此，输出为 24。
示例 2：

输入： nums = [5,0,6], k = 1
输出： 22
解释：
对于长度恰好为 1 的子序列，最小值和最大值均为元素本身。因此，总和为 `5 + 5 + 0 + 0 + 6 + 6 = 22`。
示例 3：

输入： nums = [1,1,1], k = 2
输出： 12
解释：
子序列 `[1, 1]` 和 `[1]` 各出现 3 次。对于所有这些子序列，最小值和最大值均为 1。因此，总和为 12。

提示：
`1 <= nums.length <= 10^5`
`0 <= nums[i] <= 10^9`
`1 <= k <= min(100, nums.length)`
"""

from typing import List, Optional


class Solution:
    def minMaxSums(self, nums: List[int], k: int) -> int:
        MOD = 10 ** 9 + 7
        n = len(nums)
        nums.sort()

        # Precompute factorials and inverse factorials
        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i % MOD
        inv_fact = [1] * (n + 1)
        inv_fact[n] = pow(fact[n], MOD - 2, MOD)
        for i in range(n, 0, -1):
            inv_fact[i - 1] = inv_fact[i] * i % MOD

        def C(n_val: int, r: int) -> int:
            if r < 0 or r > n_val:
                return 0
            return fact[n_val] * inv_fact[r] % MOD * inv_fact[n_val - r] % MOD

        ans = 0
        for i, x in enumerate(nums):
            left = i
            right = n - 1 - i
            for s in range(min(k, left + 1)):
                ans = (ans + x * C(left, s)) % MOD
            for s in range(min(k, right + 1)):
                ans = (ans + x * C(right, s)) % MOD

        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Math, Dynamic Programming, Combinatorics, Sorting
#
# 解题思路:
# 排序数组后，每个元素作为最小值的贡献：从右边选0~min(k-1, right)个元素组成子序列。
# 作为最大值的贡献：从左边选0~min(k-1, left)个元素。使用组合数计算每种选择的方案数，
# 乘以元素值累加。预计算阶乘和逆阶乘用于O(1)求组合数。
#
# 时间复杂度: O(n*k + n log n)
# 空间复杂度: O(n)
#
# 关键点:
# - 排序后每个元素作为最小值时，其他元素必须来自其右侧
# - 每个元素作为最大值时，其他元素必须来自其左侧
# - 需要计算组合数C(n, r)模10^9+7
