"""
LeetCode #1492 - The kth Factor of n
中文题名：n 的第 k 个因子
https://leetcode.com/problems/the-kth-factor-of-n/

Given two positive integers `n` and `k`.

A factor of an integer `n` is defined as an integer `i` where
`n % i == 0`.

Consider a list of all factors of `n` sorted in ascending
order, return the `kth` factor in this list or
return -1 if `n` has less than `k`
factors.

Example 1:

Input: n = 12, k = 3
Output: 3
Explanation: Factors list is [1, 2, 3, 4, 6, 12], the 3rd factor is 3.

Example 2:

Input: n = 7, k = 2
Output: 7
Explanation: Factors list is [1, 7], the 2nd factor is 7.

Example 3:

Input: n = 4, k = 4
Output: -1
Explanation: Factors list is [1, 2, 4], there is only 3 factors. We should return -1.

Example 4:

Input: n = 1, k = 1
Output: 1
Explanation: Factors list is [1], the 1st factor is 1.

Example 5:

Input: n = 1000, k = 3
Output: 4
Explanation: Factors list is [1, 2, 4, 5, 8, 10, 20, 25, 40, 50, 100, 125, 200, 250, 500, 1000].

Constraints:

`1 <= k <= n <= 1000`

【中文翻译】

给定两个正整数 `n` 和 `k`。

整数 `n` 的因子定义为满足 `n % i == 0` 的整数 `i`。

考虑按升序排列的 `n` 的所有因子列表，返回该列表中的第 `k` 个因子，如果 `n` 的因子少于 `k` 个则返回 -1。

示例 1：
输入：n = 12, k = 3
输出：3
解释：因子列表为 [1, 2, 3, 4, 6, 12]，第 3 个因子是 3。

示例 2：
输入：n = 7, k = 2
输出：7
解释：因子列表为 [1, 7]，第 2 个因子是 7。

示例 3：
输入：n = 4, k = 4
输出：-1
解释：因子列表为 [1, 2, 4]，只有 3 个因子，应返回 -1。

示例 4：
输入：n = 1, k = 1
输出：1
解释：因子列表为 [1]，第 1 个因子是 1。

示例 5：
输入：n = 1000, k = 3
输出：4
解释：因子列表为 [1, 2, 4, 5, 8, 10, 20, 25, 40, 50, 100, 125, 200, 250, 500, 1000]。

约束条件：
1 <= k <= n <= 1000

"""

from typing import List, Optional


class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        small = []
        large = []
        import math
        for i in range(1, int(math.sqrt(n)) + 1):
            if n % i == 0:
                small.append(i)
                if i != n // i:
                    large.append(n // i)

        factors = small + large[::-1]
        if k <= len(factors):
            return factors[k - 1]
        return -1



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 1. 遍历 1 到 sqrt(n)，找到所有因子。
# 2. 对于每个因子 i（n % i == 0）：
#    - 将 i 加入"小因子"列表 small
#    - 如果 i != n//i，将 n//i 加入"大因子"列表 large
#      （大因子按升序添加，但我们需要降序后再反转）
# 3. 合并 small 和反转后的 large 得到完整的升序因子列表。
# 4. 如果 k <= len(factors)，返回 factors[k-1]，否则返回 -1。
# 5. 例如 n=12：遍历 1,2,3（sqrt(12)≈3）：
#    i=1: small=[1], large=[12]
#    i=2: small=[1,2], large=[12,6]
#    i=3: small=[1,2,3], large=[12,6,4]
#    合并: [1,2,3,4,6,12]
#
# 时间复杂度: O(sqrt(N))
# 空间复杂度: O(sqrt(N))（因子数量约为 2*sqrt(N)）
#
# 关键点:
# - 只遍历到 sqrt(n) 即可找到所有因子
# - small 列表自然升序，large 列表需要反转
# - 注意完全平方数（如 n=16, i=4, n//i=4）不要重复添加
# - 检查 k 是否超出因子总数










