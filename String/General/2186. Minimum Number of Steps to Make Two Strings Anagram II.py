"""
LeetCode #2186 - Minimum Number of Steps to Make Two Strings Anagram II
制造字母异位词的最小步骤数 II
https://leetcode.cn/problems/minimum-number-of-steps-to-make-two-strings-anagram-ii/

给你两个字符串 `s` 和 `t` 。在一步操作中，你可以给 `s` 或者 `t` 追加 任一字符 。
返回使 `s` 和 `t` 互为 字母异位词 所需的最少步骤数。
字母异位词 指字母相同但是顺序不同（或者相同）的字符串。

示例 1：
输入：s = "leetcode", t = "coats" 输出：7 解释： - 执行 2 步操作，将 "as" 追加到 s = "leetcode" 中，得到 s = "leetcodeas" 。 - 执行 5 步操作，将 "leede" 追加到 t = "coats" 中，得到 t = "coatsleede" 。 "leetcodeas" 和 "coatsleede" 互为字母异位词。 总共用去 2 + 5 = 7 步。 可以证明，无法用少于 7 步操作使这两个字符串互为字母异位词。
示例 2：
输入：s = "night", t = "thing" 输出：0 解释：给出的字符串已经互为字母异位词。因此，不需要任何进一步操作。

提示：
`1 <= s.length, t.length <= 2 * 10^5`
`s` 和 `t` 由小写英文字符组成
"""

from typing import List, Optional


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        """
        计数法：统计 s 和 t 中每个字母的出现频率。
        对于每个字母，s 比 t 多的部分需要在 t 中补足，t 比 s 多的部分需要在 s 中补足。
        总步数 = 所有字母在两字符串中出现次数之差的绝对值之和。
        """
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord('a')] += 1
        for ch in t:
            cnt[ord(ch) - ord('a')] -= 1

        # cnt[i] > 0 表示字母 i 在 s 中比在 t 中多 cnt[i] 个，
        # cnt[i] < 0 表示字母 i 在 t 中比在 s 中多 -cnt[i] 个。
        # 这些差值都需要通过追加操作来补齐。
        return sum(abs(x) for x in cnt)


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Hash Table, String, Counting
#
# 解题思路:
# 1. 要让 s 和 t 成为字母异位词，两个字符串中每种字母的出现次数必须相同。
# 2. 使用长度为 26 的数组 cnt 记录差值：
#    - 遍历 s，对应字母计数 +1
#    - 遍历 t，对应字母计数 -1
# 3. cnt[i] 的绝对值表示第 i 个字母在两个字符串中的数量差距。
# 4. 每个差值都需要通过追加一步操作来补齐（追加到数量较少的那一侧）。
#    总步数 = sum(|cnt[i]|) 对所有 i。
# 5. 这等价于：对于每种字母，缺多少个就补多少个，两边总共需要的追加次数。
#
# 时间复杂度: O(m + n)
# - m = len(s), n = len(t)，各遍历一次。
#
# 空间复杂度: O(1)
# - 固定大小 26 的计数数组。
#
# 关键点:
# - 差值的绝对值之和即为答案。
# - 不需要实际模拟追加操作，仅通过计数即可得出最少步数。
# - 每种字母独立计算，互不影响。
