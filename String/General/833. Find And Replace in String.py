"""
LeetCode #833 - Find And Replace in String
中文题名：字符串中的查找与替换
https://leetcode.com/problems/find-and-replace-in-string/

To some string `S`, we will perform some replacement operations that
replace groups of letters with new ones (not necessarily the same size).

Each replacement operation has `3` parameters: a starting index `i`, a
source word `x` and a target word `y`.  The rule
is that if `x` starts at position
`i` in the original string
`S`, then we will replace that occurrence of `x` with `y`.
If not, we do nothing.

For example, if we have `S = "abcd"` and we have some
replacement operation `i = 2, x = "cd", y = "ffff"`,
then because `"cd"` starts at position `2` in the original string `S`, we will
replace it with `"ffff"`.

Using another example on `S = "abcd"`, if we have both the replacement
operation `i = 0, x = "ab", y = "eee"`, as well as another
replacement operation `i = 2, x = "ec", y = "ffff"`,
this second operation does nothing because in the original string `S[2] = 'c'`,
which doesn't match `x[0] = 'e'`.

All these operations occur simultaneously.  It's guaranteed that there won't be
any overlap in replacement: for example, `S = "abc", indexes = [0, 1], sources
= ["ab","bc"]` is not a valid test case.

Example 1:

Input: S = "abcd", indexes = [0,2], sources = ["a","cd"], targets = ["eee","ffff"]
Output: "eeebffff"
Explanation: "a" starts at index 0 in S, so it's replaced by "eee".
"cd" starts at index 2 in S, so it's replaced by "ffff".

Example 2:

Input: S = "abcd", indexes = [0,2], sources = ["ab","ec"], targets = ["eee","ffff"]
Output: "eeecd"
Explanation: "ab" starts at index 0 in S, so it's replaced by "eee".
"ec" doesn't starts at index 2 in the original S, so we do nothing.

Notes:

`0 <= indexes.length = sources.length = targets.length <=
100`

`0 < indexes[i] < S.length <= 1000`

All characters in given inputs are lowercase letters.

【中文翻译】
对于某个字符串 `S`，我们将执行一些替换操作，用新的字符串替换原有的子串（不一定是相同长度）。

每个替换操作有 3 个参数：起始索引 `i`、源字符串 `x` 和目标字符串 `y`。规则是：如果 `x` 在原始字符串 `S` 的位置 `i` 处开始出现，那么我们将其替换为 `y`。否则，什么都不做。

例如，如果 `S = "abcd"` 且有一个替换操作 `i = 2, x = "cd", y = "ffff"`，那么因为 `"cd"` 在原始字符串 `S` 的位置 2 处开始，我们将其替换为 `"ffff"`。

再举一个 `S = "abcd"` 的例子，如果我们同时有替换操作 `i = 0, x = "ab", y = "eee"`，以及另一个替换操作 `i = 2, x = "ec", y = "ffff"`，那么第二个操作什么也不做，因为在原始字符串中 `S[2] = 'c'`，与 `x[0] = 'e'` 不匹配。

所有这些操作同时发生。保证没有替换重叠的情况：例如，`S = "abc", indexes = [0, 1], sources = ["ab","bc"]` 不是有效的测试用例。

示例 1：

输入：S = "abcd", indexes = [0,2], sources = ["a","cd"], targets = ["eee","ffff"]
输出："eeebffff"
解释："a" 从 S 中的索引 0 开始，所以被替换为 "eee"。"cd" 从 S 中的索引 2 开始，所以被替换为 "ffff"。

示例 2：

输入：S = "abcd", indexes = [0,2], sources = ["ab","ec"], targets = ["eee","ffff"]
输出："eeecd"
解释："ab" 从 S 中的索引 0 开始，所以被替换为 "eee"。"ec" 不从原始 S 的索引 2 开始，所以我们什么也不做。

注意：

`0 <= indexes.length = sources.length = targets.length <= 100`

`0 <= indexes[i] < S.length <= 1000`

输入中的所有字符都是小写字母。

"""

from typing import List, Optional


class Solution:
    def findReplaceString(
        self, s: str, indexes: List[int], sources: List[str], targets: List[str]
    ) -> str:
        # Create a mapping from index to (source, target) for valid replacements
        replacement = {}
        for i, src, tgt in zip(indexes, sources, targets):
            if s.startswith(src, i):
                replacement[i] = (src, tgt)

        # Build result by scanning S
        result = []
        pos = 0
        while pos < len(s):
            if pos in replacement:
                src, tgt = replacement[pos]
                result.append(tgt)
                pos += len(src)
            else:
                result.append(s[pos])
                pos += 1

        return ''.join(result)



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 1. 首先遍历所有替换操作，验证 source 是否真的在 S 的 index 位置匹配。
#    如果匹配，记录到 replacement 字典中。
# 2. 然后从左到右扫描 S：
#    - 如果当前位置在 replacement 中，添加 target，指针跳过 source 的长度
#    - 否则，添加当前字符，指针前进 1
# 由于题目保证没有重叠替换，所以不需要处理冲突。
#
# 时间复杂度: O(n + m * L) — n 是 S 长度，m 是替换操作数，L 是 source 平均长度
# 空间复杂度: O(n + m) — 存储结果和 replacement 字典
#
# 关键点:
# - 先验证再替换：只有 source 真正匹配时才生效
# - 所有操作同时进行，因此不能在原字符串上边改边验证
# - 使用 startswith(source, i) 简洁检查匹配
# - 由于保证无重叠，简单的字典映射就足够了
