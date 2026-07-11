"""
LeetCode #2593 - Find Score of an Array After Marking All Elements
标记所有元素后数组的分数
https://leetcode.cn/problems/find-score-of-an-array-after-marking-all-elements/

给你一个数组 `nums` ，它包含若干正整数。
一开始分数 `score = 0` ，请你按照下面算法求出最后分数：
从数组中选择最小且没有被标记的整数。如果有相等元素，选择下标最小的一个。
将选中的整数加到 `score` 中。
标记 被选中元素，如果有相邻元素，则同时标记 与它相邻的两个元素 。
重复此过程直到数组中所有元素都被标记。
请你返回执行上述算法后最后的分数。

示例 1：
输入：nums = [2,1,3,4,5,2] 输出：7 解释：我们按照如下步骤标记元素： - 1 是最小未标记元素，所以标记它和相邻两个元素：[2,1,3,4,5,2] 。 - 2 是最小未标记元素，所以标记它和左边相邻元素：[2,1,3,4,5,2] 。 - 4 是仅剩唯一未标记的元素，所以我们标记它：[2,1,3,4,5,2] 。 总得分为 1 + 2 + 4 = 7 。
示例 2：
输入：nums = [2,3,5,1,3,2] 输出：5 解释：我们按照如下步骤标记元素： - 1 是最小未标记元素，所以标记它和相邻两个元素：[2,3,5,1,3,2] 。 - 2 是最小未标记元素，由于有两个 2 ，我们选择最左边的一个 2 ，也就是下标为 0 处的 2 ，以及它右边相邻的元素：[2,3,5,1,3,2] 。 - 2 是仅剩唯一未标记的元素，所以我们标记它：[2,3,5,1,3,2] 。 总得分为 1 + 2 + 2 = 5 。

提示：
`1 <= nums.length <= 10^5`
`1 <= nums[i] <= 10^6`
"""

from typing import List, Optional


class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)
        marked = [False] * n
        pairs = sorted((v, i) for i, v in enumerate(nums))
        score = 0
        for v, i in pairs:
            if marked[i]:
                continue
            score += v
            marked[i] = True
            if i > 0:
                marked[i - 1] = True
            if i < n - 1:
                marked[i + 1] = True
        return score



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Hash Table, Sorting, Simulation, Heap (Priority Queue)
#
# 解题思路:
# 将元素按(值,下标)排序，按顺序处理。维护marked数组标记已被选择的元素及其邻居。
# 遍历排序后的列表，若当前下标未被标记，则将值累加到分数，并标记该位置及其左右邻居。
# 已标记的元素自动跳过。贪心选最小未标记元素的策略天然保证最优。
#
# 时间复杂度: O(N log N)
# 空间复杂度: O(N)
#
# 关键点:
# - 排序确保按值从小到大处理，相等时按下标排序
# - marked数组标记"已被影响"的元素，包括被邻居标记的
# - 贪心选最小，不需要动态调整
