"""
LeetCode #3644 - Maximum K to Sort a Permutation
排序排列
https://leetcode.cn/problems/maximum-k-to-sort-a-permutation/

给你一个长度为 `n` 的整数数组 `nums`，其中 `nums` 是范围 `[0..n - 1]` 内所有数字的一个 排列 。
你可以在满足条件 `nums[i] AND nums[j] == k` 的情况下交换下标 `i` 和 `j` 的元素，其中 `AND` 表示按位与操作，`k` 是一个非负整数。
返回可以使数组按 非递减 顺序排序的最大值 `k`（允许进行任意次这样的交换）。如果 `nums` 已经是有序的，返回 0。
排列 是数组所有元素的一种重新排列。

示例 1：

输入：nums = [0,3,2,1]
输出：1
解释：
选择 `k = 1`。交换 `nums[1] = 3` 和 `nums[3] = 1`，因为 `nums[1] AND nums[3] == 1`，从而得到一个排序后的排列：`[0, 1, 2, 3]`。
示例 2：

输入：nums = [0,1,3,2]
输出：2
解释：
选择 `k = 2`。交换 `nums[2] = 3` 和 `nums[3] = 2`，因为 `nums[2] AND nums[3] == 2`，从而得到一个排序后的排列：`[0, 1, 2, 3]`。
示例 3：

输入：nums = [3,2,1,0]
输出：0
解释：
只有当 `k = 0` 时，才能进行排序，因为没有更大的 `k` 能够满足 `nums[i] AND nums[j] == k` 的交换条件。

提示：
`1 <= n == nums.length <= 10^5`
`0 <= nums[i] <= n - 1`
`nums` 是从 `0` 到 `n - 1` 的一个排列。
"""

from typing import List, Optional


class Solution:
    def maxK(self, nums: List[int]) -> int:
        k = -1  # 全 1 位（-1 在 Python 中所有位均为 1）
        for i, val in enumerate(nums):
            if val != i:
                k &= (i & val)
        return 0 if k == -1 else k










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Bit Manipulation, Array
#
# 解题思路:
# 交换 i 和 j 的条件是 nums[i] & nums[j] == k，这意味着 k 的每一位都必须是
# 两个操作数的子集。对于所有不在正确位置的元素 i（nums[i] != i），值 nums[i]
# 需要被移动到位置 nums[i]。为此 k 必须是所有错位位置上 (i & nums[i]) 的子集。
# 因此 k 的上界就是所有错位 i 的 (i & nums[i]) 的按位与结果。
# 如果数组已经有序，按题目要求返回 0。
#
# 时间复杂度: O(n) — 一次遍历
# 空间复杂度: O(1) — 仅使用常数额外空间
#
# 关键点:
# - 对每个错位位置 i，k 最多只能包含 i 和 nums[i] 共有的位
# - k = AND{ i & nums[i] | nums[i] != i }
# - Python 中 -1 的所有位均为 1，作为 AND 的初始单位元
