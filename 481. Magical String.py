"""
LeetCode #481 - Magical String
中文题名：神奇字符串
https://leetcode.com/problems/magical-string/

A magical string S consists of only '1' and '2' and obeys the following rules:

The string S is magical because concatenating the number of contiguous occurrences of
characters '1' and '2' generates the string S itself.

The first few elements of string S is the following:
S = "1221121221221121122……"

If we group the consecutive '1's and '2's in S, it will be:

1 22 11 2 1 22 1 22 11 2 11 22 ......

and the occurrences of '1's or '2's in each group are:

1 2 2 1 1 2 1 2 2 1 2 2 ......

You can see that the occurrence sequence above is the S itself.

Given an integer N as input, return the number of '1's in the first N number in the magical
string S.

Note:
N will not exceed 100,000.

Example 1:

Input: 6
Output: 3
Explanation: The first 6 elements of magical string S is "12211" and it contains three 1's, so return 3.

【中文翻译】
神奇字符串 S 仅由 '1' 和 '2' 组成，并遵循以下规则：

字符串 S 是神奇的，因为将连续出现的字符 '1' 和 '2' 的出现次数拼接起来，就生成了字符串 S 本身。

字符串 S 的前几个元素如下：
S = "1221121221221121122……"

如果将 S 中连续的 '1' 和 '2' 分组，将得到：
1 22 11 2 1 22 1 22 11 2 11 22 ......

而每组中 '1' 或 '2' 的出现次数为：
1 2 2 1 1 2 1 2 2 1 2 2 ......

可以看到，上面的出现次数序列就是 S 本身。

给定一个整数 N，返回神奇字符串 S 的前 N 个字符中 '1' 的个数。

注意：N 不超过 100,000。

示例 1：
    输入：6
    输出：3
    解释：神奇字符串 S 的前 6 个元素是 "122112"，包含三个 '1'，所以返回 3。
"""

from typing import List, Optional


class Solution:
    def magicalString(self, n: int) -> int:
        if n <= 0:
            return 0
        if n <= 3:
            return 1  # "122" has one '1' in the first min(n, 3) chars

        # Build the magical string as a list of characters
        s = [1, 2, 2]  # Start with [1, 2, 2]
        i = 2  # Pointer to read the next group size from s[i]
        next_char = 1  # The next character to append (alternates: 1, 2, 1, 2, ...)

        while len(s) < n:
            count = s[i]  # How many of next_char to append
            s.extend([next_char] * count)
            next_char = 3 - next_char  # Toggle: 1 -> 2, 2 -> 1
            i += 1

        # Count '1's in the first n characters
        return s[:n].count(1)



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 模拟生成神奇字符串。使用列表 s 存储已生成的字符，初始为 [1, 2, 2]。
# 维护指针 i 从 s 中读取接下来要添加的"组大小"（即 s[i]），交替添加字符 1 和 2。
# 每次添加 s[i] 个当前字符后，切换字符（1→2 或 2→1），指针 i 向前移动一位。
# 生成到 s 长度 >= n 后，统计前 n 个字符中 '1' 的个数。
#
# 时间复杂度: O(N) — 需要生成至少 N 个字符
# 空间复杂度: O(N) — 存储生成的前 N 个字符（列表长度不会超过 N + max_group_size）
#
# 关键点:
# - 初始序列固定为 [1, 2, 2]，然后利用自描述性质生成后续字符
# - 指针 i 从索引 2 开始（读取第三个字符作为下一个组的大小）
# - 使用 3 - next_char 技巧在 1 和 2 之间切换
# - 注意 n <= 3 的边界情况：前三个字符 "122" 中只有一个 '1'
