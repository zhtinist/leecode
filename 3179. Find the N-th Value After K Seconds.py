"""
LeetCode #3179 - Find the N-th Value After K Seconds
K 秒后第 N 个元素的值
https://leetcode.cn/problems/find-the-n-th-value-after-k-seconds/

给你两个整数 `n` 和 `k`。
最初，你有一个长度为 `n` 的整数数组 `a`，对所有 `0 <= i <= n - 1`，都有 `a[i] = 1` 。每过一秒，你会同时更新每个元素为其前面所有元素的和加上该元素本身。例如，一秒后，`a[0]` 保持不变，`a[1]` 变为 `a[0] + a[1]`，`a[2]` 变为 `a[0] + a[1] + a[2]`，以此类推。
返回 `k` 秒后 `a[n - 1]` 的值。
由于答案可能非常大，返回其对 `10^9 + 7` 取余 后的结果。

示例 1：

输入：n = 4, k = 5
输出：56
解释：   	 		 			时间（秒） 			数组状态 		 		 			0 			[1,1,1,1] 		 		 			1 			[1,2,3,4] 		 		 			2 			[1,3,6,10] 		 		 			3 			[1,4,10,20] 		 		 			4 			[1,5,15,35] 		 		 			5 			[1,6,21,56]
示例 2：

输入：n = 5, k = 3
输出：35
解释：   	 		 			时间（秒） 			数组状态 		 		 			0 			[1,1,1,1,1] 		 		 			1 			[1,2,3,4,5] 		 		 			2 			[1,3,6,10,15] 		 		 			3 			[1,4,10,20,35]

提示：
`1 <= n, k <= 1000`
"""

from typing import List, Optional


class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        MOD = 10 ** 9 + 7
        # 答案为组合数 C(k + n - 1, n - 1) = C(k + n - 1, k)
        N = k + n - 1
        r = min(k, n - 1)
        res = 1
        for i in range(r):
            res = res * (N - i) % MOD
            res = res * pow(i + 1, MOD - 2, MOD) % MOD
        return res



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Math, Combinatorics, Prefix Sum, Simulation
#
# 解题思路:
# 观察变换规律：每秒后a[i]变为前缀和。k秒后，a[i]的值等于组合数C(k+i, i)。
# 因此a[n-1] = C(k+n-1, n-1) = C(k+n-1, k)。
# 使用乘法公式计算组合数：C(N, r) = N*(N-1)*...*(N-r+1) / r!，
# 通过费马小定理求模逆元（pow(i, MOD-2, MOD)）计算除法。
#
# 时间复杂度: O(min(k, n))
# 空间复杂度: O(1)
#
# 关键点:
# - 发现数学规律：转换为组合数
# - 用乘法公式+模逆元计算组合数取模
# - 选较小的r（k或n-1）减少迭代次数
