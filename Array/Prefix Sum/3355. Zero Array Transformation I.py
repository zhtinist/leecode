"""
LeetCode #3355 - Zero Array Transformation I
零数组变换 I
https://leetcode.cn/problems/zero-array-transformation-i/

给定一个长度为 `n` 的整数数组 `nums` 和一个二维数组 `queries`，其中 `queries[i] = [l_i, r_i]`。
对于每个查询 `queries[i]`：
在 `nums` 的下标范围 `[l_i, r_i]` 内选择一个下标 子集。
将选中的每个下标对应的元素值减 1。
零数组 是指所有元素都等于 0 的数组。
如果在按顺序处理所有查询后，可以将 `nums` 转换为 零数组 ，则返回 `true`，否则返回 `false`。

示例 1：

输入： nums = [1,0,1], queries = [[0,2]]
输出： true
解释：
对于 i = 0：
选择下标子集 `[0, 2]` 并将这些下标处的值减 1。
数组将变为 `[0, 0, 0]`，这是一个零数组。
示例 2：

输入： nums = [4,3,2,1], queries = [[1,3],[0,2]]
输出： false
解释：
对于 i = 0：
选择下标子集 `[1, 2, 3]` 并将这些下标处的值减 1。
数组将变为 `[4, 2, 1, 0]`。
对于 i = 1：
选择下标子集 `[0, 1, 2]` 并将这些下标处的值减 1。
数组将变为 `[3, 1, 0, 0]`，这不是一个零数组。

提示：
`1 <= nums.length <= 10^5`
`0 <= nums[i] <= 10^5`
`1 <= queries.length <= 10^5`
`queries[i].length == 2`
`0 <= l_i <= r_i < nums.length`
"""

from typing import List, Optional


class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        diff = [0] * (n + 1)
        for l, r in queries:
            diff[l] += 1
            diff[r + 1] -= 1

        cur = 0
        for i in range(n):
            cur += diff[i]
            if cur < nums[i]:
                return False
        return True



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Prefix Sum
#
# 解题思路:
# 对于每个查询[l,r]，可以在区间内选择任意子集减1。因此每个位置i可以被覆盖它的查询
# 贡献至多减1。使用差分数组计算每个位置被查询覆盖的次数，检查是否>=nums[i]。
#
# 时间复杂度: O(n + q)
# 空间复杂度: O(n)
#
# 关键点:
# - 每个查询对每个位置最多贡献1
# - 差分数组统计覆盖次数
