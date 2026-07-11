"""
LeetCode #1262 - Greatest Sum Divisible by Three
中文题名：可被三整除的最大和
https://leetcode.com/problems/greatest-sum-divisible-by-three/

Given an array `nums` of integers, we need to find the maximum
possible sum of elements of the array such that it is divisible by three.

Example 1:

Input: nums = [3,6,5,1,8]
Output: 18
Explanation: Pick numbers 3, 6, 1 and 8 their sum is 18 (maximum sum divisible by 3).

Example 2:

Input: nums = [4]
Output: 0
Explanation: Since 4 is not divisible by 3, do not pick any number.

Example 3:

Input: nums = [1,2,3,4,4]
Output: 12
Explanation: Pick numbers 1, 3, 4 and 4 their sum is 12 (maximum sum divisible by 3).

Constraints:

`1 <= nums.length <= 4 * 10^4`

`1 <= nums[i] <= 10^4`

【中文翻译】
给你一个整数数组 `nums`，请你找出并返回能被三整除的元素最大和。

示例 1：

输入：nums = [3,6,5,1,8]
输出：18
解释：选出数字 3、6、1 和 8，它们的和是 18（可被 3 整除的最大和）。

示例 2：

输入：nums = [4]
输出：0
解释：4 不能被 3 整除，所以不选任何数字。

示例 3：

输入：nums = [1,2,3,4,4]
输出：12
解释：选出数字 1、3、4 和 4，它们的和是 12（可被 3 整除的最大和）。

约束条件：

`1 <= nums.length <= 4 * 10^4`

`1 <= nums[i] <= 10^4`
"""

from typing import List, Optional


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        # dp[0] = max sum % 3 == 0
        # dp[1] = max sum % 3 == 1
        # dp[2] = max sum % 3 == 2
        dp = [0, 0, 0]

        for num in nums:
            # Make a copy to use previous state
            prev = dp[:]
            for s in prev:
                new_sum = s + num
                mod = new_sum % 3
                dp[mod] = max(dp[mod], new_sum)

        return dp[0]










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 动态规划（DP）。用 dp[r] 表示当前能得到的最大的、模 3 余 r 的元素和。
# 1. 初始化 dp = [0, 0, 0]，分别表示模 3 余 0、1、2 的最大和（空集的和为 0 且余 0）。
# 2. 遍历每个数字 num，对于当前每个已有的和 s：
#    - 新的和 new_sum = s + num
#    - new_sum 的余数为 mod = new_sum % 3
#    - 更新 dp[mod] = max(dp[mod], new_sum)
# 3. 注意需要用上一轮的状态来计算（复制 prev = dp[:]），避免同一轮中重复使用。
# 4. 遍历结束后，dp[0] 即为答案。
# 另一种解法：贪心。计算所有数的总和 total，
# 如果 total % 3 == 0，返回 total；
# 如果 total % 3 == 1，尝试减去最小的一个余 1 的数，或减去两个最小的余 2 的数；
# 如果 total % 3 == 2，尝试减去最小的一个余 2 的数，或减去两个最小的余 1 的数。
#
# 时间复杂度: O(N)，每个数字只处理一次
# 空间复杂度: O(1)，dp 数组大小固定为 3
#
# 关键点:
# - DP 的核心是维护当前能达到的三种余数状态的最大和
# - 每次迭代需要基于上一轮的状态（用 prev 副本），避免同一个 num 被多次使用
# - dp 初始化为 [0, 0, 0]，空集和为 0（余 0）
# - 也可以使用贪心方法，复杂度同样为 O(N)，但需要跟踪最小的余 1 和余 2 的数
