"""
LeetCode #1906 - Minimum Absolute Difference Queries
查询差绝对值的最小值
https://leetcode.cn/problems/minimum-absolute-difference-queries/

一个数组 `a` 的 差绝对值的最小值 定义为：`0 |a[i] - a[j]|` 的 最小值。如果 `a` 中所有元素都 相同 ，那么差绝对值的最小值为 `-1` 。
比方说，数组 `[5,2,3,7,2]` 差绝对值的最小值是 `|2 - 3| = 1` 。注意答案不为 `0` ，因为 `a[i]` 和 `a[j]` 必须不相等。
给你一个整数数组 `nums` 和查询数组 `queries` ，其中 `queries[i] = [l_i, r_i]` 。对于每个查询 `i` ，计算 子数组 `nums[l_i...r_i]` 中 差绝对值的最小值 ，子数组 `nums[l_i...r_i]` 包含 `nums` 数组（下标从 0 开始）中下标在 `l_i` 和 `r_i` 之间的所有元素（包含 `l_i` 和 `r_i` 在内）。
请你返回 `ans` 数组，其中 `ans[i]` 是第 `i` 个查询的答案。
子数组 是一个数组中连续的一段元素。
`|x|` 的值定义为：
如果 `x >= 0` ，那么值为 `x` 。
如果 `x < 0` ，那么值为 `-x` 。

示例 1：
输入：nums = [1,3,4,8], queries = [[0,1],[1,2],[2,3],[0,3]] 输出：[2,1,4,1] 解释：查询结果如下： - queries[0] = [0,1]：子数组是 [1,3] ，差绝对值的最小值为 |1-3| = 2 。 - queries[1] = [1,2]：子数组是 [3,4] ，差绝对值的最小值为 |3-4| = 1 。 - queries[2] = [2,3]：子数组是 [4,8] ，差绝对值的最小值为 |4-8| = 4 。 - queries[3] = [0,3]：子数组是 [1,3,4,8] ，差的绝对值的最小值为 |3-4| = 1 。
示例 2：
输入：nums = [4,5,2,2,7,10], queries = [[2,3],[0,2],[0,5],[3,5]] 输出：[-1,1,1,3] 解释：查询结果如下： - queries[0] = [2,3]：子数组是 [2,2] ，差绝对值的最小值为 -1 ，因为所有元素相等。 - queries[1] = [0,2]：子数组是 [4,5,2] ，差绝对值的最小值为 |4-5| = 1 。 - queries[2] = [0,5]：子数组是 [4,5,2,2,7,10] ，差绝对值的最小值为 |4-5| = 1 。 - queries[3] = [3,5]：子数组是 [2,7,10] ，差绝对值的最小值为 |7-10| = 3 。

提示：
`2 <= nums.length <= 10^5`
`1 <= nums[i] <= 100`
`1 <= queries.length <= 2 * 10^4`
`0 <= l_i < r_i < nums.length`
"""

from typing import List, Optional


class Solution:
    def minDifference(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        # Since 1 <= nums[i] <= 100, use prefix counts for each value
        MAX_VAL = 100
        n = len(nums)

        # pref[i][v] = count of value v in nums[0..i-1]
        pref = [[0] * (MAX_VAL + 1) for _ in range(n + 1)]

        for i in range(n):
            for v in range(1, MAX_VAL + 1):
                pref[i + 1][v] = pref[i][v]
            pref[i + 1][nums[i]] += 1

        ans = []
        for l, r in queries:
            # Find all values that appear in nums[l..r]
            present = []
            for v in range(1, MAX_VAL + 1):
                if pref[r + 1][v] - pref[l][v] > 0:
                    present.append(v)

            if len(present) < 2:
                ans.append(-1)
            else:
                min_diff = float('inf')
                for i in range(1, len(present)):
                    min_diff = min(min_diff, present[i] - present[i - 1])
                ans.append(min_diff)

        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Prefix Sum
#
# 解题思路:
# 由于 nums[i] 的值域很小（1到100），可以使用前缀计数数组。
# 1. 构建前缀计数数组 pref，pref[i][v] 表示前 i 个元素中值 v 的出现次数。
# 2. 对于每个查询 [l, r]，通过前缀和差值得出区间内每个值的出现次数。
# 3. 收集所有出现的值（已自然排序），计算相邻值的最小差值。
# 4. 如果区间内不同值少于2个，返回 -1。
#
# 时间复杂度: O((n + q) * 100) — n 和 q 各最多 10^5, 但值域只有 100
# 空间复杂度: O(n * 100) — 前缀计数数组
#
# 关键点:
# - 关键观察：nums[i] <= 100，值域很小
# - 前缀计数使区间查询 O(100)
# - 相邻值的差自然就是最小值（因为已经排序）
# - 如果所有元素相同，返回 -1
