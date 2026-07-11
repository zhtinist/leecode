"""
LeetCode #2028 - Find Missing Observations
找出缺失的观测数据
https://leetcode.cn/problems/find-missing-observations/

现有一份 `n + m` 次投掷单个 六面 骰子的观测数据，骰子的每个面从 `1` 到 `6` 编号。观测数据中缺失了 `n` 份，你手上只拿到剩余 `m` 次投掷的数据。幸好你有之前计算过的这 `n + m` 次投掷数据的 平均值 。
给你一个长度为 `m` 的整数数组 `rolls` ，其中 `rolls[i]` 是第 `i` 次观测的值。同时给你两个整数 `mean` 和 `n` 。
返回一个长度为 `n` 的数组，包含所有缺失的观测数据，且满足这 `n + m` 次投掷的 平均值 是 `mean` 。如果存在多组符合要求的答案，只需要返回其中任意一组即可。如果不存在答案，返回一个空数组。
`k` 个数字的 平均值 为这些数字求和后再除以 `k` 。
注意 `mean` 是一个整数，所以 `n + m` 次投掷的总和需要被 `n + m` 整除。

示例 1：
输入：rolls = [3,2,4,3], mean = 4, n = 2 输出：[6,6] 解释：所有 n + m 次投掷的平均值是 (3 + 2 + 4 + 3 + 6 + 6) / 6 = 4 。
示例 2：
输入：rolls = [1,5,6], mean = 3, n = 4 输出：[2,3,2,2] 解释：所有 n + m 次投掷的平均值是 (1 + 5 + 6 + 2 + 3 + 2 + 2) / 7 = 3 。
示例 3：
输入：rolls = [1,2,3,4], mean = 6, n = 4 输出：[] 解释：无论丢失的 4 次数据是什么，平均值都不可能是 6 。
示例 4：
输入：rolls = [1], mean = 3, n = 1 输出：[5] 解释：所有 n + m 次投掷的平均值是 (1 + 5) / 2 = 3 。

提示：
`m == rolls.length`
`1 <= n, m <= 10^5`
`1 <= rolls[i], mean <= 6`
"""

from typing import List, Optional


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        total = mean * (m + n)
        known_sum = sum(rolls)
        missing_sum = total - known_sum

        # Each missing roll must be between 1 and 6
        if missing_sum < n or missing_sum > 6 * n:
            return []

        # Distribute missing_sum across n rolls
        base = missing_sum // n
        remainder = missing_sum % n
        result = [base] * n
        for i in range(remainder):
            result[i] += 1
        return result



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Math, Simulation
#
# 解题思路:
# 先计算所有n+m次投掷的总和 = mean * (n+m)。
# 减去已知的m次总和得到缺失部分的总和missing_sum。
# 检查missing_sum是否在[n, 6n]范围内（每次投掷取值范围1-6）。
# 如果可以，平均分配：base = missing_sum // n, 前remainder个再加1。
#
# 时间复杂度: O(n + m)
# 空间复杂度: O(n) 返回答案数组
#
# 关键点:
# - 骰子每面只能是1到6
# - 总和必须在合理范围内
# - 平均分配后前几个加1保证总和正确
