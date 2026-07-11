"""
LeetCode #2698 - Find the Punishment Number of an Integer
求一个整数的惩罚数
https://leetcode.cn/problems/find-the-punishment-number-of-an-integer/

给你一个正整数 `n` ，请你返回 `n` 的 惩罚数 。
`n` 的 惩罚数 定义为所有满足以下条件 `i` 的数的平方和：
`1 <= i <= n`
`i * i` 的十进制表示的字符串可以分割成若干连续子字符串，且这些子字符串对应的整数值之和等于 `i` 。

示例 1：
输入：n = 10 输出：182 解释：总共有 3 个范围在 [1, 10] 的整数 i 满足要求： - 1 ，因为 1 * 1 = 1 - 9 ，因为 9 * 9 = 81 ，且 81 可以分割成 8 + 1 。 - 10 ，因为 10 * 10 = 100 ，且 100 可以分割成 10 + 0 。 因此，10 的惩罚数为 1 + 81 + 100 = 182
示例 2：
输入：n = 37 输出：1478 解释：总共有 4 个范围在 [1, 37] 的整数 i 满足要求： - 1 ，因为 1 * 1 = 1 - 9 ，因为 9 * 9 = 81 ，且 81 可以分割成 8 + 1 。 - 10 ，因为 10 * 10 = 100 ，且 100 可以分割成 10 + 0 。 - 36 ，因为 36 * 36 = 1296 ，且 1296 可以分割成 1 + 29 + 6 。 因此，37 的惩罚数为 1 + 81 + 100 + 1296 = 1478

提示：
`1 <= n <= 1000`
"""

from typing import List, Optional


class Solution:
    def punishmentNumber(self, n: int) -> int:
        def can_partition(s: str, target: int, idx: int, cur_sum: int) -> bool:
            if idx == len(s):
                return cur_sum == target
            num = 0
            for i in range(idx, len(s)):
                num = num * 10 + int(s[i])
                if cur_sum + num > target:
                    break
                if can_partition(s, target, i + 1, cur_sum + num):
                    return True
            return False

        total = 0
        for i in range(1, n + 1):
            sq = i * i
            if can_partition(str(sq), i, 0, 0):
                total += sq
        return total



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Math, Backtracking
#
# 解题思路:
# 对1到n的每个数i，检查i*i的十进制字符串能否分割成若干子串使数值之和等于i。
# 使用回溯法枚举所有分割方式：从当前位置开始，取不同长度的子串转为数值，
# 累加到当前和，递归处理剩余部分。剪枝：当前和超过目标时停止。
#
# 时间复杂度: O(n * 2^d) 其中d是i*i的位数（最多7位，n<=1000时i*i<=10^6）
# 空间复杂度: O(d) 递归深度
#
# 关键点:
# - 回溯枚举所有分割方式
# - 剪枝：cur_sum + num > target时停止
# - 惩罚数是所有满足条件的i的平方和，不是i的和
