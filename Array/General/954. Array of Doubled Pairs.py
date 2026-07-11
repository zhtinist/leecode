"""
LeetCode #954 - Array of Doubled Pairs
中文题名：二倍数对数组
https://leetcode.com/problems/array-of-doubled-pairs/

Given an array of integers `A` with even length, return `true` if
and only if it is possible to reorder it such that `A[2 * i + 1] = 2 * A[2 * i]`
for every `0 <= i < len(A) / 2`.

【中文翻译】
给定一个长度为偶数的整数数组 `A`，只有可以将其重新排序使得对于每个
`0 <= i < len(A) / 2` 都有 `A[2 * i + 1] = 2 * A[2 * i]` 时，
才返回 `true`。

"""

from typing import List, Optional
from collections import Counter


class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        count = Counter(arr)
        # 按绝对值从小到大排序，确保先处理较小的数
        for x in sorted(count.keys(), key=abs):
            if count[x] == 0:
                continue
            if count[2 * x] < count[x]:
                return False
            count[2 * x] -= count[x]
        return True



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用哈希表统计每个数字出现的次数。按绝对值从小到大排序后，依次处理每个数字 x：
# 如果 x 已经被配对完（计数为 0），跳过；
# 如果 2*x 的剩余数量不足以配对当前 x，返回 False；
# 否则将 2*x 的计数减去 x 的计数，表示这些配对已完成。
# 按绝对值排序的关键原因：负数情况下，-4 的"两倍"是 -8，而 -8 的绝对值更大，
# 必须先配对绝对值小的数，否则会出现错误配对。
#
# 时间复杂度: O(N log N) — 排序开销
# 空间复杂度: O(N) — 哈希表存储计数
#
# 关键点:
# - 按绝对值排序，而非按数值排序（处理负数的关键）
# - 对于每个 x，配对目标是 2*x
# - 使用 Counter 高效管理计数
