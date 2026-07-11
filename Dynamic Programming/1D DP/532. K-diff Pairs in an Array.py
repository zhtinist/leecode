"""
LeetCode #532 - K-diff Pairs in an Array
中文题名：数组中的K-diff数对
https://leetcode.com/problems/k-diff-pairs-in-an-array/

Given an array of integers and an integer k, you need to find the number of
unique k-diff pairs in the array. Here a k-diff pair is defined as an integer
pair (i, j), where i and j are both numbers in the array and their absolute difference is
k.

Example 1:

Input: [3, 1, 4, 1, 5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.

Example 2:

Input:[1, 2, 3, 4, 5], k = 1
Output: 4
Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).

Example 3:

Input: [1, 3, 1, 5, 4], k = 0
Output: 1
Explanation: There is one 0-diff pair in the array, (1, 1).

Note:

The pairs (i, j) and (j, i) count as the same pair.

The length of the array won't exceed 10,000.

All the integers in the given input belong to the range: [-1e7, 1e7].

【中文翻译】
给定一个整数数组和一个整数 k，找出数组中唯一 k-diff 数对的数量。k-diff 数对定义为
数组中两个整数 (i, j)，满足它们的绝对差为 k（即 |i - j| == k），且 (i, j) 和 (j, i)
视为同一数对。

示例 1：
    输入：[3, 1, 4, 1, 5], k = 2
    输出：2
    解释：有两个 2-diff 数对，(1, 3) 和 (3, 5)。虽然输入中有两个 1，但只需返回唯一数对的数量。

示例 2：
    输入：[1, 2, 3, 4, 5], k = 1
    输出：4
    解释：有四个 1-diff 数对，(1, 2), (2, 3), (3, 4), (4, 5)。

示例 3：
    输入：[1, 3, 1, 5, 4], k = 0
    输出：1
    解释：有一个 0-diff 数对，(1, 1)。只有出现至少两次的数字才能形成 k=0 的数对。

说明：数组长度不超过 10000。所有整数范围 [-1e7, 1e7]。
"""

from collections import Counter
from typing import List, Optional


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0

        counter = Counter(nums)
        count = 0

        for num in counter:
            if k == 0:
                # For k == 0, count numbers that appear at least twice
                if counter[num] >= 2:
                    count += 1
            else:
                # For k > 0, check if num + k exists
                if num + k in counter:
                    count += 1

        return count


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用哈希表（Counter）统计每个数字的出现次数，然后遍历哈希表中的唯一数字。
# 分两种情况处理：当 k == 0 时，数对要求 |i - j| == 0 即 i == j，因此只需统计出现次数
# >= 2 的数字个数即可。当 k > 0 时，对每个数字 num，检查 num + k 是否也存在于哈希表中
# （这样 (num, num+k) 构成一个有效的 k-diff 数对，且不会重复计数，因为每个数对只遍历一次
# 较小的那个数）。注意 k < 0 时直接返回 0，因为绝对差不可能为负。
#
# 时间复杂度: O(N) — 构建 Counter 一次遍历，遍历唯一键一次
# 空间复杂度: O(N) — Counter 存储每个数字的频次
#
# 关键点:
# - k == 0 和 k > 0 需分开处理
# - 只需检查 num + k 即可，不会重复计数（因为遍历 num 时 num+k 更大，反之亦然）
# - 用 Counter 去重并保留频次，天然处理了唯一数对的要求
