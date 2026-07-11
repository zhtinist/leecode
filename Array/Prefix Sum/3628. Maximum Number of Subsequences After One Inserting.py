"""
LeetCode #3628 - Maximum Number of Subsequences After One Inserting
插入一个字母的最大子序列数
https://leetcode.cn/problems/maximum-number-of-subsequences-after-one-inserting/

给你一个由大写英文字母组成的字符串 `s`。
你可以在字符串的 任意 位置（包括字符串的开头或结尾）最多插入一个 大写英文字母。
返回在 最多插入一个字母 后，字符串中可以形成的 `"LCT"` 子序列的 最大 数量。
子序列 是从另一个字符串中删除某些字符（可以不删除）且不改变剩余字符顺序后得到的一个 非空 字符串。

示例 1：

输入： s = "LMCT"
输出： 2
解释：
可以在字符串 `s` 的开头插入一个 `"L"`，变为 `"LLMCT"`，其中包含 2 个子序列，分别位于下标 [0, 3, 4] 和 [1, 3, 4]。
示例 2：

输入： s = "LCCT"
输出： 4
解释：
可以在字符串 `s` 的开头插入一个 `"L"`，变为 `"LLCCT"`，其中包含 4 个子序列，分别位于下标 [0, 2, 4]、[0, 3, 4]、[1, 2, 4] 和 [1, 3, 4]。
示例 3：

输入： s = "L"
输出： 0
解释：
插入一个字母无法获得子序列 `"LCT"`，结果为 0。

提示：
`1 <= s.length <= 10^5`
`s` 仅由大写英文字母组成。
"""

from typing import List, Optional


class Solution:
    def maxSubsequences(self, s: str) -> int:
        n = len(s)
        total_T = s.count('T')

        original_lct = 0
        lc_pairs = 0    # "LC" 子序列数
        ct_pairs = 0    # "CT" 子序列数
        L_before = 0
        T_after = total_T
        C_count = 0
        max_C_benefit = 0

        for i, ch in enumerate(s):
            # 在位置 i 处插入 'C' 的收益
            max_C_benefit = max(max_C_benefit, L_before * T_after)

            if ch == 'L':
                L_before += 1
            elif ch == 'C':
                original_lct += L_before * T_after
                lc_pairs += L_before
                C_count += 1
            elif ch == 'T':
                T_after -= 1
                ct_pairs += C_count

        # 在末尾插入 'C' 的收益
        max_C_benefit = max(max_C_benefit, L_before * T_after)

        # 在开头插入 'L' 收益 = ct_pairs，在末尾插入 'T' 收益 = lc_pairs
        best = max(original_lct,
                   original_lct + ct_pairs,
                   original_lct + max_C_benefit,
                   original_lct + lc_pairs)
        return best










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, String, Dynamic Programming, Prefix Sum
#
# 解题思路:
# 先计算原始字符串中 "LCT" 子序列的数量。然后分别尝试三种插入策略：
# 1. 在开头插入 'L'：新增数量 = 原始串中 "CT" 子序列的数量；
# 2. 在最佳位置插入 'C'：对于每个候选位置，新增数量 = (之前 L 的数量) * (之后 T 的数量)；
# 3. 在末尾插入 'T'：新增数量 = 原始串中 "LC" 子序列的数量。
# 取四种情况（不插入、插入 L、插入 C、插入 T）的最大值。
#
# 时间复杂度: O(n) — 一次遍历完成所有统计
# 空间复杂度: O(1) — 仅使用常数额外空间
#
# 关键点:
# - 前缀计数与后缀计数协同：L_before 统计左侧 L，T_after 统计右侧 T
# - 插入 'C' 的位置可以是任意字符之间（包括首尾），遍历时逐步更新最大收益
