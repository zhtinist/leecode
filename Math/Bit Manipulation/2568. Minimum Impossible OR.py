"""
LeetCode #2568 - Minimum Impossible OR
最小无法得到的或值
https://leetcode.cn/problems/minimum-impossible-or/

给你一个下标从 0 开始的整数数组 `nums` 。
如果存在一些整数满足 `0 <= index_1 < index_2 < ... < index_k < nums.length` ，得到 `nums[index_1] | nums[index_2] | ... | nums[index_k] = x` ，那么我们说 `x` 是 可表达的 。换言之，如果一个整数能由 `nums` 的某个子序列的或运算得到，那么它就是可表达的。
请你返回 `nums` 不可表达的 最小非零整数 。

示例 1：
输入：nums = [2,1] 输出：4 解释：1 和 2 已经在数组中，因为 nums[0] | nums[1] = 2 | 1 = 3 ，所以 3 是可表达的。由于 4 是不可表达的，所以我们返回 4 。
示例 2：
输入：nums = [5,3,2] 输出：1 解释：1 是最小不可表达的数字。

提示：
`1 <= nums.length <= 10^5`
`1 <= nums[i] <= 10^9`
"""

from typing import List, Optional


class Solution:
    def minImpossibleOR(self, nums: List[int]) -> int:
        s = set(nums)
        p = 1
        while p in s:
            p <<= 1
        return p



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Bit Manipulation, Brainteaser, Array
#
# 解题思路:
# 最小不可表达的OR值是最小的不在数组中的2的幂。因为任何数的OR结果都可以由其二进制位对应的
# 2的幂OR得到。如果某个2的幂不在数组中，所有需要该位的数都无法表达。
# 反之，如果1,2,4,...,2^k都在数组中，则0到2^(k+1)-1的所有数都可表达。
#
# 时间复杂度: O(N)
# 空间复杂度: O(N)
#
# 关键点:
# - 核心结论：答案为最小缺失的2的幂
# - 有了所有小于2^k的2的幂，可以表达出0到2^k-1的所有数
# - 从1开始逐次左移检查是否在集合中
