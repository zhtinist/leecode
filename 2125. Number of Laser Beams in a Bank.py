"""
LeetCode #2125 - Number of Laser Beams in a Bank
银行中的激光束数量
https://leetcode.cn/problems/number-of-laser-beams-in-a-bank/

银行内部的防盗安全装置已经激活。给你一个下标从 0 开始的二进制字符串数组 `bank` ，表示银行的平面图，这是一个大小为 `m x n` 的二维矩阵。 `bank[i]` 表示第 `i` 行的设备分布，由若干 `'0'` 和若干 `'1'` 组成。`'0'` 表示单元格是空的，而 `'1'` 表示单元格有一个安全设备。
对任意两个安全设备而言，如果同时 满足下面两个条件，则二者之间存在 一个 激光束：
两个设备位于两个 不同行 ：`r_1` 和 `r_2` ，其中 `r_1 < r_2` 。
满足 `r_1 < i < r_2` 的 所有 行 `i` ，都 没有安全设备 。
激光束是独立的，也就是说，一个激光束既不会干扰另一个激光束，也不会与另一个激光束合并成一束。
返回银行中激光束的总数量。

示例 1：

输入：bank = ["011001","000000","010100","001000"] 输出：8 解释：在下面每组设备对之间，存在一条激光束。总共是 8 条激光束：  * bank[0][1] -- bank[2][1]  * bank[0][1] -- bank[2][3]  * bank[0][2] -- bank[2][1]  * bank[0][2] -- bank[2][3]  * bank[0][5] -- bank[2][1]  * bank[0][5] -- bank[2][3]  * bank[2][1] -- bank[3][2]  * bank[2][3] -- bank[3][2] 注意，第 0 行和第 3 行上的设备之间不存在激光束。 这是因为第 2 行存在安全设备，这不满足第 2 个条件。
示例 2：

输入：bank = ["000","111","000"] 输出：0 解释：不存在两个位于不同行的设备

提示：
`m == bank.length`
`n == bank[i].length`
`1 <= m, n <= 500`
`bank[i][j]` 为 `'0'` 或 `'1'`
"""

from typing import List, Optional


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev_count = 0
        total = 0

        for row in bank:
            count = row.count('1')
            if count > 0:
                total += prev_count * count
                prev_count = count

        return total



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Math, String, Matrix
#
# 解题思路:
# 激光束只存在于两个"非空行"之间，中间所有行必须全为空。
# 因此，只需要关注含有安全设备（'1'）的行：
# - 遍历每一行，统计该行中 '1' 的数量。
# - 如果当前行有设备，则它与上一行有设备的行之间的激光束数量为 prev_count * current_count。
# - 累加到总数后，更新 prev_count = current_count。
# - 如果当前行没有设备，直接跳过（不影响 prev_count）。
#
# 时间复杂度: O(m * n)，其中 m 为行数，n 为列数（每行需遍历统计 '1'）
# 空间复杂度: O(1)
#
# 关键点:
# - 空行不产生激光束，但也不影响前后的配对关系
# - 乘法原理：前一非空行的每个设备与当前行每个设备形成一条激光束
# - 跳过连续的零行，只在遇到非零行时计算
