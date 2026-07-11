"""
LeetCode #2567 - Minimum Score by Changing Two Elements
修改两个元素的最小分数
https://leetcode.cn/problems/minimum-score-by-changing-two-elements/

给你一个下标从 0 开始的整数数组 `nums` 。
`nums` 的 最小 得分是满足 `0 <= i < j < nums.length` 的 `|nums[i] - nums[j]|` 的最小值。
`nums`的 最大 得分是满足 `0 <= i < j < nums.length` 的 `|nums[i] - nums[j]|` 的最大值。
`nums` 的分数是 最大 得分与 最小 得分的和。
我们的目标是最小化 `nums` 的分数。你 最多 可以修改 `nums` 中 2 个元素的值。
请你返回修改 `nums` 中 至多两个 元素的值后，可以得到的 最小分数 。
`|x|` 表示 `x` 的绝对值。

示例 1：
输入：nums = [1,4,3] 输出：0 解释：将 nums[1] 和 nums[2] 的值改为 1 ，nums 变为 [1,1,1] 。`|nums[i] - nums[j]|` 的值永远为 0 ，所以我们返回 0 + 0 = 0 。
示例 2：
输入：nums = [1,4,7,8,5] 输出：3 解释： 将 nums[0] 和 nums[1] 的值变为 6 ，nums 变为 [6,6,7,8,5] 。 最小得分是 i = 0 且 j = 1 时得到的 |`nums[i] - nums[j]`| = |6 - 6| = 0 。 最大得分是 i = 3 且 j = 4 时得到的 |`nums[i] - nums[j]`| = |8 - 5| = 3 。 最大得分与最小得分之和为 3 。这是最优答案。

提示：
`3 <= nums.length <= 10^5`
`1 <= nums[i] <= 10^9`
"""

from typing import List, Optional


class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        # min gap with 0 changes
        min_gap = min(nums[i+1] - nums[i] for i in range(n - 1))
        # 0 changes
        ans = (nums[-1] - nums[0]) + min_gap
        # 2 changes: we can effectively remove up to 2 elements from ends
        # remove 2 from left, 0 from right
        rng = nums[-1] - nums[2]
        ans = min(ans, rng)
        # remove 0 from left, 2 from right
        rng = nums[-3] - nums[0]
        ans = min(ans, rng)
        # remove 1 from each
        rng = nums[-2] - nums[1]
        ans = min(ans, rng)
        # 1 change: remove 1 from left or right (min_gap becomes 0)
        rng = nums[-1] - nums[1]
        ans = min(ans, rng)
        rng = nums[-2] - nums[0]
        ans = min(ans, rng)
        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Array, Sorting
#
# 解题思路:
# 排序后考虑修改策略。修改元素等效于移除端点的极值。最多修改2个，可移除0/1/2个左端点+0/1/2个右端点
# （总和<=2）。若修改>=1个元素，最小差距可变为0（通过让两元素相等）。所以答案=min(各种移除方案的范围+0)。
# 同时考虑0次修改：范围+原数组最小相邻差距。取所有方案的最小值。
#
# 时间复杂度: O(N log N)
# 空间复杂度: O(1)
#
# 关键点:
# - 修改元素等效于从数组端点移除元素
# - 至少1次修改时min_gap=0；0次修改时min_gap=原始最小相邻差
# - 检查3种2次修改方案和2种1次修改方案，取最小分数
