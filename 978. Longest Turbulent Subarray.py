"""
LeetCode #978 - Longest Turbulent Subarray
中文题名：最长湍流子数组
https://leetcode.com/problems/longest-turbulent-subarray/

当 A 的子数组 A[i], A[i+1], ..., A[j] 满足下列条件时，我们称其为湍流子数组：

对于 i <= k < j，当 k 为奇数时，A[k] > A[k+1]，且当 k 为偶数时，A[k] < A[k+1]；
或者，对于 i <= k < j，当 k 为偶数时，A[k] > A[k+1]，且当 k 为奇数时，A[k] < A[k+1]。

也就是说，如果子数组中每对相邻元素之间的比较符号在子数组中翻转，则该子数组是湍流子数组。

返回 A 的最大湍流子数组的长度。

示例 1：

输入：[9,4,2,10,7,8,8,1,9]
输出：5
解释：(A[1] > A[2] < A[3] > A[4] < A[5])

示例 2：

输入：[4,8,12,16]
输出：2

示例 3：

输入：[100]
输出：1

【中文翻译】
给定一个整数数组，求最长的湍流子数组的长度。湍流子数组要求相邻元素的比较符号交替变化（大于/小于交替）。注意单个元素的子数组也是湍流的。

"""

from typing import List, Optional


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 1
        left = 0
        max_len = 1
        for right in range(1, n):
            cmp = self._cmp(arr[right - 1], arr[right])
            if cmp == 0:
                left = right
            elif right == n - 1 or cmp * self._cmp(arr[right], arr[right + 1]) != -1:
                # End of a valid turbulent segment
                max_len = max(max_len, right - left + 1)
                left = right
        return max_len

    def _cmp(self, a: int, b: int) -> int:
        if a > b:
            return 1
        elif a < b:
            return -1
        return 0



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 滑动窗口法：
# 1. 湍流子数组的核心要求是相邻元素的比较符号必须交替（即 > < > < ... 或 < > < > ...）。
# 2. 定义辅助函数 _cmp(a, b) 返回 a 与 b 的比较结果（1 表示大于，-1 表示小于，0 表示等于）。
# 3. 维护滑动窗口 [left, right]：
#    - 当 arr[right-1] 和 arr[right] 相等时，窗口重置，left = right。
#    - 当相邻三次比较符号不交替时（即 cmp(arr[i-1], arr[i]) * cmp(arr[i], arr[i+1]) != -1），
#      说明 arr[i] 是转折点，新的湍流段从 arr[i] 开始。
# 4. 每次窗口变化时更新最大长度。
# 5. 也可以使用动态规划：up[i] 表示以 i 结尾且 A[i] > A[i-1] 的最长湍流长度，
#    down[i] 表示 A[i] < A[i-1] 的最长湍流长度。
#
# 时间复杂度: O(N)，每个元素只遍历一次
# 空间复杂度: O(1)，只使用常数级别额外空间
#
# 关键点:
# - 相等元素会打断湍流（cmp == 0）
# - 湍流的本质是相邻比较符号交替，即 cmp(i-1, i) * cmp(i, i+1) == -1
# - 可以使用滑动窗口（双指针）或动态规划两种方法
# - 边界情况：单个元素本身就是长度为 1 的湍流子数组
