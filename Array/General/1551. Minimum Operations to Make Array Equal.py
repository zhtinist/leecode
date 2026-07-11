"""
LeetCode #1551 - Minimum Operations to Make Array Equal
中文题名：使数组中所有元素相等的最小操作数
https://leetcode.com/problems/minimum-operations-to-make-array-equal/


You have an array `arr` of length `n` where `arr[i] = (2
* i) + 1` for all valid values of `i` (i.e. `0 <= i <
n`).

In one operation, you can select two indices `x` and `y`
where `0 <= x, y < n` and subtract `1` from
`arr[x]` and add `1` to `arr[y]` (i.e. perform
`arr[x] -=1 `and `arr[y] += 1`). The goal is to make
all the elements of the array equal. It is
guaranteed that all the elements of the array can be made equal
using some operations.

Given an integer `n`, the length of the array. Return the minimum
number of operations needed to make all the elements of arr equal.

Example 1:

Input: n = 3
Output: 2
Explanation: arr = [1, 3, 5]
First operation choose x = 2 and y = 0, this leads arr to be [2, 3, 4]
In the second operation choose x = 2 and y = 0 again, thus arr = [3, 3, 3].

Example 2:

Input: n = 6
Output: 9

Constraints:

`1 <= n <= 10^4`

【中文翻译】
数组 arr 长度为 n，其中 arr[i] = 2*i+1（即 [1,3,5,...,2n-1]）。
每次操作可以选择两个索引 x 和 y，将 arr[x] 减 1，arr[y] 加 1。
目标是使所有元素相等。返回所需的最少操作次数。

示例 1：
输入：n = 3
输出：2
解释：arr = [1,3,5] -> [2,3,4] -> [3,3,3]。

示例 2：
输入：n = 6
输出：9
"""

from typing import List, Optional


class Solution:
    def minOperations(self, n: int) -> int:
        # Target value is n (the average/middle)
        # Operations = sum of differences between first half and n
        # Formula: (n // 2) * (n - n // 2)
        # Simplified: n * n // 4
        return (n * n) // 4



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 数学推导。数组是 [1, 3, 5, ..., 2n-1]，总和为 n^2，目标值（平均值）= n。
# 每次操作将一个元素减 1、另一个元素加 1，相当于将差值从大于 n 的元素转移到小于 n 的元素。
# 所需操作数 = 小于 n 的元素与 n 的差值之和 = 1+3+...+(n-1)（当 n 为偶数时）
# 化简公式：n^2 / 4（整数除法）。
#
# 时间复杂度: O(1)
# 空间复杂度: O(1)
#
# 关键点:
# - 目标值是数组的平均值 n
# - 每次操作转移 1 个单位的差值
# - 公式：n*n // 4












