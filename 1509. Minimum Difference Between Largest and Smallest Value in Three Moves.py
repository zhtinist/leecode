"""
LeetCode #1509 - Minimum Difference Between Largest and Smallest Value in Three Moves
中文题名：三次操作后最大值与最小值的最小差
https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/

Given an array `nums`, you are allowed to choose one element of `nums`
and change it by any value in one move.

Return the minimum difference between the largest and smallest value of
`nums` after perfoming at most 3 moves.

Example 1:

Input: nums = [5,3,2,4]
Output: 0
Explanation: Change the array [5,3,2,4] to [2,2,2,2].
The difference between the maximum and minimum is 2-2 = 0.

Example 2:

Input: nums = [1,5,0,10,14]
Output: 1
Explanation: Change the array [1,5,0,10,14] to [1,1,0,1,1].
The difference between the maximum and minimum is 1-0 = 1.

Example 3:

Input: nums = [6,6,0,1,1,4,6]
Output: 2

Example 4:

Input: nums = [1,5,6,14,15]
Output: 1

Constraints:

`1 <= nums.length <= 10^5`

`-10^9 <= nums[i] <= 10^9`

【中文翻译】
给定一个数组 nums，每次操作可以选择一个元素并将其改为任意值。
返回最多进行 3 次操作后，数组最大值与最小值的最小差值。

示例 1：

输入：nums = [5,3,2,4]
输出：0
解释：将数组改为 [2,2,2,2]，最大最小差为 0。

示例 2：

输入：nums = [1,5,0,10,14]
输出：1
解释：将数组改为 [1,1,0,1,1]，最大最小差为 1。

示例 3：

输入：nums = [6,6,0,1,1,4,6]
输出：2

示例 4：

输入：nums = [1,5,6,14,15]
输出：1
"""

from typing import List, Optional


class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 4:
            return 0
        nums.sort()
        # We can change up to 3 elements.
        # Options: remove 0,1,2,3 from left and 3,2,1,0 from right
        return min(
            nums[n - 4] - nums[0],   # change 3 smallest
            nums[n - 3] - nums[1],   # change 2 smallest + 1 largest
            nums[n - 2] - nums[2],   # change 1 smallest + 2 largest
            nums[n - 1] - nums[3],   # change 3 largest
        )



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 最多修改 3 个元素，意味着我们可以"忽略"数组中最多 3 个极端值。
# 排序后，最优策略一定是从最小端去掉 i 个、从最大端去掉 3-i 个（i=0,1,2,3）。
# 答案 = min(nums[n-4+i] - nums[i]) for i in [0,1,2,3]。
# 如果 n<=4，可以修改所有元素使它们相等，答案为 0。
#
# 时间复杂度: O(N log N) — 排序主导
# 空间复杂度: O(1) — 取决于排序是否原地
#
# 关键点:
# - 最多 3 次修改 = 可以去掉最多 3 个极端值
# - 排序后只需考虑 4 种情况
# - n<=4 时答案为 0
