"""
LeetCode #3006 - Find Beautiful Indices in the Given Array I
找出数组中的美丽下标 I
https://leetcode.cn/problems/find-beautiful-indices-in-the-given-array-i/

给你一个下标从 0 开始的字符串 `s` 、字符串 `a` 、字符串 `b` 和一个整数 `k` 。
如果下标 `i` 满足以下条件，则认为它是一个 美丽下标：
`0 <= i <= s.length - a.length`
`s[i..(i + a.length - 1)] == a`
存在下标 `j` 使得：
`0 <= j <= s.length - b.length`
`s[j..(j + b.length - 1)] == b`
`|j - i| <= k`
以数组形式按 从小到大排序 返回美丽下标。

示例 1：
输入：s = "isawsquirrelnearmysquirrelhouseohmy", a = "my", b = "squirrel", k = 15 输出：[16,33] 解释：存在 2 个美丽下标：[16,33]。 - 下标 16 是美丽下标，因为 s[16..17] == "my" ，且存在下标 4 ，满足 s[4..11] == "squirrel" 且 |16 - 4| <= 15 。 - 下标 33 是美丽下标，因为 s[33..34] == "my" ，且存在下标 18 ，满足 s[18..25] == "squirrel" 且 |33 - 18| <= 15 。 因此返回 [16,33] 作为结果。
示例 2：
输入：s = "abcd", a = "a", b = "a", k = 4 输出：[0] 解释：存在 1 个美丽下标：[0]。 - 下标 0 是美丽下标，因为 s[0..0] == "a" ，且存在下标 0 ，满足 s[0..0] == "a" 且 |0 - 0| <= 4 。 因此返回 [0] 作为结果。

提示：
`1 <= k <= s.length <= 10^5`
`1 <= a.length, b.length <= 10`
`s`、`a`、和 `b` 只包含小写英文字母。
"""

from typing import List, Optional


class Solution:
    def beautifulIndices(
        self, s: str, a: str, b: str, k: int
    ) -> List[int]:
        """
        Find all matching indices for patterns a and b in s.
        For each a-index i, check if there exists a b-index j within k distance.
        Use two-pointer technique since both index lists are sorted.
        """
        import bisect

        n = len(s)
        len_a, len_b = len(a), len(b)

        # Find all matching positions for a
        pos_a = []
        for i in range(n - len_a + 1):
            if s[i:i + len_a] == a:
                pos_a.append(i)

        # Find all matching positions for b
        pos_b = []
        for i in range(n - len_b + 1):
            if s[i:i + len_b] == b:
                pos_b.append(i)

        if not pos_a or not pos_b:
            return []

        result = []
        j = 0
        for i in pos_a:
            # Move j to the first b-index >= i - k
            while j < len(pos_b) and pos_b[j] < i - k:
                j += 1
            # Check if current b-index is within k
            if j < len(pos_b) and abs(pos_b[j] - i) <= k:
                result.append(i)

        return result



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Two Pointers, String, Binary Search, String Matching, Hash Function, Rolling Hash
#
# 解题思路:
# 首先线性扫描找出模式 a 和 b 在 s 中的所有匹配位置（两个有序列表）。
# 然后使用双指针技术：对于每个 a 的匹配位置 i，移动 b 的指针 j 到第一个 >= i-k 的位置，
# 检查 |pos_b[j] - i| <= k 是否成立，成立则将 i 加入结果。
#
# 时间复杂度: O(n + len_a_matches + len_b_matches)，每个匹配位置仅访问一次
# 空间复杂度: O(n)，存储匹配位置列表
#
# 关键点:
# - a 和 b 长度 <= 10，暴力匹配即可（无需 KMP）
# - 双指针利用两个匹配列表的有序性，避免 O(n^2) 的二重循环
# - j 指针只向前移动，保证 O(n) 总复杂度
