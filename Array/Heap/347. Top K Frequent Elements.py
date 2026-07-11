"""
LeetCode #347 - Top K Frequent Elements
中文题名：前 K 个高频元素
https://leetcode.com/problems/top-k-frequent-elements/

Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:

Input: nums = [1], k = 1
Output: [1]

【中文翻译】
给定一个非空的整数数组，返回其中出现频率前 k 高的元素。

示例 1：

输入：nums = [1,1,1,2,2,3], k = 2
输出：[1,2]

示例 2：

输入：nums = [1], k = 1
输出：[1]
"""

from typing import List, Optional


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        import heapq
        # 统计频率
        count = Counter(nums)
        # 使用堆获取频率最高的 k 个元素
        return heapq.nlargest(k, count.keys(), key=count.get)










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 首先用 Counter 统计每个元素的出现频率，得到一个频率字典。
# 然后使用小顶堆（或直接使用 heapq.nlargest）找出频率最高的 k 个元素。
# heapq.nlargest(k, iterable, key=...) 会维护一个大小为 k 的小顶堆，遍历所有元素后将堆中元素返回。
# 另一种方法：桶排序——创建一个长度为 n+1 的桶数组，桶的下标表示频率，桶中存放具有该频率的元素，
# 然后从高频率向低频率遍历桶，收集 k 个元素即可。桶排序可以做到 O(n) 时间。
# 此处使用堆方法，代码简洁且时间复杂度 O(n log k) 在 k << n 时接近线性。
#
# 时间复杂度: O(n log k) - 统计频率 O(n)，堆操作 O(n log k)；若使用桶排序则为 O(n)
# 空间复杂度: O(n) - Counter 字典和堆各 O(n)
#
# 关键点:
# - 使用 Counter 或字典统计频率
# - heapq.nlargest 自动维护大小为 k 的堆，比手动建堆更简洁
# - 桶排序是 O(n) 的替代方案，适合 k 接近 n 的场景
# - 题目保证答案唯一，即前 k 高频元素不存在并列争议
