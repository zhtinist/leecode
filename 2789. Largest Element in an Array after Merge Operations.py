"""
LeetCode #2789 - Largest Element in an Array after Merge Operations
合并后数组中的最大元素
https://leetcode.cn/problems/largest-element-in-an-array-after-merge-operations/

给你一个下标从 0 开始、由正整数组成的数组 `nums` 。
你可以在数组上执行下述操作 任意 次：
选中一个同时满足 `0 <= i < nums.length - 1` 和 `nums[i] <= nums[i + 1]` 的下标 `i` 。将元素 `nums[i + 1]` 替换为 `nums[i] + nums[i + 1]` ，并从数组中删除元素 `nums[i]` 。
返回你可以从最终数组中获得的 最大 元素的值。

示例 1：
输入：nums = [2,3,7,9,3] 输出：21 解释：我们可以在数组上执行下述操作： - 选中 i = 0 ，得到数组 nums = [5,7,9,3] 。 - 选中 i = 1 ，得到数组 nums = [5,16,3] 。 - 选中 i = 0 ，得到数组 nums = [21,3] 。 最终数组中的最大元素是 21 。可以证明我们无法获得更大的元素。
示例 2：
输入：nums = [5,3,3] 输出：11 解释：我们可以在数组上执行下述操作： - 选中 i = 1 ，得到数组 nums = [5,6] 。 - 选中 i = 0 ，得到数组 nums = [11] 。 最终数组中只有一个元素，即 11 。

提示：
`1 <= nums.length <= 10^5`
`1 <= nums[i] <= 10^6`
"""

from typing import List, Optional


class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        ans = 0
        cur = 0
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] <= cur:
                cur += nums[i]
            else:
                cur = nums[i]
            ans = max(ans, cur)
        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Array
#
# 解题思路:
# 操作条件是 nums[i] <= nums[i+1]，将 nums[i] 合并到 nums[i+1] 中（求和并删除小的）。
# 从右向左贪心：维护 cur 表示当前累积的最大值。如果 nums[i] <= cur，可以将 nums[i] 合并进来，cur += nums[i]。
# 如果 nums[i] > cur，则无法合并（因为 nums[i] > nums[i+1] 即 cur），此时重置 cur = nums[i]。
# 其实从右往左遍历，能合并就合并，不能就重新开始。记录过程中最大 cur。
#
# 时间复杂度: O(n)
# 空间复杂度: O(1)
#
# 关键点:
# - 反向思维：从右往左遍历，因为合并方向是 nums[i] 并入 nums[i+1]
# - 如果 nums[i] <= cur（右侧累积值），则可以合并
# - 如果 nums[i] > cur 则无法合并，以 nums[i] 为新的起点
