"""
LeetCode #3133 - Minimum Array End
数组最后一个元素的最小值
https://leetcode.cn/problems/minimum-array-end/

给你两个整数 `n` 和 `x` 。你需要构造一个长度为 `n` 的 正整数 数组 `nums` ，对于所有 `0 <= i < n - 1` ，满足 `nums[i + 1]` 大于 `nums[i]` ，并且数组 `nums` 中所有元素的按位 `AND` 运算结果为 `x` 。
返回 `nums[n - 1]` 可能的 最小 值。

示例 1：

输入：n = 3, x = 4
输出：6
解释：
数组 `nums` 可以是 `[4,5,6]` ，最后一个元素为 `6` 。
示例 2：

输入：n = 2, x = 7
输出：15
解释：
数组 `nums` 可以是 `[7,15]` ，最后一个元素为 `15` 。

提示：
`1 <= n, x <= 10^8`
"""

from typing import List, Optional


class Solution:
    def minEnd(self, n: int, x: int) -> int:
        n -= 1  # 第n个数，从0开始编号
        ans = x
        b = 0
        while n > 0:
            # 跳过x中为1的位
            while (x >> b) & 1:
                b += 1
            # 将n的当前位填入x的0位
            if n & 1:
                ans |= (1 << b)
            n >>= 1
            b += 1
        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Bit Manipulation
#
# 解题思路:
# 所有元素的AND结果必须为x，意味着每个元素都必须包含x的所有二进制1位。
# 问题转化为：生成第n个包含x所有1位的数。将n-1的二进制位依次填入x的0位（包括更高位），
# 得到的就是第n个满足条件的数，也是数组最后一个元素的最小值。
#
# 时间复杂度: O(log n + log x)
# 空间复杂度: O(1)
#
# 关键点:
# - nums[0]至少为x（必须包含x的1位）
# - 将n-1的二进制表示填入x的空位
# - 考虑x的有效位数之外的高位也是空位
