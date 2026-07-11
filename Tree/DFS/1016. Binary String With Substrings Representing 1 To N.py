"""
LeetCode #1016 - Binary String With Substrings Representing 1 To N
中文题名：子串能表示从1到N数字的二进制串
https://leetcode.com/problems/binary-string-with-substrings-representing-1-to-n/

Given a binary string `S` (a string consisting only of '0' and '1's)
and a positive integer `N`, return true if and only if for every integer X from 1
to N, the binary representation of X is a substring of S.

Example 1:

Input: S = "0110", N = 3
Output: true

Example 2:

Input: S = "0110", N = 4
Output: false

Note:

`1 <= S.length <= 1000`

`1 <= N <= 10^9`

【中文翻译】
给定一个二进制字符串 `S`（一个仅由 '0' 和 '1' 组成的字符串）和一个正整数 `N`，如果对于从 1 到 N 的每个整数 X，其二进制表示都是 S 的子串，则返回 true。

示例 1：

输入：S = "0110", N = 3
输出：true

示例 2：

输入：S = "0110", N = 4
输出：false

注意：

`1 <= S.length <= 1000`

`1 <= N <= 10^9`

"""

from typing import List, Optional


class Solution:
    def queryString(self, S: str, N: int) -> bool:
        seen = set()
        n = len(S)
        for i in range(n):
            if S[i] == '0':
                continue
            num = 0
            for j in range(i, min(n, i + 32)):
                num = num * 2 + (ord(S[j]) - ord('0'))
                if num > N:
                    break
                seen.add(num)
        return len(seen) == N










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 枚举 S 中所有可能的二进制子串，将其转换为十进制数字并加入集合。
# 从每个位置 i（跳过 '0' 开头以避免前导零问题）开始，逐位构建数字：
# num = num * 2 + bit，将合法的 num（1 <= num <= N）加入集合。
# 由于 N <= 10^9 < 2^30，每个起始位置最多扩展 30 位。
# 遍历完成后检查集合大小是否等于 N（包含 1 到 N 的所有数字）。
#
# 时间复杂度: O(|S| * log N) - |S| 个起始位置，每个最多扩展 log₂(N) ≈ 30 位
# 空间复杂度: O(min(|S|², N)) - 集合存储所有可能的数字值
#
# 关键点:
# - 从 S 生成所有可能的子串数字，而非检查 1 到 N 每个数字（N 可达 10^9）
# - 跳过以 '0' 开头的子串避免前导零
# - 限制每次扩展最多 30 位（因为 N <= 10^9 < 2^30）
