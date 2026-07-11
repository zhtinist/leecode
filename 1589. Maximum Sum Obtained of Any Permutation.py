"""
LeetCode #1589 - Maximum Sum Obtained of Any Permutation
中文题名：所有排列中的最大和
https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/


We have an array of integers, `nums`, and an array of
`requests` where `requests[i] = [starti,
endi]`. The `ith` request asks for the sum of
`nums[starti] + nums[starti + 1] + ... + nums[endi
- 1] + nums[endi]`. Both `starti` and `endi`
are 0-indexed.

Return the maximum total sum of all requests among all
permutations of `nums`.

Since the answer may be too large, return it modulo
`109 + 7`.

Example 1:

Input: nums = [1,2,3,4,5], requests = [[1,3],[0,1]]
Output: 19
Explanation: One permutation of nums is [2,1,3,4,5] with the following result:
requests[0] -> nums[1] + nums[2] + nums[3] = 1 + 3 + 4 = 8
requests[1] -> nums[0] + nums[1] = 2 + 1 = 3
Total sum: 8 + 3 = 11.
A permutation with a higher total sum is [3,5,4,2,1] with the following result:
requests[0] -> nums[1] + nums[2] + nums[3] = 5 + 4 + 2 = 11
requests[1] -> nums[0] + nums[1] = 3 + 5  = 8
Total sum: 11 + 8 = 19, which is the best that you can do.

Example 2:

Input: nums = [1,2,3,4,5,6], requests = [[0,1]]
Output: 11
Explanation: A permutation with the max total sum is [6,5,4,3,2,1] with request sums [11].

Example 3:

Input: nums = [1,2,3,4,5,10], requests = [[0,2],[1,3],[1,1]]
Output: 47
Explanation: A permutation with the max total sum is [4,10,5,3,2,1] with request sums [19,18,10].

Constraints:

`n == nums.length`

`1 <= n <= 105`

`0 <= nums[i] <= 105`

`1 <= requests.length <= 105`

`requests[i].length == 2`

`0 <= starti <=
endi < n`

【中文翻译】
有一个整数数组 nums 和一个请求数组 requests，其中 requests[i] = [start_i, end_i] 表示
请求 nums[start_i..end_i] 区间内所有元素的和。可以任意重新排列 nums。
返回所有请求的总和的最大值，对 10^9+7 取模。

示例 1：输入：nums = [1,2,3,4,5], requests = [[1,3],[0,1]]
输出：19

示例 2：输入：nums = [1,2,3,4,5,6], requests = [[0,1]]
输出：11
"""

from typing import List, Optional


class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        freq = [0] * (n + 1)
        for start, end in requests:
            freq[start] += 1
            freq[end + 1] -= 1
        for i in range(1, n):
            freq[i] += freq[i - 1]
        freq = freq[:n]
        freq.sort()
        nums.sort()
        result = 0
        for f, num in zip(freq, nums):
            result = (result + f * num) % MOD
        return result



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 贪心策略：频率越高的位置，应该放置越大的数字。
# 使用差分数组统计每个位置被查询的次数（freq[i] = 位置 i 被覆盖的请求数）。
# 对 freq 和 nums 分别排序，将最大的数分配给频率最高的位置。
# 最终结果 = sum(freq[i] * nums[i]) mod 1e9+7。
#
# 时间复杂度: O(N log N + R) — R 为请求数，排序主导
# 空间复杂度: O(N) — 频率数组
#
# 关键点:
# - 差分数组快速统计区间覆盖频率
# - 排序后贪心匹配：高频位置放大数据
# - 结果可能溢出，使用 mod












