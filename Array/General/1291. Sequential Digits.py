"""
LeetCode #1291 - Sequential Digits
中文题名：顺次数
https://leetcode.com/problems/sequential-digits/

An integer has sequential digits if and only if each digit in the
number is one more than the previous digit.

Return a sorted list of all the integers in the range `[low,
high]` inclusive that have sequential digits.

Example 1:

Input: low = 100, high = 300
Output: [123,234]

Example 2:

Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]

Constraints:

`10 <= low <= high <= 10^9`

【中文翻译】
如果一个整数上的每一位数字都比前一位数字大 1，则称其拥有顺次数。

返回一个排序后的列表，包含范围 [low, high] 内（包括边界）所有拥有顺次数的整数。

示例 1：

输入：low = 100, high = 300
输出：[123,234]

示例 2：

输入：low = 1000, high = 13000
输出：[1234,2345,3456,4567,5678,6789,12345]

约束条件：

10 <= low <= high <= 10^9
"""

from typing import List, Optional


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        result = []

        for start_digit in range(1, 10):
            num = start_digit
            for next_digit in range(start_digit + 1, 10):
                num = num * 10 + next_digit
                if low <= num <= high:
                    result.append(num)
                elif num > high:
                    break

        result.sort()
        return result










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 顺次数总共只有有限个（从 1 位到 9 位，不超过 36 个）。
# 可以枚举生成所有顺次数，然后筛选出在 [low, high] 范围内的。
# 外层循环选择起始数字（1 到 9），内层循环逐步添加下一位数字
# （每次将当前数字乘以 10 并加上下一位数字），直到数字超过 high 或达到 9。
# 最后对结果排序即可（生成过程本身大致有序，但为确保正确还是排序）。
#
# 时间复杂度: O(1) - 最多生成 9+8+...+1 = 45 个数字，常数级别
# 空间复杂度: O(1) - 最多存储 45 个结果
#
# 关键点:
# - 枚举所有可能的顺次数而非在范围 [low, high] 内逐个检查
# - 起始数字从 1 到 9，连续数字长度从 2 到 9-startDigit+1
# - 剪枝：当 num > high 时跳出内层循环
