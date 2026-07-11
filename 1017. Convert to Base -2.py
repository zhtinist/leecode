"""
LeetCode #1017 - Convert to Base -2
中文题名：负二进制转换
https://leetcode.com/problems/convert-to-base-2/

Given a number `N`, return a string consisting of `"0"`s and
`"1"`s that represents its value in base `-2` (negative
two).

The returned string must have no leading zeroes, unless the string is
`"0"`.

Example 1:

Input: 2
Output: "110"
Explantion: (-2) ^ 2 + (-2) ^ 1 = 2

Example 2:

Input: 3
Output: "111"
Explantion: (-2) ^ 2 + (-2) ^ 1 + (-2) ^ 0 = 3

Example 3:

Input: 4
Output: "100"
Explantion: (-2) ^ 2 = 4

Note:

`0 <= N <= 10^9`

【中文翻译】
给定一个数字 `N`，返回一个由 `"0"` 和 `"1"` 组成的字符串，表示其以 `-2`（负二进制）为底的值。

返回的字符串必须没有前导零，除非字符串是 `"0"`。

示例 1：

输入：2
输出："110"
解释：(-2)^2 + (-2)^1 = 2

示例 2：

输入：3
输出："111"
解释：(-2)^2 + (-2)^1 + (-2)^0 = 3

示例 3：

输入：4
输出："100"
解释：(-2)^2 = 4

注意：

`0 <= N <= 10^9`

"""

from typing import List, Optional


class Solution:
    def baseNeg2(self, N: int) -> str:
        if N == 0:
            return "0"
        res = []
        while N != 0:
            remainder = N & 1
            res.append(str(remainder))
            N = -(N >> 1)
        return ''.join(reversed(res))










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用位运算进行负二进制转换。对于 base = -2，规律为：
# N = (-2) * quotient + remainder，其中 remainder 只能是 0 或 1。
# 通过 N & 1 获取当前的 remainder（最低位），然后 N = -(N >> 1) 更新 N。
# 这是因为：N >> 1 等价于 N // 2（右移一位），取负后满足公式推导。
# 不断收集 remainder 直到 N 变为 0。最后将收集的 remainder 反转顺序即为结果。
# 特殊情况：N = 0 时直接返回 "0"。
#
# 时间复杂度: O(log N) - 每次循环 N 的绝对值大约减半
# 空间复杂度: O(log N) - 存储结果的字符数组
#
# 关键点:
# - 使用位运算 N & 1 和 N >> 1 高效获取余数和商
# - N = -(N >> 1) 是关键递推公式（负二进制的特殊性质）
# - 结果需要反转顺序（先收集的是低位）
# - 处理 N = 0 的特殊情况
