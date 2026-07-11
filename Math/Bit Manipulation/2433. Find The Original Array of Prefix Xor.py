"""
LeetCode #2433 - Find The Original Array of Prefix Xor
找出前缀异或的原始数组
https://leetcode.cn/problems/find-the-original-array-of-prefix-xor/

给你一个长度为 `n` 的 整数 数组 `pref` 。找出并返回满足下述条件且长度为 `n` 的数组 `arr` ：
`pref[i] = arr[0] ^ arr[1] ^ ... ^ arr[i]`.
注意 `^` 表示 按位异或（bitwise-xor）运算。
可以证明答案是 唯一 的。

示例 1：
输入：pref = [5,2,0,3,1] 输出：[5,7,2,3,2] 解释：从数组 [5,7,2,3,2] 可以得到如下结果： - pref[0] = 5 - pref[1] = 5 ^ 7 = 2 - pref[2] = 5 ^ 7 ^ 2 = 0 - pref[3] = 5 ^ 7 ^ 2 ^ 3 = 3 - pref[4] = 5 ^ 7 ^ 2 ^ 3 ^ 2 = 1
示例 2：
输入：pref = [13] 输出：[13] 解释：pref[0] = arr[0] = 13

提示：
`1 <= pref.length <= 10^5`
`0 <= pref[i] <= 10^6`
"""

from typing import List, Optional


class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        arr = [0] * len(pref)
        arr[0] = pref[0]
        for i in range(1, len(pref)):
            arr[i] = pref[i] ^ pref[i - 1]
        return arr


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Bit Manipulation, Array
#
# 解题思路:
# 利用异或运算的性质。已知 pref[i] = arr[0] ^ arr[1] ^ ... ^ arr[i]，
# 则 pref[i-1] = arr[0] ^ ... ^ arr[i-1]。
# 将两者异或：pref[i] ^ pref[i-1] = arr[i]（因为相同元素异或结果为0，0与任何数异或等于该数本身）。
# arr[0] 直接等于 pref[0]。由此可以从左到右逐个还原出 arr。
#
# 时间复杂度: O(n)
# 空间复杂度: O(1)（不计输出数组）
#
# 关键点:
# - 异或运算的自反性：a ^ b ^ b = a
# - arr[0] = pref[0] 是边界条件
# - 对于 i >= 1，arr[i] = pref[i] ^ pref[i-1]
