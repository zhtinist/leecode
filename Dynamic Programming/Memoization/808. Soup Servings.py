"""
LeetCode #808 - Soup Servings
中文题名：分汤
https://leetcode.com/problems/soup-servings/

There are two types of soup: type A and type B. Initially we have `N` ml of each
type of soup. There are four kinds of operations:

Serve 100 ml of soup A and 0 ml of soup B

Serve 75 ml of soup A and 25 ml of soup B

Serve 50 ml of soup A and 50 ml of soup B

Serve 25 ml of soup A and 75 ml of soup B

When we serve some soup, we give it to someone and we no longer have it.  Each turn, we
will choose from the four operations with equal probability 0.25. If the remaining volume of
soup is not enough to complete the operation, we will serve as much as we can.  We
stop once we no longer have some quantity of both types of soup.

Note that we do not have the operation where all 100 ml's of soup B are used first.

Return the probability that soup A will be empty first, plus half the probability that A
and B become empty at the same time.

Example:
Input: N = 50
Output: 0.625
Explanation:
If we choose the first two operations, A will become empty first. For the third operation, A and B will become empty at the same time. For the fourth operation, B will become empty first. So the total probability of A becoming empty first plus half the probability that A and B become empty at the same time, is 0.25 * (1 + 1 + 0.5 + 0) = 0.625.

Notes:

`0 <= N <= 10^9`.

Answers within `10^-6` of the true value will be accepted as
correct.

【中文翻译】
有两种汤：A 类型和 B 类型。初始时，每种汤各有 `N` 毫升。有四种操作：

- 上 100 毫升 A 汤和 0 毫升 B 汤
- 上 75 毫升 A 汤和 25 毫升 B 汤
- 上 50 毫升 A 汤和 50 毫升 B 汤
- 上 25 毫升 A 汤和 75 毫升 B 汤

上汤时，我们将其给某人，不再拥有它。每轮我们将以 0.25 的等概率从四种操作中选择一种。如果剩余汤量不足以完成操作，我们将尽可能多地端出。一旦某种汤没有了，就停止。

注意，没有"先把 100 毫升 B 汤全部用完"的操作。

返回 A 汤先被倒空的概率，加上 A 和 B 同时被倒空的概率的一半。

示例：
输入：N = 50
输出：0.625
解释：如果选择前两种操作，A 将先被倒空。对于第三种操作，A 和 B 将同时被倒空。对于第四种操作，B 将先被倒空。
所以 A 先倒空的概率加上 A 和 B 同时倒空概率的一半 = 0.25 * (1 + 1 + 0.5 + 0) = 0.625。

注意：
`0 <= N <= 10^9`。
答案与真值误差在 `10^-6` 以内将被接受。
"""

from typing import List, Optional


class Solution:
    def soupServings(self, n: int) -> float:
        # For large N, probability approaches 1
        if n >= 5000:
            return 1.0

        # Scale by 25 (all operations are multiples of 25)
        import math
        m = math.ceil(n / 25)

        from functools import lru_cache

        @lru_cache(None)
        def dp(a: int, b: int) -> float:
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1.0
            if b <= 0:
                return 0.0

            # Four operations: (4,0), (3,1), (2,2), (1,3)
            return 0.25 * (
                dp(a - 4, b) +
                dp(a - 3, b - 1) +
                dp(a - 2, b - 2) +
                dp(a - 1, b - 3)
            )

        return dp(m, m)



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用带记忆化的动态规划（自顶向下）。
# 首先将 N 按 25 缩放（因为所有操作都是 25 的倍数），
# 向上取整得到 m = ceil(N/25)。
# 对于 N >= 5000（即 m >= 200），
# 由于每次操作平均消耗 A 多于 B，当总量极大时 A 几乎必定先空，
# 概率趋近于 1.0，直接返回 1.0 避免计算溢出。
#
# DP 状态定义：dp(a, b) = 从 a 单位 A 和 b 单位 B 开始时，
# A 先空的概率 + 0.5 * 同时空的概率。
#
# 四种等概率操作（缩放后）：(4,0), (3,1), (2,2), (1,3)
#
# 边界条件：
# - a <= 0 且 b <= 0：同时空，返回 0.5
# - a <= 0 且 b > 0：A 先空，返回 1.0
# - a > 0 且 b <= 0：B 先空，返回 0.0
#
# 时间复杂度: O(m^2) - 其中 m = ceil(N/25)，最多 200x200 = 40000 状态
# 空间复杂度: O(m^2) - memoization 缓存
#
# 关键点:
# - 缩放除以 25 大幅减小状态空间
# - N >= 5000 时直接返回 1.0，防止超时
# - 四个操作等概率 0.25
# - functools.lru_cache 实现记忆化
