"""
LeetCode #949 - Largest Time for Given Digits
中文题名：给定数字能组成的最大时间
https://leetcode.com/problems/largest-time-for-given-digits/

Given an array of 4 digits, return the largest 24 hour time that can be made.

The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from 00:00, a
time is larger if more time has elapsed since midnight.

Return the answer as a string of length 5.  If no valid time can be made, return an
empty string.

Example 1:

Input: [1,2,3,4]
Output: "23:41"

Example 2:

Input: [5,5,5,5]
Output: ""

Note:

`A.length == 4`

`0 <= A[i] <= 9`

【中文翻译】
给定一个由 4 位数字组成的数组，返回可以组成的最大 24 小时制时间。

最小的 24 小时制时间是 00:00，最大的是 23:59。从 00:00 开始，
时间越大表示从午夜起经过的时间越长。

返回一个长度为 5 的字符串作为答案。如果无法组成有效的时间，则返回空字符串。

"""

from typing import List, Optional
from itertools import permutations


class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        best = -1
        best_perm = None

        for perm in permutations(arr):
            hour = perm[0] * 10 + perm[1]
            minute = perm[2] * 10 + perm[3]
            if hour < 24 and minute < 60:
                total_minutes = hour * 60 + minute
                if total_minutes > best:
                    best = total_minutes
                    best_perm = perm

        if best == -1:
            return ""

        return f"{best_perm[0]}{best_perm[1]}:{best_perm[2]}{best_perm[3]}"



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 1. 枚举所有排列：使用 itertools.permutations 生成 4 个数字的所有排列（共 4! = 24 种）。
# 2. 验证有效性：对于每个排列，检查前两位组成的数字（小时）是否 < 24，
#    后两位组成的数字（分钟）是否 < 60。
# 3. 寻找最大值：将有效时间转换为从午夜开始的分钟数（hour * 60 + minute），
#    跟踪最大值及其对应的排列。
# 4. 格式化输出：如果找到有效时间，格式化为"HH:MM"返回；否则返回空字符串。
#
# 时间复杂度: O(1) — 固定 4! = 24 种排列。
# 空间复杂度: O(1) — 仅需常数空间。
#
# 关键点:
# - 输入只有 4 个数字，暴力枚举即可（24 种排列）
# - 有效时间条件：小时 < 24 且 分钟 < 60
# - 转换为总分钟数便于比较大小
