"""
LeetCode #698 - Partition to K Equal Sum Subsets
中文题名：划分为k个相等的子集
https://leetcode.com/problems/partition-to-k-equal-sum-subsets/

Given an array of integers `nums` and a positive integer `k`, find
whether it's possible to divide this array into `k` non-empty subsets whose
sums are all equal.

Example 1:

Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: True
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.

Note:

`1 <= k <= len(nums) <= 16`.

`0 < nums[i] < 10000`.

【中文翻译】
给定一个整数数组 `nums` 和一个正整数 `k`，判断是否可以将这个数组划分为 `k` 个非空子集，使得它们的和都相等。

示例 1：

输入: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
输出: True
解释: 可以将其划分为 4 个子集 (5), (1, 4), (2,3), (2,3)，和相等。

注意：

`1 <= k <= len(nums) <= 16`。

`0 < nums[i] < 10000`。
"""

from typing import List, Optional


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        target = total // k
        nums.sort(reverse=True)
        if nums[0] > target:
            return False

        n = len(nums)
        used = [False] * n

        def backtrack(start: int, remain: int, count: int) -> bool:
            if count == k - 1:
                return True
            if remain == 0:
                return backtrack(0, target, count + 1)
            for i in range(start, n):
                if used[i] or remain < nums[i]:
                    continue
                used[i] = True
                if backtrack(i + 1, remain - nums[i], count):
                    return True
                used[i] = False
                if remain == target or remain == nums[i]:
                    return False
                while i + 1 < n and nums[i + 1] == nums[i]:
                    i += 1
            return False

        return backtrack(0, target, 0)









# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 这是一个回溯 + 剪枝问题。
# 1. 计算总和 sum(nums)，如果不能被 k 整除，返回 False。target = sum / k。
# 2. 将数组降序排序（大数优先尝试，减少搜索空间）。
# 3. 使用 used 数组标记已使用的元素。
# 4. 回溯函数 backtrack(start, remain, count)：
#    - count: 已完成多少个子集
#    - remain: 当前子集还需要多少
#    - 从 start 开始尝试添加元素
#    - 剪枝1: 如果 remain == target 且当前元素无法放入，跳过（该元素必须出现在某个子集中）
#    - 剪枝2: 如果 remain == nums[i] 且失败，跳过（放这个元素刚好填满，如果失败则这个数字无法被利用）
#    - 剪枝3: 跳过重复元素
#
# 时间复杂度: O(k * 2^n) 最坏，但剪枝极大减少实际运行时间
# 空间复杂度: O(n) - used 数组和递归栈
#
# 关键点:
# - 降序排序减少搜索分支
# - 多重剪枝条件（跳过重复、remain == target、remain == nums[i]）
# - 回溯的 used 数组标记
