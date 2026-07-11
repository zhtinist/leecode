"""
LeetCode #1562 - Find Latest Group of Size M
中文题名：查找大小为 M 的最新分组
https://leetcode.com/problems/find-latest-group-of-size-m/


Given an array `arr` that represents a permutation of numbers from
`1` to `n`. You have a binary string of
size `n` that initially has all its bits set to zero.

At each step `i` (assuming both the binary string and
`arr` are 1-indexed) from `1` to `n`, the bit
at position `arr[i]` is set to `1`. You are
given an integer `m` and you need to find the latest step at
which there exists a group of ones of length `m`. A group of ones is
a contiguous substring of 1s such that it cannot be extended in either direction.

Return the latest step at which there exists a group of ones of length exactly `m`.
If no such group exists, return `-1`.

Example 1:

Input: arr = [3,5,1,2,4], m = 1
Output: 4
Explanation:
Step 1: "00100", groups: ["1"]
Step 2: "00101", groups: ["1", "1"]
Step 3: "10101", groups: ["1", "1", "1"]
Step 4: "11101", groups: ["111", "1"]
Step 5: "11111", groups: ["11111"]
The latest step at which there exists a group of size 1 is step 4.

Example 2:

Input: arr = [3,1,5,4,2], m = 2
Output: -1
Explanation:
Step 1: "00100", groups: ["1"]
Step 2: "10100", groups: ["1", "1"]
Step 3: "10101", groups: ["1", "1", "1"]
Step 4: "10111", groups: ["1", "111"]
Step 5: "11111", groups: ["11111"]
No group of size 2 exists during any step.

Example 3:

Input: arr = [1], m = 1
Output: 1

Example 4:

Input: arr = [2,1], m = 2
Output: 2

Constraints:

`n == arr.length`

`1 <= n <= 10^5`

`1 <= arr[i] <= n`

All integers in `arr` are distinct.

`1 <= m <= arr.length`

【中文翻译】
给定一个数组 arr 表示长度为 n 的二进制字符串中 1 的位置（按操作顺序）。
每一步将 arr[i] 位置变为 1。如果一个由连续 1 组成的子串长度恰好为 m，称为一个大小为 m 的分组。
返回存在大小为 m 的分组的最后一步的编号。如果不存在，返回 -1。

示例 1：
输入：arr = [3,5,1,2,4], m = 1
输出：4

示例 2：
输入：arr = [3,1,5,4,2], m = 2
输出：-1
"""

from typing import List, Optional


class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        if m == n:
            return n
        # length[i] = length of consecutive 1s group containing position i
        length = [0] * (n + 2)
        result = -1
        for step, pos in enumerate(arr):
            left = length[pos - 1]
            right = length[pos + 1]
            total = left + right + 1
            length[pos - left] = total
            length[pos + right] = total
            # Check if merging destroyed a group of size m
            if left == m or right == m:
                result = step  # last step where m existed (before merging)
        return result



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用并查集思想维护连续 1 的分组。length 数组记录每个位置所在连续组的大小
# （只更新组的左右边界）。每次在位置 pos 插入 1 时，检查左右相邻的组长度，
# 合并后的新组长度为 left + right + 1。更新新组的左右边界。
# 如果合并前 left 或 right 恰好等于 m，则当前步之前存在大小为 m 的组，记录结果。
# 特殊处理：如果 m == n，最后一步是整个数组。
#
# 时间复杂度: O(N)
# 空间复杂度: O(N)
#
# 关键点:
# - 只更新组的左右边界（类似并查集路径压缩）
# - 检查合并前是否有大小恰好为 m 的组
# - 注意边界处理












