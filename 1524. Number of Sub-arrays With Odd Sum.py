"""
LeetCode #1524 - Number of Sub-arrays With Odd Sum
中文题名：和为奇数的子数组数目
https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/

Given an array of integers `arr`. Return the number of
sub-arrays with odd sum.

As the answer may grow large, the answer must be computed
modulo `10^9 + 7`.

Example 1:

Input: arr = [1,3,5]
Output: 4
Explanation: All sub-arrays are [[1],[1,3],[1,3,5],[3],[3,5],[5]]
All sub-arrays sum are [1,4,9,3,8,5].
Odd sums are [1,9,3,5] so the answer is 4.

Example 2:

Input: arr = [2,4,6]
Output: 0
Explanation: All sub-arrays are [[2],[2,4],[2,4,6],[4],[4,6],[6]]
All sub-arrays sum are [2,6,12,4,10,6].
All sub-arrays have even sum and the answer is 0.

Example 3:

Input: arr = [1,2,3,4,5,6,7]
Output: 16

Example 4:

Input: arr = [100,100,99,99]
Output: 4

Example 5:

Input: arr = [7]
Output: 1

Constraints:

`1 <= arr.length <= 10^5`

`1 <= arr[i] <= 100`

【中文翻译】
给定一个整数数组 arr，返回和为奇数的子数组的数目。
答案可能很大，需对 10^9+7 取模。

示例 1：

输入：arr = [1,3,5]
输出：4
解释：所有子数组和为 [1,4,9,3,8,5]，奇数和有 [1,9,3,5]，共 4 个。

示例 2：

输入：arr = [2,4,6]
输出：0
解释：所有子数组和均为偶数。

示例 3：

输入：arr = [1,2,3,4,5,6,7]
输出：16

示例 4：

输入：arr = [100,100,99,99]
输出：4

示例 5：

输入：arr = [7]
输出：1
"""

from typing import List, Optional


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        odd_count = 0  # number of prefix sums that are odd
        even_count = 1  # number of prefix sums that are even (empty prefix is even)
        prefix = 0
        result = 0
        for num in arr:
            prefix += num
            if prefix % 2 == 1:
                result = (result + even_count) % MOD
                odd_count += 1
            else:
                result = (result + odd_count) % MOD
                even_count += 1
        return result



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 利用前缀和奇偶性。子数组 arr[i..j] 的和的奇偶性 = (prefix[j] - prefix[i-1]) 的奇偶性。
# 奇数 - 奇数 = 偶数，偶数 - 奇数 = 奇数，奇数 - 偶数 = 奇数，偶数 - 偶数 = 偶数。
# 所以，一个子数组和为奇数 <=> 其两端前缀和奇偶性不同。
# 遍历时维护 odd_count（奇数前缀和个数）和 even_count（偶数前缀和个数，初始为 1 表示空前缀）。
# 对于当前位置，如果当前前缀和为奇数，则可以和之前所有偶数前缀组成奇数和子数组。
#
# 时间复杂度: O(N)
# 空间复杂度: O(1)
#
# 关键点:
# - 子数组和的奇偶性 = 前缀和奇偶性的 XOR
# - 奇 + 偶 = 奇，所以奇数前缀和需要配偶数前缀和
# - 空前缀（和为 0）是偶数，初始化 even_count = 1
