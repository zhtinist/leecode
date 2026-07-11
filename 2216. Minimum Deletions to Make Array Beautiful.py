"""
LeetCode #2216 - Minimum Deletions to Make Array Beautiful
美化数组的最少删除数
https://leetcode.cn/problems/minimum-deletions-to-make-array-beautiful/

给你一个下标从 0 开始的整数数组 `nums` ，如果满足下述条件，则认为数组 `nums` 是一个 美丽数组 ：
`nums.length` 为偶数
对所有满足 `i % 2 == 0` 的下标 `i` ，`nums[i] != nums[i + 1]` 均成立
注意，空数组同样认为是美丽数组。
你可以从 `nums` 中删除任意数量的元素。当你删除一个元素时，被删除元素右侧的所有元素将会向左移动一个单位以填补空缺，而左侧的元素将会保持 不变 。
返回使 `nums` 变为美丽数组所需删除的 最少 元素数目。

示例 1：
输入：nums = [1,1,2,3,5] 输出：1 解释：可以删除 `nums[0]` 或 `nums[1]` ，这样得到的 `nums` = [1,2,3,5] 是一个美丽数组。可以证明，要想使 nums 变为美丽数组，至少需要删除 1 个元素。
示例 2：
输入：nums = [1,1,2,2,3,3] 输出：2 解释：可以删除 `nums[0]` 和 `nums[5]` ，这样得到的 nums = [1,2,2,3] 是一个美丽数组。可以证明，要想使 nums 变为美丽数组，至少需要删除 2 个元素。

提示：
`1 <= nums.length <= 10^5`
`0 <= nums[i] <= 10^5`
"""

from typing import List, Optional


class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        deletions = 0
        n = len(nums)

        # i iterates through the original array;
        # the effective index in the final (undeleted) array is (i - deletions)
        for i in range(n - 1):
            # Check if current element would be at an even index in the final array
            if (i - deletions) % 2 == 0:
                # If it equals the next element that would be at odd index,
                # we must delete this element (the one at even index)
                if nums[i] == nums[i + 1]:
                    deletions += 1

        # After processing, if the remaining length is odd,
        # delete one more to make it even
        remaining = n - deletions
        if remaining % 2 == 1:
            deletions += 1

        return deletions


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Stack, Greedy, Array
#
# 解题思路:
# 1. 美丽数组的两个条件：
#    a) 长度为偶数。
#    b) 对于所有偶数下标 i，nums[i] != nums[i+1]。
# 2. 贪心策略：从左到右遍历数组，模拟构建最终的美丽数组。
#    使用 deletions 变量记录已删除的元素个数。
#    对于当前位置 i，它在最终数组中的有效下标为 i - deletions。
# 3. 当有效下标为偶数时，当前元素将与下一个元素配对（下一个元素在奇数下标）。
#    如果 nums[i] == nums[i+1]，则违反了条件：
#    - 我们可以删除当前元素（i 位置），这样下一个元素会左移到偶数位置，
#      它与后面的元素重新配对。这是贪心的最优选择。
# 4. 遍历结束后，检查剩余数组的长度 (n - deletions)：
#    - 如果是奇数，需要再删除一个元素（最后一个元素没有配对对象），
#      可以直接删除最后一个元素使长度变为偶数。
#
# 时间复杂度: O(N)，只需一次线性遍历。
# 空间复杂度: O(1)，只使用常数额外空间。
#
# 关键点:
# - 使用 i - deletions 来追踪元素在最终数组中的实际位置，避免实际修改数组。
# - 贪心选择：当遇到冲突时删除偶数位置的元素（而非奇数位置的），
#   因为删除偶数位置可以保留更多元素用于后续配对。
# - 最后必须确保剩余长度为偶数，若为奇数则追加一次删除。
