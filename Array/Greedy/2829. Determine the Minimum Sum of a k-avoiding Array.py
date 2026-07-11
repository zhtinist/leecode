"""
LeetCode #2829 - Determine the Minimum Sum of a k-avoiding Array
k-avoiding 数组的最小总和
https://leetcode.cn/problems/determine-the-minimum-sum-of-a-k-avoiding-array/

给你两个整数 `n` 和 `k` 。
对于一个由 不同 正整数组成的数组，如果其中不存在任何求和等于 k 的不同元素对，则称其为 k-avoiding 数组。
返回长度为 `n` 的 k-avoiding 数组的可能的最小总和。

示例 1：
输入：n = 5, k = 4 输出：18 解释：设若 k-avoiding 数组为 [1,2,4,5,6] ，其元素总和为 18 。 可以证明不存在总和小于 18 的 k-avoiding 数组。
示例 2：
输入：n = 2, k = 6 输出：3 解释：可以构造数组 [1,2] ，其元素总和为 3 。 可以证明不存在总和小于 3 的 k-avoiding 数组。

提示：
`1 <= n, k <= 50`
"""

from typing import List, Optional


class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        taken = 0
        cur = 1
        ans = 0
        while taken < n:
            ans += cur
            taken += 1
            cur += 1
            if cur >= k - cur + 1 and cur < k:
                cur = k + 1
        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Math
#
# 解题思路:
# 要最小化和，应该选择尽可能小的正整数。从 1 开始逐个选取，但遇到与已选数之和为 k 的数时跳过。
# 对于 k，数对 (x, k-x) 不能同时出现（当 x != k-x 时）。所以小于 k/2 的数都可以选，对应的补数不能选。
# 具体策略：选取 1, 2, ..., min(n, k//2)，如果还需要更多数，从 k 开始往后取。
#
# 时间复杂度: O(n)
# 空间复杂度: O(1)
#
# 关键点:
# - 只能从每对 (x, k-x) 中选一个（x != k/2）
# - 贪心选小的：1, 2, ..., k//2（不含 k/2 如果 k 是偶数）
# - 不够 n 个时从 k 开始往后取（k, k+1, ...）
