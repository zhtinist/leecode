"""
LeetCode #2786 - Visit Array Positions to Maximize Score
访问数组中的位置使分数最大
https://leetcode.cn/problems/visit-array-positions-to-maximize-score/

给你一个下标从 0 开始的整数数组 `nums` 和一个正整数 `x` 。
你 一开始 在数组的位置 `0` 处，你可以按照下述规则访问数组中的其他位置：
如果你当前在位置 `i` ，那么你可以移动到满足 `i < j` 的 任意 位置 `j` 。
对于你访问的位置 `i` ，你可以获得分数 `nums[i]` 。
如果你从位置 `i` 移动到位置 `j` 且 `nums[i]` 和 `nums[j]` 的 奇偶性 不同，那么你将失去分数 `x` 。
请你返回你能得到的 最大 得分之和。
注意 ，你一开始的分数为 `nums[0]` 。

示例 1：
输入：nums = [2,3,6,1,9,2], x = 5 输出：13 解释：我们可以按顺序访问数组中的位置：0 -> 2 -> 3 -> 4 。 对应位置的值为 2 ，6 ，1 和 9 。因为 6 和 1 的奇偶性不同，所以下标从 2 -> 3 让你失去 x = 5 分。 总得分为：2 + 6 + 1 + 9 - 5 = 13 。
示例 2：
输入：nums = [2,4,6,8], x = 3 输出：20 解释：数组中的所有元素奇偶性都一样，所以我们可以将每个元素都访问一次，而且不会失去任何分数。 总得分为：2 + 4 + 6 + 8 = 20 。

提示：
`2 <= nums.length <= 10^5`
`1 <= nums[i], x <= 10^6`
"""

from typing import List, Optional


class Solution:
    def maxScore(self, nums: List[int], x: int) -> int:
        n = len(nums)
        max_even = -10 ** 18
        max_odd = -10 ** 18
        if nums[0] % 2 == 0:
            max_even = nums[0]
        else:
            max_odd = nums[0]
        ans = nums[0]
        for i in range(1, n):
            if nums[i] % 2 == 0:
                cur = max(max_even, max_odd - x) + nums[i]
                max_even = max(max_even, cur)
            else:
                cur = max(max_odd, max_even - x) + nums[i]
                max_odd = max(max_odd, cur)
            ans = max(ans, cur)
        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Dynamic Programming
#
# 解题思路:
# DP 维护以偶数或奇数结尾的最大分数。max_even 表示当前以偶数结尾的最优分数，max_odd 表示以奇数结尾的最优分数。
# 对于 nums[i]：如果它是偶数，可以从之前的偶数结尾（不扣分）或奇数结尾（扣 x 分）转移过来。
# 初始化：起始位置 0 必须选择。然后对于每个后续位置，计算以它为结尾的最大得分并更新对应奇偶状态。
#
# 时间复杂度: O(n)
# 空间复杂度: O(1)
#
# 关键点:
# - 两个状态分别追踪以偶数和奇数结尾的最大分数
# - 奇偶切换时扣 x 分：从 max_odd 到偶数需要 -x，反之亦然
# - 起始位置必须选（已包含在分数中），后续位置可选
