"""
LeetCode #2597 - The Number of Beautiful Subsets
美丽子集的数目
https://leetcode.cn/problems/the-number-of-beautiful-subsets/

给你一个由正整数组成的数组 `nums` 和一个 正 整数 `k` 。
如果 `nums` 的子集中，任意两个整数的绝对差均不等于 `k` ，则认为该子数组是一个 美丽 子集。
返回数组 `nums` 中 非空 且 美丽 的子集数目。
`nums` 的子集定义为：可以经由 `nums` 删除某些元素（也可能不删除）得到的一个数组。只有在删除元素时选择的索引不同的情况下，两个子集才会被视作是不同的子集。

示例 1：
输入：nums = [2,4,6], k = 2 输出：4 解释：数组 nums 中的美丽子集有：[2], [4], [6], [2, 6] 。 可以证明数组 [2,4,6] 中只存在 4 个美丽子集。
示例 2：
输入：nums = [1], k = 1 输出：1 解释：数组 nums 中的美丽数组有：[1] 。 可以证明数组 [1] 中只存在 1 个美丽子集。

提示：
`1 <= nums.length <= 18`
`1 <= nums[i], k <= 1000`
"""

from typing import List, Optional


class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        def backtrack(idx: int, count: dict) -> int:
            if idx == len(nums):
                return 1 if any(v > 0 for v in count.values()) else 0

            # skip current number
            total = backtrack(idx + 1, count)

            # take current number if no conflict
            x = nums[idx]
            if count.get(x - k, 0) == 0 and count.get(x + k, 0) == 0:
                count[x] = count.get(x, 0) + 1
                total += backtrack(idx + 1, count)
                count[x] -= 1

            return total

        nums.sort()
        return backtrack(0, {})



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Hash Table, Math, Dynamic Programming, Backtracking, Combinatorics, Sorting
#
# 解题思路:
# 使用回溯法枚举所有子集。先将数组排序，对每个元素可以选择跳过或加入子集。
# 加入子集时检查该元素与已选元素是否有绝对差为k的冲突（只需检查x-k和x+k），无冲突则递归。
# 最后统计所有非空且满足条件的子集数量。
#
# 时间复杂度: O(2^n)
# 空间复杂度: O(n)
#
# 关键点:
# - 回溯时用哈希表记录已选元素的频率，方便O(1)检查冲突
# - 只需要检查x-k和x+k两个值，因为相邻元素差值为k时才冲突
# - 排序后回溯不影响结果，但有助于提前剪枝
