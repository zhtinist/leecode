"""
LeetCode #869 - Reordered Power of 2
中文题名：重新排序得到 2 的幂
https://leetcode.com/problems/reordered-power-of-2/

Starting with a positive integer `N`, we reorder the digits in any order
(including the original order) such that the leading digit is not zero.

Return `true` if and only if we can do this in a way such that the resulting
number is a power of 2.

Example 1:

Input: 1
Output: true

Example 2:

Input: 10
Output: false

Example 3:

Input: 16
Output: true

Example 4:

Input: 24
Output: false

Example 5:

Input: 46
Output: true

Note:

`1 <= N <= 10^9`

【中文翻译】
给定一个正整数 N，我们按任何顺序（包括原始顺序）将数字重新排序，注意前导数字不能为零。
如果我们可以通过上述方式得到一个 2 的幂，返回 true；否则返回 false。

"""

from typing import List, Optional
from collections import Counter


class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        # 统计 N 中每个数字(0-9)出现的频次
        count_n = Counter(str(n))
        # 遍历所有 2 的幂，范围 [1, 10^9]，即 2^0 到 2^29
        for i in range(30):
            power_of_2 = str(1 << i)
            # 长度不同直接跳过
            if len(power_of_2) != len(str(n)):
                continue
            # 比较数字频次是否相同
            if Counter(power_of_2) == count_n:
                return True
        return False



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 由于 N 的范围是 [1, 10^9]，2 的幂只需要考虑 2^0 ~ 2^29（因为 2^29 = 536870912，
# 2^30 > 10^9）。核心思路是：统计 N 中每个数字(0-9)的出现频次，然后遍历这 30 个 2 的幂，
# 检查是否有某个 2 的幂的数字频次与 N 完全一致。如果一致，说明可以通过重排 N 的数字得到
# 该 2 的幂。由于比较的是数字频次而非排列顺序，避开了首零问题：只要有一个 2 的幂与 N 的
# 数字组成完全一致，就必然存在一种不以 0 开头的排列方式（即该 2 的幂本身）。
#
# 时间复杂度: O(log N) = O(1)，因为 N 最多 10 位，2 的幂最多 30 个
# 空间复杂度: O(1)，Counter 最多存 10 个数字的频率
#
# 关键点:
# - 将问题转化为"数字频次匹配"问题，避免生成所有排列
# - 2 的幂只有 30 种可能（2^0 ~ 2^29），可以直接枚举
# - 先比较字符串长度可以快速过滤不匹配的情况
