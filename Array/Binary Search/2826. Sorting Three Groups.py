"""
LeetCode #2826 - Sorting Three Groups
将三个组排序
https://leetcode.cn/problems/sorting-three-groups/

给你一个整数数组 `nums` 。`nums` 的每个元素是 1，2 或 3。在每次操作中，你可以删除 `nums` 中的一个元素。返回使 nums 成为 非递减 顺序所需操作数的 最小值。

示例 1：
输入：nums = [2,1,3,2,1] 输出：3 解释： 其中一个最优方案是删除 nums[0]，nums[2] 和 nums[3]。
示例 2：
输入：nums = [1,3,2,1,3,3] 输出：2 解释： 其中一个最优方案是删除 nums[1] 和 nums[2]。
示例 3：
输入：nums = [2,2,2,2,3,3] 输出：0 解释： nums 已是非递减顺序的。

提示：
`1 <= nums.length <= 100`
`1 <= nums[i] <= 3`
进阶：你可以使用 `O(n)` 时间复杂度以内的算法解决吗？
"""

from typing import List, Optional


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        dp1 = dp2 = dp3 = 0
        for v in nums:
            ndp1 = dp1 + (0 if v == 1 else 1)
            ndp2 = min(dp1, dp2) + (0 if v == 2 else 1)
            ndp3 = min(dp1, dp2, dp3) + (0 if v == 3 else 1)
            dp1, dp2, dp3 = ndp1, ndp2, ndp3
        return min(dp1, dp2, dp3)



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Binary Search, Dynamic Programming
#
# 解题思路:
# 问题等价于：将数组变为非递减序列（只有 1,2,3）需要的最少删除次数。
# 删除最少 = 保留最多。即求最长的非递减子序列（允许相等的元素）。
# DP：dp1/dp2/dp3 表示以 1/2/3 结尾的非递减序列的当前最优保留数。
# 对于每个元素 v，更新三个状态。最终保留数 = min(dp1, dp2, dp3)，删除数 = n - 保留数。
# 注意这里的 dp 实际存的是"操作次数"，直接计算删除数。
#
# 时间复杂度: O(n)
# 空间复杂度: O(1)
#
# 关键点:
# - 保留最多元素 = 求最长非递减子序列（LNDS），值只有 1,2,3
# - dp1: 以 1 结尾的 LNDS 的保留数，dp2: 以 2 结尾，dp3: 以 3 结尾
# - 以 2 结尾可以从前面的 1 或 2 转移，以 3 结尾可以从 1,2,3 转移
