"""
LeetCode #2592 - Maximize Greatness of an Array
最大化数组的伟大值
https://leetcode.cn/problems/maximize-greatness-of-an-array/

给你一个下标从 0 开始的整数数组 `nums` 。你需要将 `nums` 重新排列成一个新的数组 `perm` 。
定义 `nums` 的 伟大值 为满足 `0 <= i < nums.length` 且 `perm[i] > nums[i]` 的下标数目。
请你返回重新排列 `nums` 后的 最大 伟大值。

示例 1：
输入：nums = [1,3,5,2,1,3,1] 输出：4 解释：一个最优安排方案为 perm = [2,5,1,3,3,1,1] 。 在下标为 0, 1, 3 和 4 处，都有 perm[i] > nums[i] 。因此我们返回 4 。
示例 2：
输入：nums = [1,2,3,4] 输出：3 解释：最优排列为 [2,3,4,1] 。 在下标为 0, 1 和 2 处，都有 perm[i] > nums[i] 。因此我们返回 3 。

提示：
`1 <= nums.length <= 10^5`
`0 <= nums[i] <= 10^9`
"""

from typing import List, Optional


class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        for j in range(len(nums)):
            if nums[j] > nums[i]:
                i += 1
        return i



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Array, Two Pointers, Sorting
#
# 解题思路:
# 排序后使用双指针贪心匹配。指针i指向等待匹配的较小元素，指针j遍历数组找较大元素。
# 当nums[j]>nums[i]时成功匹配一对（perm[i]=nums[j]使得perm[i]>nums[i]），i和j都前进；
# 否则仅j前进寻找更大的值。最终i的值即为成功匹配的对数。
#
# 时间复杂度: O(N log N)
# 空间复杂度: O(1)
#
# 关键点:
# - 排序后的大小关系让贪心匹配成为可能
# - i表示已成功匹配的数量，也是下一个需要匹配的较小元素位置
# - 等价于：perm是排序后数组的某个循环移位，尽量用较大元素匹配较小元素
