"""
LeetCode #1898 - Maximum Number of Removable Characters
可移除字符的最大数目
https://leetcode.cn/problems/maximum-number-of-removable-characters/

给你两个字符串 `s` 和 `p` ，其中 `p` 是 `s` 的一个 子序列 。同时，给你一个元素 互不相同 且下标 从 0 开始 计数的整数数组 `removable` ，该数组是 `s` 中下标的一个子集（`s` 的下标也 从 0 开始 计数）。
请你找出一个整数 `k`（`0 <= k <= removable.length`），选出 `removable` 中的 前 `k` 个下标，然后从 `s` 中移除这些下标对应的 `k` 个字符。整数 `k` 需满足：在执行完上述步骤后， `p` 仍然是 `s` 的一个 子序列 。更正式的解释是，对于每个 `0 <= i < k` ，先标记出位于 `s[removable[i]]` 的字符，接着移除所有标记过的字符，然后检查 `p` 是否仍然是 `s` 的一个子序列。
返回你可以找出的 最大 `k` ，满足在移除字符后 `p` 仍然是 `s` 的一个子序列。
字符串的一个 子序列 是一个由原字符串生成的新字符串，生成过程中可能会移除原字符串中的一些字符（也可能不移除）但不改变剩余字符之间的相对顺序。

示例 1：
输入：s = "abcacb", p = "ab", removable = [3,1,0] 输出：2 解释：在移除下标 3 和 1 对应的字符后，"abcacb" 变成 "accb" 。 "ab" 是 "accb" 的一个子序列。 如果移除下标 3、1 和 0 对应的字符后，"abcacb" 变成 "ccb" ，那么 "ab" 就不再是 s 的一个子序列。 因此，最大的 k 是 2 。
示例 2：
输入：s = "abcbddddd", p = "abcd", removable = [3,2,1,4,5,6] 输出：1 解释：在移除下标 3 对应的字符后，"abcbddddd" 变成 "abcddddd" 。 "abcd" 是 "abcddddd" 的一个子序列。
示例 3：
输入：s = "abcab", p = "abc", removable = [0,1,2,3,4] 输出：0 解释：如果移除数组 removable 的第一个下标，"abc" 就不再是 s 的一个子序列。

提示：
`1 <= p.length <= s.length <= 10^5`
`0 <= removable.length < s.length`
`0 <= removable[i] < s.length`
`p` 是 `s` 的一个 子字符串
`s` 和 `p` 都由小写英文字母组成
`removable` 中的元素 互不相同
"""

from typing import List, Optional


class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        def is_subsequence(k: int) -> bool:
            # Mark first k removable indices as removed
            removed = set(removable[:k])

            # Check if p is subsequence of s after removal
            j = 0  # pointer in p
            for i, ch in enumerate(s):
                if i in removed:
                    continue
                if j < len(p) and ch == p[j]:
                    j += 1
            return j == len(p)

        left, right = 0, len(removable)
        while left < right:
            mid = (left + right + 1) // 2  # Upper mid for binary search
            if is_subsequence(mid):
                left = mid
            else:
                right = mid - 1

        return left



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Two Pointers, String, Binary Search
#
# 解题思路:
# 二分查找最大的 k。
# 1. 对于给定的 k，标记 removable 前 k 个位置为已移除。
# 2. 使用双指针检查 p 是否仍是 s 的子序列：遍历 s，
#    跳过已移除的位置，尝试匹配 p 的字符。
# 3. 如果 p 能完全匹配，说明 k 可行，尝试更大的 k。
# 4. 使用 upper mid 的二分方式确保找到最大值。
#
# 时间复杂度: O((s + p) * log r) 其中 r = len(removable)
# 空间复杂度: O(k) — 存储被移除位置的集合
#
# 关键点:
# - 二分查找的上界是 len(removable)
# - 检查子序列时跳过已标记移除的位置
# - 使用 set 快速判断位置是否被移除
# - upper mid 确保二分向大的方向收敛
