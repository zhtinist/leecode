"""
LeetCode #1375 - Number of Times Binary String Is Prefix-Aligned
中文题名：二进制字符串前缀对齐的次数
https://leetcode.com/problems/number-of-times-binary-string-is-prefix-aligned/

There is a room with `n` bulbs, numbered from `1` to
`n`, arranged in a row from left to right. Initially, all the bulbs are
turned off.

At moment k (for k from `0` to `n - 1`), we
turn on the `light[k]` bulb. A bulb change color to
blue only if it is on and all the previous bulbs (to the left) are
turned on too.

Return the number of moments in which all turned on bulbs are
blue.

Example 1:

Input: light = [2,1,3,5,4]
Output: 3
Explanation: All bulbs turned on, are blue at the moment 1, 2 and 4.

Example 2:

Input: light = [3,2,4,1,5]
Output: 2
Explanation: All bulbs turned on, are blue at the moment 3, and 4 (index-0).

Example 3:

Input: light = [4,1,2,3]
Output: 1
Explanation: All bulbs turned on, are blue at the moment 3 (index-0).
Bulb 4th changes to blue at the moment 3.

Example 4:

Input: light = [2,1,4,3,6,5]
Output: 3

Example 5:

Input: light = [1,2,3,4,5,6]
Output: 6

Constraints:

`n == light.length`

`1 <= n <= 5 * 10^4`

`light` is a permutation of  `[1, 2, ..., n]`

【中文翻译】
房间中有 `n` 个灯泡，编号从 `1` 到 `n`，从左到右排成一行。初始时所有灯泡都是关闭的。

在第 k 时刻（k 从 `0` 到 `n - 1`），我们打开 `light[k]` 灯泡。一个灯泡只有当它处于打开状态且它左边的所有灯泡也都打开时，才会变成蓝色。

返回所有打开的灯泡都是蓝色的时刻数量。

示例 1：
输入：light = [2,1,3,5,4]
输出：3
解释：所有打开的灯泡都是蓝色的时刻为第 1、2 和 4 时刻。

示例 2：
输入：light = [3,2,4,1,5]
输出：2
解释：所有打开的灯泡都是蓝色的时刻为第 3 和第 4 时刻（下标从 0 开始）。

示例 3：
输入：light = [4,1,2,3]
输出：1
解释：所有打开的灯泡都是蓝色的时刻为第 3 时刻（下标从 0 开始）。第 4 个灯泡在第 3 时刻变蓝。

示例 4：
输入：light = [2,1,4,3,6,5]
输出：3

示例 5：
输入：light = [1,2,3,4,5,6]
输出：6
"""

from typing import List


class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        max_seen = 0
        result = 0

        for i, bulb in enumerate(light):
            max_seen = max(max_seen, bulb)
            # 第 i 时刻（0-indexed）打开了 i+1 个灯泡
            # 如果 max_seen == i+1，说明前 i+1 个灯泡都被打开了，全部变蓝
            if max_seen == i + 1:
                result += 1

        return result



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 在第 k 时刻（0-indexed），我们打开了 k+1 个灯泡。要使所有已打开灯泡都变蓝，
# 意味着所有编号为 1 到 k+1 的灯泡都已打开（即左侧没有空缺）。
# 换言之，当前已打开灯泡中的最大编号 max_seen 应等于已打开灯泡数量 k+1。
# 遍历 light 数组，维护当前已打开灯泡的最大编号 max_seen。
# 当 max_seen == i + 1 时，说明前 i+1 个灯泡已全部打开，该时刻所有灯泡变蓝。
#
# 时间复杂度: O(N)，单次遍历
# 空间复杂度: O(1)
#
# 关键点:
# - 前缀对齐的等价条件：max_seen == 已打开灯泡数
# - max_seen == i+1 意味着 1 到 i+1 之间没有"缺口"
# - light 是 [1,n] 的排列，保证每个灯泡只打开一次













