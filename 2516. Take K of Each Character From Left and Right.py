"""
LeetCode #2516 - Take K of Each Character From Left and Right
每种字符至少取 K 个
https://leetcode.cn/problems/take-k-of-each-character-from-left-and-right/

给你一个由字符 `'a'`、`'b'`、`'c'` 组成的字符串 `s` 和一个非负整数 `k` 。每分钟，你可以选择取走 `s` 最左侧 还是 最右侧 的那个字符。
你必须取走每种字符 至少 `k` 个，返回需要的 最少 分钟数；如果无法取到，则返回 `-1` 。

示例 1：
输入：s = "aabaaaacaabc", k = 2 输出：8 解释： 从 s 的左侧取三个字符，现在共取到两个字符 'a' 、一个字符 'b' 。 从 s 的右侧取五个字符，现在共取到四个字符 'a' 、两个字符 'b' 和两个字符 'c' 。 共需要 3 + 5 = 8 分钟。 可以证明需要的最少分钟数是 8 。
示例 2：
输入：s = "a", k = 1 输出：-1 解释：无法取到一个字符 'b' 或者 'c'，所以返回 -1 。

提示：
`1 <= s.length <= 10^5`
`s` 仅由字母 `'a'`、`'b'`、`'c'` 组成
`0 <= k <= s.length`
"""

from typing import List, Optional


class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        n = len(s)
        cnt = {'a': 0, 'b': 0, 'c': 0}
        for ch in s:
            cnt[ch] += 1
        if cnt['a'] < k or cnt['b'] < k or cnt['c'] < k:
            return -1

        # Sliding window: find max middle subarray that leaves >= k of each char
        need_a = cnt['a'] - k
        need_b = cnt['b'] - k
        need_c = cnt['c'] - k

        left = 0
        max_len = 0
        cur = {'a': 0, 'b': 0, 'c': 0}

        for right in range(n):
            cur[s[right]] += 1
            while cur['a'] > need_a or cur['b'] > need_b or cur['c'] > need_c:
                cur[s[left]] -= 1
                left += 1
            max_len = max(max_len, right - left + 1)

        return n - max_len



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Hash Table, String, Sliding Window
#
# 解题思路:
# 反向思考：从两端取等价于从中间删除一个连续子数组。滑动窗口找到最长中间子数组，
# 使得剩余的两端部分每种字符都至少k个。总长度减去最大中间子数组长度即为答案。
# 先检查总字符数是否每种都>=k，不满足则返回-1。
#
# 时间复杂度: O(N)
# 空间复杂度: O(1)
#
# 关键点:
# - 转化为"保留的最长中间子数组"问题，而非直接模拟两端取
# - 窗口中a/b/c的数量不能超过总数-k，否则两端不够
# - 当k=0时直接返回0
