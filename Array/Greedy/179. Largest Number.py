"""
LeetCode #179 - Largest Number
中文题名：最大数
https://leetcode.com/problems/largest-number/

Given a list of non negative integers, arrange them such that they form the largest
number.

Example 1:
    Input: nums = [10, 2]
    Output: "210"

Example 2:
    Input: nums = [3, 30, 34, 5, 9]
    Output: "9534330"

Note: The result may be very large, so you need to return a string instead
of an integer.

【中文翻译】
给你一个非负整数数组，将它们重新排列，使得拼接后的数字最大。

示例 1：
    输入：nums = [10, 2]
    输出："210"

示例 2：
    输入：nums = [3, 30, 34, 5, 9]
    输出："9534330"

注意：结果可能非常大，所以需要返回字符串而不是整数。
"""

from typing import List, Optional


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        from functools import cmp_to_key

        def compare(a: str, b: str) -> int:
            if a + b > b + a:
                return -1
            elif a + b < b + a:
                return 1
            else:
                return 0

        strs = [str(n) for n in nums]
        strs.sort(key=cmp_to_key(compare))
        result = "".join(strs)
        return "0" if result[0] == "0" else result


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 核心是自定义排序规则：对于任意两个数字 a 和 b，比较 a+b 和 b+a 的字符串拼接结果。
# 如果 a+b > b+a，则 a 应该排在 b 前面。将所有数字转换为字符串后按此规则排序，
# 然后拼接即可。注意处理全零数组的特殊情况（结果以 "0" 开头时返回 "0"）。
#
# 时间复杂度: O(N log N * K)，其中 K 是数字的平均长度（比较两个字符串拼接是 O(K)）
# 空间复杂度: O(N) — 存储字符串数组
#
# 关键点:
# - 自定义比较器：比较 a+b 和 b+a 而不是直接比较 a 和 b
# - 使用 functools.cmp_to_key 将旧式比较函数转换为 key 函数
# - 特殊处理 "00...0" 的情况（即数组中全是 0）
