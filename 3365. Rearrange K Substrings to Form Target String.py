"""
LeetCode #3365 - Rearrange K Substrings to Form Target String
重排子字符串以形成目标字符串
https://leetcode.cn/problems/rearrange-k-substrings-to-form-target-string/

给你两个字符串 `s` 和 `t`（它们互为字母异位词），以及一个整数 `k`。
你的任务是判断是否可以将字符串 `s` 分割成 `k` 个等长的子字符串，然后重新排列这些子字符串，并以任意顺序连接它们，使得最终得到的新字符串与给定的字符串 `t` 相匹配。
如果可以做到，返回 `true`；否则，返回 `false`。
字母异位词 是指由另一个单词或短语的所有字母重新排列形成的单词或短语，使用所有原始字母恰好一次。
子字符串 是字符串中的一个连续 非空 字符序列。

示例 1：

输入： s = "abcd", t = "cdab", k = 2
输出： true
解释：
将 `s` 分割成 2 个长度为 2 的子字符串：`["ab", "cd"]`。
重新排列这些子字符串为 `["cd", "ab"]`，然后连接它们得到 `"cdab"`，与 `t` 相匹配。
示例 2：

输入： s = "aabbcc", t = "bbaacc", k = 3
输出： true
解释：
将 `s` 分割成 3 个长度为 2 的子字符串：`["aa", "bb", "cc"]`。
重新排列这些子字符串为 `["bb", "aa", "cc"]`，然后连接它们得到 `"bbaacc"`，与 `t` 相匹配。
示例 3：

输入： s = "aabbcc", t = "bbaacc", k = 2
输出： false
解释：
将 `s` 分割成 2 个长度为 3 的子字符串：`["aab", "bcc"]`。
这些子字符串无法重新排列形成 `t = "bbaacc"`，所以输出 `false`。

提示：
`1 <= s.length == t.length <= 2 * 10^5`
`1 <= k <= s.length`
`s.length` 能被 `k` 整除。
`s` 和 `t` 仅由小写英文字母组成。
输入保证 `s` 和 `t` 互为字母异位词。
"""

from typing import List, Optional


class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
        n = len(s)
        chunk = n // k
        s_chunks = sorted(s[i:i + chunk] for i in range(0, n, chunk))
        t_chunks = sorted(t[i:i + chunk] for i in range(0, n, chunk))
        return s_chunks == t_chunks



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Hash Table, String, Sorting
#
# 解题思路:
# 将s和t分别切成k个等长子字符串，比较两个子字符串集合是否相同（忽略顺序）。将两组
# 子字符串分别排序后比较即可。
#
# 时间复杂度: O(n log k)，n为字符串长度
# 空间复杂度: O(n)
#
# 关键点:
# - 切分后排序比较
# - 子字符串必须等长
