"""
LeetCode #1131 - Maximum of Absolute Value Expression
中文题名：绝对值表达式的最大值
https://leetcode.com/problems/maximum-of-absolute-value-expression/

Given two arrays of integers with equal lengths, return the maximum value of:

`|arr1[i] - arr1[j]| + |arr2[i] - arr2[j]| + |i - j|`

where the maximum is taken over all `0 <= i, j < arr1.length`.

Example 1:

Input: arr1 = [1,2,3,4], arr2 = [-1,4,5,6]
Output: 13

Example 2:

Input: arr1 = [1,-2,-5,0,10], arr2 = [0,-2,-1,-7,-4]
Output: 20

Constraints:

`2 <= arr1.length == arr2.length <= 40000`

`-10^6 <= arr1[i], arr2[i] <= 10^6`

【中文翻译】
给定两个长度相等的整数数组，返回以下表达式的最大值：

|arr1[i] - arr1[j]| + |arr2[i] - arr2[j]| + |i - j|

其中最大值取遍所有 0 <= i, j < arr1.length。

示例 1：

输入：arr1 = [1,2,3,4], arr2 = [-1,4,5,6]
输出：13

示例 2：

输入：arr1 = [1,-2,-5,0,10], arr2 = [0,-2,-1,-7,-4]
输出：20

约束条件：

`2 <= arr1.length == arr2.length <= 40000`

`-10^6 <= arr1[i], arr2[i] <= 10^6`
"""

from typing import List, Optional


class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        n = len(arr1)
        max_vals = [float('-inf')] * 4
        min_vals = [float('inf')] * 4

        for i in range(n):
            a, b = arr1[i], arr2[i]
            vals = [
                a + b + i,
                a + b - i,
                a - b + i,
                a - b - i,
            ]
            for j in range(4):
                max_vals[j] = max(max_vals[j], vals[j])
                min_vals[j] = min(min_vals[j], vals[j])

        return max(max_vals[k] - min_vals[k] for k in range(4))










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 利用绝对值展开的数学技巧。|x| = max(x, -x)，因此：
# |arr1[i]-arr1[j]| + |arr2[i]-arr2[j]| + |i-j|
# 可以展开为以下 4 种线性组合的最大值（考察 i 和 j 的系数符号）：
# 1. (arr1[i] + arr2[i] + i) - (arr1[j] + arr2[j] + j)
# 2. (arr1[i] + arr2[i] - i) - (arr1[j] + arr2[j] - j)
# 3. (arr1[i] - arr2[i] + i) - (arr1[j] - arr2[j] + j)
# 4. (arr1[i] - arr2[i] - i) - (arr1[j] - arr2[j] - j)
# 对每种组合，最大值 = max(val over all i) - min(val over all i)。
# 遍历数组一次，同时更新 4 种线性表达式的最大值和最小值。
# 最终答案为 4 种组合中 max - min 的最大值。
#
# 时间复杂度: O(n) - 一次遍历
# 空间复杂度: O(1) - 只需存储 8 个变量（4 个 max + 4 个 min）
#
# 关键点:
# - 曼哈顿距离/切比雪夫距离的去绝对值技巧
# - 将 O(n^2) 的暴力枚举优化为 O(n) 的单次扫描
# - 4 种符号组合来源于 |arr1|、|arr2|、|i-j| 各自的正负展开
