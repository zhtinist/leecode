"""
LeetCode #503 - Next Greater Element II
中文题名：下一个更大元素 II
https://leetcode.com/problems/next-greater-element-ii/

Given a circular array (the next element of the last element is the first element of the
array), print the Next Greater Number for every element. The Next Greater Number of a number
x is the first greater number to its traversing-order next in the array, which means you
could search circularly to find its next greater number. If it doesn't exist, output -1 for
this number.

Example 1:

Input: [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2;
The number 2 can't find next greater number;

The second 1's next greater number needs to search circularly, which is also 2.

Note:
The length of given array won't exceed 10000.

【中文翻译】
给定一个循环数组（最后一个元素的下一个元素是数组的第一个元素），输出每个元素的
下一个更大元素。数字 x 的下一个更大元素是按遍历顺序在数组中找到的第一个比 x 大的数，
这意味着可以循环搜索。如果不存在，则对该位置输出 -1。

示例 1：
    输入：[1,2,1]
    输出：[2,-1,2]
    解释：第一个 1 的下一个更大数是 2；
    第二个数 2 找不到下一个更大数，输出 -1；
    第三个 1 需要循环搜索，下一个更大数也是 2。

注意：
    给定数组的长度不超过 10000。
"""

from typing import List, Optional


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [-1] * n
        stack = []  # 单调递减栈，存索引

        # 遍历两倍长度模拟循环数组
        for i in range(2 * n):
            idx = i % n
            while stack and nums[stack[-1]] < nums[idx]:
                prev_idx = stack.pop()
                result[prev_idx] = nums[idx]
            # 只在第一轮将索引入栈，避免重复处理
            if i < n:
                stack.append(idx)

        return result


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用单调递减栈处理循环数组。遍历 2 倍数组长度（模拟循环），用 i % n 取实际索引。
# 维护一个存索引的递减栈：当栈顶元素值 < 当前元素值时，说明当前元素是栈顶元素的下一个更大元素，
# 弹出栈顶并记录结果。只在第一轮遍历（i < n）时将索引入栈，第二轮只用来找更大元素但不再入栈。
# 最终栈中剩余元素没有更大元素，结果保持 -1。
#
# 时间复杂度: O(N) — 每个元素最多入栈一次、出栈一次，遍历 2N 次
# 空间复杂度: O(N) — 单调栈和结果数组
#
# 关键点:
# - 遍历 2N 次模拟循环数组效果
# - 单调递减栈：栈中元素值严格递减，遇到更大值就弹出
# - 只在第一轮入栈，避免栈中元素被重复加入
# - 结果默认值为 -1，处理不了的保持不变
