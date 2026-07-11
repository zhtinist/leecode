"""
LeetCode #2905 - Find Indices With Index and Value Difference II
找出满足差值条件的下标 II
https://leetcode.cn/problems/find-indices-with-index-and-value-difference-ii/

给你一个下标从 0 开始、长度为 `n` 的整数数组 `nums` ，以及整数 `indexDifference` 和整数 `valueDifference` 。
你的任务是从范围 `[0, n - 1]` 内找出  2 个满足下述所有条件的下标 `i` 和 `j` ：
`abs(i - j) >= indexDifference` 且
`abs(nums[i] - nums[j]) >= valueDifference`
返回整数数组 `answer`。如果存在满足题目要求的两个下标，则 `answer = [i, j]` ；否则，`answer = [-1, -1]` 。如果存在多组可供选择的下标对，只需要返回其中任意一组即可。
注意：`i` 和 `j` 可能 相等 。

示例 1：
输入：nums = [5,1,4,1], indexDifference = 2, valueDifference = 4 输出：[0,3] 解释：在示例中，可以选择 i = 0 和 j = 3 。 abs(0 - 3) >= 2 且 abs(nums[0] - nums[3]) >= 4 。 因此，[0,3] 是一个符合题目要求的答案。 [3,0] 也是符合题目要求的答案。
示例 2：
输入：nums = [2,1], indexDifference = 0, valueDifference = 0 输出：[0,0] 解释： 在示例中，可以选择 i = 0 和 j = 0 。  abs(0 - 0) >= 0 且 abs(nums[0] - nums[0]) >= 0 。  因此，[0,0] 是一个符合题目要求的答案。  [0,1]、[1,0] 和 [1,1] 也是符合题目要求的答案。
示例 3：
输入：nums = [1,2,3], indexDifference = 2, valueDifference = 4 输出：[-1,-1] 解释：在示例中，可以证明无法找出 2 个满足所有条件的下标。 因此，返回 [-1,-1] 。

提示：
`1 <= n == nums.length <= 10^5`
`0 <= nums[i] <= 10^9`
`0 <= indexDifference <= 10^5`
`0 <= valueDifference <= 10^9`
"""

from typing import List, Optional


class Solution:
    def findIndices(self, nums: List[int], indexDifference: int,
                    valueDifference: int) -> List[int]:
        n = len(nums)
        if indexDifference == 0 and valueDifference == 0:
            return [0, 0]
        # Maintain min and max in prefix up to j - indexDifference
        min_idx = 0
        max_idx = 0
        for j in range(indexDifference, n):
            i = j - indexDifference
            if nums[i] < nums[min_idx]:
                min_idx = i
            if nums[i] > nums[max_idx]:
                max_idx = i
            if abs(nums[j] - nums[min_idx]) >= valueDifference:
                return [min_idx, j]
            if abs(nums[j] - nums[max_idx]) >= valueDifference:
                return [max_idx, j]
        return [-1, -1]



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Two Pointers
#
# 解题思路:
# 对于每个位置 j（从 indexDifference 开始），维护前缀 [0, j-indexDifference] 范围中的最小值和最大值及其索引。
# 检查 nums[j] 与前缀最小值的差或前缀最大值与 nums[j] 的差是否 >= valueDifference。若是则找到答案。
# 只需一次遍历，O(n) 时间。
#
# 时间复杂度: O(n)
# 空间复杂度: O(1)
#
# 关键点:
# - 滑动前缀窗口，维护最小值和最大值的索引
# - 对于每个 j，用前缀极值与 nums[j] 比较，满足值差要求即返回
# - 不需要检查所有 i < j 的组合，只用极值代表
