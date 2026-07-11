"""
LeetCode #1899 - Merge Triplets to Form Target Triplet
合并若干三元组以形成目标三元组
https://leetcode.cn/problems/merge-triplets-to-form-target-triplet/

三元组 是一个由三个整数组成的数组。给你一个二维整数数组 `triplets` ，其中 `triplets[i] = [a_i, b_i, c_i]` 表示第 `i` 个 三元组 。同时，给你一个整数数组 `target = [x, y, z]` ，表示你想要得到的 三元组 。
为了得到 `target` ，你需要对 `triplets` 执行下面的操作 任意次（可能 零 次）：
选出两个下标（下标 从 0 开始 计数）`i` 和 `j`（`i != j`），并 更新 `triplets[j]` 为 `[max(a_i, a_j), max(b_i, b_j), max(c_i, c_j)]` 。
例如，`triplets[i] = [2, 5, 3]` 且 `triplets[j] = [1, 7, 5]`，`triplets[j]` 将会更新为 `[max(2, 1), max(5, 7), max(3, 5)] = [2, 7, 5]` 。
如果通过以上操作我们可以使得目标 三元组 `target` 成为 `triplets` 的一个 元素 ，则返回 `true` ；否则，返回 `false` 。

示例 1：
输入：triplets = [[2,5,3],[1,8,4],[1,7,5]], target = [2,7,5] 输出：true 解释：执行下述操作： - 选择第一个和最后一个三元组 [[2,5,3],[1,8,4],[1,7,5]] 。更新最后一个三元组为 [max(2,1), max(5,7), max(3,5)] = [2,7,5] 。triplets = [[2,5,3],[1,8,4],[2,7,5]] 目标三元组 [2,7,5] 现在是 triplets 的一个元素。
示例 2：
输入：triplets = [[1,3,4],[2,5,8]], target = [2,5,8] 输出：true 解释：目标三元组 [2,5,8] 已经是 triplets 的一个元素。
示例 3：
输入：triplets = [[2,5,3],[2,3,4],[1,2,5],[5,2,3]], target = [5,5,5] 输出：true 解释：执行下述操作： - 选择第一个和第三个三元组 [[2,5,3],[2,3,4],[1,2,5],[5,2,3]] 。更新第三个三元组为 [max(2,1), max(5,2), max(3,5)] = [2,5,5] 。triplets = [[2,5,3],[2,3,4],[2,5,5],[5,2,3]] 。 - 选择第三个和第四个三元组 [[2,5,3],[2,3,4],[2,5,5],[5,2,3]] 。更新第四个三元组为 [max(2,5), max(5,2), max(5,3)] = [5,5,5] 。triplets = [[2,5,3],[2,3,4],[2,5,5],[5,5,5]] 。 目标三元组 [5,5,5] 现在是 triplets 的一个元素。
示例 4：
输入：triplets = [[3,4,5],[4,5,6]], target = [3,2,5] 输出：false 解释：无法得到 [3,2,5] ，因为 triplets 不含 2 。

提示：
`1 <= triplets.length <= 10^5`
`triplets[i].length == target.length == 3`
`1 <= a_i, b_i, c_i, x, y, z <= 1000`
"""

from typing import List, Optional


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x, y, z = target
        # Track the best we can achieve for each dimension
        best = [0, 0, 0]

        for a, b, c in triplets:
            # Only consider triplets that don't exceed target in any dimension
            if a <= x and b <= y and c <= z:
                best[0] = max(best[0], a)
                best[1] = max(best[1], b)
                best[2] = max(best[2], c)

        return best == target



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Array
#
# 解题思路:
# 贪心策略：
# 1. 只考虑每个维度都不超过 target 的三元组（因为 max 操作只会增大，
#    任何维度超过 target 的三元组都不能使用）。
# 2. 对于所有可行的三元组，取每个维度的最大值。
#    由于我们可以通过反复合并来累积每个维度的最大值，
#    只要最终能达到 target 即可。
# 3. 检查 best 是否等于 target。
#
# 时间复杂度: O(n) — 遍历所有三元组一次
# 空间复杂度: O(1) — 常数空间
#
# 关键点:
# - MAX 操作具有单调性：值只会增大不会减小
# - 任何维度超过 target 的三元组不能使用
# - 只要在可行三元组中每个维度都能达到 target 的值即可
# - 不需要实际模拟合并过程
