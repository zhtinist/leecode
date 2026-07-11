"""
LeetCode #2761 - Prime Pairs With Target Sum
和等于目标值的质数对
https://leetcode.cn/problems/prime-pairs-with-target-sum/

给你一个整数 `n` 。如果两个整数 `x` 和 `y` 满足下述条件，则认为二者形成一个质数对：
`1 <= x <= y <= n`
`x + y == n`
`x` 和 `y` 都是质数
请你以二维有序列表的形式返回符合题目要求的所有 `[x_i, y_i]` ，列表需要按 `x_i` 的 非递减顺序 排序。如果不存在符合要求的质数对，则返回一个空数组。
注意：质数是大于 `1` 的自然数，并且只有两个因子，即它本身和 `1` 。

示例 1：
输入：n = 10 输出：[[3,7],[5,5]] 解释：在这个例子中，存在满足条件的两个质数对。  这两个质数对分别是 [3,7] 和 [5,5]，按照题面描述中的方式排序后返回。
示例 2：
输入：n = 2 输出：[] 解释：可以证明不存在和为 2 的质数对，所以返回一个空数组。

提示：
`1 <= n <= 10^6`
"""

from typing import List, Optional


class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False

        ans = []
        for x in range(1, n // 2 + 1):
            y = n - x
            if is_prime[x] and is_prime[y]:
                ans.append([x, y])
        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Math, Enumeration, Number Theory
#
# 解题思路:
# 先用埃拉托色尼筛法预处理出 1 到 n 的所有质数。
# 然后遍历 x 从 1 到 n//2，检查 x 和 n-x 是否都是质数。
# 因为要求 x <= y 且按 x 非递减排序，直接从小到大遍历自然满足。
#
# 时间复杂度: O(n log log n)
# 空间复杂度: O(n)
#
# 关键点:
# - 埃拉托色尼筛法 O(n log log n) 高效找出所有质数
# - 只需遍历 x 到 n/2，因为要求 x <= y
# - 注意 1 不是质数
