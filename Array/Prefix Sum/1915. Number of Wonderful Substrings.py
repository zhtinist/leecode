"""
LeetCode #1915 - Number of Wonderful Substrings
最美子字符串的数目
https://leetcode.cn/problems/number-of-wonderful-substrings/

如果某个字符串中 至多一个 字母出现 奇数 次，则称其为 最美 字符串。
例如，`"ccjjc"` 和 `"abab"` 都是最美字符串，但 `"ab"` 不是。
给你一个字符串 `word` ，该字符串由前十个小写英文字母组成（`'a'` 到 `'j'`）。请你返回 `word` 中 最美非空子字符串 的数目。如果同样的子字符串在 `word` 中出现多次，那么应当对 每次出现 分别计数。
子字符串 是字符串中的一个连续字符序列。

示例 1：
输入：word = "aba" 输出：4 解释：4 个最美子字符串如下所示： - "aba" -> "a" - "aba" -> "b" - "aba" -> "a" - "aba" -> "aba"
示例 2：
输入：word = "aabb" 输出：9 解释：9 个最美子字符串如下所示： - "aabb" -> "a" - "aabb" -> "aa" - "aabb" -> "aab" - "aabb" -> "aabb" - "aabb" -> "a" - "aabb" -> "abb" - "aabb" -> "b" - "aabb" -> "bb" - "aabb" -> "b"
示例 3：
输入：word = "he" 输出：2 解释：2 个最美子字符串如下所示： - "he" -> "h" - "he" -> "e"

提示：
`1 <= word.length <= 10^5`
`word` 由从 `'a'` 到 `'j'` 的小写英文字母组成
"""

from typing import List, Optional


class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        # Use bitmask to track parity of each character (a-j: 10 bits)
        # mask[i] = parity of counts of letters a-j in prefix word[0..i]

        count = {0: 1}  # Empty prefix has mask 0
        mask = 0
        result = 0

        for ch in word:
            # Flip the bit for this character
            bit = 1 << (ord(ch) - ord('a'))
            mask ^= bit

            # Case 1: All characters have even counts (mask matches exactly)
            result += count.get(mask, 0)

            # Case 2: Exactly one character has odd count
            # Try flipping each of the 10 bits
            for i in range(10):
                flipped = mask ^ (1 << i)
                result += count.get(flipped, 0)

            count[mask] = count.get(mask, 0) + 1

        return result



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Bit Manipulation, Hash Table, String, Prefix Sum
#
# 解题思路:
# 位掩码 + 前缀异或 + 哈希表。
# 1. 用 10 位二进制表示 a-j 每个字母出现次数的奇偶性（1=奇数次）。
# 2. 前缀 mask[i] 表示 word[0..i] 中每个字母的奇偶状态。
# 3. 子串 word[i..j] 的奇偶状态 = mask[j] ^ mask[i-1]。
# 4. "最美字符串"条件：至多一个字母出现奇数次，
#    即子串的 mask 中至多有一个 1。
# 5. 遍历时统计两种情况的子串数：
#    - mask 相同（所有字母偶数次）
#    - mask 只有一位不同（恰好一个字母奇数次）
#
# 时间复杂度: O(n * 10) = O(n) — 每个位置检查 10 种翻转
# 空间复杂度: O(2^10) = O(1) — 最多 1024 种状态
#
# 关键点:
# - 只有 10 个字母 (a-j)，适合位掩码
# - 子串的奇偶状态 = 前缀异或差
# - 最美 = mask 中至多 1 个 1
# - 统计时包括"完全相同"(0个奇数)和"差1位"(1个奇数)
