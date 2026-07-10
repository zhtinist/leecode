"""
LeetCode #259 - 3Sum Smaller
中文题名：较小的三数之和
https://leetcode.com/problems/3sum-smaller/

Given an array of *n* integers *nums* and a *target*, find the number of index
triplets `i, j, k` with `0 <= i < j < k < n` that satisfy
the condition `nums[i] + nums[j] + nums[k] < target`.

Example:

Input: *nums* = `[-2,0,1,3]`, and *target* = 2
Output: 2
Explanation: Because there are two triplets which sums are less than 2:
[-2,0,1]
[-2,0,3]

Follow up:
Could you solve it in *O*(*n*^2) runtime?

【中文翻译】
给定一个长度为 *n* 的整数数组 *nums* 和一个 *target*，找出满足 `0 <= i < j < k < n` 且 `nums[i] + nums[j] + nums[k] < target` 的下标三元组 `i, j, k` 的个数。

示例：

输入：*nums* = `[-2,0,1,3]`，且 *target* = 2
输出：2
解释：因为有两个三元组的和小于 2：
[-2,0,1]
[-2,0,3]

进阶：
你能否在 *O*(*n*^2) 时间复杂度内解决此题？
"""

from typing import List, Optional


class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        count = 0
        n = len(nums)

        for i in range(n - 2):
            left, right = i + 1, n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < target:
                    # 如果 nums[i] + nums[left] + nums[right] < target，
                    # 那么对于固定的 i 和 left，right 从 left+1 到 right 都满足
                    # 即 (right - left) 个组合都满足条件
                    count += (right - left)
                    left += 1
                else:
                    right -= 1

        return count


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: Yes
#
# 解题思路：
# 先排序，然后固定第一个数 i，使用双指针 left 和 right 在 i 右侧查找。
# 如果 nums[i] + nums[left] + nums[right] < target，则对于当前 i 和 left，
# left+1 到 right 之间的所有组合都满足条件（共 right-left 个），直接将
# right-left 加入计数，然后 left++。否则 right--。不需要去重，因为统计的是
# 不同的索引三元组。
#
# 时间复杂度: O(n^2) — 外层 O(n)，内层双指针 O(n)
# 空间复杂度: O(1) — 排序一般 O(log n) 递归栈
#
# 关键点：
# - 排序后双指针
# - total < target 时，right-left 个组合全部满足
# - 统计的是不同索引组合，不是不同值组合
