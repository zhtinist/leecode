"""
LeetCode #2135 - Count Words Obtained After Adding a Letter
统计追加字母可以获得的单词数
https://leetcode.cn/problems/count-words-obtained-after-adding-a-letter/

给你两个下标从 0 开始的字符串数组 `startWords` 和 `targetWords` 。每个字符串都仅由 小写英文字母 组成。
对于 `targetWords` 中的每个字符串，检查是否能够从 `startWords` 中选出一个字符串，执行一次 转换操作 ，得到的结果与当前 `targetWords` 字符串相等。
转换操作 如下面两步所述：
追加 任何 不存在 于当前字符串的任一小写字母到当前字符串的末尾。
例如，如果字符串为 `"abc"` ，那么字母 `'d'`、`'e'` 或 `'y'` 都可以加到该字符串末尾，但 `'a'` 就不行。如果追加的是 `'d'` ，那么结果字符串为 `"abcd"` 。
重排 新字符串中的字母，可以按 任意 顺序重新排布字母。
例如，`"abcd"` 可以重排为 `"acbd"`、`"bacd"`、`"cbda"`，以此类推。注意，它也可以重排为 `"abcd"` 自身。
找出 `targetWords` 中有多少字符串能够由 `startWords` 中的 任一 字符串执行上述转换操作获得。返回 `targetWords` 中这类 字符串的数目 。
注意：你仅能验证 `targetWords` 中的字符串是否可以由 `startWords` 中的某个字符串经执行操作获得。`startWords`  中的字符串在这一过程中 不 发生实际变更。

示例 1：
输入：startWords = ["ant","act","tack"], targetWords = ["tack","act","acti"] 输出：2 解释： - 为了形成 targetWords[0] = "tack" ，可以选用 startWords[1] = "act" ，追加字母 'k' ，并重排 "actk" 为 "tack" 。 - startWords 中不存在可以用于获得 targetWords[1] = "act" 的字符串。   注意 "act" 确实存在于 startWords ，但是 必须 在重排前给这个字符串追加一个字母。 - 为了形成 targetWords[2] = "acti" ，可以选用 startWords[1] = "act" ，追加字母 'i' ，并重排 "acti" 为 "acti" 自身。
示例 2：
输入：startWords = ["ab","a"], targetWords = ["abc","abcd"] 输出：1 解释： - 为了形成 targetWords[0] = "abc" ，可以选用 startWords[0] = "ab" ，追加字母 'c' ，并重排为 "abc" 。 - startWords 中不存在可以用于获得 targetWords[1] = "abcd" 的字符串。

提示：
`1 <= startWords.length, targetWords.length <= 5 * 10^4`
`1 <= startWords[i].length, targetWords[j].length <= 26`
`startWords` 和 `targetWords` 中的每个字符串都仅由小写英文字母组成
在 `startWords` 或 `targetWords` 的任一字符串中，每个字母至多出现一次
"""

from typing import List, Optional


class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        start_set = set()
        for word in startWords:
            mask = 0
            for ch in word:
                mask |= 1 << (ord(ch) - ord('a'))
            start_set.add(mask)

        result = 0
        for word in targetWords:
            mask = 0
            for ch in word:
                mask |= 1 << (ord(ch) - ord('a'))
            for i in range(26):
                if mask & (1 << i):
                    prev = mask ^ (1 << i)
                    if prev in start_set:
                        result += 1
                        break

        return result



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Bit Manipulation, Array, Hash Table, String, Sorting
#
# 解题思路:
# 使用位掩码表示每个单词的字母集合。对于每个 startWords 中的单词，计算其位掩码并存入集合
# start_set。对于每个 targetWords 中的单词，计算其位掩码，然后尝试移除其中任意一个字母
# （即翻转对应位），检查移除后的掩码是否在 start_set 中。如果在，说明可以通过向 startWords
# 中的某个单词添加一个字母并重排得到该 target 单词。这是逆向思维：从 target 去掉一个字母
# 后应该能匹配到某个 start 单词。
#
# 时间复杂度: O(N + M)，其中 N = len(startWords)，M = len(targetWords)。
# 每个单词长度不超过 26，字母集合用位掩码存储，操作均为 O(1)。
# 空间复杂度: O(N)，用于存储 start_set 中所有 start 单词的位掩码。
#
# 关键点:
# - 位掩码：用整数的二进制位表示字母是否出现（a 对应 bit 0，b 对应 bit 1，...）
# - 逆向思维：从 target 移除一个字母后检查是否在 start_set 中，而不是正向尝试所有添加
