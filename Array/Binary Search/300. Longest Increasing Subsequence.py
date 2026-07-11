"""
LeetCode #300 - Longest Increasing Subsequence
中文题名：最长递增子序列
https://leetcode.com/problems/longest-increasing-subsequence/

Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: `[10,9,2,5,3,7,101,18]
`Output: 4
Explanation: The longest increasing subsequence is `[2,3,7,101]`, therefore the length is `4`.

Note:

There may be more than one LIS combination, it is only necessary for you to return the
length.

Your algorithm should run in O(*n^2*) complexity.

Follow up: Could you improve it to O(*n* log *n*) time complexity?

【中文翻译】
给定一个未排序的整数数组，找到最长递增子序列的长度。

示例：

输入：`[10,9,2,5,3,7,101,18]`
输出：4
解释：最长递增子序列是 `[2,3,7,101]`，因此长度为 `4`。

注意：

可能存在多种最长递增子序列的组合，你只需要返回长度即可。

你的算法的时间复杂度应为 O(n^2)。

进阶：你能否将算法的时间复杂度优化到 O(n log n)？
"""

from typing import List, Optional


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """Find the length of longest increasing subsequence.

        Patience sorting (greedy + binary search): O(n log n)
        Maintain a tails array where tails[i] = the smallest tail value
        of all increasing subsequences of length i+1.

        For each num, binary search its position in tails:
        - If num > all tails: append (extend longest subsequence)
        - Else: replace the first element >= num (improve that length's tail)
        """
        import bisect
        tails = []

        for num in nums:
            # Find the first element in tails that is >= num
            idx = bisect.bisect_left(tails, num)
            if idx == len(tails):
                # num is greater than all tails, extend the LIS
                tails.append(num)
            else:
                # Replace to get a smaller tail for this length
                tails[idx] = num

        return len(tails)


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用耐心排序（Patience Sorting）+ 二分查找，做到 O(N log N)。
# 维护一个 tails 数组，tails[i] 表示长度为 i+1 的递增子序列的最小末尾值。
#
# 遍历每个数字 num：
# 1. 二分查找 tails 中第一个 >= num 的位置 idx
# 2. 如果 num 大于 tails 中的所有值（idx == len(tails)），将其追加到 tails
#    末尾，表示找到了一个更长的递增子序列
# 3. 否则，将 tails[idx] 替换为 num，这意味着我们找到了一个更小的结尾值
#    来构成同样长度的递增子序列，给后续扩展留下更大空间
#
# tails 的长度即为最长递增子序列的长度。
#
# 时间复杂度: O(N log N) - 每个元素二分查找 O(log N)
# 空间复杂度: O(N) - tails 数组
#
# 关键点:
# - tails 数组不是真正的 LIS 序列，只是维护了每个长度的最小末尾
# - 使用 bisect_left 找第一个 >= num 的位置
# - 耐心排序本质是贪心 + 二分
# - 也可以用 O(N^2) 的 DP: dp[i] = max(dp[j] + 1) for j < i and nums[j] < nums[i]
