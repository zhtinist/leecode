"""
LeetCode #2948 - Make Lexicographically Smallest Array by Swapping Elements
交换得到字典序最小的数组
https://leetcode.cn/problems/make-lexicographically-smallest-array-by-swapping-elements/

给你一个下标从 0 开始的 正整数 数组 `nums` 和一个 正整数 `limit` 。
在一次操作中，你可以选择任意两个下标 `i` 和 `j`，如果 满足 `|nums[i] - nums[j]| <= limit` ，则交换 `nums[i]` 和 `nums[j]` 。
返回执行任意次操作后能得到的 字典序最小的数组 。
如果在数组 `a` 和数组 `b` 第一个不同的位置上，数组 `a` 中的对应元素比数组 `b` 中的对应元素的字典序更小，则认为数组 `a` 就比数组 `b` 字典序更小。例如，数组 `[2,10,3]` 比数组 `[10,2,3]` 字典序更小，下标 `0` 处是两个数组第一个不同的位置，且 `2 < 10` 。

示例 1：
输入：nums = [1,5,3,9,8], limit = 2 输出：[1,3,5,8,9] 解释：执行 2 次操作： - 交换 nums[1] 和 nums[2] 。数组变为 [1,3,5,9,8] 。 - 交换 nums[3] 和 nums[4] 。数组变为 [1,3,5,8,9] 。 即便执行更多次操作，也无法得到字典序更小的数组。 注意，执行不同的操作也可能会得到相同的结果。
示例 2：
输入：nums = [1,7,6,18,2,1], limit = 3 输出：[1,6,7,18,1,2] 解释：执行 3 次操作： - 交换 nums[1] 和 nums[2] 。数组变为 [1,6,7,18,2,1] 。 - 交换 nums[0] 和 nums[4] 。数组变为 [2,6,7,18,1,1] 。 - 交换 nums[0] 和 nums[5] 。数组变为 [1,6,7,18,1,2] 。 即便执行更多次操作，也无法得到字典序更小的数组。
示例 3：
输入：nums = [1,7,28,19,10], limit = 3 输出：[1,7,28,19,10] 解释：[1,7,28,19,10] 是字典序最小的数组，因为不管怎么选择下标都无法执行操作。

提示：
`1 <= nums.length <= 10^5`
`1 <= nums[i] <= 10^9`
`1 <= limit <= 10^9`
"""

from typing import List, Optional


class Solution:
    def lexicographicallySmallestArray(self, nums: List[int],
                                        limit: int) -> List[int]:
        n = len(nums)
        pairs = sorted((v, i) for i, v in enumerate(nums))
        ans = [0] * n

        i = 0
        while i < n:
            j = i
            # Find the group of values within limit
            while j + 1 < n and pairs[j + 1][0] - pairs[j][0] <= limit:
                j += 1
            # Extract indices and values for this group
            indices = sorted(pairs[k][1] for k in range(i, j + 1))
            values = sorted(pairs[k][0] for k in range(i, j + 1))
            for idx, val in zip(indices, values):
                ans[idx] = val
            i = j + 1

        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Union Find, Array, Sorting
#
# 解题思路:
# 可交换的元素必须满足值差 <= limit，这意味着可以在每个"连通分量"内自由交换。
# 将元素按值排序，分组：连续元素的值差 <= limit 的属于同一组。
# 对每组，将组内元素按值排序后，按原始索引升序分配（最小值给最小索引），得到字典序最小结果。
#
# 时间复杂度: O(n log n)
# 空间复杂度: O(n)
#
# 关键点:
# - 值差 <= limit 定义了一个等价关系，形成连通分量
# - 排序后按差值分组，每组内可以任意排列
# - 字典序最小：每组内的最小值分配给最小原始索引
