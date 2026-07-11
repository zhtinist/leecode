"""
LeetCode #2266 - Count Number of Texts
统计打字方案数
https://leetcode.cn/problems/count-number-of-texts/

Alice 在给 Bob 用手机打字。数字到字母的 对应 如下图所示。

为了 打出 一个字母，Alice 需要 按 对应字母 `i` 次，`i` 是该字母在这个按键上所处的位置。
比方说，为了按出字母 `'s'` ，Alice 需要按 `'7'` 四次。类似的， Alice 需要按 `'5'` 两次得到字母  `'k'` 。
注意，数字 `'0'` 和 `'1'` 不映射到任何字母，所以 Alice 不 使用它们。
但是，由于传输的错误，Bob 没有收到 Alice 打字的字母信息，反而收到了 按键的字符串信息 。
比方说，Alice 发出的信息为 `"bob"` ，Bob 将收到字符串 `"2266622"` 。
给你一个字符串 `pressedKeys` ，表示 Bob 收到的字符串，请你返回 Alice 总共可能发出多少种文字信息 。
由于答案可能很大，将它对 `10^9 + 7` 取余 后返回。

示例 1：
输入：pressedKeys = "22233" 输出：8 解释： Alice 可能发出的文字信息包括： "aaadd", "abdd", "badd", "cdd", "aaae", "abe", "bae" 和 "ce" 。 由于总共有 8 种可能的信息，所以我们返回 8 。
示例 2：
输入：pressedKeys = "222222222222222222222222222222222222" 输出：82876089 解释： 总共有 2082876103 种 Alice 可能发出的文字信息。 由于我们需要将答案对 10^9 + 7 取余，所以我们返回 2082876103 % (10^9 + 7) = 82876089 。

提示：
`1 <= pressedKeys.length <= 10^5`
`pressedKeys` 只包含数字 `'2'` 到 `'9'` 。
"""

from typing import List, Optional


class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        """
        Count the number of possible original text messages.
        The key insight: runs of identical digits are independent.
        For a run of digit 'd', max consecutive presses that could represent one letter:
        - '7' and '9' map to 4 letters (max press = 4)
        - All other digits ('2','3','4','5','6','8') map to 3 letters (max press = 3)
        Use DP: dp[i] = number of ways to decode a run of length i.
        Finally, multiply the ways for all runs together.
        """
        MOD = 10**9 + 7
        n = len(pressedKeys)

        # Precompute DP for run lengths up to n
        dp3 = [0] * (n + 1)  # for digits with max 3 presses
        dp4 = [0] * (n + 1)  # for digits with max 4 presses
        dp3[0] = dp4[0] = 1

        for i in range(1, n + 1):
            # For max 3 presses
            for j in range(1, 4):
                if i - j >= 0:
                    dp3[i] = (dp3[i] + dp3[i - j]) % MOD
            # For max 4 presses
            for j in range(1, 5):
                if i - j >= 0:
                    dp4[i] = (dp4[i] + dp4[i - j]) % MOD

        # Identify consecutive runs of the same digit
        result = 1
        i = 0
        while i < n:
            j = i
            while j < n and pressedKeys[j] == pressedKeys[i]:
                j += 1
            run_len = j - i

            if pressedKeys[i] in ('7', '9'):
                result = (result * dp4[run_len]) % MOD
            else:
                result = (result * dp3[run_len]) % MOD

            i = j

        return result


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Hash Table, Math, String, Dynamic Programming
#
# 解题思路:
# 问题的核心在于理解连续相同数字的区段是相互独立的——因为不同数字之间必须分割。
# 例如 "22233" 中，三个连续的 '2' 组成一个区段，两个连续的 '3' 组成另一个区段。
# 对于每个区段，问题转化为：将长度为 L 的区段划分为若干组，每组长度在 1~max_press 之间
# （'7'和'9'的 max_press=4，其余数字的 max_press=3），求划分方案数。
# 这是一个标准的 DP 问题：dp[i] = sum(dp[i-1] + dp[i-2] + dp[i-3])（普通键）
# 或 dp[i] = sum(dp[i-1] + dp[i-2] + dp[i-3] + dp[i-4])（'7'和'9'）。
# 最终答案为所有区段方案数的乘积。
#
# 时间复杂度: O(n)，其中 n 是字符串长度。DP 预计算 O(n)，遍历分区段 O(n)。
# 空间复杂度: O(n)，用于 DP 数组。可优化为 O(1)，但 n <= 10^5 完全够用。
#
# 关键点:
# - 将问题分解为独立区段：连续相同数字不可跨越分割
# - '7' 和 '9' 对应 4 个字母（pqrs 和 wxyz），最多连续 4 次按键表示一个字母
# - 其他数字对应 3 个字母，最多连续 3 次按键表示一个字母
# - 每个区段内部是一个类爬楼梯的 DP 问题
# - 各独立区段的方案数相乘得到最终答案
