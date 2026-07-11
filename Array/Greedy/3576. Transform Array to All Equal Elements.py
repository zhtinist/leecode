"""
LeetCode #3576 - Transform Array to All Equal Elements
数组元素相等转换
https://leetcode.cn/problems/transform-array-to-all-equal-elements/

给你一个大小为 `n` 的整数数组 `nums`，其中只包含 `1` 和 `-1`，以及一个整数 `k`。
你可以最多进行 `k` 次以下操作：

选择一个下标 `i`（`0 <= i < n - 1`），然后将 `nums[i]` 和 `nums[i + 1]` 同时 乘以 `-1`。
注意：你可以在 不同 的操作中多次选择相同的下标 `i`。
如果在最多 `k` 次操作后可以使数组的所有元素相等，则返回 `true`；否则，返回 `false`。

示例 1：

输入： nums = [1,-1,1,-1,1], k = 3
输出： true
解释：
我们可以通过以下两次操作使数组的所有元素相等：
选择下标 `i = 1`，将 `nums[1]` 和 `nums[2]` 同时乘以 -1。此时 `nums = [1,1,-1,-1,1]`。
选择下标 `i = 2`，将 `nums[2]` 和 `nums[3]` 同时乘以 -1。此时 `nums = [1,1,1,1,1]`。
示例 2：

输入： nums = [-1,-1,-1,1,1,1], k = 5
输出： false
解释：
在最多 5 次操作内，无法使数组的所有元素相等。

提示：
`1 <= n == nums.length <= 10^5`
`nums[i]` 的值为 `-1` 或 `1`。
`1 <= k <= n`
"""

from typing import List, Optional


class Solution:
    def canMakeAllEqual(self, nums: List[int], k: int) -> bool:
        """
        操作：选择相邻两个元素同时乘以 -1（即同时取反）。
        这相当于对相邻的两个位置施加 XOR 1 操作。

        关键观察：每次操作翻转两个相邻元素。
        - 翻转两个 1 产生两个 -1（-1 数量 +2）
        - 翻转两个 -1 消灭两个 -1（-1 数量 -2）
        - 翻转 1 和 -1 相当于移动 -1（-1 数量不变）

        因此，-1 的数量的奇偶性不变（每次变化 ±2 或 0）。

        目标：使所有元素相等 → 全是 1 或全是 -1。
        - 全是 1：最终 -1 数量 = 0
        - 全是 -1：最终 -1 数量 = n

        由于奇偶性不变：
        - 若初始 -1 数量为偶数，可以达成全 1
        - 若初始 1 数量为偶数，可以达成全 -1

        最少操作次数 = 贪心配对相邻同目标位：
        将 -1 视为需要消除的"坏位"，操作本质是移动这些坏位并两两抵消。
        最少操作数 = 将相邻的 -1 两两配对的距离之和。
        """
        n = len(nums)

        # 方案一：目标全 1（消除所有 -1）
        neg_positions = [i for i in range(n) if nums[i] == -1]
        min_ops_to_all_one = float('inf')
        if len(neg_positions) % 2 == 0:
            # 偶数个 -1，可以完全消除
            ops = 0
            for i in range(0, len(neg_positions), 2):
                ops += neg_positions[i + 1] - neg_positions[i]
            min_ops_to_all_one = ops

        # 方案二：目标全 -1（消除所有 1，即翻转所有 1 变成 -1）
        one_positions = [i for i in range(n) if nums[i] == 1]
        min_ops_to_all_neg = float('inf')
        if len(one_positions) % 2 == 0:
            ops = 0
            for i in range(0, len(one_positions), 2):
                ops += one_positions[i + 1] - one_positions[i]
            min_ops_to_all_neg = ops

        return min_ops_to_all_one <= k or min_ops_to_all_neg <= k










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Array
#
# 解题思路:
# 每次操作翻转相邻两个元素，本质上是对两个相邻位置取反。
# 操作的效果：
# - 翻转 (1, 1) → (-1, -1)：-1 数量 +2
# - 翻转 (-1, -1) → (1, 1)：-1 数量 -2
# - 翻转 (1, -1) 或 (-1, 1)：-1 数量不变（相当于移动 -1 的位置）
#
# 核心观察：-1 数量的奇偶性在操作下保持不变。
#
# 目标有两种可能：
# 1. 全 1（-1 数量 = 0）：要求初始 -1 数量为偶数
# 2. 全 -1（1 数量 = 0）：要求初始 1 数量为偶数
#
# 最少操作次数：将需要消除的元素两两贪心配对（按位置排序后，相邻配对）。
# 每对的距离之和即为最少操作次数（每次移动 1 步需要 1 次操作）。
# 最终判断 min_ops ≤ k。
#
# 时间复杂度: O(n)
# 空间复杂度: O(n)（存储位置列表）
#
# 关键点:
# - -1 数量奇偶性不变（每次操作改变 0 或 ±2）
# - 贪心配对相邻的同目标位置
# - 有两个可能的目标状态：全 1 或全 -1
