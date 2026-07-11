"""
LeetCode #1461 - Check If a String Contains All Binary Codes of Size K
中文题名：检查一个字符串是否包含所有长度为 K 的二进制子串
https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/

Given a binary string `s` and an integer `k`.

Return True if all binary codes of length `k` is a substring of
`s`. Otherwise, return False.

Example 1:

Input: s = "00110110", k = 2
Output: true
Explanation: The binary codes of length 2 are "00", "01", "10" and "11". They can be all found as substrings at indicies 0, 1, 3 and 2 respectively.

Example 2:

Input: s = "00110", k = 2
Output: true

Example 3:

Input: s = "0110", k = 1
Output: true
Explanation: The binary codes of length 1 are "0" and "1", it is clear that both exist as a substring.

Example 4:

Input: s = "0110", k = 2
Output: false
Explanation: The binary code "00" is of length 2 and doesn't exist in the array.

Example 5:

Input: s = "0000000001011100", k = 4
Output: false

Constraints:

`1 <= s.length <= 5 * 10^5`

`s` consists of 0's and 1's only.

`1 <= k <= 20`

【中文翻译】
给定一个二进制字符串 `s` 和一个整数 `k`。

如果所有长度为 `k` 的二进制码都是 `s` 的子串，则返回 True。否则，返回 False。

示例 1：

输入：s = "00110110", k = 2
输出：true
解释：长度为 2 的二进制码有 "00"、"01"、"10" 和 "11"。
它们分别作为子串出现在下标 0、1、3 和 2 处。

示例 2：

输入：s = "00110", k = 2
输出：true

示例 3：

输入：s = "0110", k = 1
输出：true
解释：长度为 1 的二进制码是 "0" 和 "1"，显然两者都作为子串存在。

示例 4：

输入：s = "0110", k = 2
输出：false
解释：二进制码 "00" 长度为 2，但在数组中不存在。

示例 5：

输入：s = "0000000001011100", k = 4
输出：false

约束条件：

`1 <= s.length <= 5 * 10^5`

`s` 仅由 0 和 1 组成。

`1 <= k <= 20`
"""

from typing import List, Optional


class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        seen = set()
        for i in range(len(s) - k + 1):
            seen.add(s[i:i + k])
        return len(seen) == (1 << k)



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用滑动窗口提取所有长度为 k 的子串，放入集合 set 中自动去重。
# 最后检查集合的大小是否等于 2^k（所有可能的 k 位二进制码总数）。
# 如果等于，说明字符串包含了所有二进制码。
# 注意：如果 len(s) - k + 1 < 2^k，则可以直接返回 False（子串数量不够）。
#
# 时间复杂度: O(N * K)  -- 每个子串长度为 k，切片操作复制 O(k) 个字符
# 空间复杂度: O(2^K)  -- 集合最多存储 2^k 个不同的子串
#
# 关键点:
# - 所有长度为 k 的二进制码共有 2^k 种
# - 只需要检查去重后的子串数量是否等于 2^k
# - 可使用 rolling hash 优化到 O(N)，但对于 k <= 20 朴素方法足够









