"""
LeetCode #3282 - Reach End of Array With Max Score
到达数组末尾的最大得分
https://leetcode.cn/problems/reach-end-of-array-with-max-score/

给你一个长度为 `n` 的整数数组 `nums` 。
你的目标是从下标 `0` 出发，到达下标 `n - 1` 处。每次你只能移动到 更大 的下标处。
从下标 `i` 跳到下标 `j` 的得分为 `(j - i) * nums[i]` 。
请你返回你到达最后一个下标处能得到的 最大总得分 。

示例 1：

输入：nums = [1,3,1,5]
输出：7
解释：
一开始跳到下标 1 处，然后跳到最后一个下标处。总得分为 `1 * 1 + 2 * 3 = 7` 。
示例 2：

输入：nums = [4,3,1,3,2]
输出：16
解释：
直接跳到最后一个下标处。总得分为 `4 * 4 = 16` 。

提示：
`1 <= nums.length <= 10^5`
`1 <= nums[i] <= 10^5`
"""

from typing import List, Optional


class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        max_val = 0
        for i in range(n - 1):
            max_val = max(max_val, nums[i])
            ans += max_val
        return ans










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Array
#
# 解题思路:
# 贪心策略：每次跳跃尽可能利用当前遇到的最大值。
# 从位置 i 跳到 j 的得分 = (j - i) * nums[i]。
# 对于每一步，如果 nums[i] 不是当前遇到的最大值，那么应该早跳到最大值的位置。
# 维护当前遇到的最大值 max_val，每步加上 max_val（相当于用最大值做跳跃）。
# 等价于：在 [0, n-1) 中逐位累加前缀最大值。
# 因为可以用最大 nums[i] 跳多步（每次跳 1 步），每步都得 max_val 分。
#
# 时间复杂度: O(n)
# 空间复杂度: O(1)
#
# 关键点:
# - 贪心：每次用当前看到的最大值做跳跃
# - 答案 = sum(prefix_max[0..n-2])
