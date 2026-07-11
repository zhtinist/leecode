"""
LeetCode #2598 - Smallest Missing Non-negative Integer After Operations
执行操作后的最大 MEX
https://leetcode.cn/problems/smallest-missing-non-negative-integer-after-operations/

给你一个下标从 0 开始的整数数组 `nums` 和一个整数 `value` 。
在一步操作中，你可以对 `nums` 中的任一元素加上或减去 `value` 。
例如，如果 `nums = [1,2,3]` 且 `value = 2` ，你可以选择 `nums[0]` 减去 `value` ，得到 `nums = [-1,2,3]` 。
数组的 MEX (minimum excluded) 是指其中数组中缺失的最小非负整数。
例如，`[-1,2,3]` 的 MEX 是 `0` ，而 `[1,0,3]` 的 MEX 是 `2` 。
返回在执行上述操作 任意次 后，`nums` 的最大 MEX 。

示例 1：
输入：nums = [1,-10,7,13,6,8], value = 5 输出：4 解释：执行下述操作可以得到这一结果： - nums[1] 加上 value 两次，nums = [1,0,7,13,6,8] - nums[2] 减去 value 一次，nums = [1,0,2,13,6,8] - nums[3] 减去 value 两次，nums = [1,0,2,3,6,8] nums 的 MEX 是 4 。可以证明 4 是可以取到的最大 MEX 。
示例 2：
输入：nums = [1,-10,7,13,6,8], value = 7 输出：2 解释：执行下述操作可以得到这一结果： - nums[2] 减去 value 一次，nums = [1,-10,0,13,6,8] nums 的 MEX 是 2 。可以证明 2 是可以取到的最大 MEX 。

提示：
`1 <= nums.length, value <= 10^5`
`-10^9 <= nums[i] <= 10^9`
"""

from typing import List, Optional


class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        # count how many numbers map to each remainder mod value
        freq = [0] * value
        for x in nums:
            # we can adjust x to any value with the same remainder mod value
            # the smallest non-negative representative of that remainder
            rem = ((x % value) + value) % value
            freq[rem] += 1

        # find the smallest MEX
        # for each remainder r, we can produce numbers: r, r+value, r+2*value, ...
        # the mex is the smallest number we cannot form
        mex = 0
        while freq[mex % value] > 0:
            freq[mex % value] -= 1
            mex += 1

        return mex



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Array, Hash Table, Math
#
# 解题思路:
# 由于可以任意次加减value，每个数只能改变为与其同余的数（模value同余）。
# 统计每个余数类中数的个数，然后从小到大模拟构造非负整数：
# 对于数i，它需要来自余数i%value的类，如果该类还有剩余就消耗一个，否则i就是MEX。
#
# 时间复杂度: O(n + mex)
# 空间复杂度: O(value)
#
# 关键点:
# - 每个数只能变成与其模value同余的数，这是核心约束
# - 贪心从小到大填充，找到第一个无法填充的数即为MEX
