"""
LeetCode #3653 - XOR After Range Multiplication Queries I
区间乘法查询后的异或 I
https://leetcode.cn/problems/xor-after-range-multiplication-queries-i/

给你一个长度为 `n` 的整数数组 `nums` 和一个大小为 `q` 的二维整数数组 `queries`，其中 `queries[i] = [l_i, r_i, k_i, v_i]`。
对于每个查询，按以下步骤执行操作：
设定 `idx = l_i`。
当 `idx <= r_i` 时：
更新：`nums[idx] = (nums[idx] * v_i) % (10^9 + 7)`
将 `idx += k_i`。
在处理完所有查询后，返回数组 `nums` 中所有元素的 按位异或 结果。

示例 1：

输入： nums = [1,1,1], queries = [[0,2,1,4]]
输出： 4
解释：
唯一的查询 `[0, 2, 1, 4]` 将下标 0 到下标 2 的每个元素乘以 4。
数组从 `[1, 1, 1]` 变为 `[4, 4, 4]`。
所有元素的异或为 `4 ^ 4 ^ 4 = 4`。
示例 2：

输入： nums = [2,3,1,5,4], queries = [[1,4,2,3],[0,2,1,2]]
输出： 31
解释：
第一个查询 `[1, 4, 2, 3]` 将下标 1 和 3 的元素乘以 3，数组变为 `[2, 9, 1, 15, 4]`。
第二个查询 `[0, 2, 1, 2]` 将下标 0、1 和 2 的元素乘以 2，数组变为 `[4, 18, 2, 15, 4]`。
所有元素的异或为 `4 ^ 18 ^ 2 ^ 15 ^ 4 = 31`。

提示：
`1 <= n == nums.length <= 10^3`
`1 <= nums[i] <= 10^9`
`1 <= q == queries.length <= 10^3`
`queries[i] = [l_i, r_i, k_i, v_i]`
`0 <= l_i <= r_i < n`
`1 <= k_i <= n`
`1 <= v_i <= 10^5`
"""

from typing import List, Optional


class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7

        for l, r, k, v in queries:
            idx = l
            while idx <= r:
                nums[idx] = (nums[idx] * v) % MOD
                idx += k

        # 计算所有元素的异或
        result = 0
        for x in nums:
            result ^= x
        return result










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Simulation
#
# 解题思路:
# n, q <= 1000，因此直接模拟每个查询即可。
# 对于每个查询 [l, r, k, v]：
#   从 idx = l 开始，步长 k，直到 idx > r。
#   将 nums[idx] 乘以 v 并对 1e9+7 取模。
# 全部查询处理完毕后，计算 nums 所有元素的异或值。
#
# 时间复杂度: O(n * q / k_avg)，最坏 O(1000 * 1000) = O(10^6)
# 空间复杂度: O(1)（原地修改 nums）
#
# 关键点:
# - 取模操作在每次乘法后立即进行，防止溢出
# - n, q 较小，暴力的 O(n*q) 足够
