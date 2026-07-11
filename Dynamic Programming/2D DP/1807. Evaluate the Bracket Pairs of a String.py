"""
LeetCode #1807 - Evaluate the Bracket Pairs of a String
中文题名：替换字符串中的括号内容
https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string/

You are given a string `s` that contains some bracket pairs, with each pair containing a non-empty key.

For example, in the string `"(name)is(age)yearsold"`, there are two bracket pairs that contain the keys `"name"` and `"age"`.

You know the values of a wide range of keys. This is represented by a 2D string array `knowledge` where each `knowledge[i] = [keyi, valuei]` indicates that key `keyi` has a value of `valuei`.

You are tasked to evaluate all of the bracket pairs. When you evaluate a bracket pair that contains some key `keyi`, you will:

Replace `keyi` and the bracket pair with the key's corresponding `valuei`.

If you do not know the value of the key, you will replace `keyi` and the bracket pair with a question mark `"?"` (without the quotation marks).

Each key will appear at most once in your `knowledge`. There will not be any nested brackets in `s`.

Return the resulting string after evaluating all of the bracket pairs.

Example 1:

Input: s = "(name)is(age)yearsold", knowledge = [["name","bob"],["age","two"]]
Output: "bobistwoyearsold"
Explanation:
The key "name" has a value of "bob", so replace "(name)" with "bob".
The key "age" has a value of "two", so replace "(age)" with "two".

Example 2:

Input: s = "hi(name)", knowledge = [["a","b"]]
Output: "hi?"
Explanation: As you do not know the value of the key "name", replace "(name)" with "?".

Example 3:

Input: s = "(a)(a)(a)aaa", knowledge = [["a","yes"]]
Output: "yesyesyesaaa"
Explanation: The same key can appear multiple times.
The key "a" has a value of "yes", so replace all occurrences of "(a)" with "yes".
Notice that the "a"s not in a bracket pair are not evaluated.

Example 4:

Input: s = "(a)(b)", knowledge = [["a","b"],["b","a"]]
Output: "ba"

Constraints:

`1 <= s.length <= 105`

`0 <= knowledge.length <= 105`

`knowledge[i].length == 2`

`1 <= keyi.length, valuei.length <= 10`

`s` consists of lowercase English letters and round brackets `'('` and `')'`.

Every open bracket `'('` in `s` will have a corresponding close bracket `')'`.

The key in each bracket pair of `s` will be non-empty.

There will not be any nested bracket pairs in `s`.

`keyi` and `valuei` consist of lowercase English letters.

Each `keyi` in `knowledge` is unique.

【中文翻译】
给定一个字符串 s 和一个二维字符串数组 knowledge，knowledge[i] = [key, value]。
s 中包含括号对 "(key)"，需要将其替换为 knowledge 中 key 对应的 value。
如果找不到对应的 key，替换为 "?"。

示例 1：
输入: s = "(name)is(age)yearsold", knowledge = [["name","bob"],["age","two"]]
输出: "bobistwoyearsold"
解释: (name)→bob, (age)→two。

示例 2：
输入: s = "hi(name)", knowledge = [["a","b"]]
输出: "hi?"
解释: 没有 key="name"，替换为"?"。
"""

from typing import List, Optional


class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        kmap = {k: v for k, v in knowledge}
        result = []
        i = 0
        n = len(s)

        while i < n:
            if s[i] == '(':
                j = i + 1
                while s[j] != ')':
                    j += 1
                key = s[i + 1:j]
                result.append(kmap.get(key, '?'))
                i = j + 1
            else:
                result.append(s[i])
                i += 1

        return ''.join(result)
# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 遍历字符串，遇到 '(' 时提取括号内的 key，在 knowledge 字典中查找对应 value。
# 使用 kmap.get(key, '?') 找不到时返回 '?'。其他字符直接加入结果。
#
# 时间复杂度: O(N + K) — N 为 s 长度，K 为 knowledge 长度
# 空间复杂度: O(K + N) — 哈希表 + 结果列表
#
# 关键点:
# - 括号不会嵌套，简单解析即可
# - 用字典存储 knowledge 实现 O(1) 查找
# - get(key, '?') 处理缺省的替换
