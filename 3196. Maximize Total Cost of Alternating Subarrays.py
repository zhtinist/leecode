"""
LeetCode #3196 - Maximize Total Cost of Alternating Subarrays
最大化子数组的总成本
https://leetcode.cn/problems/maximize-total-cost-of-alternating-subarrays/

给你一个长度为 `n` 的整数数组 `nums`。
子数组 `nums[l..r]`（其中 `0 <= l <= r < n`）的 成本 定义为：
`cost(l, r) = nums[l] - nums[l + 1] + ... + nums[r] * (−1)^r − l`
你的任务是将 `nums` 分割成若干子数组，使得所有子数组的成本之和 最大化，并确保每个元素 正好 属于一个子数组。
具体来说，如果 `nums` 被分割成 `k` 个子数组，且分割点为索引 `i_1, i_2, ..., i_k − 1`（其中 `0 <= i_1 < i_2 < ... < i_k - 1 < n - 1`），则总成本为：
`cost(0, i_1) + cost(i_1 + 1, i_2) + ... + cost(i_k − 1 + 1, n − 1)`
返回在最优分割方式下的子数组成本之和的最大值。
注意：如果 `nums` 没有被分割，即 `k = 1`，则总成本即为 `cost(0, n - 1)`。

示例 1：

输入： nums = [1,-2,3,4]
输出： 10
解释：
一种总成本最大化的方法是将 `[1, -2, 3, 4]` 分割成子数组 `[1, -2, 3]` 和 `[4]`。总成本为 `(1 + 2 + 3) + 4 = 10`。
示例 2：

输入： nums = [1,-1,1,-1]
输出： 4
解释：
一种总成本最大化的方法是将 `[1, -1, 1, -1]` 分割成子数组 `[1, -1]` 和 `[1, -1]`。总成本为 `(1 + 1) + (1 + 1) = 4`。
示例 3：

输入： nums = [0]
输出： 0
解释：
无法进一步分割数组，因此答案为 0。
示例 4：

输入： nums = [1,-1]
输出： 2
解释：
选择整个数组，总成本为 `1 + 1 = 2`，这是可能的最大成本。

提示：
`1 <= nums.length <= 10^5`
`-10^9 <= nums[i] <= 10^9`
"""

from typing import List, Optional


class Solution:
    def maximumTotalCost(self, nums: List[int]) -> int:
        n = len(nums)
        # dp_plus: 当前位置符号为+的最大总成本
        # dp_minus: 当前位置符号为-的最大总成本
        dp_plus = nums[0]
        dp_minus = float('-inf')
        best = nums[0]

        for i in range(1, n):
            new_plus = nums[i] + best        # 开始新子数组 或 接在-后面
            new_minus = dp_plus - nums[i]    # 只能接在+后面（继续子数组）
            dp_plus = new_plus
            dp_minus = new_minus
            best = max(dp_plus, dp_minus)

        return best



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Dynamic Programming
#
# 解题思路:
# 子数组内符号交替（+,-,+,...），分割后新子数组首位始终为正。
# DP维护两个状态：dp_plus[i]为位置i符号为正的最大成本，dp_minus[i]为符号为负的最大成本。
# 转移：dp_plus[i] = nums[i] + max(dp_plus[i-1], dp_minus[i-1])（新建子数组或接在负号后）；
# dp_minus[i] = dp_plus[i-1] - nums[i]（只能接在正号后继续子数组）。
# 最终答案 = max(dp_plus[n-1], dp_minus[n-1])。
#
# 时间复杂度: O(n)
# 空间复杂度: O(1)
#
# 关键点:
# - 子数组内符号固定交替，分割可重置为正号
# - dp_plus可新建或继续，dp_minus只能继续
# - O(1)空间滚动更新
