"""
LeetCode #3862 - Find the Smallest Balanced Index
找出最小平衡下标
https://leetcode.cn/problems/find-the-smallest-balanced-index/

给你一个整数数组 `nums`。
如果某个下标 `i` 满足以下条件，则称其为 平衡下标： `i` 左侧所有元素的总和等于 `i` 右侧所有元素的乘积。
如果左侧没有元素，则总和视为 0。同样，如果右侧没有元素，则乘积视为 1。
要求返回最小的 平衡下标，如果不存在平衡下标，则返回 -1。

示例 1：

输入： nums = [2,1,2]
输出： 1
解释：
对于下标 `i = 1`：
左侧总和 = `nums[0] = 2`
右侧乘积 = `nums[2] = 2`
由于左侧总和等于右侧乘积，下标 1 是平衡下标。
没有更小的下标满足条件，因此答案是 1。
示例 2：

输入： nums = [2,8,2,2,5]
输出： 2
解释：
对于下标 `i = 2`：
左侧总和 = `2 + 8 = 10`
右侧乘积 = `2 * 5 = 10`
由于左侧总和等于右侧乘积，下标 2 是平衡下标。
没有更小的下标满足条件，因此答案是 2。
示例 3：

输入： nums = [1]
输出： -1
对于下标 `i = 0`：
左侧为空，因此左侧总和为 0。
右侧为空，因此右侧乘积为 1。
由于左侧总和不等于右侧乘积，下标 0 不是平衡下标。
因此，不存在平衡下标，答案是 -1。

提示：
`1 <= nums.length <= 10^5`
`1 <= nums[i] <= 10^9`
"""

from typing import List, Optional


class Solution:
    def smallestBalancedIndex(self, nums: List[int]) -> int:
        """
        For each index i:
          left sum  = sum(nums[0..i-1])
          right product = product(nums[i+1..n-1]) (1 if empty)
        Precompute a suffix product array, then scan left to right
        accumulating the left sum.
        Return the smallest i where left_sum == right_product.
        """
        n = len(nums)
        # right_prod[i] = product of nums[i..n-1]; right_prod[n] = 1
        right_prod = [1] * (n + 1)
        for i in range(n - 1, -1, -1):
            right_prod[i] = right_prod[i + 1] * nums[i]

        left_sum = 0
        for i in range(n):
            if left_sum == right_prod[i + 1]:
                return i
            left_sum += nums[i]

        return -1










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Prefix Sum
#
# 解题思路:
# 对每个下标 i，需要比较左侧元素之和与右侧元素之积。
# 预处理后缀积数组 right_prod，其中 right_prod[i] 表示 nums[i..n-1] 的乘积，
# right_prod[n] = 1（空积）。
# 然后从左到右扫描，维护前缀和 left_sum。对于每个 i：
#   左侧和 = left_sum（nums[0..i-1] 的和）
#   右侧积 = right_prod[i+1]（nums[i+1..n-1] 的积）
# 当两者相等时返回当前下标 i。
# 如果遍历结束都未找到，返回 -1。
#
# 时间复杂度: O(n)，n 为数组长度。两次遍历（一次计算后缀积，一次扫描）。
# 空间复杂度: O(n)，后缀积数组。可以优化为 O(1) 但从题目约束看 O(n) 可接受。
#   实际上 n <= 10^5，O(n) 空间完全合理。
#
# 关键点:
# - 乘积可能非常大（nums[i] <= 10^9，n <= 10^5），Python 的 big int 可处理。
# - 注意边界：i=0 时左侧为空（和为 0），i=n-1 时右侧为空（积为 1）。
# - 返回最小的平衡下标，所以从左到右扫描找到第一个即可。
