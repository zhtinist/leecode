"""
LeetCode #2165 - Smallest Value of the Rearranged Number
重排数字的最小值
https://leetcode.cn/problems/smallest-value-of-the-rearranged-number/

给你一个整数 `num` 。重排 `num` 中的各位数字，使其值 最小化 且不含 任何 前导零。
返回不含前导零且值最小的重排数字。
注意，重排各位数字后，`num` 的符号不会改变。

示例 1：
输入：num = 310 输出：103 解释：310 中各位数字的可行排列有：013、031、103、130、301、310 。 不含任何前导零且值最小的重排数字是 103 。
示例 2：
输入：num = -7605 输出：-7650 解释：-7605 中各位数字的部分可行排列为：-7650、-6705、-5076、-0567。 不含任何前导零且值最小的重排数字是 -7650 。

提示：
`-10^15 <= num <= 10^15`
"""

from typing import List, Optional


class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0

        negative = num < 0
        digits = list(str(abs(num)))

        if negative:
            digits.sort(reverse=True)
        else:
            digits.sort()
            if digits[0] == '0':
                i = 0
                while i < len(digits) and digits[i] == '0':
                    i += 1
                if i < len(digits):
                    digits[0], digits[i] = digits[i], digits[0]

        result = int(''.join(digits))
        return -result if negative else result



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Math, Sorting
#
# 解题思路:
# 如果 num 为 0 直接返回 0。对于负数，将各位数字降序排列即可得到最小值（因为负数的绝对
# 值越大，数值越小）。对于正数，将各位数字升序排列，但如果排序后首位是 '0'，则需要找
# 到第一个非零数字并与首位 0 交换，避免出现前导零。最后根据符号返回结果。
#
# 时间复杂度: O(d log d)，其中 d 是数字的位数（最多 16 位）
# 空间复杂度: O(d)
#
# 关键点:
# - 正数和负数的排序策略不同：正数升序，负数降序
# - 正数需要避免前导零：找到第一个非零数字替换到首位
# - 特殊情况：num = 0 直接返回 0
