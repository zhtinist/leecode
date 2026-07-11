"""
LeetCode #2212 - Maximum Points in an Archery Competition
射箭比赛中的最大得分
https://leetcode.cn/problems/maximum-points-in-an-archery-competition/

Alice 和 Bob 是一场射箭比赛中的对手。比赛规则如下：
Alice 先射 `numArrows` 支箭，然后 Bob 也射 `numArrows` 支箭。
分数按下述规则计算：
箭靶有若干整数计分区域，范围从 `0` 到 `11` （含 `0` 和 `11`）。
箭靶上每个区域都对应一个得分 `k`（范围是 `0` 到 `11`），Alice 和 Bob 分别在得分 `k` 区域射中 `a_k` 和 `b_k` 支箭。如果 `a_k >= b_k` ，那么 Alice 得 `k` 分。如果 `a_k < b_k` ，则 Bob 得 `k` 分
如果 `a_k == b_k == 0` ，那么无人得到 `k` 分。

例如，Alice 和 Bob 都向计分为 `11` 的区域射 `2` 支箭，那么 Alice 得 `11` 分。如果 Alice 向计分为 `11` 的区域射 `0` 支箭，但 Bob 向同一个区域射 `2` 支箭，那么 Bob 得 `11` 分。
给你整数 `numArrows` 和一个长度为 `12` 的整数数组 `aliceArrows` ，该数组表示 Alice 射中 `0` 到 `11` 每个计分区域的箭数量。现在，Bob 想要尽可能 最大化 他所能获得的总分。
返回数组 `bobArrows` ，该数组表示 Bob 射中 `0` 到 `11` 每个 计分区域的箭数量。且 `bobArrows` 的总和应当等于 `numArrows` 。
如果存在多种方法都可以使 Bob 获得最大总分，返回其中 任意一种 即可。

示例 1：

输入：numArrows = 9, aliceArrows = [1,1,0,1,0,0,2,1,0,1,2,0] 输出：[0,0,0,0,1,1,0,0,1,2,3,1] 解释：上表显示了比赛得分情况。 Bob 获得总分 4 + 5 + 8 + 9 + 10 + 11 = 47 。 可以证明 Bob 无法获得比 47 更高的分数。
示例 2：

输入：numArrows = 3, aliceArrows = [0,0,1,0,0,0,0,0,0,0,0,2] 输出：[0,0,0,0,0,0,0,0,1,1,1,0] 解释：上表显示了比赛得分情况。 Bob 获得总分 8 + 9 + 10 = 27 。 可以证明 Bob 无法获得比 27 更高的分数。

提示：
`1 <= numArrows <= 10^5`
`aliceArrows.length == bobArrows.length == 12`
`0 <= aliceArrows[i], bobArrows[i] <= numArrows`
`sum(aliceArrows[i]) == numArrows`
"""

from typing import List, Optional


class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        max_score = 0
        best_bob = [0] * 12

        # Enumerate all subsets of regions 1..11
        # (region 0 gives 0 points, so we can ignore it for winning decisions)
        # 2^11 = 2048 possible combinations
        for mask in range(1 << 11):
            arrows_needed = 0
            score = 0
            bob = [0] * 12

            # Check each region k from 1 to 11
            for k in range(1, 12):
                if mask & (1 << (k - 1)):
                    # Bob needs to beat Alice: at least aliceArrows[k] + 1
                    need = aliceArrows[k] + 1
                    arrows_needed += need
                    score += k
                    bob[k] = need

            if arrows_needed <= numArrows and score > max_score:
                max_score = score
                # Put remaining arrows in region 0 (they don't affect score)
                bob[0] = numArrows - arrows_needed
                best_bob = bob

        return best_bob


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Bit Manipulation, Array, Backtracking, Enumeration
#
# 解题思路:
# 1. 问题可以转化为：Bob 在 12 个计分区域中分配箭支，对每个区域 k，
#    Bob 可以选择"获胜"（射中 aliceArrows[k] + 1 支箭，获得 k 分）
#    或者"放弃"（射任意数量但不超过 Alice，不得分）。
# 2. 记分区域 0 的分值为 0，因此 Bob 没有理由在区域 0 上投入超过
#    aliceArrows[0] 的箭支来"获胜"（因为付出代价却没有得分回报）。
#    剩余的箭支可以全部分配给区域 0。
# 3. 对于区域 1 到 11，每个区域都是一个"物品"：花费为 aliceArrows[k] + 1，
#    收益为 k。总箭支限制为 numArrows。这是一个 0/1 背包问题。
# 4. 由于只有 11 个有效区域（k=1 到 11），我们可以枚举所有 2^11 = 2048
#    种子集组合。对于每种组合：
#    a) 计算所需的箭支总数。
#    b) 如果总数 <= numArrows，计算总得分。
#    c) 记录最高得分及其对应的箭支分配方案。
#    d) 多余的箭支全部放入区域 0。
#
# 时间复杂度: O(2^M * M)，其中 M = 11。2048 * 11 ≈ 22528 次运算，完全可行。
# 空间复杂度: O(M)，存储最佳分配方案（12 个整数）。
#
# 关键点:
# - 搜索空间小（2^11），可以直接枚举而非使用动态规划。
# - 区域 0 的分值为 0，因此不需要考虑在区域 0 上"获胜"。
# - Bob 要在一个区域获胜，需要恰好 aliceArrows[k] + 1 支箭（比 Alice 多即可）。
# - 题目保证 sum(aliceArrows) == numArrows，所以 Bob 的箭支总数也需要恰好等于 numArrows。
