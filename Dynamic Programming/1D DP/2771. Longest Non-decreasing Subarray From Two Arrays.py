"""
LeetCode #2771 - Longest Non-decreasing Subarray From Two Arrays
构造最长非递减子数组
https://leetcode.cn/problems/longest-non-decreasing-subarray-from-two-arrays/

给你两个下标从 0 开始的整数数组 `nums1` 和 `nums2` ，长度均为 `n` 。
让我们定义另一个下标从 0 开始、长度为 `n` 的整数数组，`nums3` 。对于范围 `[0, n - 1]` 的每个下标 `i` ，你可以将 `nums1[i]` 或 `nums2[i]` 的值赋给 `nums3[i]` 。
你的任务是使用最优策略为 `nums3` 赋值，以最大化 `nums3` 中 最长非递减子数组 的长度。
以整数形式表示并返回 `nums3` 中 最长非递减 子数组的长度。
注意：子数组 是数组中的一个连续非空元素序列。

示例 1：
输入：nums1 = [2,3,1], nums2 = [1,2,1] 输出：2 解释：构造 nums3 的方法之一是：  nums3 = [nums1[0], nums2[1], nums2[2]] => [2,2,1] 从下标 0 开始到下标 1 结束，形成了一个长度为 2 的非递减子数组 [2,2] 。  可以证明 2 是可达到的最大长度。
示例 2：
输入：nums1 = [1,3,2,1], nums2 = [2,2,3,4] 输出：4 解释：构造 nums3 的方法之一是：  nums3 = [nums1[0], nums2[1], nums2[2], nums2[3]] => [1,2,3,4] 整个数组形成了一个长度为 4 的非递减子数组，并且是可达到的最大长度。
示例 3：
输入：nums1 = [1,1], nums2 = [2,2] 输出：2 解释：构造 nums3 的方法之一是：  nums3 = [nums1[0], nums1[1]] => [1,1]  整个数组形成了一个长度为 2 的非递减子数组，并且是可达到的最大长度。

提示：
`1 <= nums1.length == nums2.length == n <= 10^5`
`1 <= nums1[i], nums2[i] <= 10^9`
"""

from typing import List, Optional


class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        dp1 = 1
        dp2 = 1
        ans = 1
        for i in range(1, n):
            ndp1 = ndp2 = 1
            if nums1[i] >= nums1[i - 1]:
                ndp1 = max(ndp1, dp1 + 1)
            if nums1[i] >= nums2[i - 1]:
                ndp1 = max(ndp1, dp2 + 1)
            if nums2[i] >= nums1[i - 1]:
                ndp2 = max(ndp2, dp1 + 1)
            if nums2[i] >= nums2[i - 1]:
                ndp2 = max(ndp2, dp2 + 1)
            dp1, dp2 = ndp1, ndp2
            ans = max(ans, dp1, dp2)
        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Dynamic Programming
#
# 解题思路:
# DP 维护以当前位置结尾、选择 nums1[i] 或 nums2[i] 时的最长非递减子数组长度。
# dp1 表示以 nums1[i] 结尾的最长长度，dp2 表示以 nums2[i] 结尾的最长长度。
# 对于每个位置 i，检查 4 种转移：选 nums1[i] 时从 nums1[i-1] 或 nums2[i-1] 转移，选 nums2[i] 时同理。
# 滚动数组优化空间到 O(1)。
#
# 时间复杂度: O(n)
# 空间复杂度: O(1)
#
# 关键点:
# - 每次有两个选择（nums1[i] 或 nums2[i]），需要维护两个 DP 状态
# - 如果当前值小于前一个值，该转移不可行（重置为 1）
# - 使用滚动变量 dp1/dp2 避免 O(n) 空间
