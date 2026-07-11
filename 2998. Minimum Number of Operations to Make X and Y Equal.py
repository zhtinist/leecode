"""
LeetCode #2998 - Minimum Number of Operations to Make X and Y Equal
使 X 和 Y 相等的最少操作次数
https://leetcode.cn/problems/minimum-number-of-operations-to-make-x-and-y-equal/

给你两个正整数 `x` 和 `y` 。
一次操作中，你可以执行以下四种操作之一：
如果 `x` 是 `11` 的倍数，将 `x` 除以 `11` 。
如果 `x` 是 `5` 的倍数，将 `x` 除以 `5` 。
将 `x` 减 `1` 。
将 `x` 加 `1` 。
请你返回让 `x` 和 `y` 相等的 最少 操作次数。

示例 1：
输入：x = 26, y = 1 输出：3 解释：我们可以通过以下操作将 26 变为 1 ： 1. 将 x 减 1 2. 将 x 除以 5 3. 将 x 除以 5 将 26 变为 1 最少需要 3 次操作。
示例 2：
输入：x = 54, y = 2 输出：4 解释：我们可以通过以下操作将 54 变为 2 ： 1. 将 x 加 1 2. 将 x 除以 11 3. 将 x 除以 5 4. 将 x 加 1 将 54 变为 2 最少需要 4 次操作。
示例 3：
输入：x = 25, y = 30 输出：5 解释：我们可以通过以下操作将 25 变为 30 ： 1. 将 x 加 1 2. 将 x 加 1 3. 将 x 加 1 4. 将 x 加 1 5. 将 x 加 1 将 25 变为 30 最少需要 5 次操作。

提示：
`1 <= x, y <= 10^4`
"""

from typing import List, Optional


class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        """
        BFS from x to y. Operations: /11, /5, -1, +1.
        Use a queue and visited set. Cap the search space reasonably.
        """
        if x == y:
            return 0

        from collections import deque

        # Upper bound: going above y + some padding, but going too high is wasteful
        # Actually, since we can only go up by 1, and the target is y,
        # we don't need to go much above max(x, y). But we might go up to a
        # multiple of 5 or 11 to divide. Bound by something reasonable.
        limit = max(x, y) * 2 + 100  # safe upper bound
        visited = set()
        q = deque()
        q.append((x, 0))
        visited.add(x)

        while q:
            cur, steps = q.popleft()
            if cur == y:
                return steps

            # +1
            nxt = cur + 1
            if nxt <= limit and nxt not in visited:
                if nxt == y:
                    return steps + 1
                visited.add(nxt)
                q.append((nxt, steps + 1))

            # -1
            nxt = cur - 1
            if nxt > 0 and nxt not in visited:
                if nxt == y:
                    return steps + 1
                visited.add(nxt)
                q.append((nxt, steps + 1))

            # /5
            if cur % 5 == 0:
                nxt = cur // 5
                if nxt not in visited:
                    if nxt == y:
                        return steps + 1
                    visited.add(nxt)
                    q.append((nxt, steps + 1))

            # /11
            if cur % 11 == 0:
                nxt = cur // 11
                if nxt not in visited:
                    if nxt == y:
                        return steps + 1
                    visited.add(nxt)
                    q.append((nxt, steps + 1))

        return -1  # should not reach here



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Breadth-First Search, Memoization, Dynamic Programming
#
# 解题思路:
# 使用 BFS 搜索从 x 到 y 的最短路径。每个状态有四种操作：/11（若整除）、/5（若整除）、-1、+1。
# 设置搜索上限为 max(x, y)*2+100，因为通过 +1 再除法的策略最多需要向上调整到附近的倍数即可。
# BFS 保证首次到达 y 时步数最少。
#
# 时间复杂度: O(N)，其中 N 为搜索空间大小（上限约 20000）
# 空间复杂度: O(N)，存储 visited 集合和 BFS 队列
#
# 关键点:
# - BFS 天然适合求最少操作次数（无权最短路径）
# - 上限设置：不需要无限制向上搜索，到达一定阈值后 +1 已无意义
# - 除法操作是单向缩小，+1/-1 是双向调整，需要 visited 防止重复
