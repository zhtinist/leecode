"""
LeetCode #416 - Partition Equal Subset Sum
中文题名：分割等和子集
https://leetcode.com/problems/partition-equal-subset-sum/

Given a non-empty array containing only positive integers, find if the array
can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:

Each of the array element will not exceed 100.

The array size will not exceed 200.

Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.

【中文翻译】
给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

注意：

每个数组中的元素不会超过 100。

数组的大小不会超过 200。

示例 1：

输入：[1, 5, 11, 5]

输出：true

解释：数组可以分割成 [1, 5, 5] 和 [11]。

示例 2：

输入：[1, 2, 3, 5]

输出：false

解释：数组不能分割成两个元素和相等的子集。
"""

from typing import List, Optional


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True
        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]
        return dp[target]










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 转化为 0-1 背包问题：判断能否从数组中选出若干元素，使得其和等于总和的一半。
# 1. 计算数组总和 total，若为奇数则直接返回 False（无法平分）。
# 2. 目标值 target = total // 2。
# 3. dp[i] 表示能否选出若干元素使其和为 i。
# 4. 初始化 dp[0] = True，其余为 False。
# 5. 对每个数字 num，逆序遍历 target 到 num：
#    dp[i] = dp[i] or dp[i - num]（选或不选当前数字）
# 6. 最终返回 dp[target]。
# 逆序遍历是为了 0-1 背包（每个元素只能用一次），正序会变成完全背包。
#
# 时间复杂度: O(n * target)，n 为数组长度，target 为总和的一半
# 空间复杂度: O(target)
#
# 关键点:
# - 转化为 0-1 背包子集和问题
# - 总和为奇数时直接返回 False
# - 逆序遍历金额确保每元素只使用一次
# - 可以使用 bitset 优化（Python 中可使用位运算或 int 的位表示）
