"""
LeetCode #1049 - Last Stone Weight II
中文题名：最后一块石头的重量 II
https://leetcode.com/problems/last-stone-weight-ii/

We have a collection of rocks, each rock has a positive integer weight.

Each turn, we choose any two rocks and smash them together.
Suppose the stones have weights `x` and `y` with `x <=
y`.  The result of this smash is:

If `x == y`, both stones are totally destroyed;

If `x != y`, the stone of weight `x` is totally destroyed, and the
stone of weight `y` has new weight `y-x`.

At the end, there is at most 1 stone left.  Return the smallest
possible weight of this stone (the weight is 0 if there are no stones left.)

Example 1:

Input: [2,7,4,1,8,1]
Output: 1
Explanation:
We can combine 2 and 4 to get 2 so the array converts to [2,7,1,8,1] then,
we can combine 7 and 8 to get 1 so the array converts to [2,1,1,1] then,
we can combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we can combine 1 and 1 to get 0 so the array converts to [1] then that's the optimal value.

Note:

`1 <= stones.length <= 30`

`1 <= stones[i] <= 100`

【中文翻译】
我们有一堆石头，每块石头的重量都是正整数。

每一回合，从中选出任意两块石头，将它们一起粉碎。假设石头的重量为 x 和 y，且 x <= y。粉碎的可能结果如下：

如果 x == y，那么两块石头都会被完全粉碎；
如果 x != y，那么重量为 x 的石头将会完全粉碎，而重量为 y 的石头的新重量为 y-x。

最后，最多只会剩下一块石头。返回此石头最小的可能重量（如果没有石头剩下，则返回 0）。

示例 1：

输入：[2,7,4,1,8,1]
输出：1
解释：
组合 2 和 4，得到 2，所以数组转化为 [2,7,1,8,1]，
组合 7 和 8，得到 1，所以数组转化为 [2,1,1,1]，
组合 2 和 1，得到 1，所以数组转化为 [1,1,1]，
组合 1 和 1，得到 0，所以数组转化为 [1]，这就是最优值。

注意：

1 <= stones.length <= 30
1 <= stones[i] <= 100

"""

from typing import List, Optional


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True

        for stone in stones:
            for j in range(target, stone - 1, -1):
                dp[j] = dp[j] or dp[j - stone]

        for j in range(target, -1, -1):
            if dp[j]:
                return total - 2 * j

        return 0










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 本题可以转化为 0-1 背包问题。将石头分成两组，使得两组重量和的差值最小。
# 这等价于：在石头中选择一个子集，使其和不超过 total/2 且尽可能接近 total/2。
# 设选出的子集和为 S1，则另一组和为 total - S1，最终结果为 (total - S1) - S1 = total - 2*S1。
# 使用一维布尔 DP 数组，dp[j] 表示能否选出和为 j 的子集。
# 初始化 dp[0] = True，遍历每块石头，从后向前更新 dp。
# 最后从 target 向下找到第一个为 True 的位置 j，返回 total - 2*j。
#
# 时间复杂度: O(n * sum) - n 为石头数量，sum 为总重量的一半
# 空间复杂度: O(sum) - 一维 DP 数组大小
#
# 关键点:
# - 将问题转化为"分成两组使差值最小"，等价于背包问题
# - 目标值是 total // 2（向下取整）
# - 最终结果是 total - 2 * 最大可达子集和
# - 内层循环必须从后向前遍历（0-1 背包标准做法）
