"""
LeetCode #932 - Beautiful Array
中文题名：漂亮数组
https://leetcode.com/problems/beautiful-array/

For some fixed `N`, an array `A` is beautiful if it is a
permutation of the integers `1, 2, ..., N`, such that:

For every `i < j`, there is no `k` with `i
< k < j` such that `A[k] * 2 = A[i] + A[j]`.

Given `N`, return any beautiful array `A`.  (It
is guaranteed that one exists.)

Example 1:

Input: 4
Output: [2,1,4,3]

Example 2:

Input: 5
Output: [3,1,2,5,4]

【中文翻译】

对于某个固定的 N，如果数组 A 是整数 1, 2, ..., N 的一个排列，且对于任意
i < j，不存在满足 i < k < j 的 k 使得 A[k] * 2 = A[i] + A[j]，则称 A 是
漂亮数组。给定 N，返回任意一个漂亮数组 A。（保证存在一个。）

"""

from typing import List, Optional


class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        """
        Divide and conquer:
        - If A is a beautiful array, then:
          - odd_part = [2*x - 1 for x in A] is also beautiful
          - even_part = [2*x for x in A] is also beautiful
          - Concatenation odd_part + even_part is beautiful
        because no odd + even = 2 * something (odd+even=odd, 2*anything=even).
        """
        memo = {}

        def build(m: int) -> List[int]:
            if m in memo:
                return memo[m]
            if m == 1:
                return [1]
            odd_part = build((m + 1) // 2)   # ceil(m/2)
            even_part = build(m // 2)          # floor(m/2)
            result = [2 * x - 1 for x in odd_part] + [2 * x for x in even_part]
            memo[m] = result
            return result

        return build(n)



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 分治法（Divide and Conquer）：
# 关键性质：如果 A 是漂亮数组，那么：
# - odd_part  = [2*x - 1 for x in A]（所有奇数映射）也是漂亮数组
# - even_part = [2*x for x in A]（所有偶数映射）也是漂亮数组
# - odd_part + even_part 拼接后也是漂亮数组
# 原因：奇数 + 偶数 = 奇数，而 2 * 任何数 = 偶数，所以永远不满足 A[k]*2 = A[i]+A[j]。
#
# 递归构建：
# - beautiful(1) = [1]
# - beautiful(N) = [奇数部分(来自 ceil(N/2))] + [偶数部分(来自 floor(N/2))]
# 使用记忆化避免重复计算。
#
# 时间复杂度: O(N log N)
# 空间复杂度: O(N log N)（递归调用栈和记忆化存储）
#
# 关键点:
# - 核心洞察：奇偶分离保证了跨部分不会产生违规的三元组
# - 递归时，ceil(N/2) 个奇数 + floor(N/2) 个偶数刚好覆盖 1..N
# - 使用记忆化缓存中间结果以优化性能
