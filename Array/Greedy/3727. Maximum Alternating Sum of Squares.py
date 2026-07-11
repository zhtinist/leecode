"""
LeetCode #3727 - Maximum Alternating Sum of Squares
最大交替平方和
https://leetcode.cn/problems/maximum-alternating-sum-of-squares/

给你一个整数数组 `nums`。你可以以任意顺序 重新排列元素 。
数组 `arr` 的 交替得分 定义为：
`score = arr[0]^2 - arr[1]^2 + arr[2]^2 - arr[3]^2 + ...`
在对 `nums` 重新排列后，返回其 最大可能的交替得分。

示例 1：

输入： nums = [1,2,3]
输出： 12
解释：
`nums` 的一种可行重排为 `[2,1,3]`，该排列在所有可能重排中给出了最大交替得分。
交替得分计算如下：
`score = 2^2 - 1^2 + 3^2 = 4 - 1 + 9 = 12`
示例 2：

输入： nums = [1,-1,2,-2,3,-3]
输出： 16
解释：
`nums` 的一种可行重排为 `[-3,-1,-2,1,3,2]`，该排列在所有可能重排中给出了最大交替得分。
交替得分计算如下：
`score = (-3)^2 - (-1)^2 + (-2)^2 - (1)^2 + (3)^2 - (2)^2 = 9 - 1 + 4 - 1 + 9 - 4 = 16`

提示：
`1 <= nums.length <= 10^5`
`-4 * 10^4 <= nums[i] <= 4 * 10^4`
"""

from typing import List, Optional


class Solution:
    def maxAlternatingSumOfSquares(self, nums: List[int]) -> int:
        # Calculate squares
        squares = [x * x for x in nums]
        squares.sort(reverse=True)

        n = len(squares)
        # Add ceil(n/2) largest, subtract floor(n/2) smallest
        # Even indices (0,2,4,...) are added; odd indices (1,3,5,...) are subtracted
        result = 0
        for i in range(n):
            if i % 2 == 0:
                result += squares[i]
            else:
                result -= squares[i]
        return result










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Array, Sorting
#
# 解题思路:
# 交替得分公式为 arr[0]^2 - arr[1]^2 + arr[2]^2 - arr[3]^2 + ...
# 由于平方总是非负数，要使得分最大：
# - 偶数位置（加号）应该放平方值最大的元素
# - 奇数位置（减号）应该放平方值最小的元素
# 因此，将所有元素的平方值按降序排列，然后交替加减即可：
# 最大的 ceil(n/2) 个平方值放在偶数位置（加），最小的 floor(n/2) 个放在奇数位置（减）。
#
# 时间复杂度: O(n log n)
# 空间复杂度: O(n)
#
# 关键点:
# - 平方值非负，所以排序后最大的放在加号位置
# - 不需要关心原始元素的符号，只看平方值大小
