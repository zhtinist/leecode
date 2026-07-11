"""
LeetCode #795 - Number of Subarrays with Bounded Maximum
中文题名：区间最大值的子数组数量
https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/

We are given an array `A` of positive integers, and two positive integers
`L` and `R` (`L <= R`).

Return the number of (contiguous, non-empty) subarrays such that the value of the maximum
array element in that subarray is at least `L` and at most `R`.

Example :
Input:
A = [2, 1, 4, 3]
L = 2
R = 3
Output: 3
Explanation: There are three subarrays that meet the requirements: [2], [2, 1], [3].

Note:

L, R  and `A[i]` will be an integer in the range `[0, 10^9]`.

The length of `A` will be in the range of `[1, 50000]`.

【中文翻译】
给定一个正整数数组 `A` 和两个正整数 `L` 和 `R`（`L <= R`）。

返回满足以下条件的（连续、非空）子数组的数量：该子数组中最大元素的值至少为 `L` 且至多为 `R`。

示例：
输入：A = [2, 1, 4, 3], L = 2, R = 3
输出：3
解释：满足要求的子数组有三个：[2], [2, 1], [3]。

注意：
L, R 和 `A[i]` 是范围为 `[0, 10^9]` 的整数。
`A` 的长度在 `[1, 50000]` 范围内。
"""

from typing import List, Optional


class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        def count(bound: int) -> int:
            """Count subarrays where max element <= bound."""
            ans = cur = 0
            for x in nums:
                if x <= bound:
                    cur += 1
                    ans += cur
                else:
                    cur = 0
            return ans

        return count(right) - count(left - 1)



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用容斥原理：最大元素在 [L, R] 内的子数组数量
# = 最大元素 <= R 的子数组数量 - 最大元素 <= L-1 的子数组数量。
#
# count(bound) 辅助函数：统计最大元素 <= bound 的子数组数量。
# 遍历数组，如果当前元素值 <= bound，则可以扩展前面以
# 前一个元素结尾的子数组，新增 cur 个子数组；
# 如果当前元素 > bound，则中断，重置计数。
#
# 时间复杂度: O(N) - 遍历两次数组
# 空间复杂度: O(1) - 只使用常数额外空间
#
# 关键点:
# - 转化为差值问题：<= R 减去 <= L-1
# - 滑动计数技巧：cur 表示以当前位置结尾的合法子数组数
# - cur 累加到答案中，遇到不合法元素重置为 0
