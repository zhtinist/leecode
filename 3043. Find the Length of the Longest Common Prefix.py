"""
LeetCode #3043 - Find the Length of the Longest Common Prefix
最长公共前缀的长度
https://leetcode.cn/problems/find-the-length-of-the-longest-common-prefix/

给你两个 正整数 数组 `arr1` 和 `arr2` 。
正整数的 前缀 是其 最左边 的一位或多位数字组成的整数。例如，`123` 是整数 `12345` 的前缀，而 `234` 不是 。
设若整数 `c` 是整数 `a` 和 `b` 的 公共前缀 ，那么 `c` 需要同时是 `a` 和 `b` 的前缀。例如，`5655359` 和 `56554` 有公共前缀 `565` 和 `5655`，而 `1223` 和 `43456` 没有 公共前缀。
你需要找出属于 `arr1` 的整数 `x` 和属于 `arr2` 的整数 `y` 组成的所有数对 `(x, y)` 之中最长的公共前缀的长度。
返回所有数对之中最长公共前缀的长度。如果它们之间不存在公共前缀，则返回 `0` 。

示例 1：
输入：arr1 = [1,10,100], arr2 = [1000] 输出：3 解释：存在 3 个数对 (arr1[i], arr2[j]) ： - (1, 1000) 的最长公共前缀是 1 。 - (10, 1000) 的最长公共前缀是 10 。 - (100, 1000) 的最长公共前缀是 100 。 最长的公共前缀是 100 ，长度为 3 。
示例 2：
输入：arr1 = [1,2,3], arr2 = [4,4,4] 输出：0 解释：任何数对 (arr1[i], arr2[j]) 之中都不存在公共前缀，因此返回 0 。 请注意，同一个数组内元素之间的公共前缀不在考虑范围内。

提示：
`1 <= arr1.length, arr2.length <= 5 * 10^4`
`1 <= arr1[i], arr2[i] <= 10^8`
"""

from typing import List, Optional


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        """
        Generate all prefixes of numbers in arr1 and store in a set.
        For each number in arr2, check its prefixes from longest to shortest,
        return the max length found.
        """
        prefixes = set()

        # All prefixes from arr1
        for num in arr1:
            while num > 0:
                prefixes.add(num)
                num //= 10

        max_len = 0
        # Check each number in arr2
        for num in arr2:
            while num > 0:
                if num in prefixes:
                    max_len = max(max_len, len(str(num)))
                    break  # found longest prefix for this number
                num //= 10

        return max_len



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Trie, Array, Hash Table, String
#
# 解题思路:
# 前缀是数字的最左边若干位。将 arr1 中每个数字的所有前缀（通过不断除以 10）存入哈希集合。
# 然后遍历 arr2 的每个数字，同样从完整数字开始不断除以 10，检查每个前缀是否在集合中。
# 找到的第一个（即最长的）匹配前缀的长度即为该数字的贡献，取所有数字的最大值。
#
# 时间复杂度: O((N1 + N2) * D)，D 为数字位数（最多 9），N1、N2 为数组长度
# 空间复杂度: O(N1 * D)，存储 arr1 的所有前缀
#
# 关键点:
# - 前缀通过不断除以 10 生成（如 12345 -> 1234 -> 123 -> 12 -> 1）
# - 从最长前缀开始检查，首次匹配即为最长
# - 只需存储 arr1 前缀，单次遍历 arr2 查询
