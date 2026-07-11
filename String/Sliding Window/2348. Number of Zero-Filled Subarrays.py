"""
LeetCode #2348 - Number of Zero-Filled Subarrays
全 0 子数组的数目
https://leetcode.cn/problems/number-of-zero-filled-subarrays/

给你一个整数数组 `nums` ，返回全部为 `0` 的 子数组 数目。
子数组 是一个数组中一段连续非空元素组成的序列。

示例 1：
输入：nums = [1,3,0,0,2,0,0,4] 输出：6 解释： 子数组 [0] 出现了 4 次。 子数组 [0,0] 出现了 2 次。 不存在长度大于 2 的全 0 子数组，所以我们返回 6 。
示例 2：
输入：nums = [0,0,0,2,0,0] 输出：9 解释： 子数组 [0] 出现了 5 次。 子数组 [0,0] 出现了 3 次。 子数组 [0,0,0] 出现了 1 次。 不存在长度大于 3 的全 0 子数组，所以我们返回 9 。
示例 3：
输入：nums = [2,10,2019] 输出：0 解释：没有全 0 子数组，所以我们返回 0 。

提示：
`1 <= nums.length <= 10^5`
`-10^9 <= nums[i] <= 10^9`
"""

from typing import List, Optional


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count = 0
        zeros = 0
        for num in nums:
            if num == 0:
                zeros += 1
                count += zeros
            else:
                zeros = 0
        return count



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Math
#
# 解题思路:
# 遍历数组，维护当前连续零的个数 zeros。每遇到一个零，zeros 加 1，
# 同时以该零结尾的零填充子数组有 zeros 个（长度 1 到 zeros），累加到 count。
# 遇到非零元素时，zeros 重置为 0。
# 等价公式：对于长度为 n 的连续零段，子数组数为 n*(n+1)//2。
#
# 时间复杂度: O(N) 其中 N = len(nums)
# 空间复杂度: O(1)
#
# 关键点:
# - 连续零的计数技巧：每遇到一个零就累加当前连续零长度
# - 等价于 sum of arithmetic series: n*(n+1)//2
# - 注意结果可能超过 32 位整数，使用 Python int 自动处理大数
