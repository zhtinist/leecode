"""
LeetCode #249 - Group Shifted Strings
https://leetcode.com/problems/group-shifted-strings/

Given a string, we can "shift" each of its letter to its successive letter, for
example: `"abc" -> "bcd"`. We can keep "shifting"
which forms the sequence:

"abc" -> "bcd" -> ... -> "xyz"

Given a list of strings which contains only lowercase alphabets, group all strings that
belong to the same shifting sequence.

Example:

Input: `["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],`
Output:
[
["abc","bcd","xyz"],
["az","ba"],
["acef"],
["a","z"]
]
"""

from typing import List, Optional


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        from collections import defaultdict

        groups = defaultdict(list)

        for s in strings:
            # 生成移位签名：相邻字符差值（模 26）
            key = []
            for i in range(1, len(s)):
                diff = (ord(s[i]) - ord(s[i - 1])) % 26
                key.append(str(diff))
            # 使用逗号分隔的字符串作为字典键
            key_str = ','.join(key)
            groups[key_str].append(s)

        return list(groups.values())


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: Yes
#
# 解题思路：
# 属于同一"移位序列"的字符串，其相邻字符之间的差值模式相同。
# 例如 "abc" → 差值 (1, 1)，"bcd" → 差值 (1, 1)，"xyz" → 差值 (1, 1)。
# 注意 x→y→z→a 是循环的，所以用模 26 处理。
# 计算每个字符串的差值签名作为哈希表的键，将同签名的字符串分为一组。
#
# 时间复杂度: O(N * K) — N 为字符串数量，K 为字符串平均长度
# 空间复杂度: O(N * K) — 存储所有字符串及其键
#
# 关键点：
# - 使用相邻字符差值作为分组键
# - 差值取模 26 处理循环（如 "za" → 'a'-'z' = -25, %26 = 1）
# - 单字符字符串的键为空字符串
