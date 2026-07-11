"""
LeetCode #3080 - Mark Elements on Array by Performing Queries
执行操作标记数组中的元素
https://leetcode.cn/problems/mark-elements-on-array-by-performing-queries/

给你一个长度为 `n` 下标从 0 开始的正整数数组 `nums` 。
同时给你一个长度为 `m` 的二维操作数组 `queries` ，其中 `queries[i] = [index_i, k_i]` 。
一开始，数组中的所有元素都 未标记 。
你需要依次对数组执行 `m` 次操作，第 `i` 次操作中，你需要执行：
如果下标 `index_i` 对应的元素还没标记，那么标记这个元素。
然后标记 `k_i` 个数组中还没有标记的 最小 元素。如果有元素的值相等，那么优先标记它们中下标较小的。如果少于 `k_i` 个未标记元素存在，那么将它们全部标记。
请你返回一个长度为 `m` 的数组 `answer` ，其中 `answer[i]`是第 `i` 次操作后数组中还没标记元素的 和 。

示例 1：

输入：nums = [1,2,2,1,2,3,1], queries = [[1,2],[3,3],[4,2]]
输出：[8,3,0]
解释：
我们依次对数组做以下操作：
标记下标为 `1` 的元素，同时标记 `2` 个未标记的最小元素。标记完后数组为 `nums = [1,2,2,1,2,3,1]` 。未标记元素的和为 `2 + 2 + 3 + 1 = 8` 。
标记下标为 `3` 的元素，由于它已经被标记过了，所以我们忽略这次标记，同时标记最靠前的 `3` 个未标记的最小元素。标记完后数组为 `nums = [1,2,2,1,2,3,1]` 。未标记元素的和为 `3` 。
标记下标为 `4` 的元素，由于它已经被标记过了，所以我们忽略这次标记，同时标记最靠前的 `2` 个未标记的最小元素。标记完后数组为 `nums = [1,2,2,1,2,3,1]` 。未标记元素的和为 `0` 。
示例 2：

输入：nums = [1,4,2,3], queries = [[0,1]]
输出：[7]
解释：我们执行一次操作，将下标为 `0` 处的元素标记，并且标记最靠前的 `1` 个未标记的最小元素。标记完后数组为 `nums = [1,4,2,3]` 。未标记元素的和为 `4 + 3 = 7` 。

提示：
`n == nums.length`
`m == queries.length`
`1 <= m <= n <= 10^5`
`1 <= nums[i] <= 10^5`
`queries[i].length == 2`
`0 <= index_i, k_i <= n - 1`
"""

from typing import List, Optional


class Solution:
    def unmarkedSumArray(
        self, nums: List[int], queries: List[List[int]]
    ) -> List[int]:
        """
        Sort by (value, index). Use a pointer to iterate through
        unmarked smallest elements. Track total unmarked sum.
        """
        n = len(nums)
        # Sorted list of (value, index)
        sorted_items = sorted((val, i) for i, val in enumerate(nums))
        marked = [False] * n
        ptr = 0  # pointer in sorted_items
        total = sum(nums)
        ans = []

        for idx, k in queries:
            # Mark specific index if not already marked
            if not marked[idx]:
                marked[idx] = True
                total -= nums[idx]

            # Mark k smallest unmarked elements
            while k > 0 and ptr < n:
                val, i = sorted_items[ptr]
                if not marked[i]:
                    marked[i] = True
                    total -= val
                    k -= 1
                ptr += 1

            ans.append(total)

        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Hash Table, Sorting, Simulation, Heap (Priority Queue)
#
# 解题思路:
# 将元素按 (值, 下标) 排序，使用指针遍历排序列表来找未标记的最小元素。
# 维护一个布尔数组记录已标记状态和未标记元素总和。
# 每次查询：先标记指定下标（若未标记），然后从排序列表中取前 k 个未标记的最小元素进行标记。
# 指针单调前进，每个元素最多被访问一次。
#
# 时间复杂度: O(n log n + m + n)，排序 + 查询遍历（每个元素至多一次）
# 空间复杂度: O(n)，排序列表和标记数组
#
# 关键点:
# - 排序列表中指针单调前进，保证 O(n) 的标记遍历
# - 优先标记值最小的元素，值相同时按下标小的优先（通过排序保证）
# - 维护未标记总和，每次标记后更新
