"""
LeetCode #2875 - Minimum Size Subarray in Infinite Array
无限数组的最短子数组
https://leetcode.cn/problems/minimum-size-subarray-in-infinite-array/

给你一个下标从 0 开始的数组 `nums` 和一个整数 `target` 。
下标从 0 开始的数组 `infinite_nums` 是通过无限地将 nums 的元素追加到自己之后生成的。
请你从 `infinite_nums` 中找出满足 元素和 等于 `target` 的 最短 子数组，并返回该子数组的长度。如果不存在满足条件的子数组，返回 `-1` 。

示例 1：
输入：nums = [1,2,3], target = 5 输出：2 解释：在这个例子中 infinite_nums = [1,2,3,1,2,3,1,2,...] 。 区间 [1,2] 内的子数组的元素和等于 target = 5 ，且长度 length = 2 。 可以证明，当元素和等于目标值 target = 5 时，2 是子数组的最短长度。
示例 2：
输入：nums = [1,1,1,2,3], target = 4 输出：2 解释：在这个例子中 infinite_nums = [1,1,1,2,3,1,1,1,2,3,1,1,...]. 区间 [4,5] 内的子数组的元素和等于 target = 4 ，且长度 length = 2 。 可以证明，当元素和等于目标值 target = 4 时，2 是子数组的最短长度。
示例 3：
输入：nums = [2,4,6,8], target = 3 输出：-1 解释：在这个例子中 infinite_nums = [2,4,6,8,2,4,6,8,...] 。 可以证明，不存在元素和等于目标值 target = 3 的子数组。

提示：
`1 <= nums.length <= 10^5`
`1 <= nums[i] <= 10^5`
`1 <= target <= 10^9`
"""

from typing import List, Optional


class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        n = len(nums)

        # min_len[s] = minimum subarray length in doubled array with sum s
        # Only need sums up to min(target, 2 * total)
        def min_subarray_len(goal: int) -> int:
            prefix = {0: -1}
            cur = 0
            best = float('inf')
            for i in range(2 * n):
                cur += nums[i % n]
                need = cur - goal
                if need in prefix:
                    best = min(best, i - prefix[need])
                prefix[cur] = i
            return best if best != float('inf') else -1

        q, r = divmod(target, total)

        # Case 1: r == 0
        ans = float('inf')
        if r == 0:
            ans = q * n

        # Case 2: r > 0, use q full copies
        if r > 0:
            L = min_subarray_len(r)
            if L != -1:
                ans = min(ans, q * n + L)

        # Case 3: use q-1 copies (if q >= 1), remainder r + total
        if q >= 1:
            L = min_subarray_len(r + total)
            if L != -1:
                ans = min(ans, (q - 1) * n + L)

        return -1 if ans == float('inf') else ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Hash Table, Prefix Sum, Sliding Window
#
# 解题思路:
# 设 total = sum(nums)，target = q * total + r。考虑两种情况：
# (1) 使用 q 个完整数组 + 一个和为 r 的子数组；(2) 使用 q-1 个完整数组 + 一个和为 r+total 的子数组。
# 对于子数组部分，使用前缀和+哈希表在双倍数组（nums+nums）中查找最短子数组长度。
# 取两种情况的最小值作为答案。
#
# 时间复杂度: O(n)
# 空间复杂度: O(n)
#
# 关键点:
# - 子数组可以跨越数组边界，使用双倍数组处理循环情况
# - 考虑两种完整数组数量的情况（q 或 q-1），取较小长度
# - 前缀和哈希表查找 O(1)，注意边界（子数组长度不超过 2n）
