"""
LeetCode #784 - Letter Case Permutation
中文题名：字母大小写全排列
https://leetcode.com/problems/letter-case-permutation/

Given a string S, we can transform every letter individually to be lowercase or
uppercase to create another string.  Return a list of all possible strings we could
create.

Examples:
Input: S = "a1b2"
Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

Input: S = "3z4"
Output: ["3z4", "3Z4"]

Input: S = "12345"
Output: ["12345"]

Note:

`S` will be a string with length between `1` and `12`.

`S` will consist only of letters or digits.

【中文翻译】
给定一个字符串 S，我们可以将每个字母分别转换为小写或大写来创建另一个字符串。返回所有可能生成的字符串的列表。

示例：
输入：S = "a1b2"
输出：["a1b2", "a1B2", "A1b2", "A1B2"]

输入：S = "3z4"
输出：["3z4", "3Z4"]

输入：S = "12345"
输出：["12345"]

注意：

`S` 是长度在 `1` 到 `12` 之间的字符串。

`S` 只包含字母或数字。
"""

from typing import List, Optional


class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        res = [""]
        for ch in S:
            if ch.isalpha():
                res = [s + ch.lower() for s in res] + [s + ch.upper() for s in res]
            else:
                res = [s + ch for s in res]
        return res



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 迭代 / 回溯。
# 维护结果列表 res，初始值为 [""]。
# 遍历字符串 S 的每个字符 ch：
# - 如果 ch 是字母，将当前 res 中的每个字符串分别拼接 ch.lower() 和 ch.upper()。
# - 如果 ch 是数字，将当前 res 中的每个字符串直接拼接 ch。
# 每次遇到字母，结果列表的大小翻倍。
# 也可以使用回溯（DFS）实现，在叶子节点收集结果。
#
# 时间复杂度: O(2^L * N)，其中 L 是字母数量，N 是字符串长度（拼接开销）
# 空间复杂度: O(2^L * N) - 存储所有结果
#
# 关键点:
# - 遇到字母时结果数翻倍（大小写两种选择）
# - 数字直接追加，不产生新分支
# - 迭代构建比递归回溯更简洁
# - Python 的 isalpha() 判断是否为字母
