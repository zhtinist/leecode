"""
LeetCode #2170 - Minimum Operations to Make the Array Alternating
使数组变成交替数组的最少操作数
https://leetcode.cn/problems/minimum-operations-to-make-the-array-alternating/

给你一个下标从 0 开始的数组 `nums` ，该数组由 `n` 个正整数组成。
如果满足下述条件，则数组 `nums` 是一个 交替数组 ：
`nums[i - 2] == nums[i]` ，其中 `2 <= i <= n - 1` 。
`nums[i - 1] != nums[i]` ，其中 `1 <= i <= n - 1` 。
在一步 操作 中，你可以选择下标 `i` 并将 `nums[i]` 更改 为 任一 正整数。
返回使数组变成交替数组的 最少操作数 。

示例 1：
输入：nums = [3,1,3,2,4,3] 输出：3 解释： 使数组变成交替数组的方法之一是将该数组转换为 [3,1,3,1,3,1] 。 在这种情况下，操作数为 3 。 可以证明，操作数少于 3 的情况下，无法使数组变成交替数组。
示例 2：
输入：nums = [1,2,2,2,2] 输出：2 解释： 使数组变成交替数组的方法之一是将该数组转换为 [1,2,1,2,1]. 在这种情况下，操作数为 2 。 注意，数组不能转换成 [2,2,2,2,2] 。因为在这种情况下，nums[0] == nums[1]，不满足交替数组的条件。

提示：
`1 <= nums.length <= 10^5`
`1 <= nums[i] <= 10^5`
"""

from typing import List, Optional


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        from collections import Counter
        n = len(nums)
        if n == 1:
            return 0

        even_count = Counter(nums[i] for i in range(0, n, 2))
        odd_count = Counter(nums[i] for i in range(1, n, 2))

        even_top = even_count.most_common(2)
        odd_top = odd_count.most_common(2)

        # Fill with (0, 0) if not enough
        while len(even_top) < 2:
            even_top.append((0, 0))
        while len(odd_top) < 2:
            odd_top.append((0, 0))

        even_total = (n + 1) // 2
        odd_total = n // 2

        if even_top[0][0] != odd_top[0][0]:
            return (even_total - even_top[0][1]) + (odd_total - odd_top[0][1])
        else:
            option1 = (even_total - even_top[0][1]) + (odd_total - odd_top[1][1])
            option2 = (even_total - even_top[1][1]) + (odd_total - odd_top[0][1])
            return min(option1, option2)



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Array, Hash Table, Counting
#
# 解题思路:
# 交替数组要求：偶数索引位置的元素全部相同，奇数索引位置的元素全部相同，且偶数位置的元
# 素不等于奇数位置的元素。要使操作数最少，即保留尽可能多的元素不变。分别统计偶数位置和
# 奇数位置上各元素的出现频率，取各自出现次数最多的前两名。如果偶数位置最高频元素与奇数
# 位置最高频元素不同，则两者都保留；如果两者相同，则需要考虑两种替代方案：(偶数最高频 +
# 奇数第二高频) 和 (偶数第二高频 + 奇数最高频)，选择保留总数更多的方案。总操作数 =
# 总元素数 - 保留的元素数。
#
# 时间复杂度: O(n)
# 空间复杂度: O(n)
#
# 关键点:
# - 交替数组的两个条件：偶数位相同，奇数位相同，且两者不同
# - 分别统计奇偶位置的频率分布，各取 top-2 以处理冲突
# - 边界情况：n = 1 时无需任何操作
# - 使用 Counter.most_common(2) 高效获取前两名
