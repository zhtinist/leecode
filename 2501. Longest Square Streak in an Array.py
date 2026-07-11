"""
LeetCode #2501 - Longest Square Streak in an Array
数组中最长的方波
https://leetcode.cn/problems/longest-square-streak-in-an-array/

给你一个整数数组 `nums` 。如果 `nums` 的子序列满足下述条件，则认为该子序列是一个 方波 ：
子序列的长度至少为 `2` ，并且
将子序列从小到大排序 之后 ，除第一个元素外，每个元素都是前一个元素的 平方 。
返回 `nums` 中 最长方波 的长度，如果不存在 方波 则返回 `-1` 。
子序列 也是一个数组，可以由另一个数组删除一些或不删除元素且不改变剩余元素的顺序得到。

示例 1 ：
输入：nums = [4,3,6,16,8,2] 输出：3 解释：选出子序列 [4,16,2] 。排序后，得到 [2,4,16] 。 - 4 = 2 * 2. - 16 = 4 * 4. 因此，[4,16,2] 是一个方波. 可以证明长度为 4 的子序列都不是方波。
示例 2 ：
输入：nums = [2,3,5,6,7] 输出：-1 解释：nums 不存在方波，所以返回 -1 。

提示：
`2 <= nums.length <= 10^5`
`2 <= nums[i] <= 10^5`
"""

from typing import List, Optional


class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        num_set = set(nums)
        nums_sorted = sorted(num_set)
        max_len = -1
        visited = set()

        for x in nums_sorted:
            if x in visited:
                continue
            length = 0
            cur = x
            while cur in num_set:
                visited.add(cur)
                length += 1
                cur = cur * cur
                if cur > 10**5:
                    break
            if length >= 2:
                max_len = max(max_len, length)

        return max_len



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Hash Table, Binary Search, Dynamic Programming, Sorting
#
# 解题思路:
# 将数组元素放入集合，排序后遍历。对于每个未访问的元素，不断检查其平方是否在集合中，
# 记录连续平方链的长度。若长度>=2则更新最大长度。使用visited集合避免重复计算。
#
# 时间复杂度: O(N log N)
# 空间复杂度: O(N)
#
# 关键点:
# - 平方链最多有5个元素（因为2^(2^5) > 10^5），所以while循环效率很高
# - 用visited集合避免从同一个元素开始重复查找
# - 只需考虑已排序的集合元素，而不是原始数组
