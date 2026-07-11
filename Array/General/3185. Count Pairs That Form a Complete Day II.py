"""
LeetCode #3185 - Count Pairs That Form a Complete Day II
构成整天的下标对数目 II
https://leetcode.cn/problems/count-pairs-that-form-a-complete-day-ii/

给你一个整数数组 `hours`，表示以 小时 为单位的时间，返回一个整数，表示满足 `i < j` 且 `hours[i] + hours[j]` 构成 整天 的下标对 `i`, `j` 的数目。
整天 定义为时间持续时间是 24 小时的 整数倍 。
例如，1 天是 24 小时，2 天是 48 小时，3 天是 72 小时，以此类推。

示例 1：

输入： hours = [12,12,30,24,24]
输出： 2
解释：
构成整天的下标对分别是 `(0, 1)` 和 `(3, 4)`。
示例 2：

输入： hours = [72,48,24,3]
输出： 3
解释：
构成整天的下标对分别是 `(0, 1)`、`(0, 2)` 和 `(1, 2)`。

提示：
`1 <= hours.length <= 5 * 10^5`
`1 <= hours[i] <= 10^9`
"""

from typing import List, Optional


class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        cnt = [0] * 24
        for h in hours:
            cnt[h % 24] += 1

        ans = cnt[0] * (cnt[0] - 1) // 2
        ans += cnt[12] * (cnt[12] - 1) // 2
        for r in range(1, 12):
            ans += cnt[r] * cnt[24 - r]
        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Hash Table, Counting
#
# 解题思路:
# 两数之和能被24整除等价于两数的余数之和为0或24。统计每个余数的频率，
# 余数为0和12的情况内部配对（C(cnt,2)），其余情况余数r和24-r配对（cnt[r]*cnt[24-r]）。
# 注意只计算r从1到11，避免重复计算。
#
# 时间复杂度: O(n)
# 空间复杂度: O(24) = O(1)
#
# 关键点:
# - 取模后问题简化为和等于0或24
# - 余数为0和12内部组合
# - r从1到11避免重复配对
