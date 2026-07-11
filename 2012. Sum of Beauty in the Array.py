"""
LeetCode #2012 - Sum of Beauty in the Array
数组美丽值求和
https://leetcode.cn/problems/sum-of-beauty-in-the-array/

给你一个下标从 0 开始的整数数组 `nums` 。对于每个下标 `i`（`1 <= i <= nums.length - 2`），`nums[i]` 的 美丽值 等于：
`2`，对于所有 `0 <= j < i` 且 `i < k <= nums.length - 1` ，满足 `nums[j] < nums[i] < nums[k]`
`1`，如果满足 `nums[i - 1] < nums[i] < nums[i + 1]` ，且不满足前面的条件
`0`，如果上述条件全部不满足
返回符合 `1 <= i <= nums.length - 2` 的所有 `nums[i]` 的 美丽值的总和 。

示例 1：
输入：nums = [1,2,3] 输出：2 解释：对于每个符合范围 1 <= i <= 1 的下标 i : - nums[1] 的美丽值等于 2
示例 2：
输入：nums = [2,4,6,4] 输出：1 解释：对于每个符合范围 1 <= i <= 2 的下标 i : - nums[1] 的美丽值等于 1 - nums[2] 的美丽值等于 0
示例 3：
输入：nums = [3,2,1] 输出：0 解释：对于每个符合范围 1 <= i <= 1 的下标 i : - nums[1] 的美丽值等于 0

提示：
`3 <= nums.length <= 10^5`
`1 <= nums[i] <= 10^5`
"""

from typing import List, Optional


class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        """
        Precompute prefix max and suffix min.
        For index i:
        - Beauty 2: max(nums[0..i-1]) < nums[i] < min(nums[i+1..n-1])
        - Beauty 1: nums[i-1] < nums[i] < nums[i+1] (and not beauty 2)
        - Beauty 0: otherwise
        """
        n = len(nums)
        # prefix_max[i] = max of nums[0..i]
        prefix_max = [0] * n
        prefix_max[0] = nums[0]
        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i - 1], nums[i])

        # suffix_min[i] = min of nums[i..n-1]
        suffix_min = [0] * n
        suffix_min[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(suffix_min[i + 1], nums[i])

        ans = 0
        for i in range(1, n - 1):
            if prefix_max[i - 1] < nums[i] < suffix_min[i + 1]:
                ans += 2
            elif nums[i - 1] < nums[i] < nums[i + 1]:
                ans += 1

        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array
#
# 解题思路:
# 预处理前缀最大值和后缀最小值。
# prefix_max[i] = nums[0..i] 的最大值
# suffix_min[i] = nums[i..n-1] 的最小值
# 对于每个 i (1 <= i <= n-2)：
# - 如果 prefix_max[i-1] < nums[i] < suffix_min[i+1]，美丽值为 2
#   （意味着 nums[i] 严格大于左边所有元素，严格小于右边所有元素）
# - 否则如果 nums[i-1] < nums[i] < nums[i+1]，美丽值为 1
# - 否则美丽值为 0
# 累加所有美丽值。
#
# 时间复杂度: O(N)，两次预处理扫描 + 一次遍历
# 空间复杂度: O(N)，prefix_max 和 suffix_min 数组
#
# 关键点:
# - 美丽值 2 条件更强：比左边 ALL 元素大，比右边 ALL 元素小
# - 美丽值 1 条件：仅和相邻元素比较
# - 前缀最大/后缀最小预处理一次完成所有查询
