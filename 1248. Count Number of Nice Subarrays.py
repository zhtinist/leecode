"""
LeetCode #1248 - Count Number of Nice Subarrays
中文题名：统计「优美子数组」
https://leetcode.com/problems/count-number-of-nice-subarrays/

Given an array of integers `nums` and an integer `k`.
A subarray is called nice if there
are `k` odd numbers on it.

Return the number of nice sub-arrays.

Example 1:

Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].

Example 2:

Input: nums = [2,4,6], k = 1
Output: 0
Explanation: There is no odd numbers in the array.

Example 3:

Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
Output: 16

Constraints:

`1 <= nums.length <= 50000`

`1 <= nums[i] <= 10^5`

`1 <= k <= nums.length`

【中文翻译】
给你一个整数数组 `nums` 和一个整数 `k`。如果一个子数组中恰好有 `k` 个奇数，我们就称这个子数组为「优美子数组」。

请返回优美子数组的数目。

示例 1：

输入：nums = [1,1,2,1,1], k = 3
输出：2
解释：包含 3 个奇数的子数组是 [1,1,2,1] 和 [1,2,1,1]。

示例 2：

输入：nums = [2,4,6], k = 1
输出：0
解释：数组中没有奇数，所以不存在恰好包含 1 个奇数的子数组。

示例 3：

输入：nums = [2,2,2,1,2,2,1,2,2,2], k = 2
输出：16

约束条件：

`1 <= nums.length <= 50000`

`1 <= nums[i] <= 10^5`

`1 <= k <= nums.length`
"""

from typing import List, Optional


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        from collections import defaultdict

        # Transform: odd -> 1, even -> 0
        # Then problem becomes: count subarrays with sum == k
        count = defaultdict(int)
        count[0] = 1
        prefix = 0
        res = 0

        for num in nums:
            prefix += (num % 2)  # 1 if odd, 0 if even
            res += count[prefix - k]
            count[prefix] += 1

        return res










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 前缀和 + 哈希表。将问题转化为「和为 K 的子数组个数」。
# 1. 转化：将奇数视为 1，偶数视为 0。问题变为：求子数组和为 k 的个数。
# 2. 使用前缀和：prefix[i] 表示前 i 个元素中奇数的个数。
# 3. 对于当前 prefix，需要找之前有多少个 prefix_prev 满足 prefix - prefix_prev = k，
#    即 prefix_prev = prefix - k。
# 4. 用哈希表记录每个前缀和出现的次数，O(1) 查询。
# 5. 也可以使用 atMost(k) - atMost(k-1) 的滑动窗口方法。
#
# 时间复杂度: O(N)，一次遍历
# 空间复杂度: O(N)，哈希表最坏存储 N 个不同的前缀和
#
# 关键点:
# - 将奇数/偶数映射为 1/0 转化为前缀和计数问题
# - 哈希表初始化为 count[0] = 1（空前缀和为 0 出现一次）
# - 当前前缀和为 prefix 时，寻找前缀和为 prefix - k 的位置个数
# - 此题也可用 exactly(k) = atMost(k) - atMost(k-1) 的滑动窗口方法
