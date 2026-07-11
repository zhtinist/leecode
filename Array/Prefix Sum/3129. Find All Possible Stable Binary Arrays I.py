"""
LeetCode #3129 - Find All Possible Stable Binary Arrays I
找出所有稳定的二进制数组 I
https://leetcode.cn/problems/find-all-possible-stable-binary-arrays-i/

给你 3 个正整数 `num_zeros` ，`num_ones` 和 `limit` 。
一个 二进制数组 `arr` 如果满足以下条件，那么我们称它是 稳定的 ：
0 在 `arr` 中出现次数 恰好 为 `num_zeros` 。
1 在 `arr` 中出现次数 恰好 为 `num_ones` 。
`arr` 中每个长度超过 `limit` 的 子数组 都 同时 包含 0 和 1 。
请你返回一个整数表示 稳定 二进制数组的 总 数目。
由于答案可能很大，将它对 `10^9 + 7` 取余 后返回。

示例 1：

输入：zero = 1, one = 1, limit = 2
输出：2
解释：
两个稳定的二进制数组为 `[1,0]` 和 `[0,1]` ，两个数组都有一个 0 和一个 1 ，且没有子数组长度大于 2 。
示例 2：

输入：zero = 1, one = 2, limit = 1
输出：1
解释：
唯一稳定的二进制数组是 `[1,0,1]` 。
二进制数组 `[1,1,0]` 和 `[0,1,1]` 都有长度为 2 且元素全都相同的子数组，所以它们不稳定。
示例 3：

输入：zero = 3, one = 3, limit = 2
输出：14
解释：
所有稳定的二进制数组包括 `[0,0,1,0,1,1]` ，`[0,0,1,1,0,1]` ，`[0,1,0,0,1,1]` ，`[0,1,0,1,0,1]` ，`[0,1,0,1,1,0]` ，`[0,1,1,0,0,1]` ，`[0,1,1,0,1,0]` ，`[1,0,0,1,0,1]` ，`[1,0,0,1,1,0]` ，`[1,0,1,0,0,1]` ，`[1,0,1,0,1,0]` ，`[1,0,1,1,0,0]` ，`[1,1,0,0,1,0]` 和 `[1,1,0,1,0,0]` 。

提示：
`1 <= zero, one, limit <= 200`
"""

from typing import List, Optional


class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10 ** 9 + 7
        # dp0[i][j]: 用i个0和j个1组成且以0结尾的稳定数组数
        # dp1[i][j]: 用i个0和j个1组成且以1结尾的稳定数组数
        dp0 = [[0] * (one + 1) for _ in range(zero + 1)]
        dp1 = [[0] * (one + 1) for _ in range(zero + 1)]

        # 基础情况：全0或全1（长度不超过limit）
        for i in range(1, min(zero, limit) + 1):
            dp0[i][0] = 1
        for j in range(1, min(one, limit) + 1):
            dp1[0][j] = 1

        for i in range(zero + 1):
            for j in range(one + 1):
                if i + j == 0:
                    continue
                # 以0结尾：从dp1转移，在末尾添加k个0 (1 <= k <= min(i, limit))
                for k in range(1, min(i, limit) + 1):
                    dp0[i][j] = (dp0[i][j] + dp1[i - k][j]) % MOD
                # 以1结尾：从dp0转移，在末尾添加k个1 (1 <= k <= min(j, limit))
                for k in range(1, min(j, limit) + 1):
                    dp1[i][j] = (dp1[i][j] + dp0[i][j - k]) % MOD

        return (dp0[zero][one] + dp1[zero][one]) % MOD



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Dynamic Programming, Prefix Sum
#
# 解题思路:
# "稳定"意味着任何连续相同元素长度不超过limit。用DP分别计数以0结尾和以1结尾的数组。
# dp0[i][j]表示用i个0、j个1且以0结尾的方案数，dp1[i][j]同理。
# 转移时在末尾添加1到limit个相同元素（从相反结尾状态转移）。
# 最终答案为dp0[zero][one] + dp1[zero][one]。
#
# 时间复杂度: O(zero * one * limit)
# 空间复杂度: O(zero * one)
#
# 关键点:
# - 限制转化为连续same元素长度不超过limit
# - DP状态分为以0结尾和以1结尾
# - 转移时枚举添加k个相同元素（1<=k<=limit）
