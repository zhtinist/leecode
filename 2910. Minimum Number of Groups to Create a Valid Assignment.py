"""
LeetCode #2910 - Minimum Number of Groups to Create a Valid Assignment
合法分组的最少组数
https://leetcode.cn/problems/minimum-number-of-groups-to-create-a-valid-assignment/

给你一组带编号的 `balls` 并要求将它们分类到盒子里，以便均衡地分配。你必须遵守两条规则：
同一个盒子里的球必须具有相同的编号。但是，如果你有多个相同编号的球，你可以把它们放在不同的盒子里。
最大的盒子只能比最小的盒子多一个球。
返回遵循上述规则排列这些球所需要的盒子的最小数目。

示例 1：
输入：balls = [3,2,3,2,3] 输出：2 解释：一个得到 2 个分组的方案如下，中括号内的数字都是下标： 我们可以如下排列 balls 到盒子里： - [3,3,3] - [2,2] 两个盒子之间的大小差没有超过 1。
示例 2：
输入：balls = [10,10,10,3,1,1] 输出：4 解释：我们可以如下排列 balls 到盒子里： - [10] - [10,10] - [3] - [1,1] 无法得到一个遵循上述规则且小于 4 盒的答案。例如，把所有三个编号为 10 的球都放在一个盒子里，就会打破盒子之间最大尺寸差异的规则。

提示：
`1 <= balls.length <= 10^5`
`1 <= balls[i] <= 10^9`
"""

from typing import List, Optional


class Solution:
    def minGroupsForValidAssignment(self, balls: List[int]) -> int:
        from collections import Counter
        freq = list(Counter(balls).values())
        min_freq = min(freq)
        ans = float('inf')

        for a in range(1, min_freq + 1):
            total = 0
            possible = True
            for c in freq:
                # Check if c can be split into groups of a and a+1
                # y ≡ c (mod a), we want max y <= c // (a+1)
                r = c % a
                max_k = (c // (a + 1) - r) // a
                if max_k < 0:
                    possible = False
                    break
                y = r + max_k * a
                groups = (c - y) // a  # = (c - y) // a + y... wait let me recalc
                # groups = y + (c - y*(a+1)) // a
                groups = y + (c - y * (a + 1)) // a
                total += groups
            if possible:
                ans = min(ans, total)

        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Array, Hash Table
#
# 解题思路:
# 统计每种球的频率。盒子的最小尺寸 a 从 1 到 min_freq 枚举。对于每个 a，检查所有频率值 c 是否可以拆分为大小为 a 和 a+1 的组。
# 检查条件：c 可表示为 x*a + y*(a+1) 当且仅当 (c // (a+1) - c%a) // a >= 0。
# 若可行，计算总组数 = sum(y + (c-y*(a+1))//a)，取所有可行 a 的最小总组数。
#
# 时间复杂度: O(min_freq * k) 其中 k 为不同值的数量
# 空间复杂度: O(k)
#
# 关键点:
# - 频率值 c 拆分为 a 和 a+1：先确定 (a+1) 组数 y（满足 y ≡ c mod a）
# - 要使总组数最小，应最大化 y（使用更多大盒子）
# - 枚举 a 从 1 到 min_freq，取最小总组数
