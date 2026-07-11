"""
LeetCode #2380 - Time Needed to Rearrange a Binary String
二进制字符串重新安排顺序需要的时间
https://leetcode.cn/problems/time-needed-to-rearrange-a-binary-string/

给你一个二进制字符串 `s` 。在一秒之中，所有 子字符串 `"01"` 同时 被替换成 `"10"` 。这个过程持续进行到没有 `"01"` 存在。
请你返回完成这个过程所需要的秒数。

示例 1：
输入：s = "0110101" 输出：4 解释： 一秒后，s 变成 "1011010" 。 再过 1 秒后，s 变成 "1101100" 。 第三秒过后，s 变成 "1110100" 。 第四秒后，s 变成 "1111000" 。 此时没有 "01" 存在，整个过程花费 4 秒。 所以我们返回 4 。
示例 2：
输入：s = "11100" 输出：0 解释： s 中没有 "01" 存在，整个过程花费 0 秒。 所以我们返回 0 。

提示：
`1 <= s.length <= 1000`
`s[i]` 要么是 `'0'` ，要么是 `'1'` 。

进阶：
你能以 O(n) 的时间复杂度解决这个问题吗？
"""

from typing import List, Optional


class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        ans = 0
        zeros = 0

        for ch in s:
            if ch == '0':
                zeros += 1
            elif zeros > 0:
                # 遇到 '1' 且前面有 '0'，需要一次操作
                ans = max(ans + 1, zeros)

        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: String, Dynamic Programming, Simulation
#
# 解题思路:
# 一次遍历线性解法。维护两个变量：ans（所需秒数）和 zeros（遇到的 0 的个数）。
# 遍历字符串中的每个字符：
# - 遇到 '0'：zeros 加 1
# - 遇到 '1' 且 zeros > 0：这个 '1' 需要被移到所有前面的 '0' 之后。
#   ans = max(ans + 1, zeros)。其中 ans+1 表示在前一秒基础上再加一秒，
#   zeros 表示至少需要 zeros 秒才能让这个 '1' 越过所有前面的 '0'。
# 最终返回 ans。
#
# 时间复杂度: O(n) 其中 n 为字符串 s 的长度
# 空间复杂度: O(1) 只使用了常数级别的额外空间
#
# 关键点:
# - 不需要模拟每次移动，通过分析 '1' 和前面 '0' 的关系推导最少秒数
# - ans 的递推：ans = max(ans + 1, zeros) 巧妙捕捉了并发移动的上限
# - ans+1 体现连续操作累积的时间，zeros 体现至少需要的移动步数
