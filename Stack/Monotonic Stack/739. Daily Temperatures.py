"""
LeetCode #739 - Daily Temperatures
中文题名：每日温度
https://leetcode.com/problems/daily-temperatures/

Given a list of daily temperatures `T`, return a list such that, for each day in
the input, tells you how many days you would have to wait until a warmer temperature. If
there is no future day for which this is possible, put `0` instead.

For example, given the list of temperatures `T = [73, 74, 75, 71, 69, 72, 76,
73]`, your output should be `[1, 1, 4, 2, 1, 1, 0, 0]`.

Note:
The length of `temperatures` will be in the range `[1, 30000]`.
Each temperature will be an integer in the range `[30, 100]`.

【中文翻译】
请根据每日气温列表，重新生成一个列表。对应位置的输出为：要想观测到更高的气温，至少需要等待的天数。如果气温在这之后都不会升高，请在该位置用 0 来代替。

例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。

注意：
temperatures 的长度范围是 [1, 30000]。
每个温度的值都是 [30, 100] 范围内的整数。
"""

from typing import List, Optional


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack = []
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_idx = stack.pop()
                result[prev_idx] = i - prev_idx
            stack.append(i)
        return result










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 单调递减栈（Monotonic Stack）：
# 1. 初始化结果数组全为 0，用一个栈存储索引（栈内对应温度递减）。
# 2. 遍历每一天的温度：
#    - 当栈非空且当前温度 > 栈顶索引对应的温度时，说明找到了更高温度。
#      弹出栈顶，计算等待天数 = 当前索引 - 弹出索引。
#    - 将当前索引入栈。
# 3. 未弹出的索引默认结果为 0（没有更高温度）。
# 单调栈核心：栈内存着"尚未找到更高温度"的日期索引，
# 一旦当前温度更高，就能一次性为栈中多个日期确定答案。
#
# 时间复杂度: O(n)，每个元素最多入栈和出栈一次
# 空间复杂度: O(n)，栈在最坏情况下存储所有索引
#
# 关键点:
# - 单调递减栈（温度严格递减）
# - 每个索引入栈一次出栈一次，O(n)
# - 结果默认为 0，未弹出的即找不到更暖和的温度
# - 典型的"Next Greater Element"问题变体
