"""
LeetCode #1846 - Maximum Element After Decreasing and Rearranging
中文题名：减小和重新排列数组后的最大元素
https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/

You are given an array of positive integers `arr`. Perform some operations (possibly none) on `arr` so that it satisfies these conditions:

The value of the first element in `arr` must be `1`.

The absolute difference between any 2 adjacent elements must be less than or equal to `1`. In other words, `abs(arr[i] - arr[i - 1]) <= 1` for each `i` where `1 <= i < arr.length` (0-indexed). `abs(x)` is the absolute value of `x`.

There are 2 types of operations that you can perform any number of times:

Decrease the value of any element of `arr` to a smaller positive integer.

Rearrange the elements of `arr` to be in any order.

Return the maximum possible value of an element in `arr` after performing the operations to satisfy the conditions.

Example 1:

Input: arr = [2,2,1,2,1]
Output: 2
Explanation:
We can satisfy the conditions by rearranging `arr` so it becomes `[1,2,2,2,1]`.
The largest element in `arr` is 2.

Example 2:

Input: arr = [100,1,1000]
Output: 3
Explanation:
One possible way to satisfy the conditions is by doing the following:
1. Rearrange `arr` so it becomes `[1,100,1000]`.
2. Decrease the value of the second element to 2.
3. Decrease the value of the third element to 3.
Now `arr = [1,2,3], which `satisfies the conditions.
The largest element in `arr is 3.`

Example 3:

Input: arr = [1,2,3,4,5]
Output: 5
Explanation: The array already satisfies the conditions, and the largest element is 5.

Constraints:

`1 <= arr.length <= 105`

`1 <= arr[i] <= 109`

【中文翻译】

给定一个正整数数组 `arr`。对其执行一些操作（可能为零次）使其满足以下条件：
1. `arr` 的第一个元素必须为1。
2. 相邻元素之间的绝对差必须小于或等于1。即对于所有 1 <= i < arr.length，|arr[i] - arr[i-1]| <= 1。

你可以执行两种操作任意次数：
- 将 `arr` 中任意元素的值减小为更小的正整数。
- 将 `arr` 中的元素重新排列为任意顺序。

返回满足条件后 `arr` 中元素的最大可能值。

示例：
输入：arr = [2,2,1,2,1]
输出：2
解释：重新排列为[1,2,2,2,1]满足条件，最大元素为2。

"""

from typing import List, Optional


class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        arr[0] = 1

        for i in range(1, len(arr)):
            arr[i] = min(arr[i], arr[i - 1] + 1)

        return arr[-1]










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 贪心策略。要最大化最后一个元素，应该让数组尽可能递增缓慢。
# 排序后，将第一个元素设为1。然后从第二个元素开始，
# arr[i] = min(arr[i], arr[i-1] + 1)，即每个元素最多比前一个元素大1。
# 这样可以保证相邻差<=1，同时最大化每个位置的值。返回最后一个元素。
#
# 时间复杂度: O(N log N)，排序开销
# 空间复杂度: O(1)，原地修改
#
# 关键点:
# - 第一个元素必须为1
# - 贪心：arr[i] = min(arr[i], arr[i-1] + 1)
# - 排序是必要的，使数组保持递增
