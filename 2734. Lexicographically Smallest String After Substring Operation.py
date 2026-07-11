"""
LeetCode #2734 - Lexicographically Smallest String After Substring Operation
执行子串操作后的字典序最小字符串
https://leetcode.cn/problems/lexicographically-smallest-string-after-substring-operation/

给你一个仅由小写英文字母组成的字符串 `s` 。在一步操作中，你可以完成以下行为：
选择 `s` 的任一非空子字符串，可能是整个字符串，接着将字符串中的每一个字符替换为英文字母表中的前一个字符。例如，'b' 用 'a' 替换，'a' 用 'z' 替换。
返回执行上述操作 恰好一次 后可以获得的 字典序最小 的字符串。
子字符串 是字符串中的一个连续字符序列。 现有长度相同的两个字符串 `x` 和 字符串 `y` ，在满足 `x[i] != y[i]` 的第一个位置 `i` 上，如果  `x[i]` 在字母表中先于 `y[i]` 出现，则认为字符串 `x` 比字符串 `y` 字典序更小 。

示例 1：
输入：s = "cbabc" 输出："baabc" 解释：我们选择从下标 0 开始、到下标 1 结束的子字符串执行操作。  可以证明最终得到的字符串是字典序最小的。
示例 2：
输入：s = "acbbc" 输出："abaab" 解释：我们选择从下标 1 开始、到下标 4 结束的子字符串执行操作。 可以证明最终得到的字符串是字典序最小的。
示例 3：
输入：s = "leetcode" 输出："kddsbncd" 解释：我们选择整个字符串执行操作。 可以证明最终得到的字符串是字典序最小的。

提示：
`1 <= s.length <= 3 * 10^5`
`s` 仅由小写英文字母组成
"""

from typing import List, Optional


class Solution:
    def smallestString(self, s: str) -> str:
        n = len(s)
        chars = list(s)
        i = 0
        while i < n and chars[i] == 'a':
            i += 1
        if i == n:
            chars[-1] = 'z'
            return ''.join(chars)
        j = i
        while j < n and chars[j] != 'a':
            chars[j] = chr(ord(chars[j]) - 1)
            j += 1
        return ''.join(chars)



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, String
#
# 解题思路:
# 要使字典序最小，应该把非 'a' 的字符变成前一个字母（更小）。贪心策略：
# 找到第一个不是 'a' 的位置 i，从 i 开始将连续的非 'a' 字符都减 1。
# 如果整个字符串全是 'a'，只能将最后一个字符变成 'z'（因为必须恰好执行一次操作）。
#
# 时间复杂度: O(n)
# 空间复杂度: O(n) -- 需要转为 list 以便修改
#
# 关键点:
# - 字典序最小意味着要让前面的字符尽可能小
# - 'a' 变成 'z' 会变大，所以要避开 'a'，先从第一个非 'a' 字符开始操作
# - 全 'a' 字符串必须修改至少一个字符，选择影响最小的最后一个位置改为 'z'
