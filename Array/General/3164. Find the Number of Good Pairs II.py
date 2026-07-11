"""
LeetCode #3164 - Find the Number of Good Pairs II
优质数对的总数 II
https://leetcode.cn/problems/find-the-number-of-good-pairs-ii/

给你两个整数数组 `nums1` 和 `nums2`，长度分别为 `n` 和 `m`。同时给你一个正整数 `k`。
如果 `nums1[i]` 可以被 `nums2[j] * k` 整除，则称数对 `(i, j)` 为 优质数对（`0 <= i <= n - 1`, `0 <= j <= m - 1`）。
返回 优质数对 的总数。

示例 1：

输入：nums1 = [1,3,4], nums2 = [1,3,4], k = 1
输出：5
解释：
5个优质数对分别是 `(0, 0)`, `(1, 0)`, `(1, 1)`, `(2, 0)`, 和 `(2, 2)`。
示例 2：

输入：nums1 = [1,2,4,12], nums2 = [2,4], k = 3
输出：2
解释：
2个优质数对分别是 `(3, 0)` 和 `(3, 1)`。

提示：
`1 <= n, m <= 10^5`
`1 <= nums1[i], nums2[j] <= 10^6`
`1 <= k <= 10^3`
"""

from typing import List, Optional


class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        max_val = max(nums1)

        # 统计nums1中每个值的出现次数
        freq1 = {}
        for x in nums1:
            freq1[x] = freq1.get(x, 0) + 1

        # 统计nums2中每个值的出现次数
        freq2 = {}
        for y in nums2:
            freq2[y] = freq2.get(y, 0) + 1

        ans = 0
        for y, cnt2 in freq2.items():
            target = y * k
            if target == 0:
                continue
            # 统计nums1中target的倍数
            for multiple in range(target, max_val + 1, target):
                if multiple in freq1:
                    ans += freq1[multiple] * cnt2

        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Hash Table
#
# 解题思路:
# 统计nums1和nums2中每个值的出现频率（去重）。对nums2中每个去重值y，
# 计算target = y*k，然后在[target, max(nums1)]范围内枚举target的所有倍数，
# 统计nums1中这些倍数的数量。每个倍数贡献freq1[multiple]*cnt2对。
# 利用值域上限（10^6）确保枚举倍数可行。
#
# 时间复杂度: O(max_val * H_max_val)，其中H为调和数（约log(max_val)）
# 空间复杂度: O(n + m)
#
# 关键点:
# - 频率统计去重减少计算量
# - 枚举倍数技巧：range(target, max_val+1, target)
# - target可能大于max_val直接跳过
