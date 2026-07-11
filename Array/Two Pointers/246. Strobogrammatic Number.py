"""
LeetCode #246 - Strobogrammatic Number
中文题名：中心对称数
https://leetcode.com/problems/strobogrammatic-number/

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at
upside down).

Write a function to determine if a number is strobogrammatic. The number is represented as a
string.

Example 1:

Input:  "69"
Output: true

Example 2:

Input:  "88"
Output: true

Example 3:

Input:  "962"
Output: false

【中文翻译】
中心对称数是指一个数字在 180 度旋转（上下颠倒）后，看起来和原数字一样。

编写一个函数来判断该数字是否是中心对称数。数字以字符串形式表示。

示例 1：

输入："69"
输出：true

示例 2：

输入："88"
输出：true

示例 3：

输入："962"
输出：false
"""

from typing import List, Optional


class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        # 旋转 180 度后有效的数字映射
        valid_map = {
            '0': '0',
            '1': '1',
            '6': '9',
            '8': '8',
            '9': '6',
        }

        left, right = 0, len(num) - 1
        while left <= right:
            if num[left] not in valid_map:
                return False
            if valid_map[num[left]] != num[right]:
                return False
            left += 1
            right -= 1

        return True


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Easy
# Paid Only: Yes
#
# 解题思路：
# 使用双指针法，从字符串两端向中间检查。只有 '0', '1', '6', '8', '9'
# 是旋转有效的数字，其中 '6' 和 '9' 互相旋转对应。检查每个字符是否在
# 有效集合中，以及左字符旋转后是否等于右字符。
#
# 时间复杂度: O(n) — 遍历字符串一次
# 空间复杂度: O(1) — 哈希表大小固定
#
# 关键点：
# - 建立旋转映射表: 0→0, 1→1, 6→9, 8→8, 9→6
# - 双指针从两端向中间检查
# - 注意 '6' 和 '9' 的对应关系
