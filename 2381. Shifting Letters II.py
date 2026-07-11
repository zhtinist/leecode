"""
LeetCode #2381 - Shifting Letters II
字母移位 II
https://leetcode.cn/problems/shifting-letters-ii/

给你一个小写英文字母组成的字符串 `s` 和一个二维整数数组 `shifts` ，其中 `shifts[i] = [start_i, end_i, direction_i]` 。对于每个 `i` ，将 `s` 中从下标 `start_i` 到下标 `end_i` （两者都包含）所有字符都进行移位运算，如果 `direction_i = 1` 将字符向后移位，如果 `direction_i = 0` 将字符向前移位。
将一个字符 向后 移位的意思是将这个字符用字母表中 下一个 字母替换（字母表视为环绕的，所以 `'z'` 变成 `'a'`）。类似的，将一个字符 向前 移位的意思是将这个字符用字母表中 前一个 字母替换（字母表是环绕的，所以 `'a'` 变成 `'z'` ）。
请你返回对 `s` 进行所有移位操作以后得到的最终字符串。

示例 1：
输入：s = "abc", shifts = [[0,1,0],[1,2,1],[0,2,1]] 输出："ace" 解释：首先，将下标从 0 到 1 的字母向前移位，得到 s = "zac" 。 然后，将下标从 1 到 2 的字母向后移位，得到 s = "zbd" 。 最后，将下标从 0 到 2 的字符向后移位，得到 s = "ace" 。
示例 2:
输入：s = "dztz", shifts = [[0,0,0],[1,1,1]] 输出："catz" 解释：首先，将下标从 0 到 0 的字母向前移位，得到 s = "cztz" 。 最后，将下标从 1 到 1 的字符向后移位，得到 s = "catz" 。

提示：
`1 <= s.length, shifts.length <= 5 * 10^4`
`shifts[i].length == 3`
`0 <= start_i <= end_i < s.length`
`0 <= direction_i <= 1`
`s` 只包含小写英文字母。
"""

from typing import List, Optional


class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        diff = [0] * (n + 1)

        for start, end, direction in shifts:
            delta = 1 if direction == 1 else -1
            diff[start] += delta
            diff[end + 1] -= delta

        # Compute prefix sum to get net shift for each position
        net_shift = 0
        result = []
        for i in range(n):
            net_shift += diff[i]
            # Apply shift to character
            new_char = chr(
                (ord(s[i]) - ord('a') + net_shift) % 26 + ord('a')
            )
            result.append(new_char)

        return ''.join(result)



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, String, Prefix Sum
#
# 解题思路:
# 使用差分数组优化区间更新操作。
# 1. 创建长度为 n+1 的 diff 数组，对于每个 shift 操作 [start, end, direction]：
#    delta = +1（向后移位，direction=1）或 -1（向前移位，direction=0）
#    diff[start] += delta, diff[end+1] -= delta
# 2. 通过前缀和恢复每个位置的净偏移量 net_shift
# 3. 对每个字符应用移位：(ord(ch) - ord('a') + net_shift) % 26 + ord('a')
#    注意处理负数取模的情况，Python 的 % 自带正数结果
#
# 时间复杂度: O(n + m) 其中 n 为字符串长度，m 为 shifts 数组的长度
# 空间复杂度: O(n) 差分数组的大小为 n+1
#
# 关键点:
# - 差分数组技巧将区间更新从 O(n) 优化为 O(1)
# - 前缀和恢复每个位置的实际偏移量
# - Python 的取模运算 (a % 26) 对负数也能返回 [0, 25] 范围内的正值
