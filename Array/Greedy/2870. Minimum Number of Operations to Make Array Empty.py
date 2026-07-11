"""
LeetCode #2870 - Minimum Number of Operations to Make Array Empty
使数组为空的最少操作次数
https://leetcode.cn/problems/minimum-number-of-operations-to-make-array-empty/

给你一个下标从 0 开始的正整数数组 `nums` 。
你可以对数组执行以下两种操作 任意次 ：
从数组中选择 两个 值 相等 的元素，并将它们从数组中 删除 。
从数组中选择 三个 值 相等 的元素，并将它们从数组中 删除 。
请你返回使数组为空的 最少 操作次数，如果无法达成，请返回 `-1` 。

示例 1：
输入：nums = [2,3,3,2,2,4,2,3,4] 输出：4 解释：我们可以执行以下操作使数组为空： - 对下标为 0 和 3 的元素执行第一种操作，得到 nums = [3,3,2,4,2,3,4] 。 - 对下标为 2 和 4 的元素执行第一种操作，得到 nums = [3,3,4,3,4] 。 - 对下标为 0 ，1 和 3 的元素执行第二种操作，得到 nums = [4,4] 。 - 对下标为 0 和 1 的元素执行第一种操作，得到 nums = [] 。 至少需要 4 步操作使数组为空。
示例 2：
输入：nums = [2,1,2,2,3,3] 输出：-1 解释：无法使数组为空。

提示：
`2 <= nums.length <= 10^5`
`1 <= nums[i] <= 10^6`
"""

from typing import List, Optional


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        from collections import Counter
        freq = Counter(nums)
        ans = 0
        for c in freq.values():
            if c == 1:
                return -1
            ans += (c + 2) // 3  # ceil(c / 3)
        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Array, Hash Table, Counting
#
# 解题思路:
# 统计每个元素的出现次数。每次操作可以删除2个或3个相同元素，因此对于每种元素，需要将其计数分解为2和3的组合。
# 如果计数为1则无法操作返回-1。对于计数c>=2，最小操作次数为ceil(c/3) = (c+2)//3。
# 所有元素的次数可以独立处理，结果为各元素所需操作次数之和。
#
# 时间复杂度: O(n)
# 空间复杂度: O(n)
#
# 关键点:
# - 每种元素的次数独立处理，用2和3的组合最小化操作次数
# - ceil(c/3) = (c+2)//3 对于c>=2有效
# - 计数为1时无法删除（没有1个元素的操作），返回-1
