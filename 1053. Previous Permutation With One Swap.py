"""
LeetCode #1053 - Previous Permutation With One Swap
中文题名：交换一次的先前排列
https://leetcode.com/problems/previous-permutation-with-one-swap/

Given an array `A` of positive integers (not necessarily distinct), return the
lexicographically largest permutation that is smaller than `A`, that can be
made with one swap (A swap exchanges the positions of two numbers
`A[i]` and `A[j]`).  If it cannot be done, then return the same
array.

Example 1:

Input: [3,2,1]
Output: [3,1,2]
Explanation: Swapping 2 and 1.

Example 2:

Input: [1,1,5]
Output: [1,1,5]
Explanation: This is already the smallest permutation.

Example 3:

Input: [1,9,4,6,7]
Output: [1,7,4,6,9]
Explanation: Swapping 9 and 7.

Example 4:

Input: [3,1,1,3]
Output: [1,3,1,3]
Explanation: Swapping 1 and 3.

Note:

`1 <= A.length <= 10000`

`1 <= A[i] <= 10000`

【中文翻译】
给你一个正整数数组 A（其中的元素不一定完全不同），请你返回可在一次交换（交换数组中的两个数字 A[i] 和 A[j] 的位置）后得到的、按字典序排列小于 A 的最大可能排列。

如果无法完成，就返回原数组。

示例 1：

输入：[3,2,1]
输出：[3,1,2]
解释：交换 2 和 1。

示例 2：

输入：[1,1,5]
输出：[1,1,5]
解释：这已经是最小的排列。

示例 3：

输入：[1,9,4,6,7]
输出：[1,7,4,6,9]
解释：交换 9 和 7。

示例 4：

输入：[3,1,1,3]
输出：[1,3,1,3]
解释：交换 1 和 3。

注意：

1 <= A.length <= 10000
1 <= A[i] <= 10000

"""

from typing import List, Optional


class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        n = len(arr)
        i = n - 2
        while i >= 0 and arr[i] <= arr[i + 1]:
            i -= 1

        if i < 0:
            return arr

        j = n - 1
        while j > i and arr[j] >= arr[i]:
            j -= 1

        while j > 0 and arr[j] == arr[j - 1]:
            j -= 1

        arr[i], arr[j] = arr[j], arr[i]
        return arr










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 要找到字典序小于当前排列的最大排列，需要尽量减少高位的值。
# 1. 从右向左找到第一个满足 arr[i] > arr[i+1] 的 i（即第一个"下降"位置）。
#    如果找不到，说明数组已是最小排列，返回原数组。
# 2. 在 i 右侧找到小于 arr[i] 的最大值所在位置 j。
#    从右向左找到第一个满足 arr[j] < arr[i] 的位置。
# 3. 如果该值的左边有相同的值，选择最左边的那个（因为交换后 i 位置的值越小，结果越大）。
# 4. 交换 arr[i] 和 arr[j]，返回结果。
#
# 时间复杂度: O(n) - 最多三次线性扫描
# 空间复杂度: O(1) - 原地修改
#
# 关键点:
# - 从右向左找第一个"下降"点（arr[i] > arr[i+1]）
# - 在右侧找小于 arr[i] 的最大值（最右边的）
# - 处理重复元素：选择相同值中最左边的，保证字典序最大
# - 只需一次交换，不需要反转右侧子数组（与下一排列不同）
