"""
LeetCode #2808 - Minimum Seconds to Equalize a Circular Array
使循环数组所有元素相等的最少秒数
https://leetcode.cn/problems/minimum-seconds-to-equalize-a-circular-array/

给你一个下标从 0 开始长度为 `n` 的数组 `nums` 。
每一秒，你可以对数组执行以下操作：
对于范围在 `[0, n - 1]` 内的每一个下标 `i` ，将 `nums[i]` 替换成 `nums[i]` ，`nums[(i - 1 + n) % n]` 或者 `nums[(i + 1) % n]` 三者之一。
注意，所有元素会被同时替换。
请你返回将数组 `nums` 中所有元素变成相等元素所需要的 最少 秒数。

示例 1：
输入：nums = [1,2,1,2] 输出：1 解释：我们可以在 1 秒内将数组变成相等元素： - 第 1 秒，将每个位置的元素分别变为 [nums[3],nums[1],nums[3],nums[3]] 。变化后，nums = [2,2,2,2] 。 1 秒是将数组变成相等元素所需要的最少秒数。
示例 2：
输入：nums = [2,1,3,3,2] 输出：2 解释：我们可以在 2 秒内将数组变成相等元素： - 第 1 秒，将每个位置的元素分别变为 [nums[0],nums[2],nums[2],nums[2],nums[3]] 。变化后，nums = [2,3,3,3,3] 。 - 第 2 秒，将每个位置的元素分别变为 [nums[1],nums[1],nums[2],nums[3],nums[4]] 。变化后，nums = [3,3,3,3,3] 。 2 秒是将数组变成相等元素所需要的最少秒数。
示例 3：
输入：nums = [5,5,5,5] 输出：0 解释：不需要执行任何操作，因为一开始数组中的元素已经全部相等。

提示：
`1 <= n == nums.length <= 10^5`
`1 <= nums[i] <= 10^9`
"""

from typing import List, Optional


class Solution:
    def minimumSeconds(self, nums: List[int]) -> int:
        from collections import defaultdict
        n = len(nums)
        pos = defaultdict(list)
        for i, v in enumerate(nums):
            pos[v].append(i)
        ans = n
        for idx_list in pos.values():
            max_gap = 0
            m = len(idx_list)
            for i in range(m):
                gap = (idx_list[(i + 1) % m] - idx_list[i]) % n
                max_gap = max(max_gap, gap)
            ans = min(ans, max_gap // 2)
        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Hash Table
#
# 解题思路:
# 最终全部变成的相等元素必然是原数组中的某个值。对于每种数值，找出它在循环数组中出现位置的最大间隔。
# 在每秒内，该值可以向左右各扩展 1 个位置。所以要覆盖最大间隔 max_gap，需要 ceil(max_gap / 2) 秒。
# 由于是循环数组，间隔需要取模 n。对所有数值取最小秒数即为答案。
#
# 时间复杂度: O(n)
# 空间复杂度: O(n)
#
# 关键点:
# - 最终相等的值必须是原数组中存在的一个值
# - 每种值的扩展速度是每秒向左右各 1 格，覆盖 gap 需要 ceil(gap/2) = gap//2 秒
# - 循环数组需要将首尾之间也考虑为一段间隔：gap = (first_pos - last_pos + n) % n
