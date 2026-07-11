"""
LeetCode #453 - Minimum Moves to Equal Array Elements
中文题名：最小操作次数使数组元素相等
https://leetcode.com/problems/minimum-moves-to-equal-array-elements/

Given a non-empty integer array of size n, find the minimum number of moves
required to make all array elements equal, where a move is incrementing n - 1
elements by 1.

Example:

Input:
[1,2,3]

Output:
3

Explanation:
Only three moves are needed (remember each move increments two elements):

[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]

【中文翻译】
给定一个长度为 n 的非空整数数组，每次操作可以使 n-1 个元素各增加 1。
求让所有元素相等所需的最小操作次数。

示例：
输入：[1,2,3]
输出：3
解释：只需要三次操作（每次操作增加两个元素）：
[1,2,3] => [2,3,3] => [3,4,3] => [4,4,4]
"""

from typing import List, Optional


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        # Adding 1 to n-1 elements is equivalent to subtracting 1 from 1 element
        # The goal is to make all elements equal to the minimum element
        min_val = min(nums)
        moves = 0
        for num in nums:
            moves += num - min_val
        return moves



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 数学转换：每次将 n-1 个元素加 1，等价于每次将 1 个元素减 1。
# 目标是让所有元素相等，最优策略是让所有元素减小到数组的最小值。
# 因此答案 = sum(nums) - n * min(nums) = 每个元素与最小值的差之和。
#
# 时间复杂度: O(N) — 遍历数组找最小值和求和
# 空间复杂度: O(1) — 只使用常数额外空间
#
# 关键点:
# - "n-1 个元素 +1" 等价于 "1 个元素 -1" 是本题的核心洞察
# - 目标值是最小值，因为每个元素只能减小不能增大
# - 这是一个数学问题，不需要模拟操作过程
