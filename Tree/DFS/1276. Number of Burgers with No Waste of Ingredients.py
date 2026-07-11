"""
LeetCode #1276 - Number of Burgers with No Waste of Ingredients
中文题名：不浪费原料的汉堡制作方案
https://leetcode.com/problems/number-of-burgers-with-no-waste-of-ingredients/

Given two integers `tomatoSlices` and `cheeseSlices`. The
ingredients of different burgers are as follows:

Jumbo Burger: 4 tomato slices and 1 cheese slice.

Small Burger: 2 Tomato slices and 1 cheese slice.

Return `[total_jumbo, total_small]` so that the number of remaining `tomatoSlices` equal
to 0 and the number of remaining `cheeseSlices` equal to 0. If it is not
possible to make the remaining `tomatoSlices` and
`cheeseSlices` equal to 0 return `[]`.

Example 1:

Input: tomatoSlices = 16, cheeseSlices = 7
Output: [1,6]
Explantion: To make one jumbo burger and 6 small burgers we need 4*1 + 2*6 = 16 tomato and 1 + 6 = 7 cheese. There will be no remaining ingredients.

Example 2:

Input: tomatoSlices = 17, cheeseSlices = 4
Output: []
Explantion: There will be no way to use all ingredients to make small and jumbo burgers.

Example 3:

Input: tomatoSlices = 4, cheeseSlices = 17
Output: []
Explantion: Making 1 jumbo burger there will be 16 cheese remaining and making 2 small burgers there will be 15 cheese remaining.

Example 4:

Input: tomatoSlices = 0, cheeseSlices = 0
Output: [0,0]

Example 5:

Input: tomatoSlices = 2, cheeseSlices = 1
Output: [0,1]

Constraints:

`0 <= tomatoSlices <= 10^7`

`0 <= cheeseSlices <= 10^7`

【中文翻译】
给定两个整数 tomatoSlices 和 cheeseSlices。不同汉堡的原料如下：

巨无霸汉堡：4片番茄和1片奶酪。
小汉堡：2片番茄和1片奶酪。

返回 [total_jumbo, total_small]，使得剩余的 tomatoSlices 和 cheeseSlices 的数量都等于 0。如果无法使剩余的 tomatoSlices 和 cheeseSlices 都等于 0，则返回 []。

示例 1：

输入：tomatoSlices = 16, cheeseSlices = 7
输出：[1,6]
解释：制作 1 个巨无霸汉堡和 6 个小汉堡需要 4*1 + 2*6 = 16 片番茄和 1 + 6 = 7 片奶酪。不会剩下任何原料。

示例 2：

输入：tomatoSlices = 17, cheeseSlices = 4
输出：[]
解释：没有办法使用所有原料制作小汉堡和巨无霸汉堡。

示例 3：

输入：tomatoSlices = 4, cheeseSlices = 17
输出：[]
解释：制作 1 个巨无霸汉堡会剩下 16 片奶酪，制作 2 个小汉堡会剩下 15 片奶酪。

示例 4：

输入：tomatoSlices = 0, cheeseSlices = 0
输出：[0,0]

示例 5：

输入：tomatoSlices = 2, cheeseSlices = 1
输出：[0,1]

约束条件：

0 <= tomatoSlices <= 10^7
0 <= cheeseSlices <= 10^7
"""

from typing import List, Optional


class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        # Let j = number of jumbo burgers, s = number of small burgers
        # Equations:
        # 4j + 2s = tomatoSlices  ... (1)
        # j + s = cheeseSlices     ... (2)
        # From (2): s = cheeseSlices - j
        # Substitute into (1): 4j + 2(cheeseSlices - j) = tomatoSlices
        # => 2j + 2 * cheeseSlices = tomatoSlices
        # => 2j = tomatoSlices - 2 * cheeseSlices
        # => j = (tomatoSlices - 2 * cheeseSlices) / 2

        total_jumbo = tomatoSlices - 2 * cheeseSlices

        if total_jumbo < 0 or total_jumbo % 2 != 0:
            return []

        j = total_jumbo // 2
        s = cheeseSlices - j

        if s < 0:
            return []

        return [j, s]










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 将问题转化为求解二元一次方程组。
# 设巨无霸汉堡数量为 j，小汉堡数量为 s，则有：
#   4j + 2s = tomatoSlices  (番茄片数方程)
#   j + s = cheeseSlices     (奶酪片数方程)
# 由奶酪方程得 s = cheeseSlices - j，代入番茄方程：
#   4j + 2(cheeseSlices - j) = tomatoSlices
#   2j + 2 * cheeseSlices = tomatoSlices
#   j = (tomatoSlices - 2 * cheeseSlices) / 2
# 需要验证 j >= 0, s >= 0 且 j 为整数(即分子为偶数)。
#
# 时间复杂度: O(1) - 仅进行常数次算术运算
# 空间复杂度: O(1) - 不使用额外空间
#
# 关键点:
# - 将问题抽象为线性方程组，利用数学推导直接求解
# - 验证解的有效性：j 和 s 必须为非负整数
# - 番茄数必须为偶数（两个方程的系数推导）
