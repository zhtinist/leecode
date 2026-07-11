"""
LeetCode #1073 - Adding Two Negabinary Numbers
中文题名：负二进制数相加
https://leetcode.com/problems/adding-two-negabinary-numbers/

Given two numbers `arr1` and `arr2` in base -2, return
the result of adding them together.

Each number is given in array format:  as an array of 0s and 1s, from most
significant bit to least significant bit.  For example, `arr = [1,1,0,1]`
represents the number `(-2)^3 + (-2)^2 + (-2)^0 = -3`.  A number `arr`
in array format is also guaranteed to have no leading zeros: either `arr
== [0]` or `arr[0] == 1`.

Return the result of adding `arr1` and `arr2` in the same format: as an
array of 0s and 1s with no leading zeros.

Example 1:

Input: arr1 = [1,1,1,1,1], arr2 = [1,0,1]
Output: [1,0,0,0,0]
Explanation: arr1 represents 11, arr2 represents 5, the output represents 16.

Note:

`1 <= arr1.length <= 1000`

`1 <= arr2.length <= 1000`

`arr1` and `arr2` have no leading zeros

`arr1[i]` is `0` or `1`

`arr2[i]` is `0` or `1`

【中文翻译】
给出基数为 -2 的两个数 arr1 和 arr2，返回两数相加的结果。

数字以数组形式给出：由 0 和 1 组成，按最高有效位到最低有效位的顺序排列。例如，arr = [1,1,0,1] 表示数字 (-2)^3 + (-2)^2 + (-2)^0 = -3。以数组形式给出的数字也同样保证没有前导零：即 arr == [0] 或者 arr[0] == 1。

以相同形式返回 arr1 和 arr2 相加的结果：没有前导零的 0 和 1 数组。

示例 1：

输入：arr1 = [1,1,1,1,1], arr2 = [1,0,1]
输出：[1,0,0,0,0]
解释：arr1 表示 11，arr2 表示 5，输出表示 16。

注意：

1 <= arr1.length <= 1000
1 <= arr2.length <= 1000
arr1 和 arr2 没有前导零
arr1[i] 为 0 或 1
arr2[i] 为 0 或 1

"""

from typing import List, Optional


class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        result = []
        carry = 0
        i, j = len(arr1) - 1, len(arr2) - 1

        while i >= 0 or j >= 0 or carry:
            if i >= 0:
                carry += arr1[i]
                i -= 1
            if j >= 0:
                carry += arr2[j]
                j -= 1

            result.append(carry & 1)
            carry = -(carry // 2)

        while len(result) > 1 and result[-1] == 0:
            result.pop()

        return result[::-1]










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 模拟基数为 -2 的加法。从最低位（数组末尾）开始逐位相加。
# 设当前位的和为 carry = carry + arr1[i] + arr2[j]。
# 当前位的结果 digit = carry % 2（即 carry & 1），因为基数为负时，每一位仍是 0 或 1。
# 进位 new_carry = -(carry // 2)。
# 推导：sum = digit + (-2) * new_carry => new_carry = -(sum - digit) / 2。
# 由于 digit = sum % 2，所以 new_carry = -(sum // 2)。
# 最后去除前导零并反转数组（因为从低位向高位构建结果）。
#
# 时间复杂度: O(max(n, m)) - n 和 m 分别为两数组长度
# 空间复杂度: O(max(n, m)) - 结果数组
#
# 关键点:
# - 负基数加法中进位公式为 carry = -(sum // 2)
# - 每位结果 digit = sum & 1（0 或 1）
# - Python 的 // 是向下取整，对负数需注意
# - 最后需要去除前导零并反转数组
# - 循环条件包含 carry，确保最高位进位也被处理
