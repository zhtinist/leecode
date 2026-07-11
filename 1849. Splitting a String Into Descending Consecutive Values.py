"""
LeetCode #1849 - Splitting a String Into Descending Consecutive Values
中文题名：将字符串拆分为递减的连续值
https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/

You are given a string `s` that consists of only digits.

Check if we can split `s` into two or more non-empty substrings such that the numerical values of the substrings are in descending order and the difference between numerical values of every two adjacent substrings is equal to `1`.

For example, the string `s = "0090089"` can be split into `["0090", "089"]` with numerical values `[90,89]`. The values are in descending order and adjacent values differ by `1`, so this way is valid.

Another example, the string `s = "001"` can be split into `["0", "01"]`, `["00", "1"]`, or `["0", "0", "1"]`. However all the ways are invalid because they have numerical values `[0,1]`, `[0,1]`, and `[0,0,1]` respectively, all of which are not in descending order.

Return `true` if it is possible to split `s`​​​​​​ as described above, or `false` otherwise.

A substring is a contiguous sequence of characters in a string.

Example 1:

Input: s = "1234"
Output: false
Explanation: There is no valid way to split s.

Example 2:

Input: s = "050043"
Output: true
Explanation: s can be split into ["05", "004", "3"] with numerical values [5,4,3].
The values are in descending order with adjacent values differing by 1.

Example 3:

Input: s = "9080701"
Output: false
Explanation: There is no valid way to split s.

Example 4:

Input: s = "10009998"
Output: true
Explanation: s can be split into ["100", "099", "98"] with numerical values [100,99,98].
The values are in descending order with adjacent values differing by 1.

Constraints:

`1 <= s.length <= 20`

`s` only consists of digits.

【中文翻译】

给定一个只包含数字的字符串 `s`。判断是否可以将 `s` 分割成两个或更多非空子串，使得子串的数字值按递减顺序排列，且相邻子串的数字值之差恰好为1。

例如，字符串 s = "0090089" 可以分割为 ["0090", "089"]，对应数值 [90, 89]，满足递减且差1。

返回 `true` 如果可以按上述方式分割，否则返回 `false`。

示例：
输入：s = "050043"
输出：true
解释：可以分割为 ["05", "004", "3"]，数值为 [5,4,3]。

"""

from typing import List, Optional


class Solution:
    def splitString(self, s: str) -> bool:
        def backtrack(start: int, prev: int) -> bool:
            if start == len(s):
                return True

            for end in range(start + 1, len(s) + 1):
                curr_val = int(s[start:end])
                if prev == -1 or curr_val == prev - 1:
                    if backtrack(end, curr_val):
                        return True
            return False

        # 尝试所有可能的第一段数字（至少需要两个部分）
        for end in range(1, len(s)):
            first_val = int(s[:end])
            if backtrack(end, first_val):
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
# 回溯法。遍历所有可能的第一段数字，然后递归检查剩余部分是否能形成
# 递减1的连续值。回溯函数backtrack(start, prev)从start位置开始，
# 尝试各种长度的子串，检查其数值是否等于prev-1。s长度<=20，
# 整数范围在Python中可以安全处理。
#
# 时间复杂度: O(N * 2^N)，最坏情况下每个位置都有分割/不分割两种选择
# 但实际由于递减约束和s长度<=20，回溯很快收敛
# 空间复杂度: O(N)，递归栈深度
#
# 关键点:
# - 至少需要两个部分，所以第一段只遍历到len(s)-1
# - 前导零不影响int()转换：int("05") = 5
# - 递减条件：curr_val == prev - 1
