"""
LeetCode #1404 - Number of Steps to Reduce a Number in Binary Representation to One
中文题名：将二进制表示减到 1 的步骤数
https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/

Given a number `s` in their binary representation. Return the number
of steps to reduce it to 1 under the following rules:

If the current number is even, you have to divide it by 2.

If the current number is odd, you have to add 1 to it.

It's guaranteed that you can always reach to one for all testcases.

Example 1:

Input: s = "1101"
Output: 6
Explanation: "1101" corressponds to number 13 in their decimal representation.
Step 1) 13 is odd, add 1 and obtain 14.
Step 2) 14 is even, divide by 2 and obtain 7.
Step 3) 7 is odd, add 1 and obtain 8.
Step 4) 8 is even, divide by 2 and obtain 4.
Step 5) 4 is even, divide by 2 and obtain 2.
Step 6) 2 is even, divide by 2 and obtain 1.

Example 2:

Input: s = "10"
Output: 1
Explanation: "10" corressponds to number 2 in their decimal representation.
Step 1) 2 is even, divide by 2 and obtain 1.

Example 3:

Input: s = "1"
Output: 0

Constraints:

`1 <= s.length <= 500`

`s` consists of characters '0' or '1'

`s[0] == '1'`

【中文翻译】

给定一个二进制表示的数字 s。返回按以下规则将其减为 1 所需的步数：

如果当前数字是偶数，将其除以 2。
如果当前数字是奇数，将其加 1。

保证所有测试用例都能最终达到 1。

示例 1：
输入：s = "1101"
输出：6
解释："1101" 对应十进制数 13。
第 1 步）13 是奇数，加 1 得 14。
第 2 步）14 是偶数，除以 2 得 7。
第 3 步）7 是奇数，加 1 得 8。
第 4 步）8 是偶数，除以 2 得 4。
第 5 步）4 是偶数，除以 2 得 2。
第 6 步）2 是偶数，除以 2 得 1。

示例 2：
输入：s = "10"
输出：1
解释："10" 对应十进制数 2。第 1 步）2 是偶数，除以 2 得 1。

示例 3：
输入：s = "1"
输出：0

约束条件：
1 <= s.length <= 500
s 由字符 '0' 或 '1' 组成
s[0] == '1'
"""

from typing import List, Optional


class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0
        carry = 0
        # 从右向左处理（跳过最高位 s[0]）
        for i in range(len(s) - 1, 0, -1):
            if int(s[i]) + carry == 1:
                # 奇数：加 1（产生进位）然后除以 2，共 2 步
                carry = 1
                steps += 2
            else:
                # 偶数：直接除以 2，1 步
                steps += 1
        # 处理最高位 + 最终进位
        return steps + carry



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 从二进制字符串的最低位（最右端）开始模拟：
# - 如果当前位（含进位）为偶数（即当前位为 0），则除以 2（右移一位），步数 +1
# - 如果当前位（含进位）为奇数（即当前位为 1），则加 1（会产生进位），步数 +1
# 特殊情况：当 s 为 "1" 且进位为 0 时结束。
# 优化思路：遍历字符串时，遇到 '0' 表示偶数，直接除 2；
# 遇到 '1' 表示奇数，需要加 1（可能触发连续进位）。
#
# 更简洁的解法：从右向左遍历，维护进位。
# 时间复杂度: O(N)  N 为字符串长度
# 空间复杂度: O(1)
#
# 关键点:
# - 二进制模拟：除以 2 = 右移一位，加 1 = 从最低位开始处理进位
# - s 长度可达 500，不能转成整数后计算（会溢出）
# - 从右向左逐位处理，维护进位标志
# - 当只剩下 "1" 且无进位时停止










