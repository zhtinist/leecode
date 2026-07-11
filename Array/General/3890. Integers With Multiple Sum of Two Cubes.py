"""
LeetCode #3890 - Integers With Multiple Sum of Two Cubes
可由多种立方和构造的整数
https://leetcode.cn/problems/integers-with-multiple-sum-of-two-cubes/

给你一个整数 `n`。
当存在 至少 两组不同的整数对 `(a, b)` 满足以下条件时，整数 `x` 被称为 好整数：
`a` 和 `b` 是正整数。
`a <= b`
`x = a^3 + b^3`
返回一个数组，其中包含所有小于等于 `n` 的好整数，并按升序排序。

示例 1：

输入： n = 4104
输出： [1729,4104]
解释：
在小于等于 4104 的整数中，好整数包括：
1729：`1^3 + 12^3 = 1729`，以及 `9^3 + 10^3 = 1729`。
4104：`2^3 + 16^3 = 4104`，以及 `9^3 + 15^3 = 4104`。
因此，答案是 `[1729, 4104]`。
示例 2：

输入： n = 578
输出： []
解释：
不存在小于等于 578 的好整数，因此答案是空数组。

提示：
`1 <= n <= 10^9`
"""

from typing import List, Optional


class Solution:
    def integersWithMultipleSumOfTwoCubes(self, n: int) -> List[int]:
        from collections import Counter

        # 计算最大可能的 b 值：b^3 <= n
        limit = 1
        while limit * limit * limit <= n:
            limit += 1
        # limit 是第一个立方大于 n 的数，有效范围是 1 到 limit-1

        cnt = Counter()
        for a in range(1, limit):
            a3 = a * a * a
            for b in range(a, limit):
                s = a3 + b * b * b
                if s > n:
                    break
                cnt[s] += 1

        result = [s for s, c in cnt.items() if c >= 2]
        result.sort()
        return result










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Hash Table, Counting, Enumeration, Sorting
#
# 解题思路:
# 1. 确定枚举上界：若 a^3 + b^3 <= n 且 a <= b，则 b^3 <= n，故 b <= cbrt(n)。
#    通过 while 循环精确计算 limit = floor(cbrt(n)) + 1。
# 2. 双重循环枚举所有正整数对 (a, b)，满足 a <= b 且 a^3 + b^3 <= n。
#    内层循环从 b = a 开始（保证 a <= b），一旦 s > n 立即 break 剪枝。
# 3. 使用 Counter 统计每个立方和 s 出现的次数，即有多少种不同的 (a, b) 表示方式。
# 4. 筛选出现次数 >= 2 的和——这些是可以用至少两种方式表示为两个立方和的整数。
# 5. 将结果排序后返回（Counter 本身无序）。
#
# 时间复杂度: O(n^{2/3}) — 双重循环枚举约 (n^{1/3})^2 / 2 对，n=10^9 时约 5×10^5 对
# 空间复杂度: O(n^{2/3}) — Counter 最多存储所有可能的立方和
#
# 关键点:
# - 这类数被称为“的士数”（taxicab numbers），Ta(2) = 1729 是最小的能表示为两组立方和的数
# - 内层循环 j 从 i 开始，保证了 a <= b 的条件
# - 当 s > n 时 break 剪枝，避免无效枚举
# - 使用整数乘法 a*a*a 而非 a**3 或 pow(a,3)，避免浮点精度问题
