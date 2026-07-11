"""
LeetCode #3335 - Total Characters in String After Transformations I
字符串转换后的长度 I
https://leetcode.cn/problems/total-characters-in-string-after-transformations-i/

给你一个字符串 `s` 和一个整数 `t`，表示要执行的 转换 次数。每次 转换 需要根据以下规则替换字符串 `s` 中的每个字符：
如果字符是 `'z'`，则将其替换为字符串 `"ab"`。
否则，将其替换为字母表中的下一个字符。例如，`'a'` 替换为 `'b'`，`'b'` 替换为 `'c'`，依此类推。
返回 恰好 执行 `t` 次转换后得到的字符串的 长度。
由于答案可能非常大，返回其对 `10^9 + 7` 取余的结果。

示例 1：

输入： s = "abcyy", t = 2
输出： 7
解释：
第一次转换 (t = 1)
`'a'` 变为 `'b'`
`'b'` 变为 `'c'`
`'c'` 变为 `'d'`
`'y'` 变为 `'z'`
`'y'` 变为 `'z'`
第一次转换后的字符串为：`"bcdzz"`
第二次转换 (t = 2)
`'b'` 变为 `'c'`
`'c'` 变为 `'d'`
`'d'` 变为 `'e'`
`'z'` 变为 `"ab"`
`'z'` 变为 `"ab"`
第二次转换后的字符串为：`"cdeabab"`
最终字符串长度：字符串为 `"cdeabab"`，长度为 7 个字符。
示例 2：

输入： s = "azbk", t = 1
输出： 5
解释：
第一次转换 (t = 1)
`'a'` 变为 `'b'`
`'z'` 变为 `"ab"`
`'b'` 变为 `'c'`
`'k'` 变为 `'l'`
第一次转换后的字符串为：`"babcl"`
最终字符串长度：字符串为 `"babcl"`，长度为 5 个字符。

提示：
`1 <= s.length <= 10^5`
`s` 仅由小写英文字母组成。
`1 <= t <= 10^5`
"""

from typing import List, Optional


class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = 10 ** 9 + 7
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - 97] += 1

        for _ in range(t):
            new_cnt = [0] * 26
            for i in range(25):
                new_cnt[i + 1] = (new_cnt[i + 1] + cnt[i]) % MOD
            new_cnt[0] = (new_cnt[0] + cnt[25]) % MOD
            new_cnt[1] = (new_cnt[1] + cnt[25]) % MOD
            cnt = new_cnt

        return sum(cnt) % MOD



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Hash Table, Math, String, Dynamic Programming, Counting
#
# 解题思路:
# 统计每个字符的频率，然后执行t次变换。每次变换：
# 'a'-'y'各向后移动一位（频率转移到下一个字符）
# 'z'变为"ab"，即频率分别加到'a'和'b'
# 最后返回总频率的模。
#
# 时间复杂度: O(t * 26)，t <= 10^5
# 空间复杂度: O(26) = O(1)
#
# 关键点:
# - 不需要逐字符变换，而是统计每种字符的频率批量更新
# - 'z'的变换是唯一特殊规则：一个'z'变成两个字符"ab"
