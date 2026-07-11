"""
LeetCode #2611 - Mice and Cheese
老鼠和奶酪
https://leetcode.cn/problems/mice-and-cheese/

有两只老鼠和 `n` 块不同类型的奶酪，每块奶酪都只能被其中一只老鼠吃掉。
下标为 `i` 处的奶酪被吃掉的得分为：
如果第一只老鼠吃掉，则得分为 `reward1[i]` 。
如果第二只老鼠吃掉，则得分为 `reward2[i]` 。
给你一个正整数数组 `reward1` ，一个正整数数组 `reward2` ，和一个非负整数 `k` 。
请你返回第一只老鼠恰好吃掉 `k` 块奶酪的情况下，最大 得分为多少。

示例 1：
输入：reward1 = [1,1,3,4], reward2 = [4,4,1,1], k = 2 输出：15 解释：这个例子中，第一只老鼠吃掉第 2 和 3 块奶酪（下标从 0 开始），第二只老鼠吃掉第 0 和 1 块奶酪。 总得分为 4 + 4 + 3 + 4 = 15 。 15 是最高得分。
示例 2：
输入：reward1 = [1,1], reward2 = [1,1], k = 2 输出：2 解释：这个例子中，第一只老鼠吃掉第 0 和 1 块奶酪（下标从 0 开始），第二只老鼠不吃任何奶酪。 总得分为 1 + 1 = 2 。 2 是最高得分。

提示：
`1 <= n == reward1.length == reward2.length <= 10^5`
`1 <= reward1[i], reward2[i] <= 1000`
`0 <= k <= n`
"""

from typing import List, Optional


class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        total = sum(reward2)
        diff = [reward1[i] - reward2[i] for i in range(len(reward1))]
        diff.sort(reverse=True)
        total += sum(diff[:k])
        return total



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Array, Sorting, Heap (Priority Queue)
#
# 解题思路:
# 先假设第二只老鼠吃掉所有奶酪，总分=sum(reward2)。然后选择k块改为第一只老鼠吃。
# 每块切换的收益为reward1[i]-reward2[i]，选收益最大的k块切换即可获得最大总得分。
#
# 时间复杂度: O(n log n)
# 空间复杂度: O(n)
#
# 关键点:
# - 贪心策略：计算每块奶酪的切换收益(reward1[i]-reward2[i])，选最大的k个
# - 基础总分是reward2全和，加上k个最大差值
