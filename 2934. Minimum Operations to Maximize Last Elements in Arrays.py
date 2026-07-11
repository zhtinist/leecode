"""
LeetCode #2934 - Minimum Operations to Maximize Last Elements in Arrays
最大化数组末位元素的最少操作次数
https://leetcode.cn/problems/minimum-operations-to-maximize-last-elements-in-arrays/

给你两个下标从 0 开始的整数数组 `nums1` 和 `nums2` ，这两个数组的长度都是 `n` 。
你可以执行一系列 操作（可能不执行）。
在每次操作中，你可以选择一个在范围 `[0, n - 1]` 内的下标 `i` ，并交换 `nums1[i]` 和 `nums2[i]` 的值。
你的任务是找到满足以下条件所需的 最小 操作次数：
`nums1[n - 1]` 等于 `nums1` 中所有元素的 最大值 ，即 `nums1[n - 1] = max(nums1[0], nums1[1], ..., nums1[n - 1])` 。
`nums2[n - 1]` 等于 `nums2` 中所有元素的 最大值 ，即 `nums2[n - 1] = max(nums2[0], nums2[1], ..., nums2[n - 1])` 。
以整数形式，表示并返回满足上述 全部 条件所需的 最小 操作次数，如果无法同时满足两个条件，则返回 `-1` 。

示例 1：
输入：nums1 = [1,2,7]，nums2 = [4,5,3] 输出：1 解释：在这个示例中，可以选择下标 i = 2 执行一次操作。 交换 nums1[2] 和 nums2[2] 的值，nums1 变为 [1,2,3] ，nums2 变为 [4,5,7] 。 同时满足两个条件。 可以证明，需要执行的最小操作次数为 1 。 因此，答案是 1 。
示例 2：
输入：nums1 = [2,3,4,5,9]，nums2 = [8,8,4,4,4] 输出：2 解释：在这个示例中，可以执行以下操作： 首先，选择下标 i = 4 执行操作。 交换 nums1[4] 和 nums2[4] 的值，nums1 变为 [2,3,4,5,4] ，nums2 变为 [8,8,4,4,9] 。 然后，选择下标 i = 3 执行操作。 交换 nums1[3] 和 nums2[3] 的值，nums1 变为 [2,3,4,4,4] ，nums2 变为 [8,8,4,5,9] 。 同时满足两个条件。  可以证明，需要执行的最小操作次数为 2 。  因此，答案是 2 。
示例 3：
输入：nums1 = [1,5,4]，nums2 = [2,5,3] 输出：-1 解释：在这个示例中，无法同时满足两个条件。 因此，答案是 -1 。

提示：
`1 <= n == nums1.length == nums2.length <= 1000`
`1 <= nums1[i] <= 10^9`
`1 <= nums2[i] <= 10^9`
"""

from typing import List, Optional


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        INF = 10**9

        def solve(swap_last: bool) -> int:
            max1 = nums2[n - 1] if swap_last else nums1[n - 1]
            max2 = nums1[n - 1] if swap_last else nums2[n - 1]
            ops = 1 if swap_last else 0
            for i in range(n - 1):
                a, b = nums1[i], nums2[i]
                keep_ok = (a <= max1 and b <= max2)
                swap_ok = (b <= max1 and a <= max2)
                if not keep_ok and not swap_ok:
                    return INF
                if not keep_ok:
                    ops += 1
                # if both OK, keep (no swap) — already counted as 0 extra ops
                # if keep_ok and not swap_ok: ops += 0
                # if swap_ok and not keep_ok: ops += 1
                # if both: ops += 0
            return ops

        ans = min(solve(False), solve(True))
        return -1 if ans == INF else ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Enumeration
#
# 解题思路:
# 枚举最后一个位置是否交换（2种情况）。对于每种情况，确定了 nums1[n-1] 和 nums2[n-1] 的最终值作为各自数组的最大值。
# 然后遍历前 n-1 个位置，对每个位置检查保持不变或交换后是否满足不大于各自最大值的要求。
# 优先选择不交换（操作数最小），取所有可行情况的最小操作数。
#
# 时间复杂度: O(n)
# 空间复杂度: O(1)
#
# 关键点:
# - 枚举最后一位是否交换（2种case）
# - 每个位置独立决策：保持或交换，选操作少的可行方案
# - 若某位置两种方案都不可行，该case无解
