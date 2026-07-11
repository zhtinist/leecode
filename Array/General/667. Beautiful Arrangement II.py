"""
LeetCode #667 - Beautiful Arrangement II
中文题名：优美的排列 II
https://leetcode.com/problems/beautiful-arrangement-ii/

Given two integers `n` and `k`, you need to construct a list which
contains `n` different positive integers ranging from `1` to
`n` and obeys the following requirement:

Suppose this list is [a1, a2, a3, ... , an],
then the list [|a1 - a2|, |a2 - a3|,
|a3 - a4|, ... , |an-1 - an|] has exactly `k`
distinct integers.

If there are multiple answers, print any of them.

Example 1:

Input: n = 3, k = 1
Output: [1, 2, 3]
Explanation: The [1, 2, 3] has three different positive integers ranging from 1 to 3, and the [1, 1] has exactly 1 distinct integer: 1.

Example 2:

Input: n = 3, k = 2
Output: [1, 3, 2]
Explanation: The [1, 3, 2] has three different positive integers ranging from 1 to 3, and the [2, 1] has exactly 2 distinct integers: 1 and 2.

Note:

The `n` and `k` are in the range 1 4.

【中文翻译】
给定两个整数 `n` 和 `k`，你需要构造一个包含 `n` 个不同正整数的列表，这些正整数范围从 `1` 到 `n`，并满足以下要求：

假设这个列表是 [a1, a2, a3, ... , an]，则列表 [|a1 - a2|, |a2 - a3|, |a3 - a4|, ... , |a(n-1) - an|] 恰好包含 `k` 个不同的整数。

如果有多个答案，输出其中任意一个。

示例 1：

输入：n = 3，k = 1
输出：[1, 2, 3]
解释：[1, 2, 3] 包含 3 个范围从 1 到 3 的不同正整数，并且 [1, 1] 恰好有 1 个不同的整数：1。

示例 2：

输入：n = 3，k = 2
输出：[1, 3, 2]
解释：[1, 3, 2] 包含 3 个范围从 1 到 3 的不同正整数，并且 [2, 1] 恰好有 2 个不同的整数：1 和 2。

注意：

`n` 和 `k` 的范围是 1 <= k < n <= 10^4。
"""

from typing import List, Optional


class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        result: list[int] = []
        left, right = 1, n

        while left <= right:
            if k > 1:
                if k % 2 == 1:
                    result.append(left)
                    left += 1
                else:
                    result.append(right)
                    right -= 1
                k -= 1
            else:
                result.append(left)
                left += 1

        return result











# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 构造性解法。要得到恰好 k 个不同的差值，使用交错法：
# 对于前 k+1 个位置，交替从最小值（left）和最大值（right）取数：
# - 当 k 为奇数时：取 left，left++
# - 当 k 为偶数时：取 right，right--
# - 每次取数后 k--
# 当 k 变为 1 后，剩余的差值都是 1，直接按升序填入剩余数字。
#
# 原理：
# 交错法产生的差值序列从大逐渐变小：n-1, n-2, ..., 1
# 当我们控制交错的次数为 k+1 个元素时，恰好产生 k 个不同的差值。
# 之后按顺序填入，差值全部为 1（已出现过）。
#
# 时间复杂度: O(n) - 构造 n 个元素
# 空间复杂度: O(n) - 结果数组（或 O(1) 不算输出）
#
# 关键点:
# - 构造题的技巧：交替取极值来产生不同的差值
# - 差值种类 = 前 k+1 个元素交错排列产生 k 种不同差值
# - 剩余部分差值全是 1（在 k>=1 时已经包含 1）
# - 例子：n=10, k=4 → [1,10,2,9,3,4,5,6,7,8]
