"""
LeetCode #220 - Contains Duplicate III
中文题名：存在重复元素 III
https://leetcode.com/problems/contains-duplicate-iii/

Given an array of integers, find out whether there are two distinct indices *i* and
*j* in the array such that the absolute difference between nums[i] and
nums[j] is at most *t* and the absolute difference between *i* and
*j* is at most *k*.

Example 1:

Input: nums = [1,2,3,1], k = 3, t = 0
Output: true

Example 2:

Input: nums = [1,0,1,1], k = 1, t = 2
Output: true

Example 3:

Output: false

【中文翻译】
给你一个整数数组 nums 和两个整数 k 和 t。判断是否存在两个不同的索引 i 和 j，使得 abs(nums[i] - nums[j]) <= t，同时又满足 abs(i - j) <= k。

示例 1：

输入：nums = [1,2,3,1], k = 3, t = 0
输出：true

示例 2：

输入：nums = [1,0,1,1], k = 1, t = 2
输出：true

示例 3：

输入：nums = [1,5,9,1,5,9], k = 2, t = 3
输出：false
"""

from typing import List, Optional


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if t < 0:
            return False

        buckets: dict[int, int] = {}
        width = t + 1

        for i, num in enumerate(nums):
            bucket = num // width

            if bucket in buckets:
                return True
            if bucket - 1 in buckets and abs(num - buckets[bucket - 1]) <= t:
                return True
            if bucket + 1 in buckets and abs(num - buckets[bucket + 1]) <= t:
                return True

            buckets[bucket] = num

            if i >= k:
                old_bucket = nums[i - k] // width
                del buckets[old_bucket]

        return False












# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Hard
# Paid Only: No
#
# 解题思路:
# 桶排序(Bucket Sort) + 滑动窗口方法。
# 核心洞察：若两个数的差 <= t，则它们要么在同一个桶中，要么在相邻的桶中。
# 1. 桶的宽度设为 t + 1（确保桶内任意两数之差 <= t）。
# 2. 对于每个元素 num，计算桶编号 bucket = num // (t + 1)。
# 3. 检查当前桶是否已有元素 → 直接返回 True。
# 4. 检查相邻桶(前一个和后一个)中的元素，若差值 <= t → 返回 True。
# 5. 将该元素放入对应桶中。
# 6. 维护大小为 k 的滑动窗口：当 i >= k 时，移除 nums[i-k] 所在桶的元素。
#
# 时间复杂度: O(n) - 每个元素只需常数次桶操作
# 空间复杂度: O(k) - 最多存储 k+1 个桶
#
# 关键点:
# - 桶宽度 t+1 确保桶内任意两元素差值 <= t
# - 每个桶最多保留一个元素(因为若有第二个，早已返回 True)
# - 使用整除分配桶号，需注意 Python 对负数的地板除行为
# - 边界条件：t < 0 直接返回 False
