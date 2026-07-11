"""
LeetCode #3091 - Apply Operations to Make Sum of Array Greater Than or Equal to k
执行操作使数据元素之和大于等于 K
https://leetcode.cn/problems/apply-operations-to-make-sum-of-array-greater-than-or-equal-to-k/

给你一个正整数 `k` 。最初，你有一个数组 `nums = [1]` 。
你可以对数组执行以下 任意 操作 任意 次数（可能为零）：
选择数组中的任何一个元素，然后将它的值 增加 `1` 。
复制数组中的任何一个元素，然后将它附加到数组的末尾。
返回使得最终数组元素之 和 大于或等于 `k` 所需的 最少 操作次数。

示例 1：

输入：k = 11
输出：5
解释：
可以对数组 `nums = [1]` 执行以下操作：
将元素的值增加 `1` 三次。结果数组为 `nums = [4]` 。
复制元素两次。结果数组为 `nums = [4,4,4]` 。
最终数组的和为 `4 + 4 + 4 = 12` ，大于等于 `k = 11` 。
执行的总操作次数为 `3 + 2 = 5` 。
示例 2：

输入：k = 1
输出：0
解释：
原始数组的和已经大于等于 `1` ，因此不需要执行操作。

提示：
`1 <= k <= 10^5`
"""

from typing import List, Optional


class Solution:
    def minOperations(self, k: int) -> int:
        if k == 1:
            return 0
        ans = k  # 最多操作k次（每次+1）
        # 枚举增加操作次数 add (将初始的1增加到add+1)
        for add in range(k + 1):
            val = add + 1  # 增加add次后元素的值
            # 复制次数：需要 ceil(k/val) - 1 次复制
            copies = (k + val - 1) // val - 1
            ans = min(ans, add + copies)
        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Math, Enumeration
#
# 解题思路:
# 初始数组只有一个元素1。我们可以进行增加操作（值+1）和复制操作（复制到末尾）。
# 最优策略是先将元素增到某个值x，然后复制多次。枚举增加次数add（0到k），
# 增加add次后元素值为add+1，复制次数的计算公式为 ceil(k/(add+1)) - 1。
# 取所有枚举中的最小值即可。
#
# 时间复杂度: O(k)
# 空间复杂度: O(1)
#
# 关键点:
# - 先增加后复制的策略最优
# - 枚举增加次数，用公式计算对应的复制次数
# - 总操作数 = 增加次数 + 复制次数
