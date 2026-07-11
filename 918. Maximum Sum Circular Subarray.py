"""
LeetCode #918 - Maximum Sum Circular Subarray
中文题名：环形子数组的最大和
https://leetcode.com/problems/maximum-sum-circular-subarray/

Given a circular array C of integers represented
by `A`, find the maximum possible sum of a non-empty subarray of
C.

Here, a circular array means the end of the array connects to the
beginning of the array.  (Formally, `C[i] = A[i]` when `0 <= i <
A.length`, and `C[i+A.length] = C[i]` when `i >=
0`.)

Also, a subarray may only include each element of the fixed buffer `A` at most
once.  (Formally, for a subarray `C[i], C[i+1], ..., C[j]`, there does not
exist `i <= k1, k2 <= j` with `k1 % A.length = k2 %
A.length`.)

Example 1:

Input: [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3

Example 2:

Input: [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10

Example 3:

Input: [3,-1,2,-1]
Output: 4
Explanation: Subarray [2,-1,3] has maximum sum 2 + (-1) + 3 = 4

Example 4:

Input: [3,-2,2,-3]
Output: 3
Explanation: Subarray [3] and [3,-2,2] both have maximum sum 3

Example 5:

Input: [-2,-3,-1]
Output: -1
Explanation: Subarray [-1] has maximum sum -1

Note:

`-30000 <= A[i] <= 30000`

`1 <= A.length <= 30000`

【中文翻译】

给定一个由整数数组 A 表示的循环数组 C，找到 C 的非空子数组的最大可能和。
这里，循环数组意味着数组的末尾连接到数组的开头。
（形式化地，当 0 <= i < A.length 时 C[i] = A[i]，且当 i >= 0 时 C[i+A.length] = C[i]。）
另外，一个子数组最多只能包含固定缓冲区 A 中的每个元素一次。

"""

from typing import List, Optional


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        """
        Case 1: Maximum subarray is not circular → standard Kadane.
        Case 2: Maximum subarray wraps around → total_sum - min_subarray.
        Answer = max(case1, case2), but handle all-negative case.
        """
        total = 0
        max_sum = float('-inf')
        min_sum = float('inf')
        cur_max = 0
        cur_min = 0

        for num in nums:
            total += num
            # Kadane for maximum subarray
            cur_max = max(cur_max + num, num)
            max_sum = max(max_sum, cur_max)
            # Kadane for minimum subarray
            cur_min = min(cur_min + num, num)
            min_sum = min(min_sum, cur_min)

        # If all numbers are negative, max_sum is the answer (non-empty subarray)
        if max_sum < 0:
            return max_sum

        # Otherwise, answer is max of non-circular and circular cases
        return max(max_sum, total - min_sum)



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 环形子数组的最大和有两种情况：
# 1. 最大子数组不跨越边界 → 标准 Kadane 算法即可求出 max_subarray。
# 2. 最大子数组跨越边界 → 等价于总和减去最小子数组和 (total - min_subarray)，
#    因为我们"绕过"了中间的最小部分。
# 最终答案 = max(max_subarray, total - min_subarray)。
# 特殊情况：如果所有元素都是负数，max_subarray 就是答案（不能取空数组）。
#
# 时间复杂度: O(N)
# 空间复杂度: O(1)
#
# 关键点:
# - 同时运行 Kadane 求最大子数组和与最小子数组和
# - 全负数数组时，total - min_subarray = 0（空数组），需要排除这种情况
# - 最大子数组和与最小子数组和可以在一趟遍历中同时计算
