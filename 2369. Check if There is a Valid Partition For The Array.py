"""
LeetCode #2369 - Check if There is a Valid Partition For The Array
检查数组是否存在有效划分
https://leetcode.cn/problems/check-if-there-is-a-valid-partition-for-the-array/

给你一个下标从 0 开始的整数数组 `nums` ，你必须将数组划分为一个或多个 连续 子数组。
如果获得的这些子数组中每个都能满足下述条件 之一 ，则可以称其为数组的一种 有效 划分：
子数组 恰 由 `2` 个相等元素组成，例如，子数组 `[2,2]` 。
子数组 恰 由 `3` 个相等元素组成，例如，子数组 `[4,4,4]` 。
子数组 恰 由 `3` 个连续递增元素组成，并且相邻元素之间的差值为 `1` 。例如，子数组 `[3,4,5]` ，但是子数组 `[1,3,5]` 不符合要求。
如果数组 至少 存在一种有效划分，返回 `true` ，否则，返回 `false` 。

示例 1：
输入：nums = [4,4,4,5,6] 输出：true 解释：数组可以划分成子数组 [4,4] 和 [4,5,6] 。 这是一种有效划分，所以返回 true 。
示例 2：
输入：nums = [1,1,1,2] 输出：false 解释：该数组不存在有效划分。

提示：
`2 <= nums.length <= 10^5`
`1 <= nums[i] <= 10^6`
"""

from typing import List, Optional


class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        # dp[i] 表示 nums[0:i] 是否可以有效划分（i 表示前缀长度）
        dp = [False] * (n + 1)
        dp[0] = True  # 空数组视为有效

        for i in range(2, n + 1):
            # 检查最后两个元素是否相等
            if nums[i - 1] == nums[i - 2]:
                dp[i] = dp[i] or dp[i - 2]

            # 检查最后三个元素
            if i >= 3:
                # 三个相等元素
                if nums[i - 1] == nums[i - 2] == nums[i - 3]:
                    dp[i] = dp[i] or dp[i - 3]
                # 三个连续递增元素
                if nums[i - 1] == nums[i - 2] + 1 == nums[i - 3] + 2:
                    dp[i] = dp[i] or dp[i - 3]

        return dp[n]



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Dynamic Programming
#
# 解题思路:
# 使用动态规划。定义 dp[i] 表示 nums 的前 i 个元素（即 nums[0:i]）是否可以有效划分。
# 初始状态 dp[0] = True（空数组视为有效划分）。
# 遍历 i 从 2 到 n，对每个位置检查两种可能的结尾情况：
# 1. 最后两个元素相等（2 个相等元素）：如果 dp[i-2] 为 True 且 nums[i-1]==nums[i-2]，则 dp[i]=True
# 2. 最后三个元素满足条件（3 个相等 或 3 个连续递增）：如果 dp[i-3] 为 True 且满足条件，则 dp[i]=True
# 最终返回 dp[n]。
#
# 时间复杂度: O(n) 其中 n 为 nums 数组的长度
# 空间复杂度: O(n) dp 数组的大小为 n+1
#
# 关键点:
# - dp[i] 表示前缀长度为 i 的子数组是否可以有效划分
# - 三种有效子数组的条件：两个相等、三个相等、三个连续递增
# - dp[0] = True 是关键初始化，确保长度为 2 或 3 的整个数组可以被正确判定
