"""
LeetCode #1419 - Minimum Number of Frogs Croaking
中文题名：数青蛙
https://leetcode.com/problems/minimum-number-of-frogs-croaking/

Given the string `croakOfFrogs`, which represents a combination of the
string "croak" from different frogs, that is, multiple frogs can croak at the same time,
so multiple “croak” are mixed. Return the minimum number of different
frogs to finish all the croak in the given string.

A valid "croak" means a frog is printing 5 letters ‘c’, ’r’, ’o’, ’a’, ’k’ sequentially. The
frogs have to print all five letters to finish a croak. If the given string is
not a combination of valid "croak" return -1.

Example 1:

Input: croakOfFrogs = "croakcroak"
Output: 1
Explanation: One frog yelling "croak" twice.

Example 2:

Input: croakOfFrogs = "crcoakroak"
Output: 2
Explanation: The minimum number of frogs is two.
The first frog could yell "crcoakroak".
The second frog could yell later "crcoakroak".

Example 3:

Input: croakOfFrogs = "croakcrook"
Output: -1
Explanation: The given string is an invalid combination of "croak" from different frogs.

Example 4:

Input: croakOfFrogs = "croakcroa"
Output: -1

Constraints:

`1 <= croakOfFrogs.length <= 10^5`

All characters in the string are: `'c'`, `'r'`,
`'o'`, `'a'` or `'k'`.

【中文翻译】

给定一个字符串 `croakOfFrogs`，表示来自不同青蛙的 "croak" 字符串的组合，即多只青蛙可以同时鸣叫，因此多个 "croak" 是混合在一起的。返回完成给定字符串中所有 croak 所需的不同青蛙的最少数量。

一个有效的 "croak" 表示一只青蛙按顺序发出 5 个字母 'c'、'r'、'o'、'a'、'k'。青蛙必须发出全部五个字母才能完成一次 croak。如果给定的字符串不是有效 "croak" 的组合，则返回 -1。

示例 1：
输入：croakOfFrogs = "croakcroak"
输出：1
解释：一只青蛙叫了两声 "croak"。

示例 2：
输入：croakOfFrogs = "crcoakroak"
输出：2
解释：最少需要两只青蛙。
第一只青蛙可以叫 "crcoakroak"。
第二只青蛙稍后叫 "crcoakroak"。

示例 3：
输入：croakOfFrogs = "croakcrook"
输出：-1
解释：给定的字符串不是来自不同青蛙的有效 "croak" 组合。

示例 4：
输入：croakOfFrogs = "croakcroa"
输出：-1

约束条件：
`1 <= croakOfFrogs.length <= 10^5`
字符串中的所有字符都是：`'c'`、`'r'`、`'o'`、`'a'` 或 `'k'`。

"""

from typing import List, Optional


class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        # 字符到索引的映射
        char_to_idx = {'c': 0, 'r': 1, 'o': 2, 'a': 3, 'k': 4}
        # counts[0]: c 的数量, counts[1]: r 的数量, ..., counts[4]: k 的数量
        counts = [0] * 5

        max_frogs = 0
        active_frogs = 0  # 当前正在鸣叫中的青蛙数

        for ch in croakOfFrogs:
            idx = char_to_idx.get(ch, -1)
            if idx == -1:
                return -1

            if idx == 0:  # 'c'
                # 开始一次新的 croak
                counts[0] += 1
                active_frogs += 1
                max_frogs = max(max_frogs, active_frogs)
            else:
                # 前一个阶段的字符必须有计数 > 0
                if counts[idx - 1] == 0:
                    return -1
                counts[idx - 1] -= 1
                counts[idx] += 1

                if idx == 4:  # 'k'，一次 croak 完成
                    active_frogs -= 1

        # 所有呼叫必须完整结束（所有中间状态计数应为 0，除了 k）
        if active_frogs != 0 or any(counts[i] != 0 for i in range(4)):
            return -1

        return max_frogs



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 状态计数法（模拟并发 croak）：
# 1. 将字符 'c', 'r', 'o', 'a', 'k' 映射到索引 0-4，表示 croak 的五个阶段。
# 2. 使用数组 counts[5] 记录当前处于每个阶段的字符数量。
# 3. 使用 active_frogs 记录当前正在鸣叫（尚未完成 k）的青蛙数量。
# 4. 遍历字符串中的每个字符 ch：
#    a. 如果是 'c'（idx=0）：
#       - counts[0] += 1，active_frogs += 1。
#       - 更新 max_frogs = max(max_frogs, active_frogs)。
#       - 这表示一只新的青蛙开始鸣叫（或复用已完成鸣叫的青蛙）。
#    b. 如果是其他字符（idx > 0）：
#       - 检查前一个阶段 counts[idx-1] 是否 > 0。若否，说明没有正在进行的 croak
#         可以继续此阶段，返回 -1。
#       - counts[idx-1] -= 1，counts[idx] += 1。
#       - 如果 idx == 4（'k'），一次 croak 完成，active_frogs -= 1。
# 5. 遍历结束后，检查所有阶段计数是否归零（active_frogs == 0 且 counts[0..3] 全为 0）。
#    如果不是，说明有未完成的 croak，返回 -1。
# 6. 返回 max_frogs。
#
# 时间复杂度: O(N)，只遍历一次字符串。
# 空间复杂度: O(1)，只使用固定大小的数组。
#
# 关键点:
# - 用 active_frogs 跟踪并发青蛙数，max_frogs 记录峰值
# - 每个字符必须是 croak 序列的下一个合法字符
# - 遍历完必须所有青蛙都完成鸣叫（状态的最后检查）










