"""
LeetCode #3334 - Find the Maximum Factor Score of Array
数组的最大因子得分
https://leetcode.cn/problems/find-the-maximum-factor-score-of-array/

给你一个整数数组 `nums`。
因子得分 定义为数组所有元素的最小公倍数（LCM）与最大公约数（GCD）的 乘积。
在 最多 移除一个元素的情况下，返回 `nums` 的 最大因子得分。
注意，单个数字的 LCM 和 GCD 都是其本身，而 空数组 的因子得分为 0。

示例 1：

输入： nums = [2,4,8,16]
输出： 64
解释：
移除数字 2 后，剩余元素的 GCD 为 4，LCM 为 16，因此最大因子得分为 `4 * 16 = 64`。
示例 2：

输入： nums = [1,2,3,4,5]
输出： 60
解释：
无需移除任何元素即可获得最大因子得分 60。
示例 3：

输入： nums = [3]
输出： 9

提示：
`1 <= nums.length <= 100`
`1 <= nums[i] <= 30`
"""

from typing import List, Optional


class Solution:
    def maxScore(self, nums: List[int]) -> int:
        from math import gcd, lcm

        n = len(nums)
        if n == 1:
            return nums[0] * nums[0]

        def compute_gcd(arr):
            g = arr[0]
            for x in arr[1:]:
                g = gcd(g, x)
            return g

        def compute_lcm(arr):
            l = arr[0]
            for x in arr[1:]:
                l = l * x // gcd(l, x)
            return l

        ans = compute_gcd(nums) * compute_lcm(nums)
        for i in range(n):
            remaining = nums[:i] + nums[i + 1:]
            if not remaining:
                ans = max(ans, 0)
            else:
                ans = max(ans, compute_gcd(remaining) * compute_lcm(remaining))
        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Math, Number Theory
#
# 解题思路:
# 枚举所有可能的移除情况（包括不移除）。对于每种情况，计算剩余元素的GCD和LCM的乘积。
# nums长度<=100，枚举每个元素移除一次和保留全部的情况，共O(n)种情况。
# 对每种情况计算GCD和LCM，取最大乘积作为答案。
#
# 时间复杂度: O(n^2)，n <= 100
# 空间复杂度: O(n)
#
# 关键点:
# - 最多移除一个元素（包括不移除），所以枚举所有n+1种情况即可
# - 使用math.gcd和逐步计算LCM
