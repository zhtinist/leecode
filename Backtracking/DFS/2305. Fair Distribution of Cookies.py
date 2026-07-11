"""
LeetCode #2305 - Fair Distribution of Cookies
公平分发饼干
https://leetcode.cn/problems/fair-distribution-of-cookies/

给你一个整数数组 `cookies` ，其中 `cookies[i]` 表示在第 `i` 个零食包中的饼干数量。另给你一个整数 `k` 表示等待分发零食包的孩子数量，所有 零食包都需要分发。在同一个零食包中的所有饼干都必须分发给同一个孩子，不能分开。
分发的 不公平程度 定义为单个孩子在分发过程中能够获得饼干的最大总数。
返回所有分发的最小不公平程度。

示例 1：
输入：cookies = [8,15,10,20,8], k = 2 输出：31 解释：一种最优方案是 [8,15,8] 和 [10,20] 。 - 第 1 个孩子分到 [8,15,8] ，总计 8 + 15 + 8 = 31 块饼干。 - 第 2 个孩子分到 [10,20] ，总计 10 + 20 = 30 块饼干。 分发的不公平程度为 max(31,30) = 31 。 可以证明不存在不公平程度小于 31 的分发方案。
示例 2：
输入：cookies = [6,1,3,2,2,4,1,2], k = 3 输出：7 解释：一种最优方案是 [6,1]、[3,2,2] 和 [4,1,2] 。 - 第 1 个孩子分到 [6,1] ，总计 6 + 1 = 7 块饼干。  - 第 2 个孩子分到 [3,2,2] ，总计 3 + 2 + 2 = 7 块饼干。 - 第 3 个孩子分到 [4,1,2] ，总计 4 + 1 + 2 = 7 块饼干。 分发的不公平程度为 max(7,7,7) = 7 。 可以证明不存在不公平程度小于 7 的分发方案。

提示：
`2 <= cookies.length <= 8`
`1 <= cookies[i] <= 10^5`
`2 <= k <= cookies.length`
"""

from typing import List, Optional


class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        n = len(cookies)
        # 将饼干包按降序排序，大包优先分配有利于剪枝
        cookies.sort(reverse=True)

        # children[i] 表示第 i 个孩子当前分到的饼干总数
        children = [0] * k
        # 全局最优解，初始化为无穷大
        self.answer = float('inf')

        def backtrack(idx: int) -> None:
            # 所有饼干包都已分配完毕
            if idx == n:
                # 不公平程度 = max(children)
                self.answer = min(self.answer, max(children))
                return

            # 剪枝：当前最大分配量已 >= 已知最优解，无需继续
            if max(children) >= self.answer:
                return

            # 将第 idx 包饼干分配给某个孩子
            for i in range(k):
                # 剪枝优化：如果当前孩子和前一个孩子分配量相同，
                # 分配给他和分配给前一个孩子效果一样，跳过避免重复搜索
                if i > 0 and children[i] == children[i - 1]:
                    continue

                children[i] += cookies[idx]
                backtrack(idx + 1)
                children[i] -= cookies[idx]

                # 如果当前孩子之前是空的（0），那么后续空孩子也都是同样情况，跳过
                if children[i] == 0:
                    break

        backtrack(0)
        return self.answer


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Bit Manipulation, Array, Dynamic Programming, Backtracking, Bitmask
#
# 解题思路:
# 使用回溯法（DFS）枚举所有可能的分配方案。由于 cookies.length <= 8，搜索空间有限，
# 回溯加上有效的剪枝策略可以在合理时间内找到最优解。
#
# 算法流程：
# 1. 将 cookies 按降序排序（大包优先），这样在搜索早期就能确定更紧的上界，有利于剪枝。
# 2. 用一个数组 children 记录每个孩子当前分到的饼干总数。
# 3. 递归地尝试将每包饼干分配给每个孩子：
#    - 如果分配后所有孩子的最大值已经 >= 当前已知最优解，剪枝返回。
#    - 如果两个连续孩子当前分配量相同，跳过（避免对称重复）。
#    - 如果分配后当前孩子仍为 0（说明他是第一次被分配），后续空孩子同理，break 跳过。
# 4. 当所有饼干包分配完毕时，更新最优解。
#
# 时间复杂度: O(k^n)
# - 最坏情况下每个饼干包可以分配给 k 个孩子，但剪枝大幅减少实际搜索量
# - 由于 n <= 8，实际运行时间在可控范围内
#
# 空间复杂度: O(k + n)
# - children 数组 O(k)，递归栈深度 O(n)
#
# 关键点:
# - 降序排序当前包，优先分配大包以尽早建立紧上界
# - 多种剪枝策略：当前最大 >= 最优解、跳过相同分配量的孩子、空孩子去重
# - 回溯时记得还原 children 状态
