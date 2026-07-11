"""
LeetCode #2443 - Sum of Number and Its Reverse
反转之后的数字和
https://leetcode.cn/problems/sum-of-number-and-its-reverse/

给你一个 非负 整数 `num` 。如果存在某个 非负 整数 `k` 满足 `k + reverse(k) = num`  ，则返回 `true` ；否则，返回 `false` 。
`reverse(k)` 表示 `k` 反转每个数位后得到的数字。

示例 1：
输入：num = 443 输出：true 解释：172 + 271 = 443 ，所以返回 true 。
示例 2：
输入：num = 63 输出：false 解释：63 不能表示为非负整数及其反转后数字之和，返回 false 。
示例 3：
输入：num = 181 输出：true 解释：140 + 041 = 181 ，所以返回 true 。注意，反转后的数字可能包含前导零。

提示：
`0 <= num <= 10^5`
"""

from typing import List, Optional


class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        for k in range(num + 1):
            rev = int(str(k)[::-1])
            if k + rev == num:
                return True
        return False



# ════════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ════════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Math, Enumeration
#
# 解题思路:
# 暴力枚举所有可能的 k 从 0 到 num。对于每个 k，将其转换为字符串后反转再转回整数得到 reverse(k)。
# 检查 k + reverse(k) 是否等于 num，如果等于则返回 True。如果枚举完所有 k 都没有找到，返回 False。
# 由于 num 最大为 10^5，暴力枚举完全可行。
#
# 时间复杂度: O(num * log(num))
# 空间复杂度: O(1)
#
# 关键点:
# - 暴力枚举：num <= 10^5 使得 O(num) 枚举可行
# - 反转数字：通过字符串转换 str(k)[::-1] 实现，也可以用数学方法逐位反转
# - 注意边界：k 可以等于 0（0 + 0 = 0），所以从 0 开始枚举
