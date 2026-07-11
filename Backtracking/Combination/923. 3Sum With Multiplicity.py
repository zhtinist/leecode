"""
LeetCode #923 - 3Sum With Multiplicity
中文题名：三数之和的多种可能
https://leetcode.com/problems/3sum-with-multiplicity/

Given an integer array `A`, and an integer `target`, return the number
of tuples `i, j, k`  such that `i < j < k` and `A[i]
+ A[j] + A[k] == target`.

As the answer can be very large, return it modulo `10^9 + 7`.

Example 1:

Input: A = [1,1,2,2,3,3,4,4,5,5], target = 8
Output: 20
Explanation:
Enumerating by the values (A[i], A[j], A[k]):
(1, 2, 5) occurs 8 times;
(1, 3, 4) occurs 8 times;
(2, 2, 4) occurs 2 times;
(2, 3, 3) occurs 2 times.

Example 2:

Input: A = [1,1,2,2,2,2], target = 5
Output: 12
Explanation:
A[i] = 1, A[j] = A[k] = 2 occurs 12 times:
We choose one 1 from [1,1] in 2 ways,
and two 2s from [2,2,2,2] in 6 ways.

【中文翻译】

给定一个整数数组 A 和一个整数 target，返回满足 i < j < k 且
A[i] + A[j] + A[k] == target 的元组 (i, j, k) 的数量。
由于答案可能非常大，请将其对 10^9 + 7 取模后返回。

"""

from typing import List, Optional


class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        """
        Use a frequency counter. Iterate i through unique values,
        then j from i up to avoid duplicates. For the pair (i, j),
        k = target - i - j. Count combinations based on whether
        i == j == k, i == j != k, or all distinct.
        """
        from collections import Counter
        MOD = 10 ** 9 + 7
        count = Counter(arr)
        keys = sorted(count.keys())
        result = 0

        for i_idx, i in enumerate(keys):
            for j_idx in range(i_idx, len(keys)):
                j = keys[j_idx]
                k = target - i - j
                if k < j or k not in count:
                    continue
                ci, cj, ck = count[i], count[j], count[k]

                if i == j == k:
                    # Choose 3 from ci: C(ci, 3)
                    result = (result + ci * (ci - 1) * (ci - 2) // 6) % MOD
                elif i == j:
                    # Choose 2 from ci, 1 from ck: C(ci, 2) * ck
                    result = (result + ci * (ci - 1) // 2 * ck) % MOD
                elif j == k:
                    # Choose 2 from cj, 1 from ci: ci * C(cj, 2)
                    result = (result + ci * cj * (cj - 1) // 2) % MOD
                else:
                    # All distinct: ci * cj * ck
                    result = (result + ci * cj * ck) % MOD

        return result



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用计数法代替直接的三重循环：
# 1. 用 Counter 统计每个值的出现频率。
# 2. 对去重排序后的键值进行双重循环，枚举 i 和 j (i <= j)。
# 3. 计算 k = target - i - j，若 k < j 或 k 不在计数中则跳过。
# 4. 根据 i, j, k 是否相等分情况计算组合数：
#    - i == j == k: C(count[i], 3)
#    - i == j != k: C(count[i], 2) * count[k]
#    - j == k: count[i] * C(count[j], 2)
#    - 全不同: count[i] * count[j] * count[k]
# 5. 所有结果累加并对 10^9+7 取模。
#
# 时间复杂度: O(N + V^2)，其中 V 是不同值的数量（最多 101）
# 空间复杂度: O(V)
#
# 关键点:
# - 数组值范围有限（0~100），V ≤ 101，所以 O(V^2) 很快
# - 需要区分三个值相等、两个相等、全不相等的情况来计算组合数
# - 保证 i <= j <= k 避免重复计数
