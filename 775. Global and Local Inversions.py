"""
LeetCode #775 - Global and Local Inversions
中文题名：全局倒置与局部倒置
https://leetcode.com/problems/global-and-local-inversions/

We have some permutation `A` of `[0, 1, ..., N - 1]`, where
`N` is the length of `A`.

The number of (global) inversions is the number of `i < j` with `0 <= i
< j < N` and `A[i] > A[j]`.

The number of local inversions is the number of `i` with `0 <= i <
N` and `A[i] > A[i+1]`.

Return `true` if and only if the number of global inversions is equal to the
number of local inversions.

Example 1:

Input: A = [1,0,2]
Output: true
Explanation: There is 1 global inversion, and 1 local inversion.

Example 2:

Input: A = [1,2,0]
Output: false
Explanation: There are 2 global inversions, and 1 local inversion.

Note:

`A` will be a permutation of `[0, 1, ..., A.length - 1]`.

`A` will have length in range `[1, 5000]`.

The time limit for this problem has been reduced.

【中文翻译】
我们有一个 `[0, 1, ..., N - 1]` 的排列 `A`，其中 `N` 是 `A` 的长度。

（全局）倒置的数量是满足 `0 <= i < j < N` 且 `A[i] > A[j]` 的 `i < j` 对的数量。

局部倒置的数量是满足 `0 <= i < N` 且 `A[i] > A[i+1]` 的 `i` 的数量。

当且仅当全局倒置的数量等于局部倒置的数量时，返回 `true`。

示例 1：

输入：A = [1,0,2]
输出：true
解释：有 1 个全局倒置和 1 个局部倒置。

示例 2：

输入：A = [1,2,0]
输出：false
解释：有 2 个全局倒置和 1 个局部倒置。

注意：

`A` 将是 `[0, 1, ..., A.length - 1]` 的一个排列。

`A` 的长度范围在 `[1, 5000]`。

该问题的时间限制已被缩短。
"""

from typing import List, Optional


class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        # Every local inversion is a global inversion.
        # We need to ensure there is NO non-local global inversion.
        # That means no A[i] > A[j] where j > i + 1.
        # For a permutation of [0..N-1], A[i] can be at most 1 away from i.
        for i, val in enumerate(A):
            if abs(val - i) > 1:
                return False
        return True



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 数学洞察。
# 每个局部倒置都是全局倒置。若全局倒置数等于局部倒置数，则不存在"非局部的全局倒置"。
# 也就是说，不存在 i 和 j 满足 j > i+1 且 A[i] > A[j]。
# 对于 [0, 1, ..., N-1] 的排列，这意味着每个元素距离其正确位置不超过 1。
# 换句说，任何元素的偏移量 |A[i] - i| 必须 <= 1。
# 反证：若某个元素偏移 >= 2，则必定产生一个非局部全局倒置。
# 只需一次遍历检查所有元素即可。
#
# 时间复杂度: O(N) - 一次遍历
# 空间复杂度: O(1) - 只使用常数额外空间
#
# 关键点:
# - 核心洞察：全局倒置 = 局部倒置 => 不存在跨元素的倒置
# - 排列性质：每个元素距离其正确下标最多为 1
# - abs(A[i] - i) > 1 即可判断 false
# - 也可以维护后缀最小值，但利用排列性质更简洁
