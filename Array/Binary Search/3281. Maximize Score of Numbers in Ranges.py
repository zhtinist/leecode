"""
LeetCode #3281 - Maximize Score of Numbers in Ranges
范围内整数的最大得分
https://leetcode.cn/problems/maximize-score-of-numbers-in-ranges/

给你一个整数数组 `start` 和一个整数 `d`，代表 `n` 个区间 `[start[i], start[i] + d]`。
你需要选择 `n` 个整数，其中第 `i` 个整数必须属于第 `i` 个区间。所选整数的 得分 定义为所选整数两两之间的 最小 绝对差。
返回所选整数的 最大可能得分 。

示例 1：

输入： start = [6,0,3], d = 2
输出： 4
解释：
可以选择整数 8, 0 和 4 获得最大可能得分，得分为 `min(|8 - 0|, |8 - 4|, |0 - 4|)`，等于 4。
示例 2：

输入： start = [2,6,13,13], d = 5
输出： 5
解释：
可以选择整数 2, 7, 13 和 18 获得最大可能得分，得分为 `min(|2 - 7|, |2 - 13|, |2 - 18|, |7 - 13|, |7 - 18|, |13 - 18|)`，等于 5。

提示：
`2 <= start.length <= 10^5`
`0 <= start[i] <= 10^9`
`0 <= d <= 10^9`
"""

from typing import List, Optional


class Solution:
    def maxPossibleScore(self, start: List[int], d: int) -> int:
        start.sort()
        n = len(start)

        def check(mid: int) -> bool:
            # 贪心：每个区间选尽可能小的值，且与上一个值的间隔 >= mid
            prev = start[0]  # 第一个选区间左端点
            for i in range(1, n):
                # 下一个至少要比 prev 大 mid
                nxt = prev + mid
                if nxt > start[i] + d:
                    return False
                prev = max(nxt, start[i])
            return True

        lo, hi = 0, start[-1] + d - start[0]
        ans = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if check(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return ans










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Array, Binary Search, Sorting
#
# 解题思路:
# 最大化最小值 → 二分答案。
# 对 start 排序后，二分可能的得分 mid。
# check(mid): 贪心验证能否使相邻数字差 >= mid。
# 第一个数字选 start[0]（尽量小），后续每个数字尽量小但保证与前一个的差 >= mid。
# 如果某个数字无法在其区间内找到合法值，mid 不可行。
#
# 时间复杂度: O(n log n + n log(range))
# 空间复杂度: O(1)
#
# 关键点:
# - "最大化最小差值" 是典型的二分答案模式
# - 贪心放置：每个数尽量小，为后面的数留更多空间
