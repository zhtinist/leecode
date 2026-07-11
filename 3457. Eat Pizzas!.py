"""
LeetCode #3457 - Eat Pizzas!
吃披萨
https://leetcode.cn/problems/eat-pizzas/

给你一个长度为 `n` 的整数数组 `pizzas`，其中 `pizzas[i]` 表示第 `i` 个披萨的重量。每天你会吃 恰好 4 个披萨。由于你的新陈代谢能力惊人，当你吃重量为 `W`、`X`、`Y` 和 `Z` 的披萨（其中 `W <= X <= Y <= Z`）时，你只会增加 1 个披萨的重量！体重增加规则如下：
在 奇数天（按 1 开始计数）你会增加 `Z` 的重量。
在 偶数天，你会增加 `Y` 的重量。
请你设计吃掉 所有 披萨的最优方案，并计算你可以增加的 最大 总重量。
注意：保证 `n` 是 4 的倍数，并且每个披萨只吃一次。

示例 1：

输入： pizzas = [1,2,3,4,5,6,7,8]
输出： 14
解释：
第 1 天，你吃掉下标为 `[1, 2, 4, 7] = [2, 3, 5, 8]` 的披萨。你增加的重量为 8。
第 2 天，你吃掉下标为 `[0, 3, 5, 6] = [1, 4, 6, 7]` 的披萨。你增加的重量为 6。
吃掉所有披萨后，你增加的总重量为 `8 + 6 = 14`。
示例 2：

输入： pizzas = [2,1,1,1,1,1,1,1]
输出： 3
解释：
第 1 天，你吃掉下标为 `[4, 5, 6, 0] = [1, 1, 1, 2]` 的披萨。你增加的重量为 2。
第 2 天，你吃掉下标为 `[1, 2, 3, 7] = [1, 1, 1, 1]` 的披萨。你增加的重量为 1。
吃掉所有披萨后，你增加的总重量为 `2 + 1 = 3`。

提示：
`4 <= n == pizzas.length <= 2 * 10^5`
`1 <= pizzas[i] <= 10^5`
`n` 是 4 的倍数。
"""

from typing import List, Optional


class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:
        pizzas.sort(reverse=True)
        days = len(pizzas) // 4
        odd_days = (days + 1) // 2
        even_days = days // 2

        ans = 0
        # Odd days: pick the largest pizzas directly
        for i in range(odd_days):
            ans += pizzas[i]

        # Even days: skip one (the wasted Z), pick the next as Y
        idx = odd_days
        for _ in range(even_days):
            idx += 1  # skip Z (non-contributing)
            ans += pizzas[idx]
            idx += 1

        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Array, Sorting
#
# 解题思路:
# 1. 总天数 D = n/4，奇数天 O = ceil(D/2)，偶数天 E = floor(D/2)
# 2. 降序排列披萨重量
# 3. 奇数天：取最大披萨即为 Z（收益），其他 3 个披萨可以任意选最小的
#    → 取最大的 O 个披萨作为奇数天收益
# 4. 偶数天：需要 2 个较大披萨（Z 不贡献收益，Y 贡献收益）
#    → 从剩余披萨中，每 2 个一组（Z, Y），取每组第二个（Y）作为收益
#    → 即跳过第 O+1, O+3, ...（Z 们），取 O+2, O+4, ...（Y 们）
# 5. 收益总和 = sum(奇数天 Z) + sum(偶数天 Y)
#
# 时间复杂度: O(n log n)
# 空间复杂度: O(1) (不计排序空间)
#
# 关键点:
# - 奇数天的 Z 无相对大小约束，直接用最大披萨
# - 偶数天 Z > Y，Z 不贡献，所以用次大的做 Z，"牺牲"尽可能小的值
# - 降序排列后贪心取对应位置
