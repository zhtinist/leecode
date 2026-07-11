"""
LeetCode #873 - Length of Longest Fibonacci Subsequence
中文题名：最长的斐波那契子序列的长度
https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/

A sequence `X_1, X_2, ..., X_n` is fibonacci-like if:

`n >= 3`

`X_i + X_{i+1} = X_{i+2}` for all `i + 2 <= n`

Given a strictly increasing array `A` of positive integers
forming a sequence, find the length of the longest fibonacci-like
subsequence of `A`.  If one does not exist, return 0.

(Recall that a subsequence is derived from another sequence `A` by deleting
any number of elements (including none) from `A`, without changing the
order of the remaining elements.  For example, `[3, 5, 8]` is a subsequence
of `[3, 4, 5, 6, 7, 8]`.)

Example 1:

Input: [1,2,3,4,5,6,7,8]
Output: 5
Explanation:
The longest subsequence that is fibonacci-like: [1,2,3,5,8].

Example 2:

Input: [1,3,7,11,12,14,18]
Output: 3
Explanation:
The longest subsequence that is fibonacci-like:
[1,11,12], [3,11,14] or [7,11,18].

Note:

`3 <= A.length <= 1000`

`1 <= A[0] < A[1] < ... < A[A.length - 1] <= 10^9`

(The time limit has been reduced by 50% for submissions in Java, C, and C++.)

【中文翻译】
一个序列 X_1, X_2, ..., X_n 是斐波那契式的，如果满足 n >= 3 且对于所有 i + 2 <= n，
都有 X_i + X_{i+1} = X_{i+2}。给定一个严格递增的正整数数组 A，找出 A 中最长的
斐波那契式子序列的长度。如果不存在，返回 0。

"""

from typing import List, Optional


class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        # 建立值到索引的映射，方便 O(1) 查找补数
        index_map = {val: i for i, val in enumerate(arr)}
        # dp[i][j] 表示以 arr[i], arr[j] 结尾的斐波那契子序列长度（至少 2）
        dp = [[2] * n for _ in range(n)]
        max_len = 0

        # 固定 j，向前找 i
        for j in range(n):
            for i in range(j):
                # X_k + X_i = X_j  =>  X_k = X_j - X_i
                needed = arr[j] - arr[i]
                # 由于数组严格递增，needed 必须 < arr[i] 才可能在前面
                if needed < arr[i] and needed in index_map:
                    k = index_map[needed]
                    # 在 dp[k][i] 的基础上增加 arr[j]，构成长度 +1 的序列
                    dp[i][j] = dp[k][i] + 1
                    max_len = max(max_len, dp[i][j])

        return max_len if max_len >= 3 else 0



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 动态规划。定义 dp[i][j] 表示以 arr[i] 和 arr[j] 作为最后两个元素的斐波那契子序列的长度
# （至少为 2）。对于每一对 (i, j)，我们需要找到前一个元素 k，使得 arr[k] + arr[i] = arr[j]，
# 即 arr[k] = arr[j] - arr[i]。使用哈希表 index_map 将每个值映射到其索引，以便 O(1) 查找 k。
# 如果找到 k 且 k < i，则 dp[i][j] = dp[k][i] + 1，相当于在已有序列后追加 arr[j]。
# 最终答案取所有 dp[i][j] >= 3 中的最大值。
#
# 时间复杂度: O(N^2)，其中 N <= 1000
# 空间复杂度: O(N^2)，DP 表格大小
#
# 关键点:
# - 状态定义：dp[i][j] 表示以 arr[i], arr[j] 结尾的斐波那契序列长度
# - 使用哈希表快速查找前驱元素 arr[k] = arr[j] - arr[i]
# - 利用 strict increasing 的性质：arr[k] 必须小于 arr[i]
