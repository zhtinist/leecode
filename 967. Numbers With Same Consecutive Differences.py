"""
LeetCode #967 - Numbers With Same Consecutive Differences
中文题名：连续差相同的数字
https://leetcode.com/problems/numbers-with-same-consecutive-differences/

Return all non-negative integers of length `N` such that the
absolute difference between every two consecutive digits is `K`.

Note that every number in the answer must not have leading
zeros except for the number `0` itself. For example,
`01` has one leading zero and is invalid, but `0` is valid.

You may return the answer in any order.

Example 1:

Input: N = 3, K = 7
Output: [181,292,707,818,929]
Explanation: Note that 070 is not a valid number, because it has leading zeroes.

Example 2:

Input: N = 2, K = 1
Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]

【中文翻译】
返回所有长度为 `N` 且满足每两个连续数字之间的绝对差为 `K` 的非负整数。
注意，答案中的每个数字都不能有前导零，数字 `0` 本身除外。例如，
`01` 有一个前导零，无效；但 `0` 有效。
可以按任意顺序返回答案。

"""

from typing import List, Optional


class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        if n == 1:
            return list(range(10))

        result = []

        def dfs(num: int, length: int) -> None:
            if length == n:
                result.append(num)
                return

            last_digit = num % 10

            # 下一个数字：last_digit + K
            if last_digit + k <= 9:
                dfs(num * 10 + last_digit + k, length + 1)

            # 下一个数字：last_digit - K（注意 K > 0 时避免重复）
            if k > 0 and last_digit - k >= 0:
                dfs(num * 10 + last_digit - k, length + 1)

        # 第一位不能是 0（除非 N=1，已处理）
        for first_digit in range(1, 10):
            dfs(first_digit, 1)

        return result



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用 DFS（深度优先搜索）逐位构建数字。
# 从第一位（1-9，不能是 0）开始，每次基于最后一位数字，尝试加上 K 或减去 K。
# 如果结果在 0-9 范围内，则将其添加到数字末尾，继续递归。
# 当数字长度达到 N 时，将其加入结果列表。
# 特殊情况：
# - K = 0 时，加 K 和减 K 结果相同，只需处理一次避免重复。
# - N = 1 时，返回 0-9 所有数字。
#
# 时间复杂度: O(2^N) — 每位最多 2 个分支
# 空间复杂度: O(2^N) — 存储所有结果和递归栈
#
# 关键点:
# - DFS 逐位构建数字
# - K = 0 时加和减结果相同，需去重
# - 第一位不能为 0（除非 N=1）
# - 使用整数构建而非字符串，更高效
