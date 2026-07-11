"""
LeetCode #2232 - Minimize Result by Adding Parentheses to Expression
向表达式添加括号后的最小结果
https://leetcode.cn/problems/minimize-result-by-adding-parentheses-to-expression/

给你一个下标从 0 开始的字符串 `expression` ，格式为 `"<num1>+<num2>"` ，其中 `<num1>` 和 `<num2>` 表示正整数。
请你向 `expression` 中添加一对括号，使得在添加之后， `expression` 仍然是一个有效的数学表达式，并且计算后可以得到 最小 可能值。左括号 必须 添加在 `'+'` 的左侧，而右括号必须添加在 `'+'` 的右侧。
返回添加一对括号后形成的表达式 `expression` ，且满足 `expression` 计算得到 最小 可能值。如果存在多个答案都能产生相同结果，返回任意一个答案。
生成的输入满足：`expression` 的原始值和添加满足要求的任一对括号之后 `expression` 的值，都符合 32-bit 带符号整数范围。

示例 1：
输入：expression = "247+38" 输出："2(47+38)" 解释：表达式计算得到 2 * (47 + 38) = 2 * 85 = 170 。 注意 "2(4)7+38" 不是有效的结果，因为右括号必须添加在 `'+' 的右侧。` 可以证明 170 是最小可能值。
示例 2：
输入：expression = "12+34" 输出："1(2+3)4" 解释：表达式计算得到 1 * (2 + 3) * 4 = 1 * 5 * 4 = 20 。
示例 3：
输入：expression = "999+999" 输出："(999+999)" 解释：表达式计算得到 999 + 999 = 1998 。

提示：
`3 <= expression.length <= 10`
`expression` 仅由数字 `'1'` 到 `'9'` 和 `'+'` 组成
`expression` 由数字开始和结束
`expression` 恰好仅含有一个 `'+'`.
`expression` 的原始值和添加满足要求的任一对括号之后 `expression` 的值，都符合 32-bit 带符号整数范围
"""

from typing import List, Optional


class Solution:
    def minimizeResult(self, expression: str) -> str:
        plus_idx = expression.index('+')
        num1 = expression[:plus_idx]   # 加号左侧的数字字符串
        num2 = expression[plus_idx + 1:]  # 加号右侧的数字字符串

        min_val = float('inf')
        best_expr = ""

        # 枚举左括号在 num1 中的位置 i（左侧截断点）
        # 枚举右括号在 num2 中的位置 j（右侧截断点）
        for i in range(len(num1)):
            for j in range(1, len(num2) + 1):
                left_outer = num1[:i]          # 左括号左侧（乘数，空则为 1）
                left_inner = num1[i:]          # 左括号到加号之间（加数）
                right_inner = num2[:j]         # 加号到右括号之间（加数）
                right_outer = num2[j:]         # 右括号右侧（乘数，空则为 1）

                # 空字符串视为 1（乘数）或 0（加数不会为空因为 i/j 范围保证）
                l_outer = int(left_outer) if left_outer else 1
                l_inner = int(left_inner)      # left_inner 非空（i < len(num1)）
                r_inner = int(right_inner)     # right_inner 非空（j >= 1）
                r_outer = int(right_outer) if right_outer else 1

                val = l_outer * (l_inner + r_inner) * r_outer
                if val < min_val:
                    min_val = val
                    best_expr = left_outer + "(" + left_inner + "+" + right_inner + ")" + right_outer

        return best_expr


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: String, Enumeration
#
# 解题思路:
# 枚举所有可能的括号位置：左括号必须在 num1 中某个位置，右括号在 num2 中某个位置。
# 将表达式拆分为：left_outer * (left_inner + right_inner) * right_outer。
# - left_outer：num1 中左括号左边的部分，作为乘数（空则视为 1）
# - left_inner：num1 中左括号到加号的部分，作为加法左操作数
# - right_inner：num2 中加号到右括号的部分，作为加法右操作数
# - right_outer：num2 中右括号右边的部分，作为乘数（空则视为 1）
# 遍历所有组合，记录最小值对应的表达式。
# expression 长度 <= 10，O(n^2) 枚举完全足够。
#
# 时间复杂度: O(L1 * L2) 其中 L1, L2 分别为加号两侧数字长度，最多 9*9 = 81 种组合
# 空间复杂度: O(1) 不计返回字符串
#
# 关键点:
# - 外层为空时乘数视为 1（而非 0）
# - 内层数字不会为空（循环范围保证）
# - 暴力枚举即可，数据范围极小
