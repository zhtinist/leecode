"""
LeetCode #1806 - Minimum Number of Operations to Reinitialize a Permutation
中文题名：还原排列的最少操作步数
https://leetcode.com/problems/minimum-number-of-operations-to-reinitialize-a-permutation/

You are given an even integer `n`​​​​​​. You initially have a permutation `perm` of size `n`​​ where `perm[i] == i`​ (0-indexed)​​​​.

In one operation, you will create a new array `arr`, and for each `i`:

If `i % 2 == 0`, then `arr[i] = perm[i / 2]`.

If `i % 2 == 1`, then `arr[i] = perm[n / 2 + (i - 1) / 2]`.

You will then assign `arr`​​​​ to `perm`.

Return the minimum non-zero number of operations you need to perform on `perm` to return the permutation to its initial value.

Example 1:

Input: n = 2
Output: 1
Explanation: perm = [0,1] initially.
After the 1st operation, perm = [0,1]
So it takes only 1 operation.

Example 2:

Input: n = 4
Output: 2
Explanation: perm = [0,1,2,3] initially.
After the 1st operation, perm = [0,2,1,3]
After the 2nd operation, perm = [0,1,2,3]
So it takes only 2 operations.

Example 3:

Input: n = 6
Output: 4

Constraints:

`2 <= n <= 1000`

`n`​​​​​​ is even.

【中文翻译】
给定一个偶数 n。初始排列 perm[i] = i (0 <= i < n)。
每次操作将 perm 变为新数组 arr：
- 若 i % 2 == 0：arr[i] = perm[i/2]
- 若 i % 2 == 1：arr[i] = perm[n/2 + (i-1)/2]
求最少操作次数，使 perm 恢复初始状态。

示例 1：
输入: n = 2
输出: 1
解释: perm = [0,1]。一次操作：arr[0]=perm[0]=0, arr[1]=perm[1]=1。已恢复。
"""

from typing import List, Optional


class Solution:
    def reinitializePermutation(self, n: int) -> int:
        # 只需追踪数字 1 的位置
        pos = 1
        ops = 0

        while True:
            ops += 1
            if pos < n // 2:
                pos = pos * 2
            else:
                pos = (pos - n // 2) * 2 + 1

            if pos == 1:
                break

        return ops
# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 只需追踪元素 1 的位置（因为排列的结构是线性的，1 回到原位等价于整个排列恢复）。
# 每次操作的公式：
# - 若 pos < n/2：新位置 = 2 * pos
# - 若 pos >= n/2：新位置 = 2 * (pos - n/2) + 1
# 不断应用操作直到 pos 回到 1，计数操作次数。
#
# 时间复杂度: O(N) — 最坏需要 n 次
# 空间复杂度: O(1)
#
# 关键点:
# - 只需追踪元素 1 即可，因为排列恢复等价于所有元素回到原位
# - 操作公式简化后就是上述两条规则
# - 也可用模拟整个数组的方法（O(N^2)）
