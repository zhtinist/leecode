"""
LeetCode #2740 - Find the Value of the Partition
找出分区值
https://leetcode.cn/problems/find-the-value-of-the-partition/

给你一个 正 整数数组 `nums` 。
将 `nums` 分成两个数组：`nums1` 和 `nums2` ，并满足下述条件：
数组 `nums` 中的每个元素都属于数组 `nums1` 或数组 `nums2` 。
两个数组都 非空 。
分区值 最小 。
分区值的计算方法是 `|max(nums1) - min(nums2)|` 。
其中，`max(nums1)` 表示数组 `nums1` 中的最大元素，`min(nums2)` 表示数组 `nums2` 中的最小元素。
返回表示分区值的整数。

示例 1：
输入：nums = [1,3,2,4] 输出：1 解释：可以将数组 nums 分成 nums1 = [1,2] 和 nums2 = [3,4] 。 - 数组 nums1 的最大值等于 2 。 - 数组 nums2 的最小值等于 3 。 分区值等于 |2 - 3| = 1 。 可以证明 1 是所有分区方案的最小值。
示例 2：
输入：nums = [100,1,10] 输出：9 解释：可以将数组 nums 分成 nums1 = [10] 和 nums2 = [100,1] 。  - 数组 nums1 的最大值等于 10 。  - 数组 nums2 的最小值等于 1 。  分区值等于 |10 - 1| = 9 。  可以证明 9 是所有分区方案的最小值。

提示：
`2 <= nums.length <= 10^5`
`1 <= nums[i] <= 10^9`
"""

from typing import List, Optional


class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums.sort()
        ans = float('inf')
        for i in range(1, len(nums)):
            ans = min(ans, nums[i] - nums[i - 1])
        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Sorting
#
# 解题思路:
# 排序后，最优分区一定是在某对相邻元素之间切开：nums1 包含排序后前一段，nums2 包含后一段。
# 分区值 = |max(nums1) - min(nums2)| = |nums[i] - nums[i-1]|，即某对相邻元素的差值。
# 遍历排序数组的所有相邻差值，取最小值即为答案。
#
# 时间复杂度: O(n log n)
# 空间复杂度: O(1) 或 O(n) 取决于排序是否原地
#
# 关键点:
# - 排序后最优分区必然在相邻元素之间切开
# - 不可能跨越元素产生更小的 max-min 差值
# - 如果 max(nums1) 和 min(nums2) 之间还有其他元素，分区值只会更大
