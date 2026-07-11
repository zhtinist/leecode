"""
LeetCode #494 - Target Sum
中文题名：目标和
https://leetcode.com/problems/target-sum/

You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you
have 2 symbols `+` and `-`. For each integer, you should choose one
from `+` and `-` as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:

Input: nums is [1, 1, 1, 1, 1], S is 3.
Output: 5
Explanation:

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.

Note:

The length of the given array is positive and will not exceed 20.

The sum of elements in the given array will not exceed 1000.

Your output answer is guaranteed to be fitted in a 32-bit integer.

【中文翻译】
给定一个非负整数数组 a1, a2, ..., an 和一个目标数 S。现在你有两个符号 + 和 -。
对于数组中的任意一个整数，你都可以从 + 或 - 中选择一个符号添加在前面。

返回可以使最终数组和为目标数 S 的所有添加符号的方法数。

示例 1：

输入：nums = [1, 1, 1, 1, 1], S = 3
输出：5
解释：

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

一共有 5 种方法让最终目标和为 3。

注意：

给定数组的长度为正且不会超过 20。

数组元素的总和不会超过 1000。

返回的答案保证可以存入 32 位有符号整数。
"""

from typing import List, Optional


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if abs(target) > total or (total + target) % 2 != 0:
            return 0
        subset_sum = (total + target) // 2
        dp = [0] * (subset_sum + 1)
        dp[0] = 1
        for num in nums:
            for i in range(subset_sum, num - 1, -1):
                dp[i] += dp[i - num]
        return dp[subset_sum]




# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 转化为 0-1 背包子集和问题。
# 设选择 + 的元素和为 P，选择 - 的元素和为 N。
# 则有：P - N = target
# 又：P + N = total（所有元素之和）
# 二式相加：2P = total + target，即 P = (total + target) / 2。
# 问题转化为：从数组中选若干元素使其和等于 P 的方案数。
# 1. 若 total + target 为奇数或 |target| > total，返回 0。
# 2. dp[i] 表示和为 i 的子集方案数，dp[0] = 1。
# 3. 对每个 num，逆序遍历求方案数（0-1 背包）。
# 4. 返回 dp[subset_sum]。
#
# 时间复杂度: O(n * subset_sum)，n 为数组长度
# 空间复杂度: O(subset_sum)
#
# 关键点:
# - 数学转化：将正负号问题转化为子集和问题
# - P = (total + target) / 2 是关键推导
# - 需要检查 target + total 是否为偶数且 target <= total
# - 0-1 背包方案数问题，逆序更新
