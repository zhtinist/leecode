"""
LeetCode #2439 - Minimize Maximum of Array
最小化数组中的最大值
https://leetcode.cn/problems/minimize-maximum-of-array/

给你一个下标从 0 开始的数组 `nums` ，它含有 `n` 个非负整数。
每一步操作中，你需要：
选择一个满足 `1 <= i < n` 的整数 `i` ，且 `nums[i] > 0` 。
将 `nums[i]` 减 1 。
将 `nums[i - 1]` 加 1 。
你可以对数组执行 任意 次上述操作，请你返回可以得到的 `nums` 数组中 最大值 最小 为多少。

示例 1：
输入：nums = [3,7,1,6] 输出：5 解释： 一串最优操作是： 1. 选择 i = 1 ，nums 变为 [4,6,1,6] 。 2. 选择 i = 3 ，nums 变为 [4,6,2,5] 。 3. 选择 i = 1 ，nums 变为 [5,5,2,5] 。 nums 中最大值为 5 。无法得到比 5 更小的最大值。 所以我们返回 5 。
示例 2：
输入：nums = [10,1] 输出：10 解释： 最优解是不改动 nums ，10 是最大值，所以返回 10 。

提示：
`n == nums.length`
`2 <= n <= 10^5`
`0 <= nums[i] <= 10^9`
"""

from typing import List, Optional


class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        # 操作只能把后面的值往前移，因此从左到右累加前缀和
        # 对于前缀 i，最小的最大值至少为 ceil(prefix_sum / (i+1))
        ans = 0
        prefix_sum = 0
        for i, num in enumerate(nums):
            prefix_sum += num
            # 向上取整：等价于 (prefix_sum + i) // (i + 1)
            ans = max(ans, (prefix_sum + i) // (i + 1))
        return ans


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Array, Binary Search, Dynamic Programming, Prefix Sum
#
# 解题思路:
# 操作规定只能将 nums[i] 减 1 并将 nums[i-1] 加 1，即只能将值向左移动。
# 这意味着对于任意前缀 [0...i]，这些元素的总和不会改变，
# 我们只能在这些元素内部重新分配值。
# 因此前缀中的最大值至少为 ceil(前缀和 / (i+1))（即平均值向上取整）。
# 遍历所有前缀，取这些下限的最大值就是答案。
# 因为操作只能向左移动，越靠左的元素越容易变大，前缀平均值是最紧的下界。
#
# 时间复杂度: O(n)
# 空间复杂度: O(1)
#
# 关键点:
# - 核心观察：只能把值向左移动，前缀和不变
# - 答案 = max(ceil(prefix_sum[i] / (i+1))) 对所有 i
# - 向上取整技巧：(a + b - 1) // b 即 (prefix_sum + i) // (i + 1)
