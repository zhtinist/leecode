"""
LeetCode #2295 - Replace Elements in an Array
替换数组中的元素
https://leetcode.cn/problems/replace-elements-in-an-array/

给你一个下标从 0 开始的数组 `nums` ，它包含 `n` 个 互不相同 的正整数。请你对这个数组执行 `m` 个操作，在第 `i` 个操作中，你需要将数字 `operations[i][0]` 替换成 `operations[i][1]` 。
题目保证在第 `i` 个操作中：
`operations[i][0]` 在 `nums` 中存在。
`operations[i][1]` 在 `nums` 中不存在。
请你返回执行完所有操作后的数组。

示例 1：
输入：nums = [1,2,4,6], operations = [[1,3],[4,7],[6,1]] 输出：[3,2,7,1] 解释：我们对 nums 执行以下操作： - 将数字 1 替换为 3 。nums 变为 [3,2,4,6] 。 - 将数字 4 替换为 7 。nums 变为 [3,2,7,6] 。 - 将数字 6 替换为 1 。nums 变为 [3,2,7,1] 。 返回最终数组 [3,2,7,1] 。
示例 2：
输入：nums = [1,2], operations = [[1,3],[2,1],[3,2]] 输出：[2,1] 解释：我们对 nums 执行以下操作： - 将数字 1 替换为 3 。nums 变为 [3,2] 。 - 将数字 2 替换为 1 。nums 变为 [3,1] 。 - 将数字 3 替换为 2 。nums 变为 [2,1] 。 返回最终数组 [2,1] 。

提示：
`n == nums.length`
`m == operations.length`
`1 <= n, m <= 10^5`
`nums` 中所有数字 互不相同 。
`operations[i].length == 2`
`1 <= nums[i], operations[i][0], operations[i][1] <= 10^6`
在执行第 `i` 个操作时，`operations[i][0]` 在 `nums` 中存在。
在执行第 `i` 个操作时，`operations[i][1]` 在 `nums` 中不存在。
"""

from typing import List, Optional


class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        # 构建值到索引的映射：由于 nums 中的数字互不相同，每个值对应唯一位置
        val_to_idx = {val: i for i, val in enumerate(nums)}

        for old_val, new_val in operations:
            # 找到旧值在数组中的位置
            idx = val_to_idx[old_val]
            # 在数组中原地替换
            nums[idx] = new_val
            # 更新映射：删除旧值，添加新值
            del val_to_idx[old_val]
            val_to_idx[new_val] = idx

        return nums


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Hash Table, Simulation
#
# 解题思路:
# 由于 nums 中的所有数字互不相同，我们可以构建一个哈希表（字典），将每个值映射到它在数组中的索引位置。
# 对于每个操作 [old_val, new_val]：
# 1. 通过哈希表 O(1) 找到 old_val 在数组中的索引
# 2. 将该位置的值更新为 new_val
# 3. 删除哈希表中 old_val 的映射，添加 new_val -> idx 的映射
# 这样每次操作只需 O(1) 时间，避免了在数组中线性搜索的开销。
# 题目保证了 old_val 一定存在且 new_val 一定不存在，所以上述操作始终合法。
#
# 时间复杂度: O(n + m)
# - 构建初始哈希表需要 O(n)
# - 每个操作 O(1)，共 m 个操作 O(m)
#
# 空间复杂度: O(n)
# - 哈希表存储 n 个键值对
#
# 关键点:
# - 利用"所有数字互不相同"的性质，使用哈希表建立值到索引的映射
# - 每次操作后同步更新哈希表，保持映射的正确性
# - 原地修改数组，避免额外空间开销
