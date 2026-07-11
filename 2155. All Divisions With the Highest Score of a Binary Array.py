"""
LeetCode #2155 - All Divisions With the Highest Score of a Binary Array
分组得分最高的所有下标
https://leetcode.cn/problems/all-divisions-with-the-highest-score-of-a-binary-array/

给你一个下标从 0 开始的二进制数组 `nums` ，数组长度为 `n` 。`nums` 可以按下标 `i`（ `0 <= i <= n` ）拆分成两个数组（可能为空）：`nums_left` 和 `nums_right` 。
`nums_left` 包含 `nums` 中从下标 `0` 到 `i - 1` 的所有元素（包括 `0` 和 `i - 1` ），而 `nums_right` 包含 `nums` 中从下标 `i` 到 `n - 1` 的所有元素（包括 `i` 和 `n - 1` ）。
如果 `i == 0` ，`nums_left` 为 空 ，而 `nums_right` 将包含 `nums` 中的所有元素。
如果 `i == n` ，`nums_left` 将包含 `nums` 中的所有元素，而 `nums_right` 为 空 。
下标 `i` 的 分组得分 为 `nums_left` 中 `0` 的个数和 `nums_right` 中 `1` 的个数之 和 。
返回 分组得分 最高 的 所有不同下标 。你可以按 任意顺序 返回答案。

示例 1：
输入：nums = [0,0,1,0] 输出：[2,4] 解释：按下标分组 - 0 ：nums_left 为 [] 。nums_right 为 [0,0,1,0] 。得分为 0 + 1 = 1 。 - 1 ：nums_left 为 [0] 。nums_right 为 [0,1,0] 。得分为 1 + 1 = 2 。 - 2 ：nums_left 为 [0,0] 。nums_right 为 [1,0] 。得分为 2 + 1 = 3 。 - 3 ：nums_left 为 [0,0,1] 。nums_right 为 [0] 。得分为 2 + 0 = 2 。 - 4 ：nums_left 为 [0,0,1,0] 。nums_right 为 [] 。得分为 3 + 0 = 3 。 下标 2 和 4 都可以得到最高的分组得分 3 。 注意，答案 [4,2] 也被视为正确答案。
示例 2：
输入：nums = [0,0,0] 输出：[3] 解释：按下标分组 - 0 ：nums_left 为 [] 。nums_right 为 [0,0,0] 。得分为 0 + 0 = 0 。 - 1 ：nums_left 为 [0] 。nums_right 为 [0,0] 。得分为 1 + 0 = 1 。 - 2 ：nums_left 为 [0,0] 。nums_right 为 [0] 。得分为 2 + 0 = 2 。 - 3 ：nums_left 为 [0,0,0] 。nums_right 为 [] 。得分为 3 + 0 = 3 。 只有下标 3 可以得到最高的分组得分 3 。
示例 3：
输入：nums = [1,1] 输出：[0] 解释：按下标分组 - 0 ：nums_left 为 [] 。nums_right 为 [1,1] 。得分为 0 + 2 = 2 。 - 1 ：nums_left 为 [1] 。nums_right 为 [1] 。得分为 0 + 1 = 1 。 - 2 ：nums_left 为 [1,1] 。nums_right 为 [] 。得分为 0 + 0 = 0 。 只有下标 0 可以得到最高的分组得分 2 。

提示：
`n == nums.length`
`1 <= n <= 10^5`
`nums[i]` 为 `0` 或 `1`
"""

from typing import List, Optional


class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        n = len(nums)
        total_ones = sum(nums)

        max_score = 0
        result = []

        left_zeros = 0
        right_ones = total_ones

        for i in range(n + 1):
            score = left_zeros + right_ones
            if score > max_score:
                max_score = score
                result = [i]
            elif score == max_score:
                result.append(i)

            if i < n:
                if nums[i] == 0:
                    left_zeros += 1
                else:
                    right_ones -= 1

        return result



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array
#
# 解题思路:
# 遍历所有可能的分割点 i（从 0 到 n，共 n+1 个可能下标）。维护两个变量：
#   left_zeros：左侧子数组 nums[0..i-1] 中 0 的个数
#   right_ones：右侧子数组 nums[i..n-1] 中 1 的个数
# 初始时 left_zeros = 0，right_ones = total_ones（total_ones 为整个数组中 1 的总数）。
# 对于每个 i，计算得分 score = left_zeros + right_ones，更新最大得分并记录对应的下标。
# 然后根据 nums[i] 更新左右计数：
#   - 如果 nums[i] == 0，它即将从右侧移动到左侧，left_zeros++
#   - 如果 nums[i] == 1，它即将从右侧移动到左侧，right_ones--
# 这样一次线性扫描即可完成所有分割点的得分计算。
#
# 时间复杂度: O(N)，一次遍历即可。
# 空间复杂度: O(1)，不计输出结果数组的额外空间。
#
# 关键点:
# - 动态维护 left_zeros 和 right_ones，避免每个分割点都重新计算
# - 分割点 i 表示 nums[0..i-1] 在左侧，nums[i..n-1] 在右侧
