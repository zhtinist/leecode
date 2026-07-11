"""
LeetCode #2110 - Number of Smooth Descent Periods of a Stock
股票平滑下跌阶段的数目
https://leetcode.cn/problems/number-of-smooth-descent-periods-of-a-stock/

给你一个整数数组 `prices` ，表示一支股票的历史每日股价，其中 `prices[i]` 是这支股票第 `i` 天的价格。
一个 平滑下降的阶段 定义为：对于 连续一天或者多天 ，每日股价都比 前一日股价恰好少 `1` ，这个阶段第一天的股价没有限制。
请你返回 平滑下降阶段 的数目。

示例 1：
输入：prices = [3,2,1,4] 输出：7 解释：总共有 7 个平滑下降阶段： [3], [2], [1], [4], [3,2], [2,1] 和 [3,2,1] 注意，仅一天按照定义也是平滑下降阶段。
示例 2：
输入：prices = [8,6,7,7] 输出：4 解释：总共有 4 个连续平滑下降阶段：[8], [6], [7] 和 [7] 由于 8 - 6 ≠ 1 ，所以 [8,6] 不是平滑下降阶段。
示例 3：
输入：prices = [1] 输出：1 解释：总共有 1 个平滑下降阶段：[1]

提示：
`1 <= prices.length <= 10^5`
`1 <= prices[i] <= 10^5`
"""

from typing import List, Optional


class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)
        total = 0
        length = 1

        for i in range(1, n):
            if prices[i] == prices[i - 1] - 1:
                length += 1
            else:
                total += length * (length + 1) // 2
                length = 1

        total += length * (length + 1) // 2
        return total



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Math, Two Pointers, Dynamic Programming, Sliding Window
#
# 解题思路:
# 遍历价格数组，统计连续满足 prices[i] == prices[i-1] - 1 的区段长度。
# 对于一个长度为 L 的连续平滑下降区段，其包含的所有子区段（包括单个元素）数量
# 等于 L * (L + 1) / 2（即1+2+...+L）。
# 遇到不满足条件的位置时，结算当前区段计数并重置长度为1。
# 遍历结束后需要再结算一次最后一个区段。
#
# 时间复杂度: O(N)，一次线性遍历。
# 空间复杂度: O(1)，仅使用常数额外空间。
#
# 关键点:
# - 长度为L的连续区段包含 L*(L+1)//2 个子区段（每个子区段对应一个平滑下降阶段）。
# - 注意条件为"恰好少1"（prices[i] == prices[i-1] - 1），不是任意下降。
# - 单个元素也视为一个平滑下降阶段（长度为1，贡献为1）。
