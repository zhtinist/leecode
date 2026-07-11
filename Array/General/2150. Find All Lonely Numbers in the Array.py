"""
LeetCode #2150 - Find All Lonely Numbers in the Array
找出数组中的所有孤独数字
https://leetcode.cn/problems/find-all-lonely-numbers-in-the-array/

给你一个整数数组 `nums` 。如果数字 `x` 在数组中仅出现 一次 ，且没有 相邻 数字（即，`x + 1` 和 `x - 1`）出现在数组中，则认为数字 `x` 是 孤独数字 。
返回 `nums` 中的 所有 孤独数字。你可以按 任何顺序 返回答案。

示例 1：
输入：nums = [10,6,5,8] 输出：[10,8] 解释： - 10 是一个孤独数字，因为它只出现一次，并且 9 和 11 没有在 nums 中出现。 - 8 是一个孤独数字，因为它只出现一次，并且 7 和 9 没有在 nums 中出现。 - 5 不是一个孤独数字，因为 6 出现在 nums 中，反之亦然。 因此，nums 中的孤独数字是 [10, 8] 。 注意，也可以返回 [8, 10] 。
示例 2：
输入：nums = [1,3,5,3] 输出：[1,5] 解释： - 1 是一个孤独数字，因为它只出现一次，并且 0 和 2 没有在 nums 中出现。 - 5 是一个孤独数字，因为它只出现一次，并且 4 和 6 没有在 nums 中出现。 - 3 不是一个孤独数字，因为它出现两次。 因此，nums 中的孤独数字是 [1, 5] 。 注意，也可以返回 [5, 1] 。

提示：
`1 <= nums.length <= 10^5`
`0 <= nums[i] <= 10^6`
"""

from typing import List, Optional


class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        from collections import Counter
        count = Counter(nums)
        result = []
        for x in nums:
            if count[x] == 1 and count[x - 1] == 0 and count[x + 1] == 0:
                result.append(x)
        return result



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Hash Table, Counting
#
# 解题思路:
# 使用 Counter 统计每个数字的出现次数。然后遍历数组，对于每个数字 x：
#   1. count[x] == 1：x 必须只出现一次
#   2. count[x - 1] == 0 且 count[x + 1] == 0：相邻数字都不存在
# 同时满足以上条件则为"孤独数字"，加入结果列表。
#
# 时间复杂度: O(N)，统计频率 O(N)，遍历检查 O(N)。
# 空间复杂度: O(N)，用于 Counter 存储频率信息。
#
# 关键点:
# - Counter 统一统计频率，O(1) 时间查询相邻数字是否存在
# - 题目允许任意顺序返回结果，不需要额外排序
