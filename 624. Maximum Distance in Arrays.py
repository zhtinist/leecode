"""
LeetCode #624 - Maximum Distance in Arrays
中文题名：数组列表中的最大距离
https://leetcode.com/problems/maximum-distance-in-arrays/

Given `m` arrays, and each array is sorted in ascending order. Now you can pick
up two integers from two different arrays (each array picks one) and calculate the distance.
We define the distance between two integers `a` and `b` to be their
absolute difference `|a-b|`. Your task is to find the maximum distance.

Example 1:

Input:
[[1,2,3],
[4,5],
[1,2,3]]
Output: 4
Explanation:
One way to reach the maximum distance 4 is to pick 1 in the first or third array and pick 5 in the second array.

Note:

Each given array will have at least 1 number. There will be at least two non-empty
arrays.

The total number of the integers in all the `m` arrays will be in the
range of [2, 10000].

The integers in the `m` arrays will be in the range of [-10000, 10000].

【中文翻译】
给定 `m` 个数组，每个数组已按升序排列。现在你可以从两个不同的数组中各挑选一个整数
（每个数组选一个）并计算距离。我们定义两个整数 `a` 和 `b` 之间的距离为
它们的绝对差 `|a-b|`。你的任务是求出最大距离。

示例 1：

输入：
[[1,2,3],
 [4,5],
 [1,2,3]]
输出：4
解释：
一种得到最大距离 4 的方法是从第一个或第三个数组中取 1，从第二个数组中取 5。

注意：

每个给定的数组至少包含 1 个数字。至少有两个非空数组。

所有 `m` 个数组中整数的总数在 [2, 10000] 范围内。

`m` 个数组中的整数在 [-10000, 10000] 范围内。
"""

import math
from typing import List


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        res = 0
        # Initialize with the first array's min and max
        min_val = arrays[0][0]
        max_val = arrays[0][-1]

        for i in range(1, len(arrays)):
            arr = arrays[i]
            # Max distance from current array's max to previous smallest min,
            # or from current array's min to previous largest max
            res = max(res, abs(arr[-1] - min_val), abs(max_val - arr[0]))
            # Update global min and max
            min_val = min(min_val, arr[0])
            max_val = max(max_val, arr[-1])

        return res



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 由于每个数组已排序，每个数组的最小值在第一个位置，最大值在最后一个位置。
# 最大距离一定来自两个不同数组，且一定是某个数组的最大值减去另一个数组的最小值。
# 因此只需一次线性扫描：
# 1. 维护全局最小值 min_val 和全局最大值 max_val（来自已遍历过的数组）。
# 2. 对于当前数组，计算以下两种情况的价值并更新答案：
#    - |当前数组最大值 - 全局最小值|
#    - |全局最大值 - 当前数组最小值|
# 3. 更新全局最小值和最大值（包含当前数组的信息）。
#
# 时间复杂度: O(m) - m 为数组个数
# 空间复杂度: O(1) - 只使用常数额外空间
#
# 关键点:
# - 因为数组已排序，最小值和最大值一定在两端
# - 两个数必须来自不同数组，不能是同一个数组里的
# - 通过先计算距离再更新全局 min/max，避免同数组比较
# - 与买卖股票的最佳时机问题思路类似（维护遍历过程中的极值）
