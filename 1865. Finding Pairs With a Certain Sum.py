"""
LeetCode #1865 - Finding Pairs With a Certain Sum
找出和为指定值的下标对
https://leetcode.cn/problems/finding-pairs-with-a-certain-sum/

给你两个整数数组 `nums1` 和 `nums2` ，请你实现一个支持下述两类查询的数据结构：
累加 ，将一个正整数加到 `nums2` 中指定下标对应元素上。
计数 ，统计满足 `nums1[i] + nums2[j]` 等于指定值的下标对 `(i, j)` 数目（`0 <= i < nums1.length` 且 `0 <= j < nums2.length`）。
实现 `FindSumPairs` 类：
`FindSumPairs(int[] nums1, int[] nums2)` 使用整数数组 `nums1` 和 `nums2` 初始化 `FindSumPairs` 对象。
`void add(int index, int val)` 将 `val` 加到 `nums2[index]` 上，即，执行 `nums2[index] += val` 。
`int count(int tot)` 返回满足 `nums1[i] + nums2[j] == tot` 的下标对 `(i, j)` 数目。

示例：
输入： ["FindSumPairs", "count", "add", "count", "count", "add", "add", "count"] [[[1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4]], [7], [3, 2], [8], [4], [0, 1], [1, 1], [7]] 输出： [null, 8, null, 2, 1, null, null, 11]  解释： FindSumPairs findSumPairs = new FindSumPairs([1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4]); findSumPairs.count(7);  // 返回 8 ; 下标对 (2,2), (3,2), (4,2), (2,4), (3,4), (4,4) 满足 2 + 5 = 7 ，下标对 (5,1), (5,5) 满足 3 + 4 = 7 findSumPairs.add(3, 2); // 此时 nums2 = [1,4,5,4`,5,4`] findSumPairs.count(8);  // 返回 2 ；下标对 (5,2), (5,4) 满足 3 + 5 = 8 findSumPairs.count(4);  // 返回 1 ；下标对 (5,0) 满足 3 + 1 = 4 findSumPairs.add(0, 1); // 此时 nums2 = [`2`,4,5,4`,5,4`] findSumPairs.add(1, 1); // 此时 nums2 = [`2`,5,5,4`,5,4`] findSumPairs.count(7);  // 返回 11 ；下标对 (2,1), (2,2), (2,4), (3,1), (3,2), (3,4), (4,1), (4,2), (4,4) 满足 2 + 5 = 7 ，下标对 (5,3), (5,5) 满足 3 + 4 = 7

提示：
`1 <= nums1.length <= 1000`
`1 <= nums2.length <= 10^5`
`1 <= nums1[i] <= 10^9`
`1 <= nums2[i] <= 10^5`
`0 <= index < nums2.length`
`1 <= val <= 10^5`
`1 <= tot <= 10^9`
最多调用 `add` 和 `count` 函数各 `1000` 次
"""

from typing import List, Optional


class FindSumPairs:
    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.freq2 = {}
        for num in nums2:
            self.freq2[num] = self.freq2.get(num, 0) + 1

    def add(self, index: int, val: int) -> None:
        old_val = self.nums2[index]
        self.freq2[old_val] -= 1
        if self.freq2[old_val] == 0:
            del self.freq2[old_val]
        new_val = old_val + val
        self.nums2[index] = new_val
        self.freq2[new_val] = self.freq2.get(new_val, 0) + 1

    def count(self, tot: int) -> int:
        result = 0
        for num1 in self.nums1:
            complement = tot - num1
            if complement in self.freq2:
                result += self.freq2[complement]
        return result




# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Design, Array, Hash Table
#
# 解题思路:
# 使用哈希表存储 nums2 中每个值的出现频率。
# - count 操作：遍历 nums1，对于每个 num1，查找 tot - num1 在
#   nums2 中的出现次数，累加结果。O(n1)
# - add 操作：更新 nums2[index] 的值，同时更新哈希表中的频率。O(1)
# 由于 nums1 长度最多 1000，count 操作 O(1000) 可以接受。
#
# 时间复杂度: add: O(1), count: O(nums1.length)
# 空间复杂度: O(nums2.length) — 哈希表存储 nums2 的频率
#
# 关键点:
# - 类名是 FindSumPairs 不是 Solution
# - 使用哈希表优化 count 查询，避免每次 O(n1 * n2)
# - add 时需要更新旧值和新值的频率
# - nums1 长度较小（<=1000），直接遍历即可
