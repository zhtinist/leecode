"""
LeetCode #2364 - Count Number of Bad Pairs
统计坏数对的数目
https://leetcode.cn/problems/count-number-of-bad-pairs/

给你一个下标从 0 开始的整数数组 `nums` 。如果 `i < j` 且 `j - i != nums[j] - nums[i]` ，那么我们称 `(i, j)` 是一个 坏数对 。
请你返回 `nums` 中 坏数对 的总数目。

示例 1：
输入：nums = [4,1,3,3] 输出：5 解释：数对 (0, 1) 是坏数对，因为 1 - 0 != 1 - 4 。 数对 (0, 2) 是坏数对，因为 2 - 0 != 3 - 4, 2 != -1 。 数对 (0, 3) 是坏数对，因为 3 - 0 != 3 - 4, 3 != -1 。 数对 (1, 2) 是坏数对，因为 2 - 1 != 3 - 1, 1 != 2 。 数对 (2, 3) 是坏数对，因为 3 - 2 != 3 - 3, 1 != 0 。 总共有 5 个坏数对，所以我们返回 5 。
示例 2：
输入：nums = [1,2,3,4,5] 输出：0 解释：没有坏数对。

提示：
`1 <= nums.length <= 10^5`
`1 <= nums[i] <= 10^9`
"""

from typing import List, Optional


from collections import Counter


class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        # Good pairs: j - i == nums[j] - nums[i]
        # => nums[i] - i == nums[j] - j
        freq = Counter(nums[i] - i for i in range(n))

        good_pairs = sum(v * (v - 1) // 2 for v in freq.values())
        total_pairs = n * (n - 1) // 2
        return total_pairs - good_pairs



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Hash Table, Math, Counting
#
# 解题思路:
# 坏数对定义：i < j 且 j - i != nums[j] - nums[i]。
# 变换等式：nums[i] - i == nums[j] - j 时是好数对。
# 因此统计每个 nums[i] - i 的出现频次，对于频次为 v 的值，可形成 v*(v-1)//2 个好数对。
# 总对数 = n*(n-1)//2，坏数对 = 总对数 - 好数对。
#
# 时间复杂度: O(N) 其中 N = len(nums)
# 空间复杂度: O(N) 用于 Counter 存储
#
# 关键点:
# - 数学变换：将条件 j - i == nums[j] - nums[i] 转为 nums[i] - i == nums[j] - j
# - 逆向思维：直接统计好数对比统计坏数对更高效
# - 组合数公式：从 v 个相同 key 中选 2 个 = v*(v-1)//2
