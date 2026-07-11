"""
LeetCode #442 - Find All Duplicates in an Array
中文题名：数组中重复的数据
https://leetcode.com/problems/find-all-duplicates-in-an-array/

Given an array of integers, 1 <= a[i] <= n (n = size of array), some
elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]

【中文翻译】
给定一个整数数组，1 <= a[i] <= n（n 为数组大小），有些元素出现两次，其他出现一次。
找出所有出现两次的元素。能否不使用额外空间、O(n) 时间复杂度完成？

示例：
    输入：[4,3,2,7,8,2,3,1]
    输出：[2,3]
"""

from typing import List, Optional


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []

        for num in nums:
            idx = abs(num) - 1
            if nums[idx] < 0:
                result.append(abs(num))  # Already negative → seen before → duplicate
            else:
                nums[idx] = -nums[idx]   # Mark as seen by negating

        return result


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 原地标记法。利用数组元素范围 1 <= a[i] <= n 的特性，将数组本身用作哈希表。
#
# 对于每个元素 num = |nums[i]|：
# 1. 将 num 作为索引 idx = num - 1
# 2. 检查 nums[idx] 是否为负数：
#    - 如果是负数，说明之前已经遇到过 num（之前已将此处标记负），num 是重复元素
#    - 如果是正数，将其取负标记为"已见过"
#
# 例如 [4,3,2,7,8,2,3,1]：
# - 遇到 4：标记 nums[3]=-7
# - 遇到 3：标记 nums[2]=-2
# - 遇到 2：标记 nums[1]=-3
# - 遇到 7：标记 nums[6]=-3
# - 遇到 8：标记 nums[7]=-1
# - 遇到 2：idx=1，nums[1]=-3（负数），发现重复 2
# - 遇到 3：idx=2，nums[2]=-2（负数），发现重复 3
#
# 时间复杂度: O(N) — 一次遍历
# 空间复杂度: O(1) — 输出数组不计入额外空间，原地标记不使用额外空间
#
# 关键点:
# - 利用值范围 [1, n] 将数组下标作为哈希键
# - 通过取负数标记访问过的元素（不丢失原始值信息，因为可以用 abs 还原）
# - 当发现对应位置已为负数时，当前数字就是重复的
