"""
LeetCode #462 - Minimum Moves to Equal Array Elements II
中文题名：最少移动次数使数组元素相等 II
https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/

Given a non-empty integer array, find the minimum number of moves required to make all
array elements equal, where a move is incrementing a selected element by 1 or decrementing a
selected element by 1.

You may assume the array's length is at most 10,000.

Example:

Input:
[1,2,3]

Output:
2

Explanation:
Only two moves are needed (remember each move increments or decrements one element):

[1,2,3]  =>  [2,2,3]  =>  [2,2,2]

【中文翻译】
给定一个非空整数数组，求使所有数组元素相等所需的最少移动次数。每次移动定义为将选中的元素
加 1 或减 1。可假设数组长度不超过 10000。

示例：
    输入：[1,2,3]
    输出：2
    解释：只需两次移动（每次移动对一个元素加 1 或减 1）：
    [1,2,3] => [2,2,3] => [2,2,2]
"""

from typing import List, Optional


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        """
        Sort and find the median. The minimum moves to make all elements equal
        is the sum of absolute differences from each element to the median.
        """
        nums.sort()
        median = nums[len(nums) // 2]
        return sum(abs(num - median) for num in nums)



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 排序后取中位数作为目标值。由于每次移动只能将元素增 1 或减 1，将所有元素变为中位数
# 所需的总移动次数最少。中位数具有"最小化绝对偏差和"的性质：对于一组数，中位数使得
# 所有数到该点的绝对距离之和达到最小。若目标值偏离中位数，总移动次数会增加。
#
# 时间复杂度: O(N log N) — 排序开销，也可用快速选择优化至 O(N) 平均时间
# 空间复杂度: O(1) — 原地排序不计额外空间，或 O(N) 若需复制数组
#
# 关键点:
# - 最优目标值是中位数，而非平均值
# - 排序后 nums[len(nums)//2] 即为中位数
# - 也可用快速选择 (QuickSelect) 算法在 O(N) 平均时间内找到中位数
