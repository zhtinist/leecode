"""
LeetCode #3211 - Generate Binary Strings Without Adjacent Zeros
生成不含相邻零的二进制字符串
https://leetcode.cn/problems/generate-binary-strings-without-adjacent-zeros/

给你一个正整数 `n`。
如果一个二进制字符串 `x` 的所有长度为 2 的子字符串中包含 至少 一个 `"1"`，则称 `x` 是一个 有效 字符串。
返回所有长度为 `n` 的 有效 字符串，可以以任意顺序排列。

示例 1：

输入： n = 3
输出： ["010","011","101","110","111"]
解释：
长度为 3 的有效字符串有：`"010"`、`"011"`、`"101"`、`"110"` 和 `"111"`。
示例 2：

输入： n = 1
输出： ["0","1"]
解释：
长度为 1 的有效字符串有：`"0"` 和 `"1"`。

提示：
`1 <= n <= 18`
"""

from typing import List, Optional


class Solution:
    def validStrings(self, n: int) -> List[str]:
        res = []

        def backtrack(path: str):
            if len(path) == n:
                res.append(path)
                return
            # 总是可以加 '1'
            backtrack(path + '1')
            # 只有当前最后一个字符不是 '0' 时才能加 '0'
            if not path or path[-1] != '0':
                backtrack(path + '0')

        backtrack('')
        return res










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Bit Manipulation, String, Backtracking
#
# 解题思路:
# 回溯法生成所有长度为 n 的二进制字符串，限制是不允许相邻的 '0'。
# 在构建字符串时：
# - 总是可以追加 '1'
# - 只有当前末尾不是 '0' 时才能追加 '0'（即不能出现 "00"）
# 当字符串长度达到 n 时加入结果。
#
# 时间复杂度: O(2^n) — 结果数量为 Fibonacci 数 F_{n+2}
# 空间复杂度: O(n) — 递归深度
#
# 关键点:
# - 条件 "不含相邻零" 等价于不允许 "00" 子串
# - 回溯时剪枝：path 末尾为 '0' 时只能加 '1'
