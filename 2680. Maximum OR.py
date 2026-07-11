"""
LeetCode #2680 - Maximum OR
最大或值
https://leetcode.cn/problems/maximum-or/

给你一个下标从 0 开始长度为 `n` 的整数数组 `nums` 和一个整数 `k` 。每一次操作中，你可以选择一个数并将它乘 `2` 。
你最多可以进行 `k` 次操作，请你返回 `nums[0] | nums[1] | ... | nums[n - 1]` 的最大值。
`a | b` 表示两个整数 `a` 和 `b` 的 按位或 运算。

示例 1：
输入：nums = [12,9], k = 1 输出：30 解释：如果我们对下标为 1 的元素进行操作，新的数组为 [12,18] 。此时得到最优答案为 12 和 18 的按位或运算的结果，也就是 30 。
示例 2：
输入：nums = [8,1,2], k = 2 输出：35 解释：如果我们对下标 0 处的元素进行操作，得到新数组 [32,1,2] 。此时得到最优答案为 32|1|2 = 35 。

提示：
`1 <= nums.length <= 10^5`
`1 <= nums[i] <= 10^9`
`1 <= k <= 15`
"""

from typing import List, Optional


class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # prefix[i] = OR of nums[0..i-1]
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] | nums[i]

        # suffix[i] = OR of nums[i+1..n-1]
        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] | nums[i]

        ans = 0
        for i in range(n):
            # multiply nums[i] by 2^k (i.e., left shift by k)
            modified = nums[i] << k
            cur = prefix[i] | modified | suffix[i + 1]
            ans = max(ans, cur)

        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Bit Manipulation, Array, Prefix Sum
#
# 解题思路:
# 由于乘2等价于左移一位，k次操作应全部用在同一个数上（乘法集中在单个数上OR结果最大）。
# 使用前缀OR和后缀OR数组，枚举每个位置作为被操作的元素：
# 当前结果 = 前缀OR(不含i) | nums[i]<<k | 后缀OR(不含i)。
# 取所有位置的最大值。
#
# 时间复杂度: O(n)
# 空间复杂度: O(n)
#
# 关键点:
# - k次操作应全部集中在同一个数上（贪心最优）
# - 前缀/后缀OR数组快速计算"除当前元素外"的OR值
# - nums[i] << k 等价于乘2^k
