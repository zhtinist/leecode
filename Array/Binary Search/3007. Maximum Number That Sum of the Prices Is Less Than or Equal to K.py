"""
LeetCode #3007 - Maximum Number That Sum of the Prices Is Less Than or Equal to K
价值和小于等于 K 的最大数字
https://leetcode.cn/problems/maximum-number-that-sum-of-the-prices-is-less-than-or-equal-to-k/

给你一个整数 `k` 和一个整数 `x` 。整数 `num` 的价值是它的二进制表示中在 `x`，`2x`，`3x` 等位置处 设置位 的数目（从最低有效位开始）。下面的表格包含了如何计算价值的例子。   	 		 			x 			num 			Binary Representation 			Price 		 		 			1 			13 			000001101 			3 		 		 			2 			13 			000001101 			1 		 		 			2 			233 			011101001 			3 		 		 			3 			13 			000001101 			1 		 		 			3 			362 			101101010 			2

`num` 的 累加价值 是从 `1` 到 `num` 的数字的 总 价值。如果 `num` 的累加价值小于或等于 `k` 则被认为是 廉价 的。
请你返回 最大 的廉价数字。

示例 1：
输入：k = 9, x = 1 输出：6 解释：由下表所示，6 是最大的廉价数字。    	 		 			x 			num 			Binary Representation 			Price 			Accumulated Price 		 		 			1 			1 			001 			1 			1 		 		 			1 			2 			010 			1 			2 		 		 			1 			3 			011 			2 			4 		 		 			1 			4 			100 			1 			5 		 		 			1 			5 			101 			2 			7 		 		 			1 			6 			110 			2 			9 		 		 			1 			7 			111 			3 			12
示例 2：
输入：k = 7, x = 2 输出：9 解释：由下表所示，9 是最大的廉价数字。    	 		 			x 			num 			Binary Representation 			Price 			Accumulated Price 		 		 			2 			1 			0001 			0 			0 		 		 			2 			2 			0010 			1 			1 		 		 			2 			3 			0011 			1 			2 		 		 			2 			4 			0100 			0 			2 		 		 			2 			5 			0101 			0 			2 		 		 			2 			6 			0110 			1 			3 		 		 			2 			7 			0111 			1 			4 		 		 			2 			8 			1000 			1 			5 		 		 			2 			9 			1001 			1 			6 		 		 			2 			10 			1010 			2 			8

提示：
`1 <= k <= 10^15`
`1 <= x <= 8`
"""

from typing import List, Optional


class Solution:
    def findMaximumNumber(self, k: int, x: int) -> int:
        """
        Binary search for the maximum num. For a given num, compute
        accumulated price using bit counting at positions x, 2x, 3x, ...
        """

        def accumulated_price(num: int) -> int:
            """Sum of set bits at positions x, 2x, 3x, ... for 1..num."""
            total = 0
            p = x - 1  # 0-indexed position
            # While 2^p <= num (position is within range)
            while p <= 60 and (1 << p) <= num:
                period = 1 << (p + 1)
                half = 1 << p
                full = (num + 1) // period
                rem = (num + 1) % period
                total += full * half + max(0, rem - half)
                p += x
            return total

        lo, hi = 1, 10**16  # k up to 10^15, num could be larger
        ans = 0

        while lo <= hi:
            mid = (lo + hi) // 2
            if accumulated_price(mid) <= k:
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1

        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Bit Manipulation, Math, Binary Search, Dynamic Programming
#
# 解题思路:
# 二分搜索最大的 num。对于给定的 num，统计 1..num 范围内所有数在位置 x, 2x, 3x, ... 上的置位数之和。
# 每个位位置 p 的 1 的数量有周期性规律：每 2^(p+1) 个数为一个周期，前 2^p 个数的该位为 1。
# 利用该公式 O(log(num)) 计算累加价值，然后在 [1, 10^16] 上二分搜索。
#
# 时间复杂度: O(log(K) * log(N))，二分约 54 次，每次计算约 7 个位位置
# 空间复杂度: O(1)
#
# 关键点:
# - 位计数的周期性：位置 p 的 1 以 2^(p+1) 为周期，每周期有 2^p 个 1
# - 累加价值随 num 单调递增，可以用二分查找
# - 只需检查 x, 2x, 3x, ... 这些位置，不是所有位置
