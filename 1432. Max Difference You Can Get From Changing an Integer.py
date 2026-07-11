"""
LeetCode #1432 - Max Difference You Can Get From Changing an Integer
中文题名：改变一个整数能得到的最大差值
https://leetcode.com/problems/max-difference-you-can-get-from-changing-an-integer/

You are given an integer `num`. You will apply the following steps
exactly two times:

Pick a digit `x (0 <= x <= 9)`.

Pick another digit `y (0 <= y <= 9)`. The digit
`y` can be equal to `x`.

Replace all the occurrences of `x` in the decimal representation of
`num` by `y`.

The new integer cannot have any leading zeros, also the new
integer cannot be 0.

Let `a` and `b` be the results of applying the
operations to `num` the first and second times, respectively.

Return the max difference between `a` and `b`.

Example 1:

Input: num = 555
Output: 888
Explanation: The first time pick x = 5 and y = 9 and store the new integer in a.
The second time pick x = 5 and y = 1 and store the new integer in b.
We have now a = 999 and b = 111 and max difference = 888

Example 2:

Input: num = 9
Output: 8
Explanation: The first time pick x = 9 and y = 9 and store the new integer in a.
The second time pick x = 9 and y = 1 and store the new integer in b.
We have now a = 9 and b = 1 and max difference = 8

Example 3:

Input: num = 123456
Output: 820000

Example 4:

Input: num = 10000
Output: 80000

Example 5:

Input: num = 9288
Output: 8700

Constraints:

`1 <= num <= 10^8`

【中文翻译】

给定一个整数 `num`。你将恰好执行以下步骤两次：

选择一个数字 `x (0 <= x <= 9)`。
选择另一个数字 `y (0 <= y <= 9)`。数字 `y` 可以等于 `x`。
用 `y` 替换 `num` 的十进制表示中所有出现的 `x`。
得到的新整数不能有前导零，也不能为 0。

设 `a` 和 `b` 分别为第一次和第二次操作应用于 `num` 的结果。

返回 `a` 和 `b` 之间的最大差值。

示例 1：
输入：num = 555
输出：888
解释：第一次选择 x = 5 和 y = 9，将新整数存入 a。
第二次选择 x = 5 和 y = 1，将新整数存入 b。
此时 a = 999，b = 111，最大差值 = 888。

示例 2：
输入：num = 9
输出：8
解释：第一次选择 x = 9 和 y = 9，将新整数存入 a。
第二次选择 x = 9 和 y = 1，将新整数存入 b。
此时 a = 9，b = 1，最大差值 = 8。

示例 3：
输入：num = 123456
输出：820000

示例 4：
输入：num = 10000
输出：80000

示例 5：
输入：num = 9288
输出：8700

约束条件：
`1 <= num <= 10^8`

"""

from typing import List, Optional


class Solution:
    def maxDiff(self, num: int) -> int:
        s = str(num)
        n = len(s)

        # 求最大值 a：将第一个非 9 的数字替换为 9
        a_str = list(s)
        for i in range(n):
            if a_str[i] != '9':
                target = a_str[i]
                for j in range(i, n):
                    if a_str[j] == target:
                        a_str[j] = '9'
                break
        a = int("".join(a_str))

        # 求最小值 b
        b_str = list(s)
        if b_str[0] != '1':
            # 首位不是 1，将首位替换为 1
            target = b_str[0]
            for i in range(n):
                if b_str[i] == target:
                    b_str[i] = '1'
        else:
            # 首位是 1，找到第一个不是 0 且不是 1 的数字，替换为 0
            for i in range(1, n):
                if b_str[i] != '0' and b_str[i] != '1':
                    target = b_str[i]
                    for j in range(i, n):
                        if b_str[j] == target:
                            b_str[j] = '0'
                    break
        b = int("".join(b_str))

        return a - b



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 贪心构造法：
# 目标是最大化 a - b，所以 a 要尽可能大，b 要尽可能小。
#
# 求最大值 a 的策略：
# 1. 将数字转为字符串 s。
# 2. 从左到右找第一个不等于 '9' 的数字，将它（及其所有出现）替换为 '9'。
#    这样可以最大化数值。如果所有数字都是 9，则不替换（a = num）。
#
# 求最小值 b 的策略：
# 1. 如果首位 s[0] != '1'：
#    将首位（及其所有出现）替换为 '1'。这样可以保证不能有前导零，且最小。
# 2. 如果首位 s[0] == '1'：
#    从第 2 位开始找第一个不是 '0' 也不是 '1' 的数字，
#    将它（及其所有出现）替换为 '0'。
#    这保证了 b 不会以 0 开头，且尽可能小。
#    如果找不到（所有非首位的数字都是 0 或 1），在首位是 1 的情况下无法变得更小，
#    b 保持不变（b = num）。
#
# 3. 返回 a - b。
#
# 时间复杂度: O(L)，L 是数字的位数（最多 9 位）。
# 空间复杂度: O(L)，用于存储字符串表示。
#
# 关键点:
# - a 最大化：从左找第一个非 9 的数字，全部替换为 9
# - b 最小化：如果首位 != 1，替换为 1；否则找第一个 > 1 的数字替换为 0
# - 注意约束：新整数不能有前导零，不能为 0










