"""
LeetCode #2466 - Count Ways To Build Good Strings
统计构造好字符串的方案数
https://leetcode.cn/problems/count-ways-to-build-good-strings/

给你整数 `zero` ，`one` ，`low` 和 `high` ，我们从空字符串开始构造一个字符串，每一步执行下面操作中的一种：
将 `'0'` 在字符串末尾添加 `zero`  次。
将 `'1'` 在字符串末尾添加 `one` 次。
以上操作可以执行任意次。
如果通过以上过程得到一个 长度 在 `low` 和 `high` 之间（包含上下边界）的字符串，那么这个字符串我们称为 好 字符串。
请你返回满足以上要求的 不同 好字符串数目。由于答案可能很大，请将结果对 `10^9 + 7` 取余 后返回。

示例 1：
输入：low = 3, high = 3, zero = 1, one = 1 输出：8 解释： 一个可能的好字符串是 "011" 。 可以这样构造得到："" -> "0" -> "01" -> "011" 。 从 "000" 到 "111" 之间所有的二进制字符串都是好字符串。
示例 2：
输入：low = 2, high = 3, zero = 1, one = 2 输出：5 解释：好字符串为 "00" ，"11" ，"000" ，"110" 和 "011" 。

提示：
`1 <= low <= high <= 10^5`
`1 <= zero, one <= low`
"""

from typing import List, Optional


class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 10 ** 9 + 7

        # dp[i] = 构成长度为 i 的字符串的方案数
        dp = [0] * (high + 1)
        dp[0] = 1  # 空字符串有一种方案

        for i in range(1, high + 1):
            if i >= zero:
                dp[i] = (dp[i] + dp[i - zero]) % MOD
            if i >= one:
                dp[i] = (dp[i] + dp[i - one]) % MOD

        # 累加长度在 [low, high] 之间的方案数
        ans = 0
        for i in range(low, high + 1):
            ans = (ans + dp[i]) % MOD

        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Dynamic Programming
#
# 解题思路:
# 动态规划。定义 dp[i] 为构成长度恰好为 i 的字符串的方案数。
# 状态转移：
#   - 如果最后一步追加了 zero 个 '0'，则方案来自 dp[i - zero]
#   - 如果最后一步追加了 one 个 '1'，则方案来自 dp[i - one]
#   - dp[i] = dp[i - zero] + dp[i - one]（需判断 i >= zero 和 i >= one）
# 初始状态：dp[0] = 1（空字符串只有一种构建方式）
# 最终答案为 sum(dp[low] ... dp[high])，对 10^9 + 7 取模。
#
# 时间复杂度: O(high)，对 1 到 high 每个长度计算一次
# 空间复杂度: O(high)，dp 数组长度为 high + 1
#
# 关键点:
# - 问题本质是求硬币找零的变体：两种面额 zero 和 one，凑出 [low, high] 区间金额的组合数
# - 每一步取模避免溢出
# - dp[0] = 1 是关键边界条件
