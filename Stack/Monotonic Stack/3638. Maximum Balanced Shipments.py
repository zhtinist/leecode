"""
LeetCode #3638 - Maximum Balanced Shipments
平衡装运的最大数量
https://leetcode.cn/problems/maximum-balanced-shipments/

给你一个长度为 `n` 的整数数组 `weight`，表示按直线排列的 `n` 个包裹的重量。装运 定义为包裹的一个连续子数组。如果一个装运满足以下条件，则称其为 平衡装运：最后一个包裹的重量 严格小于 该装运中所有包裹中 最大重量 。
选择若干个 不重叠 的连续平衡装运，并满足 每个包裹最多出现在一次装运中（部分包裹可以不被装运）。
返回 可以形成的平衡装运的最大数量 。

示例 1:

输入: weight = [2,5,1,4,3]
输出: 2
解释:
我们可以形成最多两个平衡装运：
装运 1: `[2, 5, 1]`
包裹的最大重量 = 5
最后一个包裹的重量 = 1，严格小于 5，因此这是平衡装运。
装运 2: `[4, 3]`
包裹的最大重量 = 4
最后一个包裹的重量 = 3，严格小于 4，因此这是平衡装运。
无法通过其他方式划分包裹获得超过两个平衡装运，因此答案是 2。
示例 2:

输入: weight = [4,4]
输出: 0
解释:
在这种情况下无法形成平衡装运：
装运 `[4, 4]` 的最大重量为 4，而最后一个包裹的重量也是 4，不严格小于最大重量，因此不是平衡的。
单个包裹的装运 `[4]` 中，最后一个包裹的重量等于最大重量，因此也不是平衡的。
由于无法形成任何平衡装运，答案是 0。

提示:
`2 <= n <= 10^5`
`1 <= weight[i] <= 10^9`
"""

from typing import List, Optional


class Solution:
    def maxBalancedShipments(self, weight: List[int]) -> int:
        count = 0
        running_max = 0
        for w in weight:
            running_max = max(running_max, w)
            if w < running_max:
                count += 1
                running_max = 0
        return count










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Stack, Greedy, Array, Dynamic Programming, Monotonic Stack
#
# 解题思路:
# 使用贪心策略扫描数组，维护当前段的最大值 running_max。当遇到一个元素 w 满足
# w < running_max 时，意味着可以以 w 结尾形成一个平衡装运（最后一个元素严格
# 小于段内最大值）。此时立即结束该段，装运数 +1，并重置 running_max 开始新段。
# 贪心策略的正确性：当 w < running_max 时，如果不在此时结束装运，继续扩展只会
# 让 running_max 不降（可能更大），而最后一个元素会变，不会增加装运数量。
#
# 时间复杂度: O(n) — 一次遍历
# 空间复杂度: O(1) — 仅使用常数额外空间
#
# 关键点:
# - 一旦 w < running_max 就立即截断形成装运
# - 重置 running_max 为 0 表示新段开始
# - 单元素段永远不是平衡的（最大元素等于最后一个元素）
