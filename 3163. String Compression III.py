"""
LeetCode #3163 - String Compression III
压缩字符串 III
https://leetcode.cn/problems/string-compression-iii/

给你一个字符串 `word`，请你使用以下算法进行压缩：
从空字符串 `comp` 开始。当 `word` 不为空 时，执行以下操作：
移除 `word` 的最长单字符前缀，该前缀由单一字符 `c` 重复多次组成，且该前缀长度 最多 为 9 。
将前缀的长度和字符 `c` 追加到 `comp` 。
返回字符串 `comp` 。

示例 1：

输入：word = "abcde"
输出："1a1b1c1d1e"
解释：
初始时，`comp = ""` 。进行 5 次操作，每次操作分别选择 `"a"`、`"b"`、`"c"`、`"d"` 和 `"e"` 作为前缀。
对每个前缀，将 `"1"` 和对应的字符追加到 `comp`。
示例 2：

输入：word = "aaaaaaaaaaaaaabb"
输出："9a5a2b"
解释：
初始时，`comp = ""`。进行 3 次操作，每次操作分别选择 `"aaaaaaaaa"`、`"aaaaa"` 和 `"bb"` 作为前缀。
对于前缀 `"aaaaaaaaa"`，将 `"9"` 和 `"a"` 追加到 `comp`。
对于前缀 `"aaaaa"`，将 `"5"` 和 `"a"` 追加到 `comp`。
对于前缀 `"bb"`，将 `"2"` 和 `"b"` 追加到 `comp`。

提示：
`1 <= word.length <= 2 * 10^5`
`word` 仅由小写英文字母组成。
"""

from typing import List, Optional


class Solution:
    def compressedString(self, word: str) -> str:
        comp = []
        i = 0
        n = len(word)
        while i < n:
            ch = word[i]
            cnt = 0
            while i < n and word[i] == ch and cnt < 9:
                cnt += 1
                i += 1
            comp.append(str(cnt))
            comp.append(ch)
        return ''.join(comp)



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: String
#
# 解题思路:
# 按要求模拟压缩过程。遍历字符串，每次取一个字符，统计其连续重复次数（最多9次），
# 将次数和字符拼接到结果中，然后从下一个位置继续。使用列表拼接提高效率。
#
# 时间复杂度: O(n)
# 空间复杂度: O(n)
#
# 关键点:
# - 每次最多取9个相同字符
# - 超过9个需要分段处理
# - 使用list+join代替字符串拼接提高效率
