"""
LeetCode #306 - Additive Number
中文题名：累加数
https://leetcode.com/problems/additive-number/

Additive number is a string whose digits can form additive sequence.

A valid additive sequence should contain at least three numbers. Except for the first
two numbers, each subsequent number in the sequence must be the sum of the preceding two.

Given a string containing only digits `'0'-'9'`, write a function
to determine if it's an additive number.

Note: Numbers in the additive sequence cannot have leading zeros, so sequence
`1, 2, 03` or `1, 02, 3` is invalid.

Example 1:

Input: "112358"
Output: true
Explanation: The digits can form an additive sequence: 1, 1, 2, 3, 5, 8.
1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8

Example 2:

Input: "199100199"
Output: true
Explanation: The additive sequence is: 1, 99, 100, 199.
1 + 99 = 100, 99 + 100 = 199

Constraints:

`num` consists only of digits `'0'-'9'`.

`1 <= num.length <= 35`

Follow up:

How would you handle overflow for very large input integers?

【中文翻译】
累加数是一个字符串，其数字可以形成累加序列。

一个有效的累加序列必须至少包含三个数。除了最开始的两个数以外，序列中的每个后续数字必须是它之前两个数字之和。

给定一个只包含数字 '0'-'9' 的字符串，编写一个函数来判断它是否是一个累加数。

注意：累加序列中的数不能有前导零，所以序列 1, 2, 03 或 1, 02, 3 是无效的。

示例 1：

输入："112358"
输出：true
解释：数字可以形成累加序列：1, 1, 2, 3, 5, 8。
1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8

示例 2：

输入："199100199"
输出：true
解释：累加序列为：1, 99, 100, 199。
1 + 99 = 100, 99 + 100 = 199

约束条件：

num 仅由数字 '0'-'9' 组成。
1 <= num.length <= 35

进阶：
对于非常大的输入整数，你将如何处理溢出问题？
"""

from typing import List, Optional


class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        for i in range(1, n):
            for j in range(i + 1, n):
                # 跳过有前导零的情况
                if (num[0] == '0' and i > 1) or (num[i] == '0' and j - i > 1):
                    continue
                a = int(num[:i])
                b = int(num[i:j])
                k = j
                while k < n:
                    c = a + b
                    s = str(c)
                    if not num.startswith(s, k):
                        break
                    k += len(s)
                    a, b = b, c
                    if k == n:
                        return True
        return False










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 穷举前两个数的所有可能组合，然后模拟累加序列的生成过程进行验证。
# 第一个数 num[:i] 的长度从 1 到 n-2，第二个数 num[i:j] 的长度从 1 到剩余部分。
# 确定前两个数后，不断计算它们的和 c = a + b，检查字符串从位置 k 开始是否以 str(c) 开头。
# 如果是则继续推进，直到遍历完整个字符串返回 True。
# 注意处理前导零：长度大于 1 且以 '0' 开头的数字（如 "03"）不合法，需要跳过。
# 进阶问题：Python 的 int 可处理任意大整数，因此不会溢出。
#
# 时间复杂度: O(n^3) - 两层循环 O(n^2) 枚举前两个数，内部验证最多走 O(n) 步
# 空间复杂度: O(1) - 仅使用常量额外空间
#
# 关键点:
# - 枚举前两个数的长度组合作为序列的起点
# - 使用 str.startswith() 检查后续字符串是否匹配累加和，简洁高效
# - 注意前导零边界条件：不能以 "0" 开头的多位数字
# - 字符串长度最大 35，暴力枚举完全可行
