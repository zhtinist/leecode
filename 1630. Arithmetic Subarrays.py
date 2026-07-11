"""
LeetCode #1630 - Arithmetic Subarrays
中文题名：等差子数组
https://leetcode.com/problems/arithmetic-subarrays/

A sequence of numbers is called arithmetic if it consists of at
least two elements, and the difference between every two consecutive elements is the
same. More formally, a sequence `s` is arithmetic if and only if `s[i+1]
- s[i] == s[1] - s[0] `for all valid `i`.

For example, these are arithmetic sequences:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9

The following sequence is not arithmetic:

1, 1, 2, 5, 7

You are given an array of `n` integers, `nums`, and two arrays
of `m` integers each, `l` and `r`, representing the
`m` range queries, where the `ith` query is the
range `[l[i], r[i]]`. All the arrays are 0-indexed.

Return a list of `boolean` elements
`answer`, where `answer[i]` is
`true` if the subarray `nums[l[i]], nums[l[i]+1], ... ,
nums[r[i]]` can be rearranged to form an arithmetic
sequence, and `false` otherwise.

Example 1:

Input: nums = `[4,6,5,9,3,7]`, l = `[0,0,2]`, r = `[2,3,5]`
Output: `[true,false,true]`
Explanation:
In the 0th query, the subarray is [4,6,5]. This can be rearranged as [6,5,4], which is an arithmetic sequence.
In the 1st query, the subarray is [4,6,5,9]. This cannot be rearranged as an arithmetic sequence.
In the 2nd query, the subarray is `[5,9,3,7]. This` can be rearranged as `[3,5,7,9]`, which is an arithmetic sequence.

Example 2:

Input: nums = [-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10], l = [0,1,6,4,8,7], r = [4,4,9,7,9,10]
Output: [false,true,false,false,true,true]

Constraints:

`n == nums.length`

`m == l.length`

`m == r.length`

`2 <= n <= 500`

`1 <= m <= 500`

`0 <= l[i] < r[i] < n`

`-105 <= nums[i] <= 105`

【中文翻译】
给定一个整数数组 nums 和两个数组 l 和 r，分别表示 m 个查询的范围边界。
对于每个查询 i，判断子数组 nums[l[i]], nums[l[i]+1], ..., nums[r[i]] 重新排列后是否可以形成等差数列。
返回布尔值列表 answer。

示例 1：
输入: nums = [4,6,5,9,3,7], l = [0,0,2], r = [2,3,5]
输出: [true,false,true]
解释: 查询[0,2]: [4,6,5] 可重排为 [4,5,6] (等差)；查询[0,3]: [4,6,5,9] 不可等差；查询[2,5]: [5,9,3,7] 可重排为 [3,5,7,9] (等差)
"""

from typing import List, Optional


class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def is_arithmetic(arr: List[int]) -> bool:
            if len(arr) <= 2:
                return True
            arr_sorted = sorted(arr)
            diff = arr_sorted[1] - arr_sorted[0]
            for i in range(2, len(arr_sorted)):
                if arr_sorted[i] - arr_sorted[i - 1] != diff:
                    return False
            return True

        result = []
        for left, right in zip(l, r):
            sub = nums[left:right + 1]
            result.append(is_arithmetic(sub))
        return result
# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 对于每个查询 [l, r]，提取子数组并排序，检查相邻元素的差是否相等。
# 也可使用数学方法判断：子数组的最大值减最小值 = (len-1) * 公差，且所有元素对公差的取模结果唯一。
#
# 时间复杂度: O(M * K log K) — M 个查询，每个子数组长度为 K 需要排序
# 空间复杂度: O(K) — 每个查询的子数组拷贝
#
# 关键点:
# - 等差数列的充要条件：最大-最小 = (n-1)*diff 且元素模 diff 全相等
# - 小数据量可以直接排序判断
