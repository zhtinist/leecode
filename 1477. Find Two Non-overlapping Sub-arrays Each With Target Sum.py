"""
LeetCode #1477 - Find Two Non-overlapping Sub-arrays Each With Target Sum
中文题名：找两个和为目标值且不重叠的子数组
https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/

Given an array of integers `arr` and an integer `target`.

You have to find two non-overlapping sub-arrays of `arr`
each with sum equal `target`. There can be multiple answers so you have
to find an answer where the sum of the lengths of the two sub-arrays is minimum.

Return the minimum sum of the lengths of the two required sub-arrays, or
return -1 if you cannot find such two sub-arrays.

Example 1:

Input: arr = [3,2,2,4,3], target = 3
Output: 2
Explanation: Only two sub-arrays have sum = 3 ([3] and [3]). The sum of their lengths is 2.

Example 2:

Input: arr = [7,3,4,7], target = 7
Output: 2
Explanation: Although we have three non-overlapping sub-arrays of sum = 7 ([7], [3,4] and [7]), but we will choose the first and third sub-arrays as the sum of their lengths is 2.

Example 3:

Input: arr = [4,3,2,6,2,3,4], target = 6
Output: -1
Explanation: We have only one sub-array of sum = 6.

Example 4:

Input: arr = [5,5,4,4,5], target = 3
Output: -1
Explanation: We cannot find a sub-array of sum = 3.

Example 5:

Input: arr = [3,1,1,1,5,1,2,1], target = 3
Output: 3
Explanation: Note that sub-arrays [1,2] and [2,1] cannot be an answer because they overlap.

Constraints:

`1 <= arr.length <= 10^5`

`1 <= arr[i] <= 1000`

`1 <= target <= 10^8`

【中文翻译】

给定一个整数数组 `arr` 和一个整数 `target`。

你需要找到 `arr` 中两个不重叠的子数组，每个子数组的和都等于 `target`。可能有多个答案，你需要找到两个子数组长度之和最小的答案。

返回两个所需子数组的最小长度之和，如果找不到这样的两个子数组则返回 -1。

示例 1：
输入：arr = [3,2,2,4,3], target = 3
输出：2
解释：只有两个子数组的和为 3（[3] 和 [3]）。它们的长度之和为 2。

示例 2：
输入：arr = [7,3,4,7], target = 7
输出：2
解释：虽然我们有三个和为 7 的不重叠子数组（[7]、[3,4] 和 [7]），但我们会选择第一个和第三个子数组，因为它们的长度之和为 2。

示例 3：
输入：arr = [4,3,2,6,2,3,4], target = 6
输出：-1
解释：我们只有一个和为 6 的子数组。

示例 4：
输入：arr = [5,5,4,4,5], target = 3
输出：-1
解释：找不到和为 3 的子数组。

示例 5：
输入：arr = [3,1,1,1,5,1,2,1], target = 3
输出：3
解释：注意子数组 [1,2] 和 [2,1] 不能作为答案，因为它们重叠。

约束条件：
1 <= arr.length <= 10^5
1 <= arr[i] <= 1000
1 <= target <= 10^8

"""

from typing import List, Optional


class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        INF = float('inf')
        # dp[i] = min length of valid subarray ending at or before index i
        dp = [INF] * n

        left = 0
        window_sum = 0
        ans = INF

        for right in range(n):
            window_sum += arr[right]

            while window_sum > target:
                window_sum -= arr[left]
                left += 1

            if window_sum == target:
                length = right - left + 1
                # Check if there's a non-overlapping subarray before 'left'
                if left > 0 and dp[left - 1] != INF:
                    ans = min(ans, length + dp[left - 1])
                # Update dp[right] with current subarray
                dp[right] = min(dp[right - 1] if right > 0 else INF, length)
            else:
                dp[right] = dp[right - 1] if right > 0 else INF

        return ans if ans != INF else -1



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 1. 使用滑动窗口找出所有和为 target 的子数组。
# 2. 维护一个 dp 数组，其中 dp[i] 表示在索引 i 及其之前
#    结束的、和为 target 的最小子数组长度。
# 3. 遍历数组，维护窗口 [left, right] 的和 window_sum：
#    - 当 window_sum > target 时，收缩左边界
#    - 当 window_sum == target 时，当前子数组长度为 len = right-left+1
#    - 如果 left > 0 且 dp[left-1] != INF，说明存在一个不重叠的
#      前置子数组，可以更新答案 ans = min(ans, len + dp[left-1])
#    - 更新 dp[right] = min(上一个dp值, 当前长度)
# 4. dp 数组确保我们总是知道在任意位置之前的最短有效子数组长度。
#
# 时间复杂度: O(N)
# 空间复杂度: O(N)
#
# 关键点:
# - 滑动窗口找到所有和为 target 的子数组
# - dp[i] 记录在索引 i 及之前的最短有效子数组长度
# - 不重叠的条件：当前子数组的 start > 前一个子数组的 end
# - 初始化为 INF（无穷大）表示不存在










