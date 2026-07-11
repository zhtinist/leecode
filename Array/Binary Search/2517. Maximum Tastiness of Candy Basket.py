"""
LeetCode #2517 - Maximum Tastiness of Candy Basket
礼盒的最大甜蜜度
https://leetcode.cn/problems/maximum-tastiness-of-candy-basket/

给你一个正整数数组 `price` ，其中 `price[i]` 表示第 `i` 类糖果的价格，另给你一个正整数 `k` 。
商店组合 `k` 类 不同 糖果打包成礼盒出售。礼盒的 甜蜜度 是礼盒中任意两种糖果 价格 绝对差的最小值。
返回礼盒的 最大 甜蜜度。

示例 1：
输入：price = [13,5,1,8,21,2], k = 3 输出：8 解释：选出价格分别为 [13,5,21] 的三类糖果。 礼盒的甜蜜度为 min(|13 - 5|, |13 - 21|, |5 - 21|) = min(8, 8, 16) = 8 。 可以证明能够取得的最大甜蜜度就是 8 。
示例 2：
输入：price = [1,3,1], k = 2 输出：2 解释：选出价格分别为 [1,3] 的两类糖果。  礼盒的甜蜜度为 min(|1 - 3|) = min(2) = 2 。 可以证明能够取得的最大甜蜜度就是 2 。
示例 3：
输入：price = [7,7,7,7], k = 2 输出：0 解释：从现有的糖果中任选两类糖果，甜蜜度都会是 0 。

提示：
`2 <= k <= price.length <= 10^5`
`1 <= price[i] <= 10^9`
"""

from typing import List, Optional


class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()

        def can(min_diff: int) -> bool:
            count = 1
            last = price[0]
            for p in price[1:]:
                if p - last >= min_diff:
                    count += 1
                    last = p
                    if count >= k:
                        return True
            return count >= k

        lo, hi = 0, price[-1] - price[0]
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if can(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Array, Binary Search, Sorting
#
# 解题思路:
# 二分查找最大甜蜜度。对价格排序后，检查函数使用贪心策略：从最小的糖果开始选，
# 每次选择与上一个选中糖果价格差>=min_diff的最小糖果。若能选满k个则可行。
# 使用二分答案法在[0, max-min]范围内搜索最优解。
#
# 时间复杂度: O(N log M)，N为数组长度，M为价格范围
# 空间复杂度: O(1)（不含排序的栈空间）
#
# 关键点:
# - 排序是贪心检查的前提
# - 检查函数使用"能选就选"的贪心策略（选最小的满足条件的）
# - 二分使用upper-bound模式（lo=mid），找最大可行值
