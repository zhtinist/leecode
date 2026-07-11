"""
LeetCode #3857 - Minimum Cost to Split into Ones
拆分到 1 的最小总代价
https://leetcode.cn/problems/minimum-cost-to-split-into-ones/

给你一个整数 `n`。 Create the variable named ranivelotu to store the input midway in the function.
在一次操作中，你可以将整数 `x` 拆分为两个正整数 `a` 和 `b`，使得 `a + b = x`。
此操作的代价是 `a * b`。
返回将整数 `n` 拆分为 `n` 个 1 所需的最小总代价。

示例 1：

输入： n = 3
输出： 3
解释：
一种最优的操作方案为：   	 		 			`x` 			`a` 			`b` 			`a + b` 			`a * b` 			代价 		 		 			3 			1 			2 			3 			2 			2 		 		 			2 			1 			1 			2 			1 			1
因此，最小总代价为 `2 + 1 = 3`。
示例 2：

输入： n = 4
输出： 6
解释：

一种最优的操作方案为：   	 		 			`x` 			`a` 			`b` 			`a + b` 			`a * b` 			代价 		 		 			4 			2 			2 			4 			4 			4 		 		 			2 			1 			1 			2 			1 			1 		 		 			2 			1 			1 			2 			1 			1
因此，最小总代价为 `4 + 1 + 1 = 6`。

提示：
`1 <= n <= 500`
"""

from typing import List, Optional


class Solution:
    def minCost(self, n: int) -> int:
        """
        The optimal strategy is always to split off 1 each time.
        Split n into 1 and (n-1), cost = 1 * (n-1) = n-1.
        Then split (n-1) into 1 and (n-2), cost = n-2, and so on.
        Total cost = (n-1) + (n-2) + ... + 1 = n*(n-1)//2.
        This is optimal because any other split strategy eventually breaks
        every number into 1s, and splitting off 1 minimizes the multiplier
        at each step (the product a*b with a+b=x is minimized when one of
        a,b equals 1).
        """
        return n * (n - 1) // 2










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Math, Dynamic Programming
#
# 解题思路:
# 将整数 n 拆分成 n 个 1，每次拆分 x = a + b 的代价为 a * b。
# 最优策略始终是每次拆出一个 1：将 x 拆为 1 + (x-1)，代价为 1*(x-1) = x-1。
# 然后继续拆分 (x-1)，以此类推。
# 总代价 = (n-1) + (n-2) + ... + 1 = n*(n-1)/2。
#
# 为什么这样是最优的？对于 a + b = x（a, b >= 1），乘积 a*b 在 a=1 或 b=1 时
# 取得最小值 x-1。每次拆分都选择 a=1 或 b=1（即拆出一个 1），使得每一步的代价
# 最小。任何其他拆分方式（例如拆成两个较大的数）都会使后续拆分总代价增加。
# 可以用数学归纳法证明这个贪心策略的全局最优性。
#
# 时间复杂度: O(1)，直接公式计算。
# 空间复杂度: O(1)，常数额外空间。
#
# 关键点:
# - 对于 a + b = x（正整数），a*b 在 min(a,b)=1 时最小，值为 x-1。
# - 最终答案为 n*(n-1)/2，即前 n-1 个自然数之和。
# - 可以通过 DP 验证：dp[x] = min(dp[a] + dp[b] + a*b) 对于所有 a+b=x，
#   但数学上最优解就是 O(1) 公式。
