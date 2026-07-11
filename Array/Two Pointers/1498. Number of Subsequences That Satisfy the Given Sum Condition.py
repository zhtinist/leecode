"""
LeetCode #1498 - Number of Subsequences That Satisfy the Given Sum Condition
中文题名：满足条件的子序列数目
https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/

Given an array of integers `nums` and an integer `target`.

Return the number of non-empty subsequences of `nums` such
that the sum of the minimum and maximum element on it is less or equal than
`target`.

Since the answer may be too large, return it modulo 10^9 + 7.

Example 1:

Input: nums = [3,5,6,7], target = 9
Output: 4
Explanation: There are 4 subsequences that satisfy the condition.
[3] -> Min value + max value <= target (3 + 3 <= 9)
[3,5] -> (3 + 5 <= 9)
[3,5,6] -> (3 + 6 <= 9)
[3,6] -> (3 + 6 <= 9)

Example 2:

Input: nums = [3,3,6,8], target = 10
Output: 6
Explanation: There are 6 subsequences that satisfy the condition. (nums can have repeated numbers).
[3] , [3] , [3,3], [3,6] , [3,6] , [3,3,6]

Example 3:

Input: nums = [2,3,3,4,6,7], target = 12
Output: 61
Explanation: There are 63 non-empty subsequences, two of them don't satisfy the condition ([6,7], [7]).
Number of valid subsequences (63 - 2 = 61).

Example 4:

Input: nums = [5,2,4,1,7,6,8], target = 16
Output: 127
Explanation: All non-empty subset satisfy the condition (2^7 - 1) = 127

Constraints:

`1 <= nums.length <= 10^5`

`1 <= nums[i] <= 10^6`

`1 <= target <= 10^6`

【中文翻译】

给定一个整数数组 `nums` 和一个整数 `target`。

返回 `nums` 中满足最小元素与最大元素之和小于等于 `target` 的非空子序列的数量。

由于答案可能非常大，将其对 10^9 + 7 取模后返回。

示例 1：
输入：nums = [3,5,6,7], target = 9
输出：4
解释：有 4 个子序列满足条件。
[3] -> 最小值 + 最大值 <= target (3 + 3 <= 9)
[3,5] -> (3 + 5 <= 9)
[3,5,6] -> (3 + 6 <= 9)
[3,6] -> (3 + 6 <= 9)

示例 2：
输入：nums = [3,3,6,8], target = 10
输出：6
解释：有 6 个子序列满足条件（nums 可以有重复数字）。
[3]、[3]、[3,3]、[3,6]、[3,6]、[3,3,6]

示例 3：
输入：nums = [2,3,3,4,6,7], target = 12
输出：61
解释：共有 63 个非空子序列，其中两个不满足条件（[6,7]、[7]）。有效子序列数量 (63 - 2 = 61)。

示例 4：
输入：nums = [5,2,4,1,7,6,8], target = 16
输出：127
解释：所有非空子集都满足条件 (2^7 - 1) = 127

约束条件：
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^6
1 <= target <= 10^6

"""

from typing import List, Optional


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10 ** 9 + 7
        nums.sort()
        n = len(nums)

        # Precompute powers of 2
        pow2 = [1] * n
        for i in range(1, n):
            pow2[i] = (pow2[i - 1] * 2) % MOD

        ans = 0
        left, right = 0, n - 1

        while left <= right:
            if nums[left] + nums[right] <= target:
                # For left fixed, any subset of [left+1, right] works
                ans = (ans + pow2[right - left]) % MOD
                left += 1
            else:
                right -= 1

        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 1. 排序数组（子序列问题排序后不影响结果，因为子序列的
#    最小值和最大值由最小和最大元素决定，中间元素任意）。
# 2. 使用双指针：left 指向最小候选元素，right 指向最大候选元素。
# 3. 对于每个 left，找到满足 nums[left] + nums[right] <= target
#    的最大 right。此时，以 nums[left] 为最小值，可以选择
#    [left+1, right] 范围内的任意子集作为中间元素的子序列。
#    - 子集数量 = 2^(right - left)（每个中间元素可选或不选）
# 4. 如果 nums[left] + nums[right] > target，right 左移。
# 5. 预计算 2 的幂次以避免重复计算，结果对 MOD = 10^9+7 取模。
# 6. 排序是关键预处理步骤，使得双指针法适用。
#
# 时间复杂度: O(N log N)
# 空间复杂度: O(N)
#
# 关键点:
# - 排序后子序列的最小值/最大值由选取的最小/最大索引决定
# - 双指针法高效计数满足条件的子序列
# - 预计算 2 的幂次
# - 注意取模操作：每次加法后都取模
# - 对于固定的 min 和 max，中间元素可以任意选择（2^(right-left) 种）










