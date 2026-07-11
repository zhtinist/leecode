"""
LeetCode #2100 - Find Good Days to Rob the Bank
适合野炊的日子
https://leetcode.cn/problems/find-good-days-to-rob-the-bank/

你和朋友们准备去野炊。给你一个下标从 0 开始的整数数组 `security` ，其中 `security[i]` 是第 `i` 天的建议出行指数。日子从 `0` 开始编号。同时给你一个整数 `time` 。
如果第 `i` 天满足以下所有条件，我们称它为一个适合野炊的日子：
第 `i` 天前和后都分别至少有 `time` 天。
第 `i` 天前连续 `time` 天建议出行指数都是非递增的。
第 `i` 天后连续 `time` 天建议出行指数都是非递减的。
更正式的，第 `i` 天是一个适合野炊的日子当且仅当：`security[i - time] >= security[i - time + 1] >= ... >= security[i] <= ... <= security[i + time - 1] <= security[i + time]`.
请你返回一个数组，包含 所有 适合野炊的日子（下标从 0 开始）。返回的日子可以 任意 顺序排列。

示例 1：
输入：security = [5,3,3,3,5,6,2], time = 2 输出：[2,3] 解释： 第 2 天，我们有 security[0] >= security[1] >= security[2] <= security[3] <= security[4] 。 第 3 天，我们有 security[1] >= security[2] >= security[3] <= security[4] <= security[5] 。 没有其他日子符合这个条件，所以日子 2 和 3 是适合野炊的日子。
示例 2：
输入：security = [1,1,1,1,1], time = 0 输出：[0,1,2,3,4] 解释： 因为 time 等于 0 ，所以每一天都是适合野炊的日子，所以返回每一天。
示例 3：
输入：security = [1,2,3,4,5,6], time = 2 输出：[] 解释： 没有任何一天的前 2 天建议出行指数是非递增的。 所以没有适合野炊的日子，返回空数组。

提示：
`1 <= security.length <= 10^5`
`0 <= security[i], time <= 10^5`
"""

from typing import List, Optional


class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        left = [0] * n
        right = [0] * n

        for i in range(1, n):
            if security[i] <= security[i - 1]:
                left[i] = left[i - 1] + 1

        for i in range(n - 2, -1, -1):
            if security[i] <= security[i + 1]:
                right[i] = right[i + 1] + 1

        result = []
        for i in range(n):
            if left[i] >= time and right[i] >= time:
                result.append(i)

        return result



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Dynamic Programming, Prefix Sum
#
# 解题思路:
# 预处理两个数组 left 和 right：
# left[i] 记录在位置 i 之前（含 i）连续非递增的天数（即 security[i] <= security[i-1] 的连续长度）。
# right[i] 记录在位置 i 之后（含 i）连续非递减的天数（即 security[i] <= security[i+1] 的连续长度）。
# 遍历每一天 i，如果 left[i] >= time 且 right[i] >= time，则第 i 天是适合的日子。
#
# 时间复杂度: O(N)，其中N为数组长度。三次线性遍历：计算left、计算right、筛选结果。
# 空间复杂度: O(N)，需要两个辅助数组 left 和 right 存储连续天数。
#
# 关键点:
# - 正向遍历计算非递增连续长度，反向遍历计算非递减连续长度。
# - 条件是"非递增"和"非递减"，即允许相等的情况（<= 而非 <）。
# - 连续长度包含自身（初始为0），所以 left[i] >= time 表示前面至少有 time 天满足条件。
