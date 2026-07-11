"""
LeetCode #2048 - Next Greater Numerically Balanced Number
下一个更大的数值平衡数
https://leetcode.cn/problems/next-greater-numerically-balanced-number/

如果整数  `x` 满足：对于每个数位 `d` ，这个数位 恰好 在 `x` 中出现 `d` 次。那么整数 `x` 就是一个 数值平衡数 。
给你一个整数 `n` ，请你返回 严格大于 `n` 的 最小数值平衡数 。

示例 1：
输入：n = 1 输出：22 解释： 22 是一个数值平衡数，因为： - 数字 2 出现 2 次  这也是严格大于 1 的最小数值平衡数。
示例 2：
输入：n = 1000 输出：1333 解释： 1333 是一个数值平衡数，因为： - 数字 1 出现 1 次。 - 数字 3 出现 3 次。  这也是严格大于 1000 的最小数值平衡数。 注意，1022 不能作为本输入的答案，因为数字 0 的出现次数超过了 0 。
示例 3：
输入：n = 3000 输出：3133 解释： 3133 是一个数值平衡数，因为： - 数字 1 出现 1 次。 - 数字 3 出现 3 次。  这也是严格大于 3000 的最小数值平衡数。

提示：
`0 <= n <= 10^6`
"""

from typing import List, Optional


class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        def is_balanced(x: int) -> bool:
            s = str(x)
            count = [0] * 10
            for ch in s:
                count[int(ch)] += 1
            for d in range(10):
                if count[d] > 0 and count[d] != d:
                    return False
            return True

        x = n + 1
        while True:
            if is_balanced(x):
                return x
            x += 1



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Hash Table, Math, Backtracking, Counting, Enumeration
#
# 解题思路:
# 从n+1开始逐个检查每个整数是否是数值平衡数。数值平衡数的定义是：
# 每个数字d在数中恰好出现d次。由于n <= 10^6，下一个平衡数不会太远，
# 线性搜索即可。检查函数统计0-9每个数字的出现次数，验证是否满足条件。
#
# 时间复杂度: O(K) 其中K是搜索范围内数字个数
# 空间复杂度: O(1)
#
# 关键点:
# - 逐个递增检查直到找到平衡数
# - 数字计数判断平衡性
# - n上限10^6，搜索空间有限
