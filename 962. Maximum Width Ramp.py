"""
LeetCode #962 - Maximum Width Ramp
中文题名：最大宽度坡
https://leetcode.com/problems/maximum-width-ramp/

Given an array `A` of integers, a ramp is a tuple `(i,
j)` for which `i < j` and `A[i] <= A[j]`.
The width of such a ramp is `j - i`.

Find the maximum width of a ramp in `A`.  If one doesn't exist, return 0.

Example 1:

Input: [6,0,8,2,1,5]
Output: 4
Explanation:
The maximum width ramp is achieved at (i, j) = (1, 5): A[1] = 0 and A[5] = 5.

Example 2:

Input: [9,8,1,0,1,9,4,0,4,1]
Output: 7
Explanation:
The maximum width ramp is achieved at (i, j) = (2, 9): A[2] = 1 and A[9] = 1.

【中文翻译】
给定一个整数数组 `A`，坡是满足 `i < j` 且 `A[i] <= A[j]` 的元组 `(i, j)`。
坡的宽度为 `j - i`。
找出 `A` 中坡的最大宽度，如果不存在则返回 0。

"""

from typing import List, Optional


class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        # 构建单调递减栈，存储候选的左边界索引 i
        stack = []
        for i in range(n):
            if not stack or nums[i] < nums[stack[-1]]:
                stack.append(i)

        max_width = 0
        # 从右向左扫描，寻找每个右边界 j 能匹配的最左 i
        for j in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[j]:
                max_width = max(max_width, j - stack.pop())

        return max_width



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用单调栈 + 从右向左扫描的两遍法：
# 1. 第一遍从左到右，构建一个严格单调递减的栈，存储候选的左边界索引 i。
#    递减栈保证了栈中元素对应的值依次减小，且索引依次增大。
# 2. 第二遍从右到左扫描 j，对于每个 j，不断弹出栈顶的 i（满足 A[i] <= A[j]），
#    计算宽度 j - i 并更新最大值。
# 为什么单调递减栈有效：如果存在 i1 < i2 且 A[i1] <= A[i2]，那么 i1 作为左边界
# 总是优于 i2（更靠左且值更小），因此 i2 不需要进入栈。
#
# 时间复杂度: O(N) — 每个元素最多入栈一次、出栈一次
# 空间复杂度: O(N) — 栈的空间
#
# 关键点:
# - 单调递减栈只存储"可能成为最优左边界"的索引
# - 从右向左扫描利用贪心：更大的 j 配合更小的 i 获得更大宽度
# - 每个元素只被处理常数次
