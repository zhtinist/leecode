"""
LeetCode #1696 - Jump Game VI
中文题名：跳跃游戏 VI
https://leetcode.com/problems/jump-game-vi/

You are given a 0-indexed integer array `nums` and an
integer `k`.

You are initially standing at index `0`. In one move, you can jump at most
`k` steps forward without going outside the boundaries of the array. That
is, you can jump from index `i` to any index in the range `[i + 1,
min(n - 1, i + k)]` inclusive.

You want to reach the last index of the array (index `n - 1`). Your
score is the sum of all `nums[j]` for
each index `j` you visited in the array.

Return the maximum score you can get.

Example 1:

Input: nums = [1,-1,-2,4,-7,3], k = 2
Output: 7
Explanation: You can choose your jumps forming the subsequence [1,-1,4,3] (underlined above). The sum is 7.

Example 2:

Input: nums = [10,-5,-2,4,0,3], k = 3
Output: 17
Explanation: You can choose your jumps forming the subsequence [10,4,3] (underlined above). The sum is 17.

Example 3:

Input: nums = [1,-5,-20,4,-1,3,-6,-3], k = 2
Output: 0

Constraints:

`1 <= nums.length, k <= 105`

`-104 <= nums[i] <= 104`

【中文翻译】
给定一个下标从 0 开始的整数数组 `nums` 和一个整数 `k`。

你初始站在下标 `0` 处。一次移动中，你最多可以向前跳 `k` 步，且不能跳出数组边界。
即，你可以从下标 `i` 跳到范围 `[i+1, min(n-1, i+k)]` 内的任意下标。

你希望到达数组的最后一个下标（`n-1`）。你的得分是你在数组中访问过的所有 `nums[j]` 之和。

返回你能获得的最大得分。

示例 1：

输入: nums = [1,-1,-2,4,-7,3], k = 2
输出: 7
解释: 你可以选择跳跃路径 [1,-1,4,3]，和为 7

示例 2：

输入: nums = [10,-5,-2,4,0,3], k = 3
输出: 17
解释: 你可以选择跳跃路径 [10,4,3]，和为 17

示例 3：

输入: nums = [1,-5,-20,4,-1,3,-6,-3], k = 2
输出: 0

约束条件：

`1 <= nums.length, k <= 10^5`
`-10^4 <= nums[i] <= 10^4`
"""

from typing import List, Optional
from collections import deque


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        """
        DP + 单调队列优化：
        dp[i] = 到达下标 i 的最大得分
        dp[i] = nums[i] + max(dp[j]) for j in [i-k, i-1]

        使用单调递减双端队列维护滑动窗口 [i-k, i-1] 内的最大 dp 值。
        队首始终是窗口内的最大值。
        """
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        dq = deque([0])  # 存储下标，队首 dp 值最大

        for i in range(1, n):
            # 移除超出窗口 [i-k, i-1] 的元素
            while dq and dq[0] < i - k:
                dq.popleft()

            # dp[i] = nums[i] + 窗口内最大 dp 值
            dp[i] = nums[i] + dp[dq[0]]

            # 维护单调递减队列：移除队尾所有 <= 当前 dp[i] 的元素
            while dq and dp[dq[-1]] <= dp[i]:
                dq.pop()
            dq.append(i)

        return dp[-1]










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 定义 dp[i] = 从下标 0 跳到下标 i 能获得的最大得分。
# 转移方程: dp[i] = nums[i] + max(dp[j])，其中 j ∈ [i-k, i-1]。
# 即当前格的得分必须加上之前 k 步内能跳到的最大得分。
#
# 朴素做法是 O(n*k) 会超时。使用单调递减双端队列（monotonic deque）优化：
# - 队列存储下标，队首 dp 值最大，队列内 dp 值递减
# - 每次计算 dp[i] 前，移除队首所有过期的下标（< i - k）
# - dp[i] = nums[i] + dp[队首]
# - 将 i 入队前，移除队尾所有 dp 值 <= dp[i] 的下标（它们永远不会成为最大值）
#
# 时间复杂度: O(n)，每个元素入队出队各一次
# 空间复杂度: O(n)，dp 数组和队列
#
# 关键点:
# - 滑动窗口最值问题用单调队列优化，从 O(k) 降到 O(1)
# - 队列维护的是 dp 值的单调递减顺序，而非 nums 值
# - 队首过期条件：d[0] < i - k（严格小于窗口左边界）
