"""
LeetCode #1673 - Find the Most Competitive Subsequence
中文题名：找出最具竞争力的子序列
https://leetcode.com/problems/find-the-most-competitive-subsequence/

Given an integer array `nums` and a positive integer `k`,
return the most competitive subsequence of `nums`
of size `k`.

An array's subsequence is a resulting sequence obtained by erasing some (possibly
zero) elements from the array.

We define that a subsequence `a` is more competitive than
a subsequence `b` (of the same length) if in the first position where
`a` and `b` differ, subsequence `a` has a number
less than the corresponding number in `b`. For example,
`[1,3,4]` is more competitive than `[1,3,5]` because the first
position they differ is at the final number, and `4` is less than
`5`.

Example 1:

Input: nums = [3,5,2,6], k = 2
Output: [2,6]
Explanation: Among the set of every possible subsequence: {[3,5], [3,2], [3,6], [5,2], [5,6], [2,6]}, [2,6] is the most competitive.

Example 2:

Input: nums = [2,4,3,3,5,4,9,6], k = 4
Output: [2,3,3,4]

Constraints:

`1 <= nums.length <= 105`

`0 <= nums[i] <= 109`

`1 <= k <= nums.length`

【中文翻译】
给定一个整数数组nums和一个正整数k，返回长度为k的nums的最具竞争力子序列。

数组的子序列是通过删除数组中一些（可能为零个）元素得到的序列。

我们定义：如果对于两个相同长度的子序列a和b，在a和b第一个不同的位置上，a的对应数字小于b的对应数字，则a比b更具竞争力。例如，[1,3,4]比[1,3,5]更具竞争力，因为它们第一个不同的位置在最后一个数字，而4小于5。

示例1：

输入：nums = [3,5,2,6], k = 2
输出：[2,6]
解释：在所有可能的子序列{[3,5], [3,2], [3,6], [5,2], [5,6], [2,6]}中，[2,6]最具竞争力。

示例2：

输入：nums = [2,4,3,3,5,4,9,6], k = 4
输出：[2,3,3,4]

约束条件：

1 <= nums.length <= 10^5
0 <= nums[i] <= 10^9
1 <= k <= nums.length

"""

from typing import List, Optional


class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = []
        n = len(nums)
        for i, num in enumerate(nums):
            # 当栈非空、栈顶元素大于当前元素、且剩余元素足够填满k个位置时，弹出栈顶
            while stack and stack[-1] > num and len(stack) - 1 + (n - i) >= k:
                stack.pop()
            if len(stack) < k:
                stack.append(num)
        return stack










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 单调栈。目标是找到一个长度为k的字典序最小的子序列。
# 遍历数组，使用单调栈维护当前候选子序列：
# - 当栈顶元素大于当前元素且栈中剩余元素加上数组剩余元素仍然足够填满k个位置时（即len(stack)-1 + (n-i) >= k），弹出栈顶
# - 如果栈中元素不足k个，压入当前元素
# 最终栈中就是答案（长度为k的最具竞争力子序列）。
#
# 时间复杂度: O(n)，每个元素最多入栈出栈一次
# 空间复杂度: O(k)，栈的大小
#
# 关键点:
# - 单调栈保持递增顺序
# - 弹栈条件：栈顶大于当前元素且剩余元素足够填满k个位置
# - 与"移掉K位数字"问题类似
