"""
LeetCode #2772 - Apply Operations to Make All Array Elements Equal to Zero
使数组中的所有元素都等于零
https://leetcode.cn/problems/apply-operations-to-make-all-array-elements-equal-to-zero/

给你一个下标从 0 开始的整数数组 `nums` 和一个正整数 `k` 。
你可以对数组执行下述操作 任意次 ：
从数组中选出长度为 `k` 的 任一 子数组，并将子数组中每个元素都 减去 `1` 。
如果你可以使数组中的所有元素都等于 `0` ，返回  `true` ；否则，返回 `false` 。
子数组 是数组中的一个非空连续元素序列。

示例 1：
输入：nums = [2,2,3,1,1,0], k = 3 输出：true 解释：可以执行下述操作： - 选出子数组 [2,2,3] ，执行操作后，数组变为 nums = [1,1,2,1,1,0] 。 - 选出子数组 [2,1,1] ，执行操作后，数组变为 nums = [1,1,1,0,0,0] 。 - 选出子数组 [1,1,1] ，执行操作后，数组变为 nums = [0,0,0,0,0,0] 。
示例 2：
输入：nums = [1,3,1,1], k = 2 输出：false 解释：无法使数组中的所有元素等于 0 。

提示：
`1 <= k <= nums.length <= 10^5`
`0 <= nums[i] <= 10^6`
"""

from typing import List, Optional


class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        diff = [0] * (n + 1)
        cur = 0
        for i in range(n):
            cur += diff[i]
            need = nums[i] - cur
            if need < 0:
                return False
            if need > 0:
                if i + k > n:
                    return False
                cur += need
                diff[i + k] -= need
        return True



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Prefix Sum
#
# 解题思路:
# 使用差分数组模拟区间减法操作。从左到右处理每个元素，维护当前累计减去的值 cur。
# 对于 nums[i]，需要再减去 need = nums[i] - cur。
# 如果 need < 0 则已经减过头（不可能），如果 need > 0 则必须以 i 为起点执行 need 次长度为 k 的区间减操作。
# 通过差分数组 diff[i] += need, diff[i+k] -= need 记录操作。
# 若 i + k > n 说明无法完整执行区间操作，返回 False。
#
# 时间复杂度: O(n)
# 空间复杂度: O(n) 差分数组
#
# 关键点:
# - 贪心从左到右处理，每次必须将当前位置减到 0
# - 差分数组高效维护区间操作：diff[l] += val, diff[r+1] -= val
# - 每次操作长度必须为 k，若越界则不可行
