"""
LeetCode #2856 - Minimum Array Length After Pair Removals
删除数对后的最小数组长度
https://leetcode.cn/problems/minimum-array-length-after-pair-removals/

给你一个下标从 0 开始的 非递减 整数数组 `nums` 。
你可以执行以下操作任意次：
选择 两个 下标 `i` 和 `j` ，满足 `nums[i] < nums[j]` 。
将 `nums` 中下标在 `i` 和 `j` 处的元素删除。剩余元素按照原来的顺序组成新的数组，下标也重新从 0 开始编号。
请你返回一个整数，表示执行以上操作任意次后（可以执行 0 次），`nums` 数组的 最小 数组长度。

示例 1：

输入：nums = [1,2,3,4]
输出：0
解释：

示例 2：

输入：nums = [1,1,2,2,3,3]
输出：0
解释：

示例 3：

输入：nums = [1000000000,1000000000]
输出：2
解释：
由于两个数字相等，不能删除它们。
示例 4：

输入：nums = [2,3,4,4,4]
输出：1
解释：

提示：
`1 <= nums.length <= 10^5`
`1 <= nums[i] <= 10^9`
`nums` 是 非递减 数组。
"""

from typing import List, Optional


class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        from collections import Counter
        n = len(nums)
        freq = Counter(nums)
        max_freq = max(freq.values())
        # If the most frequent element appears more than half the time,
        # the excess cannot be paired
        if max_freq > n - max_freq:
            return 2 * max_freq - n
        # Otherwise we can pair all but possibly one (if n is odd)
        return n % 2



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Array, Hash Table, Two Pointers, Binary Search, Counting
#
# 解题思路:
# 统计出现频率最高的元素次数 max_freq。如果 max_freq 超过数组长度的一半，那么多出的部分（max_freq - (n - max_freq)）
# 无法被配对删除（因为相同元素不能配对）。否则，最多只会有 n%2 个元素剩余（偶数长度可以全部删除，奇数长度剩1个）。
#
# 时间复杂度: O(n)
# 空间复杂度: O(n)
#
# 关键点:
# - 相同元素之间不能配对（需要严格小于），因此最频繁的元素是瓶颈
# - 答案 = max(2 * max_freq - n, n % 2)
# - 数组是非递减的，简化了分析但不需要用到
