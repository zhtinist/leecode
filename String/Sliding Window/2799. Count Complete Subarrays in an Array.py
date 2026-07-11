"""
LeetCode #2799 - Count Complete Subarrays in an Array
统计完全子数组的数目
https://leetcode.cn/problems/count-complete-subarrays-in-an-array/

给你一个由 正 整数组成的数组 `nums` 。
如果数组中的某个子数组满足下述条件，则称之为 完全子数组 ：
子数组中 不同 元素的数目等于整个数组不同元素的数目。
返回数组中 完全子数组 的数目。
子数组 是数组中的一个连续非空序列。

示例 1：
输入：nums = [1,3,1,2,2] 输出：4 解释：完全子数组有：[1,3,1,2]、[1,3,1,2,2]、[3,1,2] 和 [3,1,2,2] 。
示例 2：
输入：nums = [5,5,5,5] 输出：10 解释：数组仅由整数 5 组成，所以任意子数组都满足完全子数组的条件。子数组的总数为 10 。

提示：
`1 <= nums.length <= 1000`
`1 <= nums[i] <= 2000`
"""

from typing import List, Optional


class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        total_distinct = len(set(nums))
        ans = 0
        left = 0
        freq = {}
        for right in range(n):
            freq[nums[right]] = freq.get(nums[right], 0) + 1
            while len(freq) == total_distinct:
                ans += n - right
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left += 1
        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Hash Table, Sliding Window
#
# 解题思路:
# 滑动窗口计数。首先计算整个数组的不同元素总数 total_distinct。
# 维护窗口 [left, right]，确保窗口内包含所有不同元素。当窗口满足条件时（len(freq) == total_distinct），
# 所有以 right 结尾、left 为起点的子数组都是完全子数组，共 n - right 个。
# 然后收缩 left（移除一个元素）继续寻找下一个满足条件的窗口。
#
# 时间复杂度: O(n)
# 空间复杂度: O(n)
#
# 关键点:
# - 窗口包含全部不同元素时，所有右边界 >= right 的扩展都是有效的完全子数组
# - 收缩左边界是为了找到下一个最小合法窗口
# - 使用哈希表 freq 维护窗口内各元素的频次
