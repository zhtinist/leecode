"""
LeetCode #1814 - Count Nice Pairs in an Array
中文题名：统计一个数组中好对子的数目
https://leetcode.com/problems/count-nice-pairs-in-an-array/

You are given an array `nums` that consists of non-negative integers. Let us define `rev(x)` as the reverse of the non-negative integer `x`. For example, `rev(123) = 321`, and `rev(120) = 21`. A pair of indices `(i, j)` is nice if it satisfies all of the following conditions:

`0 <= i < j < nums.length`

`nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])`

Return the number of nice pairs of indices. Since that number can be too large, return it modulo `109 + 7`.

Example 1:

Input: nums = [42,11,1,97]
Output: 2
Explanation: The two pairs are:
- (0,3) : 42 + rev(97) = 42 + 79 = 121, 97 + rev(42) = 97 + 24 = 121.
- (1,2) : 11 + rev(1) = 11 + 1 = 12, 1 + rev(11) = 1 + 11 = 12.

Example 2:

Input: nums = [13,10,35,24,76]
Output: 4

Constraints:

`1 <= nums.length <= 105`

`0 <= nums[i] <= 109`

【中文翻译】
给定一个整数数组 nums。rev(x) 表示将 x 的十进制数字反转（去掉前导零）。
好对子 (i, j) 满足 i < j 且 nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])。
返回到好对子的数量，对 10^9+7 取模。

示例 1：
输入: nums = [42,11,1,97]
输出: 2
解释: (0,1): 42+rev(11)=42+11=53, 11+rev(42)=11+24=35 ≠ 53。
(1,2): 11+rev(1)=11+1=12, 1+rev(11)=1+11=12 ✓。(0,3): 42+rev(97)=42+79=121, 97+rev(42)=97+24=121 ✓。
"""

from typing import List, Optional
from collections import Counter


class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7

        def rev(n: int) -> int:
            return int(str(n)[::-1])

        # nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])
        # 移项: nums[i] - rev(nums[i]) == nums[j] - rev(nums[j])
        diffs = [num - rev(num) for num in nums]
        count = Counter(diffs)

        ans = 0
        for c in count.values():
            # C(c, 2) 个对子
            ans = (ans + c * (c - 1) // 2) % MOD

        return ans
# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 将等式变形：
# nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])
# => nums[i] - rev(nums[i]) == nums[j] - rev(nums[j])
# 统计每个 diff = num - rev(num) 的出现频次。
# 对于频次 c，从中任选两个组成 C(c,2) 个对子。
# 答案 = sum(C(c, 2)) % MOD。
#
# 时间复杂度: O(N log M) — N 为数组长度，log M 来自数字反转
# 空间复杂度: O(N) — Counter 存储
#
# 关键点:
# - 等式变形是关键的数学推导
# - 转化为统计相同 diff 的频次
# - 组合计数 C(c,2) = c*(c-1)//2
