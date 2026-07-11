"""
LeetCode #1191 - K-Concatenation Maximum Sum
中文题名：K 次串联后最大子数组之和
https://leetcode.com/problems/k-concatenation-maximum-sum/

Given an integer array `arr` and an integer `k`, modify the array
by repeating it `k` times.

For example, if `arr = [1, 2]` and `k = 3 `then the modified array
will be `[1, 2, 1, 2, 1, 2]`.

Return the maximum sub-array sum in the modified array. Note that the length of the sub-array
can be `0` and its sum in that case is `0`.

As the answer can be very large, return the answer modulo `10^9
+ 7`.

Example 1:

Input: arr = [1,2], k = 3
Output: 9

Example 2:

Input: arr = [1,-2,1], k = 5
Output: 2

Example 3:

Input: arr = [-1,-2], k = 7
Output: 0

Constraints:

`1 <= arr.length <= 10^5`

`1 <= k <= 10^5`

`-10^4 <= arr[i] <= 10^4`

【中文翻译】
给你一个整数数组 arr 和一个整数 k。

首先，我们要对该数组进行修改，即把原数组 arr 重复 k 次。

举个例子，如果 arr = [1, 2] 且 k = 3，那么修改后的数组就是 [1, 2, 1, 2, 1, 2]。

然后，请你返回修改后的数组中的最大的子数组之和。注意，子数组长度可以是 0，这种情况下它的和是 0。

由于结果可能会很大，所以需要模 10^9 + 7 后再返回。

示例 1：

输入：arr = [1,2], k = 3
输出：9

示例 2：

输入：arr = [1,-2,1], k = 5
输出：2

示例 3：

输入：arr = [-1,-2], k = 7
输出：0

约束条件：

1 <= arr.length <= 10^5
1 <= k <= 10^5
-10^4 <= arr[i] <= 10^4

"""

from typing import List, Optional


class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        MOD = 10 ** 9 + 7

        def kadane(a: List[int]) -> int:
            max_sum = cur_sum = 0
            for x in a:
                cur_sum = max(cur_sum + x, x)
                max_sum = max(max_sum, cur_sum)
            return max_sum

        total = sum(arr)

        if k == 1:
            return kadane(arr) % MOD

        # 两个数组拼接后的最大子数组和
        max_two = kadane(arr + arr)

        if total > 0:
            # 中间的 k-2 个完整数组贡献 (k-2) * total
            return (max_two + (k - 2) * total) % MOD
        else:
            return max_two % MOD










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 分情况讨论 K 次串联后的最大子数组和：
# 1. k = 1: 直接对原数组运行 Kadane 算法求最大子数组和。
# 2. k >= 2:
#    a. 计算两个数组拼接后的最大子数组和 max_two = kadane(arr + arr)。
#       （因为最大子数组最多跨越两个 arr 的边界，不会跨越更多，除非 total > 0）
#    b. 如果数组总和 total > 0，则中间剩余的 k-2 个完整数组全取更优，
#       结果为 max_two + (k - 2) * total。
#    c. 如果 total <= 0，则结果就是 max_two（跨越边界不超过一次拼接）。
# 注意结果取模 MOD = 10^9 + 7。
#
# 时间复杂度: O(n) - Kadane 算法线性时间，两次 Kadane 仍 O(n)
# 空间复杂度: O(n) - 拼接两个数组需要额外 O(2n) 空间（可优化为 O(1)，但简洁优先）
#
# 关键点:
# - 核心分类：k=1、k>=2 且 total>0、k>=2 且 total<=0 三种情况
# - 最大子数组最多跨越一次 arr 边界（当 total<=0 时），因为跨越更多次意味着包含了完整的负和数组
# - 当 total>0 时，中间的完整数组全取，加起来更大
# - 结果取模不要忘记
