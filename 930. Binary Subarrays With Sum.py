"""
LeetCode #930 - Binary Subarrays With Sum
中文题名：和相同的二元子数组
https://leetcode.com/problems/binary-subarrays-with-sum/

In an array `A` of `0`s and `1`s, how many
non-empty subarrays have sum `S`?

Example 1:

Input: A = [1,0,1,0,1], S = 2
Output: 4
Explanation:
The 4 subarrays are bolded below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]

Note:

`A.length <= 30000`

`0 <= S <= A.length`

`A[i]` is either `0` or `1`.

【中文翻译】

在一个由 0 和 1 组成的数组 A 中，有多少个非空子数组的和为 S？

"""

from typing import List, Optional


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        """
        Use the atMost technique: count subarrays with sum <= goal
        minus subarrays with sum <= goal-1.
        """
        def atMost(k: int) -> int:
            if k < 0:
                return 0
            left = 0
            current_sum = 0
            count = 0
            for right in range(len(nums)):
                current_sum += nums[right]
                while current_sum > k:
                    current_sum -= nums[left]
                    left += 1
                # All subarrays ending at right with start in [left, right]
                count += right - left + 1
            return count

        return atMost(goal) - atMost(goal - 1)



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用 atMost 技巧（滑动窗口）：
# 定义辅助函数 atMost(k)：返回和 <= k 的子数组个数。
# 维护滑动窗口 [left, right]，保证窗口内的和 <= k。
# 对于每个 right，以 right 结尾且和 <= k 的子数组个数 = right - left + 1。
# 最终答案 = atMost(goal) - atMost(goal - 1)（即和恰好等于 goal 的子数组数）。
#
# 另一种方法：前缀和 + 哈希表，记录每个前缀和出现的次数。
#
# 时间复杂度: O(N)
# 空间复杂度: O(1)
#
# 关键点:
# - atMost 技巧适用于数组中只有非负数的场景
# - atMost(k) - atMost(k-1) = 恰好等于 k 的数量
# - 如果可以使用前缀和+哈希表则数组可以有负数
