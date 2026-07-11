"""
LeetCode #870 - Advantage Shuffle
中文题名：优势洗牌
https://leetcode.com/problems/advantage-shuffle/

Given two arrays `A` and `B` of equal size, the advantage of `A`
with respect to `B` is the number of indices `i` for which
`A[i] > B[i]`.

Return any permutation of `A` that maximizes its advantage with
respect to `B`.

Example 1:

Input: A = [2,7,11,15], B = [1,10,4,11]
Output: [2,11,7,15]

Example 2:

Input: A = [12,24,8,32], B = [13,25,32,11]
Output: [24,32,8,12]

Note:

`1 <= A.length = B.length <= 10000`

`0 <= A[i] <= 10^9`

`0 <= B[i] <= 10^9`

【中文翻译】
给定两个大小相等的数组 A 和 B，A 相对于 B 的优势是满足 A[i] > B[i] 的索引 i 的数量。
返回 A 的任意排列，使其相对于 B 的优势最大化。

"""

from typing import List, Optional


class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        # 对 A 排序（从小到大）
        sorted_a = sorted(nums1)
        # 记录 B 中每个值对应的原始索引
        # 因为 B 可能有重复元素，需要用 list of pairs
        b_with_idx = sorted([(val, i) for i, val in enumerate(nums2)], key=lambda x: x[0])

        res = [0] * n
        # 双指针：left 指向 sorted_a 的开头（上等马），right 指向 sorted_a 的末尾（下等马）
        left, right = 0, n - 1

        # 从大到小处理 B（田忌赛马策略）
        for val, idx in reversed(b_with_idx):
            if sorted_a[right] > val:
                # A 中最大的能赢 B 中当前最大的，就用它
                res[idx] = sorted_a[right]
                right -= 1
            else:
                # A 中最大的也赢不了，就用 A 中最小的去当"炮灰"
                res[idx] = sorted_a[left]
                left += 1

        return res



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 经典的"田忌赛马"贪心策略。将 A 排序，同时记录 B 中每个元素的原始索引并按值排序。
# 然后从大到小处理 B 中的每个元素：
#   - 如果 A 中当前最大的元素 > B 中当前最大的元素，则用 A 的这个元素应对 B 的该元素（获得优势）；
#   - 否则，用 A 中最小的元素去"当炮灰"应对 B 的该元素（放弃这局，保留强马）。
# 这正是田忌赛马的"以上驷对中驷，以中驷对下驷，以下驷对上驷"策略。
#
# 时间复杂度: O(N log N)，主要来自排序
# 空间复杂度: O(N)，存储结果数组和带索引的 B 排序数组
#
# 关键点:
# - 田忌赛马贪心策略：强对强，弱对弱
# - 需要保留 B 的原始索引以正确输出结果
# - 从大到小处理 B，双指针在排序后的 A 上移动
