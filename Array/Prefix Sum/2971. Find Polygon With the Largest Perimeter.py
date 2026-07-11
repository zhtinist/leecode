"""
LeetCode #2971 - Find Polygon With the Largest Perimeter
找到最大周长的多边形
https://leetcode.cn/problems/find-polygon-with-the-largest-perimeter/

给你一个长度为 `n` 的 正 整数数组 `nums` 。
多边形 指的是一个至少有 `3` 条边的封闭二维图形。多边形的 最长边 一定 小于 所有其他边长度之和。
如果你有 `k` （`k >= 3`）个 正 数 `a_1`，`a_2`，`a_3`, ...，`a_k` 满足 `a_1 <= a_2 <= a_3 <= ... <= a_k` 且 `a_1 + a_2 + a_3 + ... + a_k-1 > a_k`_ ，那么 一定 存在一个 `k` 条边的多边形，每条边的长度分别为 `a_1` ，`a_2` ，`a_3` ， ...，`a_k` 。
一个多边形的 周长 指的是它所有边之和。
请你返回从 `nums` 中可以构造的 多边形 的 最大周长 。如果不能构造出任何多边形，请你返回 `-1` 。

示例 1：
输入：nums = [5,5,5] 输出：15 解释：nums 中唯一可以构造的多边形为三角形，每条边的长度分别为 5 ，5 和 5 ，周长为 5 + 5 + 5 = 15 。
示例 2：
输入：nums = [1,12,1,2,5,50,3] 输出：12 解释：最大周长多边形为五边形，每条边的长度分别为 1 ，1 ，2 ，3 和 5 ，周长为 1 + 1 + 2 + 3 + 5 = 12 。 我们无法构造一个包含变长为 12 或者 50 的多边形，因为其他边之和没法大于两者中的任何一个。 所以最大周长为 12 。
示例 3：
输入：nums = [5,5,50] 输出：-1 解释：无法构造任何多边形，因为多边形至少要有 3 条边且 50 > 5 + 5 。

提示：
`3 <= n <= 10^5`
`1 <= nums[i] <= 10^9`
"""

from typing import List, Optional


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        """
        Sort the array and maintain prefix sum. For a polygon with sides
        a1 <= a2 <= ... <= ak, the condition is sum of first k-1 sides > ak.
        Scan from left to right, track the maximum valid perimeter.
        """
        nums.sort()
        prefix_sum = 0
        ans = -1

        for i, num in enumerate(nums):
            # num is the longest side so far
            if i >= 2 and prefix_sum > num:
                ans = prefix_sum + num
            prefix_sum += num

        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Array, Prefix Sum, Sorting
#
# 解题思路:
# 排序后贪心扫描：维护前缀和 prefix_sum（即当前元素之前所有元素之和）。
# 对于排好序的数组，若 prefix_sum > nums[i]（当前最长边），
# 则前 i+1 条边可以构成多边形，周长为 prefix_sum + nums[i]。
# 遍历整个数组，不断更新最大周长。
#
# 时间复杂度: O(n log n)，主要开销在排序
# 空间复杂度: O(1)，仅使用常数空间（或 O(n) 取决于排序实现）
#
# 关键点:
# - 多边形条件：最长边 < 其他边之和（排序后等价于前缀和 > 当前元素）
# - 贪心正确性：使用更多元素只会增加周长，只要条件满足就一直扩展
# - 排序保证当前元素是已扫描元素中的最大值
