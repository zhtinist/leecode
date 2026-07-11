"""
LeetCode #2470 - Number of Subarrays With LCM Equal to K
最小公倍数等于 K 的子数组数目
https://leetcode.cn/problems/number-of-subarrays-with-lcm-equal-to-k/

给你一个整数数组 `nums` 和一个整数 `k` ，请你统计并返回 `nums` 的 子数组 中满足 元素最小公倍数为 `k` 的子数组数目。
子数组 是数组中一个连续非空的元素序列。
数组的最小公倍数 是可被所有数组元素整除的最小正整数。

示例 1 ：
输入：nums = [3,6,2,7,1], k = 6 输出：4 解释：以 6 为最小公倍数的子数组是： - [3,6,2,7,1] - [3,6,2,7,1] - [3,6,2,7,1] - [3,6,2,7,1]
示例 2 ：
输入：nums = [3], k = 2 输出：0 解释：不存在以 2 为最小公倍数的子数组。

提示：
`1 <= nums.length <= 1000`
`1 <= nums[i], k <= 1000`
"""

from typing import List, Optional


class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        from math import gcd

        def lcm(a: int, b: int) -> int:
            return a * b // gcd(a, b)

        n = len(nums)
        count = 0

        for i in range(n):
            cur_lcm = nums[i]
            for j in range(i, n):
                cur_lcm = lcm(cur_lcm, nums[j])
                if cur_lcm == k:
                    count += 1
                elif cur_lcm > k or k % cur_lcm != 0:
                    # LCM can only grow; if it exceeds k or is not a divisor of k,
                    # further extension won't yield LCM == k
                    break

        return count

# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Math, Number Theory
#
# 解题思路:
# 枚举所有子数组的起点 i，从 i 开始向右扩展，维护当前子数组的 LCM。
# 由于 LCM 只能增大或保持不变，当 LCM 超过 k 或者 LCM 不能被 k 整除时，
# 后续扩展不可能使 LCM 等于 k，可以提前 break。
# 当 LCM 恰好等于 k 时，计数器加一。
#
# 时间复杂度: O(n^2 * log M)，其中 n 是数组长度，M 是元素最大值
# 空间复杂度: O(1)，只使用常数额外空间
#
# 关键点:
# - 利用 LCM 单调不减的性质进行剪枝
# - 当 cur_lcm 不是 k 的约数时，永远不可能等于 k
# - 使用 math.gcd 实现 LCM 计算
