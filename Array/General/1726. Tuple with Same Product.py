"""
LeetCode #1726 - Tuple with Same Product
中文题名：同积元组
https://leetcode.com/problems/tuple-with-same-product/

Given an array `nums` of distinct positive integers,
return the number of tuples `(a, b, c, d)` such that `a
* b = c * d` where `a`, `b`, `c`,
and `d` are elements of `nums`,
and `a != b != c != d`.

Example 1:

Input: nums = [2,3,4,6]
Output: 8
Explanation: There are 8 valid tuples:
(2,6,3,4) , (2,6,4,3) , (6,2,3,4) , (6,2,4,3)
(3,4,2,6) , (4,3,2,6) , (3,4,6,2) , (4,3,6,2)

Example 2:

Input: nums = [1,2,4,5,10]
Output: 16
Explanation: There are 16 valids tuples:
(1,10,2,5) , (1,10,5,2) , (10,1,2,5) , (10,1,5,2)
(2,5,1,10) , (2,5,10,1) , (5,2,1,10) , (5,2,10,1)
(2,10,4,5) , (2,10,5,4) , (10,2,4,5) , (10,2,4,5)
(4,5,2,10) , (4,5,10,2) , (5,4,2,10) , (5,4,10,2)

Example 3:

Input: nums = [2,3,4,6,8,12]
Output: 40

Example 4:

Input: nums = [2,3,5,7]
Output: 0

Constraints:

`1 <= nums.length <= 1000`

`1 <= nums[i] <= 104`

All elements in `nums` are distinct.

【中文翻译】
给定一个由不同正整数组成的数组 nums。返回满足 a*b = c*d 的元组 (a,b,c,d) 的数量，其中 a、b、c、d 都是 nums 的元素，且 a、b、c、d 两两不同。
注意 (2,6,3,4) 和 (6,2,3,4) 是不同的元组。

示例 1：
输入: nums = [2,3,4,6]
输出: 8
解释: 8个有效元组: (2,6,3,4),(2,6,4,3),(6,2,3,4),(6,2,4,3),(3,4,2,6),(3,4,6,2),(4,3,2,6),(4,3,6,2)。
"""

from typing import List, Optional
from collections import defaultdict


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        n = len(nums)
        product_count = defaultdict(int)

        for i in range(n):
            for j in range(i + 1, n):
                product = nums[i] * nums[j]
                product_count[product] += 1

        ans = 0
        for count in product_count.values():
            if count >= 2:
                # 从 count 对数中选2对：C(count,2) = count*(count-1)//2
                # 每对有8种排列方式
                ans += count * (count - 1) // 2 * 8

        return ans
# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 哈希表统计每两个不同元素的乘积。
# 对于乘积 p，如果有 c 对数对的乘积等于 p，则可以从 c 对中选择 2 对组成 C(c,2) 种组合。
# 每个组合中的4个数可以以 8 种方式排列（两对数对内部各2种排列，两对数对之间2种排列：2*2*2=8）。
# 答案 = sum(C(count, 2) * 8)。
#
# 时间复杂度: O(N^2) — 枚举所有数对
# 空间复杂度: O(N^2) — 哈希表存储乘积
#
# 关键点:
# - a*b = c*d => 统计所有两数乘积的频次
# - C(count, 2) * 8 公式：选2对 × 每种排列
# - 题目中 a,b,c,d 两两不同且顺序重要
