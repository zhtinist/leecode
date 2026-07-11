"""
LeetCode #670 - Maximum Swap
中文题名：最大交换
https://leetcode.com/problems/maximum-swap/

Given a non-negative integer, you could swap two digits at most once to get the
maximum valued number. Return the maximum valued number you could get.

Example 1:

Input: 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.

Example 2:

Input: 9973
Output: 9973
Explanation: No swap.

Note:

The given number is in the range [0, 108]

【中文翻译】
给定一个非负整数，你最多可以交换一次数字中的任意两位，以获得最大的可能数值。返回你能得到的最大数值。

示例 1：

输入：2736
输出：7236
解释：交换数字 2 和数字 7。

示例 2：

输入：9973
输出：9973
解释：不需要交换。

注意：

给定数字的范围是 [0, 10^8]。
"""

from typing import List, Optional


class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))
        n = len(digits)
        last = {int(d): i for i, d in enumerate(digits)}

        for i in range(n):
            for d in range(9, int(digits[i]), -1):
                if last.get(d, -1) > i:
                    digits[i], digits[last[d]] = digits[last[d]], digits[i]
                    return int(''.join(digits))

        return num











# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 贪心策略：我们希望将数字中尽可能靠左的较小数字，与尽可能靠右的较大数字交换。
#
# 1. 将数字转换为字符数组（或列表）
# 2. 建立 last 字典：记录每个数字（0-9）最后出现的位置
# 3. 从左到右遍历每一位数字：
#    - 对于当前位置 i，检查是否存在比 digits[i] 更大的数字，
#      且该数字在位置 i 之后出现（从 9 向下查找到 digits[i]+1）
#    - 如果存在，交换这两个位置的数字并立即返回结果
# 4. 如果遍历完也没有找到可交换的情况，说明数字已经最大，返回原数字
#
# 时间复杂度: O(n) - 数字长度最多 9 位（10^8 范围内），每位最多检查 9 次
# 空间复杂度: O(n) - 存储数字的字符列表
#
# 关键点:
- 贪心：左边优先找到可以变大的位置，右边选最大的数字与之交换
# - last 字典存储每个数字的最右位置，保证选到尽可能靠右的较大数字
# - 从 9 向下检查确保选择的是最大的可能数字
# - 示例 2736：第 0 位 2，右边最大是 7，交换得 7236
