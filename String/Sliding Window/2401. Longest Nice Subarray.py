"""
LeetCode #2401 - Longest Nice Subarray
最长优雅子数组
https://leetcode.cn/problems/longest-nice-subarray/

给你一个由 正 整数组成的数组 `nums` 。
如果 `nums` 的子数组中位于 不同 位置的每对元素按位 与（AND）运算的结果等于 `0` ，则称该子数组为 优雅 子数组。
返回 最长 的优雅子数组的长度。
子数组 是数组中的一个 连续 部分。
注意：长度为 `1` 的子数组始终视作优雅子数组。

示例 1：
输入：nums = [1,3,8,48,10] 输出：3 解释：最长的优雅子数组是 [3,8,48] 。子数组满足题目条件： - 3 AND 8 = 0 - 3 AND 48 = 0 - 8 AND 48 = 0 可以证明不存在更长的优雅子数组，所以返回 3 。
示例 2：
输入：nums = [3,1,5,11,13] 输出：1 解释：最长的优雅子数组长度为 1 ，任何长度为 1 的子数组都满足题目条件。

提示：
`1 <= nums.length <= 10^5`
`1 <= nums[i] <= 10^9`
"""

from typing import List, Optional


class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        """
        Sliding window: maintain the bitwise OR of elements in the current window.
        A new element nums[right] can be added only if (used_bits & nums[right]) == 0,
        meaning it shares no set bits with any element already in the window.
        If there's a conflict, shrink from the left until the conflict is resolved.
        """
        left = 0
        used_bits = 0
        max_len = 0

        for right in range(len(nums)):
            # Shrink window while there is a bit conflict
            while used_bits & nums[right]:
                used_bits ^= nums[left]  # remove nums[left] from used_bits
                left += 1
            # Add nums[right] to the window
            used_bits |= nums[right]
            max_len = max(max_len, right - left + 1)

        return max_len



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Bit Manipulation, Array, Sliding Window
#
# 解题思路:
# 1. 优雅子数组的核心条件：子数组内任意两个元素的按位与为 0，等价于所有元素的二进制位互不重叠。
# 2. 使用滑动窗口维护一个 used_bits（窗口内所有元素的按位或结果）。
# 3. 当加入 nums[right] 时，若 used_bits & nums[right] != 0，说明与窗口内已有元素共享比特位，需要收缩左边界。
# 4. 收缩时，用 XOR (used_bits ^= nums[left]) 移除 nums[left] 的比特位（因为 XOR 会清除已设置的重复位）。
# 5. 每次成功加入元素后更新最大窗口长度。
#
# 时间复杂度: O(n) — 每个元素最多被加入和移除一次（平摊 O(1)）
# 空间复杂度: O(1) — 只使用几个变量
#
# 关键点:
# - 子数组内任意两元素 AND 为 0，等价于所有元素二进制位不重叠 —— 这是使用按位或追踪窗口的关键性质
# - XOR 可以安全地移除元素（因为已知没有重叠位，XOR 等于按位清除）
# - 滑动窗口适用于"最长满足某条件的连续子数组"问题
