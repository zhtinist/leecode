"""
LeetCode #791 - Custom Sort String
中文题名：自定义字符串排序
https://leetcode.com/problems/custom-sort-string/

`S` and `T` are strings composed of lowercase letters. In
`S`, no letter occurs more than once.

`S` was sorted in some custom order previously. We want to permute the characters
of `T` so that they match the order that `S` was sorted. More
specifically, if `x` occurs before `y` in `S`, then
`x` should occur before `y` in the returned string.

Return any permutation of `T` (as a string) that satisfies this property.

Example :
Input:
S = "cba"
T = "abcd"
Output: "cbad"
Explanation:
"a", "b", "c" appear in S, so the order of "a", "b", "c" should be "c", "b", and "a".
Since "d" does not appear in S, it can be at any position in T. "dcba", "cdba", "cbda" are also valid outputs.

Note:

`S` has length at most `26`, and no character is repeated in
`S`.

`T` has length at most `200`.

`S` and `T` consist of lowercase letters only.

【中文翻译】
`S` 和 `T` 是由小写字母组成的字符串。在 `S` 中，没有字母重复出现。

`S` 之前以某种自定义顺序排序。我们希望排列 `T` 中的字符，使其与 `S` 的排序顺序一致。具体来说，如果 `x` 在 `S` 中出现在 `y` 之前，那么在返回的字符串中 `x` 也应该出现在 `y` 之前。

返回满足此性质的任意一个 `T` 的排列（作为字符串）。

示例：
输入：
S = "cba"
T = "abcd"
输出："cbad"
解释："a"、"b"、"c" 出现在 S 中，因此 "a"、"b"、"c" 的顺序应该是 "c"、"b" 和 "a"。
由于 "d" 不出现在 S 中，它可以放在 T 的任意位置。"dcba"、"cdba"、"cbda" 也是有效的输出。

注意：

`S` 的长度最多为 `26`，且没有重复字符。

`T` 的长度最多为 `200`。

`S` 和 `T` 只包含小写字母。
"""

from typing import List, Optional


class Solution:
    def customSortString(self, S: str, T: str) -> str:
        from collections import Counter
        cnt = Counter(T)
        res = []
        # Append chars in S order by their count
        for ch in S:
            if ch in cnt:
                res.append(ch * cnt[ch])
                del cnt[ch]
        # Append remaining chars not in S
        for ch, freq in cnt.items():
            res.append(ch * freq)
        return "".join(res)



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 计数排序 / 哈希表。
# 1. 统计 T 中每个字符的出现次数。
# 2. 按照 S 中字符的顺序，依次将对应计数的字符加入结果。
# 3. 将不在 S 中的剩余字符任意顺序追加到末尾。
# S 中定义了字符之间的相对顺序。先放排在前的字符，再放排在后的，
# 最后处理 S 中不存在的字符（它们之间没有顺序约束）。
#
# 时间复杂度: O(S + T) - 遍历 S 和 T
# 空间复杂度: O(1) - 最多 26 个小写字母
#
# 关键点:
# - 用 Counter 统计 T 中字符频率
# - 按 S 顺序输出对应字符
# - 剩余字符排在末尾即可
# - 使用乘法 ch * freq 高效拼接重复字符
# - 从 Counter 中删除已处理字符，避免重复遍历
