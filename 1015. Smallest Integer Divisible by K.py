"""
LeetCode #1015 - Smallest Integer Divisible by K
中文题名：可被K整除的最小整数
https://leetcode.com/problems/smallest-integer-divisible-by-k/

Given a positive integer `K`, you need find the smallest positive
integer `N` such that `N` is divisible by `K`, and
`N` only contains the digit 1.

Return the length of `N`.  If there is no such `N`, return
-1.

Example 1:

Input: 1
Output: 1
Explanation: The smallest answer is N = 1, which has length 1.

Example 2:

Input: 2
Output: -1
Explanation: There is no such positive integer N divisible by 2.

Example 3:

Input: 3
Output: 3
Explanation: The smallest answer is N = 111, which has length 3.

Note:

`1 <= K <= 10^5`

【中文翻译】
给定一个正整数 `K`，你需要找到最小的正整数 `N`，使得 `N` 能被 `K` 整除，且 `N` 只包含数字 `1`。

返回 `N` 的长度。如果不存在这样的 `N`，返回 `-1`。

示例 1：

输入：1
输出：1
解释：最小的答案是 N = 1，其长度为 1。

示例 2：

输入：2
输出：-1
解释：不存在可被 2 整除的正整数 N。

示例 3：

输入：3
输出：3
解释：最小的答案是 N = 111，其长度为 3。

注意：

`1 <= K <= 10^5`

"""

from typing import List, Optional


class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        if K % 2 == 0 or K % 5 == 0:
            return -1
        remainder = 0
        for length in range(1, K + 1):
            remainder = (remainder * 10 + 1) % K
            if remainder == 0:
                return length
        return -1










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 需要找到最小的全由 1 组成的数 N 能被 K 整除。首先，如果 K 是 2 或 5 的倍数，
# 则不可能（因为全 1 的数不可能是偶数，也不可能是 5 的倍数）。否则：
# 使用模运算逐位构建：从 remainder = 0 开始，每次 remainder = (remainder * 10 + 1) % K。
# 这等价于逐位构建 1, 11, 111, ... 并同时取模。如果在 K 步内 remainder 变为 0，
# 则找到了答案；否则根据鸽巢原理，余数会重复（0 到 K-1 共 K 个可能值），
# 说明会进入循环，不存在这样的 N，返回 -1。
#
# 时间复杂度: O(K) - 最坏情况需要 K 次迭代
# 空间复杂度: O(1) - 只使用常数额外空间
#
# 关键点:
# - 提前判断 K 为 2 或 5 的倍数时直接返回 -1（优化）
# - 模运算性质：(a * 10 + 1) % K = ((a % K) * 10 + 1) % K，避免大数
# - 最多迭代 K 次：鸽巢原理保证 K 次内必重复或找到答案
