"""
LeetCode #1218 - Longest Arithmetic Subsequence of Given Difference
中文题名：最长定差子序列
https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/

Given an integer array `arr` and an integer `difference`,
return the length of the longest subsequence in `arr` which
is an arithmetic sequence such that the difference between adjacent elements in the
subsequence equals `difference`.

Example 1:

Input: arr = [1,2,3,4], difference = 1
Output: 4
Explanation: The longest arithmetic subsequence is [1,2,3,4].

Example 2:

Input: arr = [1,3,5,7], difference = 1
Output: 1
Explanation: The longest arithmetic subsequence is any single element.

Example 3:

Input: arr = [1,5,7,8,5,3,4,2,1], difference = -2
Output: 4
Explanation: The longest arithmetic subsequence is [7,5,3,1].

Constraints:

`1 <= arr.length <= 10^5`

`-10^4 <= arr[i], difference <= 10^4`

【中文翻译】
给你一个整数数组 arr 和一个整数 difference，请你返回在 arr 中最长等差子序列的长度，该子序列中相邻元素之间的差等于 difference。

子序列是指在不改变其余元素顺序的情况下，通过删除一些（或不删除）元素而从原序列派生出的序列。

示例 1：

输入：arr = [1,2,3,4], difference = 1
输出：4
解释：最长的等差子序列是 [1,2,3,4]。

示例 2：

输入：arr = [1,3,5,7], difference = 1
输出：1
解释：最长的等差子序列是任意单个元素。

示例 3：

输入：arr = [1,5,7,8,5,3,4,2,1], difference = -2
输出：4
解释：最长的等差子序列是 [7,5,3,1]。

约束条件：

1 <= arr.length <= 10^5
-10^4 <= arr[i], difference <= 10^4

"""

from typing import List, Optional


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}
        max_len = 0

        for x in arr:
            prev = dp.get(x - difference, 0)
            dp[x] = prev + 1
            max_len = max(max_len, dp[x])

        return max_len










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用哈希表进行动态规划（类似于最长递增子序列的优化版本）。
# 定义 dp[x] = 以值为 x 的元素结尾的最长定差子序列的长度。
#
# 状态转移：对于数组中的每个元素 x：
# - 前一个元素的值为 x - difference（因为公差为 difference）。
# - 如果 x - difference 已经出现过，则 dp[x] = dp[x - difference] + 1。
# - 如果未出现过，则 dp[x] = 1（单独一个元素）。
#
# 遍历过程中维护最大长度即可。
# 由于只需要知道以 x 结尾的最长长度，且 difference 固定，所以只需要一维 DP。
#
# 时间复杂度: O(n) - 遍历数组一次，每次哈希表查询 O(1)
# 空间复杂度: O(n) - 哈希表最多存储 n 个键值对
#
# 关键点:
# - DP 状态定义基于元素值而非索引：dp[x] 表示以值 x 结尾的最长子序列长度
# - 转移方程：dp[x] = dp[x - difference] + 1，差值固定使问题从 O(n^2) 优化到 O(n)
# - 使用 dict.get(x - difference, 0) 优雅处理键不存在的情况
# - 与经典 LIS 不同，这里不需要二分查找或线段树，因为公差固定
