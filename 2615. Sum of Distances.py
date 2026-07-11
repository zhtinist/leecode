"""
LeetCode #2615 - Sum of Distances
等值距离和
https://leetcode.cn/problems/sum-of-distances/

给你一个下标从 0 开始的整数数组 `nums` 。现有一个长度等于 `nums.length` 的数组 `arr` 。对于满足 `nums[j] == nums[i]` 且 `j != i` 的所有 `j` ，`arr[i]` 等于所有 `|i - j|` 之和。如果不存在这样的 `j` ，则令 `arr[i]` 等于 `0` 。
返回数组 `arr` 。

示例 1：
输入：nums = [1,3,1,1,2] 输出：[5,0,3,4,0] 解释： i = 0 ，nums[0] == nums[2] 且 nums[0] == nums[3] 。因此，arr[0] = |0 - 2| + |0 - 3| = 5 。  i = 1 ，arr[1] = 0 因为不存在值等于 3 的其他下标。 i = 2 ，nums[2] == nums[0] 且 nums[2] == nums[3] 。因此，arr[2] = |2 - 0| + |2 - 3| = 3 。 i = 3 ，nums[3] == nums[0] 且 nums[3] == nums[2] 。因此，arr[3] = |3 - 0| + |3 - 2| = 4 。  i = 4 ，arr[4] = 0 因为不存在值等于 2 的其他下标。
示例 2：
输入：nums = [0,5,3] 输出：[0,0,0] 解释：因为 nums 中的元素互不相同，对于所有 i ，都有 arr[i] = 0 。

提示：
`1 <= nums.length <= 10^5`
`0 <= nums[i] <= 10^9`

注意：本题与 2121. 相同元素的间隔之和 相同。
"""

from typing import List, Optional


class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        from collections import defaultdict
        groups = defaultdict(list)
        for i, v in enumerate(nums):
            groups[v].append(i)

        for indices in groups.values():
            m = len(indices)
            if m == 1:
                continue
            prefix = 0
            total = sum(indices)
            for i, idx in enumerate(indices):
                left_sum = i * idx - prefix
                right_sum = (total - prefix - idx) - (m - 1 - i) * idx
                res[idx] = left_sum + right_sum
                prefix += idx
        return res



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Hash Table, Prefix Sum
#
# 解题思路:
# 将相同值的索引分组。对每组索引，使用前缀和技巧O(m)计算每个位置的绝对差值和。
# 对于排序后的索引列表，左距离和 = i*idx - 左边前缀和，右距离和 = 右边和 - (m-1-i)*idx。
#
# 时间复杂度: O(n)
# 空间复杂度: O(n)
#
# 关键点:
# - 按值分组，每组内索引自然有序
# - 使用前缀和避免O(m^2)的暴力计算
# - 左右距离分别用公式O(1)计算
