"""
LeetCode #1529 - Minimum Suffix Flips
中文题名：最少的后缀翻转次数
https://leetcode.com/problems/minimum-suffix-flips/

There is a room with `n` bulbs, numbered from `0` to `n-1`, arranged
in a row from left to right. Initially all the bulbs are turned off.

Your task is to obtain the configuration represented by `target` where `target[i]`
is '1' if the i-th bulb is turned on and is '0' if it is turned off.

You have a switch to flip the state of the bulb, a flip operation is
defined as follows:

Choose any bulb (index `i`) of your
current configuration.

Flip each bulb from index `i` to `n-1`.

When any bulb is flipped it means that if it is 0 it changes to 1 and if it is 1 it
changes to 0.

Return the minimum number of flips required to form
`target`.

Example 1:

Input: target = "10111"
Output: 3
Explanation: Initial configuration "00000".
flip from the third bulb:  "00000" -> "00111"
flip from the first bulb:  "00111" -> "11000"
flip from the second bulb:  "11000" -> "10111"
We need at least 3 flip operations to form target.

Example 2:

Input: target = "101"
Output: 3
Explanation: "000" -> "111" -> "100" -> "101".

Example 3:

Input: target = "00000"
Output: 0

Example 4:

Input: target = "001011101"
Output: 5

Constraints:

`1 <= target.length <= 10^5`

`target[i] == '0'` or `target[i] == '1'`

【中文翻译】
有 n 个灯泡，从左到右排列，初始全部关闭（全 0）。
每次操作可以选择一个索引 i，翻转从 i 到 n-1 的所有灯泡（0 变 1，1 变 0）。
返回形成目标配置 target 所需的最少操作次数。

示例 1：

输入：target = "10111"
输出：3
解释：初始 "00000" -> 翻转第三个 -> "00111" -> 翻转第一个 -> "11000" -> 翻转第二个 -> "10111"

示例 2：

输入：target = "101"
输出：3
解释："000" -> "111" -> "100" -> "101"

示例 3：

输入：target = "00000"
输出：0

示例 4：

输入：target = "001011101"
输出：5
"""

from typing import List, Optional


class Solution:
    def minFlips(self, target: str) -> int:
        # Count transitions between 0 and 1
        flips = 0
        prev = '0'
        for ch in target:
            if ch != prev:
                flips += 1
                prev = ch
        return flips



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 从全 0 开始，每次翻转后缀会改变从某位置到末尾的所有灯泡状态。
# 从左到右扫描 target，当前期望的状态与之前不同时，需要一次翻转。
# 翻转次数等于相邻字符不同的次数。如果 target 以 '1' 开始，还需要额外一次翻转。
# 初始化 prev='0'，遍历 target，如果 ch != prev，flips++，更新 prev=ch。
#
# 时间复杂度: O(N)
# 空间复杂度: O(1)
#
# 关键点:
# - 翻转操作只影响后缀，所以从左到右处理是最优策略
# - 翻转次数 = target 中相邻字符变化的次数
# - 初始状态为全 0，以 '0' 作为 prev 的初始值
