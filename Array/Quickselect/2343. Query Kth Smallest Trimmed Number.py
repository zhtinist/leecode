"""
LeetCode #2343 - Query Kth Smallest Trimmed Number
裁剪数字后查询第 K 小的数字
https://leetcode.cn/problems/query-kth-smallest-trimmed-number/

给你一个下标从 0 开始的字符串数组 `nums` ，其中每个字符串 长度相等 且只包含数字。
再给你一个下标从 0 开始的二维整数数组 `queries` ，其中 `queries[i] = [k_i, trim_i]` 。对于每个 `queries[i]` ，你需要：
将 `nums` 中每个数字 裁剪 到剩下 最右边 `trim_i` 个数位。
在裁剪过后的数字中，找到 `nums` 中第 `k_i` 小数字对应的 下标 。如果两个裁剪后数字一样大，那么下标 更小 的数字视为更小的数字。
将 `nums` 中每个数字恢复到原本字符串。
请你返回一个长度与 `queries` 相等的数组 `answer`，其中 `answer[i]`是第 `i` 次查询的结果。
提示：
裁剪到剩下最右边 `x` 个数位的意思是不断删除最左边的数位，直到剩下 `x` 个数位。
`nums` 中的字符串可能会有前导 0 。

示例 1：
输入：nums = ["102","473","251","814"], queries = [[1,1],[2,3],[4,2],[1,2]] 输出：[2,2,1,0] 解释： 1. 裁剪到只剩 1 个数位后，nums = ["2","3","1","4"] 。最小的数字是 1 ，下标为 2 。 2. 裁剪到剩 3 个数位后，nums 没有变化。第 2 小的数字是 251 ，下标为 2 。 3. 裁剪到剩 2 个数位后，nums = ["02","73","51","14"] 。第 4 小的数字是 73 ，下标为 1 。 4. 裁剪到剩 2 个数位后，最小数字是 2 ，下标为 0 。    注意，裁剪后数字 "02" 值为 2 。
示例 2：
输入：nums = ["24","37","96","04"], queries = [[2,1],[2,2]] 输出：[3,0] 解释： 1. 裁剪到剩 1 个数位，nums = ["4","7","6","4"] 。第 2 小的数字是 4 ，下标为 3 。    有两个 4 ，下标为 0 的 4 视为小于下标为 3 的 4 。 2. 裁剪到剩 2 个数位，nums 不变。第二小的数字是 24 ，下标为 0 。

提示：
`1 <= nums.length <= 100`
`1 <= nums[i].length <= 100`
`nums[i]` 只包含数字。
所有 `nums[i].length` 的长度 相同 。
`1 <= queries.length <= 100`
`queries[i].length == 2`
`1 <= k_i <= nums.length`
`1 <= trim_i <= nums[0].length`

进阶：你能使用 基数排序算法 解决此问题吗？这种解法的复杂度又是多少？
"""

from typing import List, Optional


class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        answer = []
        for k, trim in queries:
            # Create list of (trimmed_string, original_index)
            trimmed = [(num[-trim:], i) for i, num in enumerate(nums)]
            # Sort by trimmed string then by original index (for tie-breaking)
            trimmed.sort(key=lambda x: (x[0], x[1]))
            # k is 1-indexed
            answer.append(trimmed[k - 1][1])
        return answer



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, String, Divide and Conquer, Quickselect, Radix Sort, Sorting, Heap (Priority Queue)
#
# 解题思路:
# 对于每个查询 [k, trim]，将 nums 中每个数字裁剪到最右边 trim 个数位（num[-trim:]）。
# 然后按 (裁剪后的字符串, 原始下标) 排序，取第 k 小的原始下标（k 从 1 开始）。
# 注意题目要求：如果两个裁剪后数字一样大，下标更小的视为更小，因此排序 key 需要包含下标。
#
# 时间复杂度: O(Q * N * log N) 其中 Q = len(queries), N = len(nums)
# 空间复杂度: O(N) 用于存储每个查询的裁剪结果
#
# 关键点:
# - 字符串切片 num[-trim:] 完成裁剪
# - 排序 key 为 (trimmed_string, original_index) 以处理平局
# - k 是 1-indexed，需要取 trimmed[k-1][1]
