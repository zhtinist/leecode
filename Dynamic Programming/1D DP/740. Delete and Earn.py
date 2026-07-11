"""
LeetCode #740 - Delete and Earn
中文题名：删除与获得点数
https://leetcode.com/problems/delete-and-earn/

Given an array `nums` of integers, you can perform operations on the array.

In each operation, you pick any `nums[i]` and delete it to earn
`nums[i]` points. After, you must delete every element equal to `nums[i]
- 1` or `nums[i] + 1`.

You start with 0 points. Return the maximum number of points you can earn by applying such
operations.

Example 1:

Input: nums = [3, 4, 2]
Output: 6
Explanation:
Delete 4 to earn 4 points, consequently 3 is also deleted.
Then, delete 2 to earn 2 points. 6 total points are earned.

Example 2:

Input: nums = [2, 2, 3, 3, 3, 4]
Output: 9
Explanation:
Delete 3 to earn 3 points, deleting both 2's and the 4.
Then, delete 3 again to earn 3 points, and 3 again to earn 3 points.
9 total points are earned.

Note:

The length of `nums` is at most `20000`.

Each element `nums[i]` is an integer in the range `[1, 10000]`.

【中文翻译】
给定一个整数数组 nums，你可以对它进行一些操作。

每次操作中，选择任意一个 nums[i]，删除它并获得 nums[i] 的点数。之后，你必须删除每个等于 nums[i] - 1 或 nums[i] + 1 的元素。

开始你拥有 0 个点数。返回你能通过这些操作获得的最大点数。

示例 1：

输入：nums = [3, 4, 2]
输出：6
解释：
删除 4 获得 4 个点数，因此 3 也被删除。
之后，删除 2 获得 2 个点数。总共获得 6 个点数。

示例 2：

输入：nums = [2, 2, 3, 3, 3, 4]
输出：9
解释：
删除 3 获得 3 个点数，同时删除所有的 2 和 4。
之后，再次删除 3 获得 3 个点数，再次删除 3 获得 3 个点数。
总共获得 9 个点数。

注意：

nums 的长度最大为 20000。

每个整数 nums[i] 的大小都在 [1, 10000] 范围内。
"""

from typing import List, Optional


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max_val = max(nums)
        points = [0] * (max_val + 1)
        for num in nums:
            points[num] += num
        # House Robber on points array
        prev, curr = 0, 0
        for p in points:
            prev, curr = curr, max(curr, prev + p)
        return curr



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 将问题转化为"打家劫舍"（House Robber）问题。
# 1. 统计每个数字的总点数：points[num] = num * count(num)
# 2. 问题变成：在 points 数组中，不能同时选取相邻元素（因为 num 和 num+1 互斥），求最大和。
#    这与 LeetCode 198 - House Robber 完全相同。
# 3. 使用 DP：prev 表示 dp[i-2]（前前一个的最优解），curr 表示 dp[i-1]（前一个的最优解）。
#    对于当前点数 p：要么跳过（保持 curr），要么选取（prev + p），取两者较大值。
#
# 时间复杂度: O(N + M) - N 为 nums 长度，M = max(nums) <= 10000
# 空间复杂度: O(M) - points 数组大小
#
# 关键点:
# - 转化为 House Robber：如果你选了 num，就不能选 num-1 和 num+1
# - 先通过计数将 nums 转换为 points 数组
# - DP 状态转移：curr = max(curr, prev + p)，其中 prev 是跳过前一个的结果
# - 由于数据范围限制（max <= 10000），可以使用数组而非哈希表
