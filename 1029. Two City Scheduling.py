"""
LeetCode #1029 - Two City Scheduling
中文题名：两地调度
https://leetcode.com/problems/two-city-scheduling/

There are `2N` people a company is planning to interview. The cost of flying the
`i`-th person to city `A` is `costs[i][0]`, and the cost of
flying the `i`-th person to city `B` is `costs[i][1]`.

Return the minimum cost to fly every person to a city such that exactly `N` people
arrive in each city.

Example 1:

Input: [[10,20],[30,200],[400,50],[30,20]]
Output: 110
Explanation:
The first person goes to city A for a cost of 10.
The second person goes to city A for a cost of 30.
The third person goes to city B for a cost of 50.
The fourth person goes to city B for a cost of 20.

The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.

Note:

`1 <= costs.length <= 100`

It is guaranteed that `costs.length` is even.

`1 <= costs[i][0], costs[i][1] <= 1000`

【中文翻译】
一家公司计划面试 2N 个人。第 i 个人飞往城市 A 的费用为 costs[i][0]，飞往城市 B 的费用为 costs[i][1]。

返回让每个人都飞到某个城市的最低总费用，要求每个城市恰好有 N 个人到达。

示例 1：

输入：[[10,20],[30,200],[400,50],[30,20]]
输出：110
解释：
第一个人去城市 A，费用为 10。
第二个人去城市 A，费用为 30。
第三个人去城市 B，费用为 50。
第四个人去城市 B，费用为 20。

总最低费用为 10 + 30 + 50 + 20 = 110，每个城市恰好有一半的人参加面试。

注意：

1 <= costs.length <= 100
保证 costs.length 是偶数。
1 <= costs[i][0], costs[i][1] <= 1000
"""

from typing import List, Optional


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # Sort by the cost difference (savings) of sending to A instead of B
        # Negative diff means A is cheaper, positive means B is cheaper
        costs.sort(key=lambda x: x[0] - x[1])
        n = len(costs) // 2
        total = 0
        # First N go to city A, rest go to city B
        for i in range(n):
            total += costs[i][0] + costs[i + n][1]
        return total










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用贪心算法。关键在于如何将人员分配给两个城市。计算每个人去A市相比去B市的费用差：
# diff = costs[i][0] - costs[i][1]。diff越小（越负），说明去A市越划算。
# 按 diff 排序后，前 N 个人去A市（diff最小，即去A最划算的），后 N 个人去B市。
# 这样确保总费用最小。
#
# 时间复杂度: O(N log N) - 排序开销
# 空间复杂度: O(1) - 不计输入，只使用常量额外空间
#
# 关键点:
# - 贪心策略：按 costA - costB 排序，差值越小的越应该去A市
# - 前N个分配给A，后N个分配给B
# - 总费用 = sum(前N个的costA) + sum(后N个的costB)
